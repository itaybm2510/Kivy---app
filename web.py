import os
import sqlite3
import logging
import json
from flask import Flask, render_template_string, request, redirect, url_for, session, send_file, jsonify
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
app.secret_key = 'smart_biz_premium_cyber_key_2026'

CORRECT_PIN = "4444"

# --- 🗄️ DATABASE SETUP ---
def get_db_connection():
    conn = sqlite3.connect('business_v50.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, stock INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, items TEXT, total REAL, 
                        method TEXT, phone TEXT, address TEXT, status TEXT DEFAULT '⏳ בהמתנה', 
                        coupon_used TEXT DEFAULT NULL, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS coupons (
                        code TEXT PRIMARY KEY, discount_percent INTEGER, used_count INTEGER DEFAULT 0, referrer_id TEXT DEFAULT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL, description TEXT, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # הוספת מוצרי דוגמה מרשימים אם מסד הנתונים ריק כדי שהטסט שלך ייראה מטורף
    if cursor.execute("SELECT COUNT(*) FROM inventory").fetchone()[0] == 0:
        cursor.executemany("INSERT INTO inventory (name, price, stock) VALUES (?, ?, ?)", [
            ("💻 מחשב נייד CyberBook Pro", 4500, 10),
            ("🎧 אוזניות Quantum Sound ANC", 850, 25),
            ("⌚ שעון חכם Titan Chrono", 1200, 15),
            ("📱 סמארטפון Edge Nebula v5", 3800, 8)
        ])
    conn.commit()
    conn.close()

init_db()

# --- 📄 PDF GENERATION ---
def generate_pdf_invoice(order_id, customer_name, items_str, total_amount, date_str):
    filename = f"invoice_{order_id}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    story = []
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=24, leading=28, textColor=colors.HexColor("#0F172A"), spaceAfter=12)
    meta_style = ParagraphStyle('MetaStyle', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor("#475569"))
    table_header_style = ParagraphStyle('TableHeader', parent=styles['Normal'], fontSize=11, leading=14, textColor=colors.white, fontName="Helvetica-Bold")
    table_cell_style = ParagraphStyle('TableCell', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor("#1E293B"))
    
    story.append(Paragraph("INVOICE / RECEIPT", title_style))
    story.append(Paragraph(f"<b>Invoice No:</b> #{order_id}", meta_style))
    story.append(Paragraph(f"<b>Date:</b> {date_str}", meta_style))
    story.append(Paragraph(f"<b>Customer Name:</b> {customer_name}", meta_style))
    story.append(Spacer(1, 15))
    
    data = [[Paragraph("Item Description & Qty", table_header_style), Paragraph("Total Price", table_header_style)]]
    for part in items_str.split(', '):
        if part:
            data.append([Paragraph(part, table_cell_style), Paragraph("-", table_cell_style)])
    data.append([Paragraph("<b>Total Amount Paid:</b>", table_cell_style), Paragraph(f"<b>{total_amount} ILS</b>", table_cell_style)])
    
    t = Table(data, colWidths=[350, 120])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0F172A")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#F1F5F9")),
    ]))
    story.append(t)
    doc.build(story)
    return filename

# --- 🌐 HTML TEMPLATES ---
BASE_TEMPLATE = """
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SmartBiz OS - Premium Tech Store</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        .cyber-gradient { background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); }
        .neon-border { border-color: #3b82f6; box-shadow: 0 0 15px rgba(59, 130, 246, 0.4); }
        .neon-glow-green { box-shadow: 0 0 15px rgba(34, 197, 94, 0.3); }
    </style>
</head>
<body class="bg-[#0b0f19] text-gray-100 font-sans antialiased min-h-screen flex flex-col">
    <nav class="border-b border-gray-800 bg-[#0f172a]/80 backdrop-blur-md sticky top-0 z-40 p-4">
        <div class="container mx-auto flex justify-between items-center">
            <a href="/" class="text-xl font-black tracking-wider text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-400">
                💎 SMARTBIZ <span class="text-blue-500 font-light text-sm">PREMIUM OS</span>
            </a>
            <div class="flex items-center space-x-6 space-x-reverse">
                <a href="/" class="text-gray-300 hover:text-blue-400 transition font-medium">🛍️ קטלוג</a>
                <button onclick="toggleCartDrawer()" class="relative text-gray-300 hover:text-blue-400 transition font-medium cursor-pointer">
                    🛒 סל קניות
                    <span id="cart-badge" class="absolute -top-3 -left-4 bg-blue-600 text-white text-xs px-2 py-0.5 rounded-full font-bold shadow-lg">0</span>
                </button>
                <a href="/admin" class="bg-gradient-to-r from-blue-600 to-indigo-600 px-4 py-1.5 rounded-lg text-sm font-semibold hover:from-blue-500 hover:to-indigo-500 shadow-md transition">⚙️ מערכת ניהול</a>
            </div>
        </div>
    </nav>

    <main class="container mx-auto p-6 flex-grow">
        CHANNELS_CONTENT_PLACEHOLDER
    </main>

    <div id="cart-drawer" class="fixed inset-0 z-50 hidden transition-opacity">
        <div class="absolute inset-0 bg-black/60 backdrop-blur-sm" onclick="toggleCartDrawer()"></div>
        <div class="absolute inset-y-0 right-0 max-w-full flex">
            <div class="w-screen max-w-md bg-[#0f172a] border-l border-gray-800 shadow-2xl flex flex-col p-6">
                <div class="flex justify-between items-center mb-6 border-b border-gray-800 pb-4">
                    <h2 class="text-xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-400">🛒 סל הקניות שלך</h2>
                    <button onclick="toggleCartDrawer()" class="text-gray-400 hover:text-white text-2xl cursor-pointer">&times;</button>
                </div>
                <div id="drawer-items-container" class="flex-grow overflow-y-auto space-y-4 pr-1">
                    </div>
                <div class="border-t border-gray-800 pt-4 mt-4 space-y-4">
                    <div class="flex justify-between font-bold text-lg">
                        <span>סה"כ לתשלום:</span>
                        <span id="drawer-total" class="text-blue-400">0₪</span>
                    </div>
                    <a href="/cart" class="block text-center bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-3 rounded-xl font-bold hover:from-blue-500 hover:to-indigo-500 transition shadow-lg shadow-blue-900/30">🔒 מעבר לקופה מאובטחת</a>
                </div>
            </div>
        </div>
    </div>

    <div id="toast-container" class="fixed bottom-5 left-5 z-50 space-y-2"></div>

    <footer class="border-t border-gray-900 p-4 text-center text-xs text-gray-600 mt-12 bg-[#060913]">
        SmartBiz OS v5.0 - Showcase Experience Portfolio Engine
    </footer>

    <script>
        function toggleCartDrawer() {
            const drawer = document.getElementById('cart-drawer');
            drawer.classList.toggle('hidden');
            if(!drawer.classList.contains('hidden')) { updateDrawerCart(); }
        }

        function showToast(message, type='info') {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = `p-4 rounded-xl shadow-xl text-sm font-semibold border backdrop-blur-md flex items-center gap-2 transform transition duration-300 translate-y-2 opacity-0 neon-border ${type === 'success' ? 'border-green-500 bg-green-950/80 text-green-300' : 'border-blue-500 bg-slate-900/90 text-blue-300'}`;
            toast.innerHTML = `<span>${message}</span>`;
            container.appendChild(toast);
            setTimeout(() => { toast.classList.remove('translate-y-2', 'opacity-0'); }, 10);
            setTimeout(() => {
                toast.classList.add('opacity-0');
                setTimeout(() => { toast.remove(); }, 300);
            }, 3000);
        }

        function updateDrawerCart() {
            fetch('/api/cart-data')
                .then(res => res.json())
                .then(data => {
                    document.getElementById('cart-badge').innerText = data.total_qty;
                    document.getElementById('drawer-total').innerText = data.total_price + '₪';
                    const container = document.getElementById('drawer-items-container');
                    container.innerHTML = '';
                    if (Object.keys(data.items).length === 0) {
                        container.innerHTML = '<p class="text-gray-500 text-center py-8">הסל שלך ריק כרגע.</p>';
                        return;
                    }
                    for (const [name, details] of Object.entries(data.items)) {
                        container.innerHTML += `
                            <div class="bg-[#1e293b]/40 border border-gray-800 p-3 rounded-xl flex justify-between items-center">
                                <div>
                                    <h4 class="font-bold text-sm text-gray-200">${name}</h4>
                                    <p class="text-xs text-gray-400">${details.price}₪ × ${details.qty}</p>
                                </div>
                                <span class="font-bold text-sm text-blue-400">${details.price * details.qty}₪</span>
                            </div>
                        `;
                    }
                });
        }
        
        // טעינה ראשונית של המונה בסנכרון
        document.addEventListener('DOMContentLoaded', () => {
            fetch('/api/cart-data').then(res=>res.json()).then(data=>{
                document.getElementById('cart-badge').innerText = data.total_qty;
            });
        });
    </script>
</body>
</html>
"""

CATALOG_TEMPLATE = """
<div class="max-w-6xl mx-auto">
    <div class="text-center my-12 space-y-4">
        <h1 class="text-4xl md:text-5xl font-black tracking-tight text-white">העתיד של המסחר האלקטרוני כבר כאן</h1>
        <p class="text-gray-400 max-w-xl mx-auto text-sm md:text-base">פרוטוטייפ חנות פרימיום מהירה, מאובטחת ומותאמת אישית לכל סוגי העסקים בדינמיות מלאה.</p>
        
        <div class="max-w-md mx-auto pt-6">
            <div class="relative">
                <span class="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-500">🔍</span>
                <input type="text" id="live-search" onkeyup="searchProducts()" placeholder="חפש מוצרים מותגים בזמן אמת..." 
                       class="w-full bg-[#111827] border border-gray-800 rounded-2xl py-3 pr-10 pl-4 text-white placeholder-gray-500 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-900/30 transition text-sm">
            </div>
        </div>
    </div>

    <div id="products-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {% for item in items %}
        <div class="product-card bg-[#0f172a]/60 border border-gray-800 rounded-3xl p-5 hover:border-gray-700 transition duration-300 flex flex-col justify-between group relative overflow-hidden" data-name="{{ item['name'].lower() }}">
            <div class="absolute top-0 left-0 bg-blue-500/10 text-blue-400 text-xs px-3 py-1 rounded-br-2xl font-semibold border-b border-r border-blue-500/20">🔥 פופולרי</div>
            <div class="pt-4">
                <h3 class="text-lg font-bold text-gray-100 group-hover:text-blue-400 transition duration-200 mb-1 mt-2">{{ item['name'] }}</h3>
                <p class="text-xs text-gray-500 flex items-center gap-1 mb-4">💎 זמין במלאי המערכת: <span class="text-gray-300 font-bold font-mono">{{ item['stock'] }}</span></p>
            </div>
            <div class="flex justify-between items-center pt-4 border-t border-gray-800/60">
                <div class="flex flex-col">
                    <span class="text-2xl font-black text-white font-mono">{{ item['price'] }}₪</span>
                </div>
                <button onclick="addToCartApi({{ item['id'] }}, '{{ item['name'] }}')" class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-4 py-2 rounded-xl text-xs font-bold hover:from-blue-500 hover:to-indigo-500 shadow-md shadow-blue-950 transition cursor-pointer">➕ הוסף לסל</button>
            </div>
        </div>
        {% endfor %}
    </div>
</div>

<script>
    function searchProducts() {
        const query = document.getElementById('live-search').value.toLowerCase();
        const cards = document.querySelectorAll('.product-card');
        cards.forEach(card => {
            const name = card.getAttribute('data-name');
            if(name.includes(query)) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }

    function addToCartApi(id, name) {
        fetch(`/add_to_cart_api/${id}`)
            .then(res => res.json())
            .then(data => {
                if(data.success) {
                    showToast(`המוצר "${name}" נוסף לסל בהצלחה`, 'success');
                    document.getElementById('cart-badge').innerText = data.total_qty;
                }
            });
    }
</script>
"""

CART_TEMPLATE = """
<div class="max-w-3xl mx-auto my-8">
    <div class="bg-[#0f172a]/90 border border-gray-800 rounded-3xl p-8 shadow-2xl backdrop-blur-md">
        <h2 class="text-2xl font-black mb-6 text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-400 flex items-center gap-2">🛒 קופה מאובטחת</h2>
        
        {% if not cart_items %}
            <div class="text-center py-12">
                <p class="text-gray-400 text-lg mb-4">סל הקניות שלך ריק לגמרי.</p>
                <a href="/" class="inline-block bg-blue-600 text-white px-6 py-2 rounded-xl font-bold hover:bg-blue-500 transition text-sm">🛍️ חזרה לקטלוג</a>
            </div>
        {% else %}
            <div class="space-y-4 mb-6">
                {% for name, details in cart_items.items() %}
                <div class="bg-[#1e293b]/30 border border-gray-800/80 p-4 rounded-2xl flex justify-between items-center">
                    <div>
                        <h3 class="font-bold text-gray-200">{{ name }}</h3>
                        <p class="text-xs text-gray-500">מחיר ליחידה: {{ details.price }}₪</p>
                    </div>
                    <div class="text-left">
                        <span class="bg-gray-800 text-gray-300 text-xs px-2.5 py-1 rounded-lg ml-3 font-bold font-mono">x{{ details.qty }}</span>
                        <span class="font-black text-white font-mono">{{ details.price * details.qty }}₪</span>
                    </div>
                </div>
                {% endfor %}
            </div>

            <form action="/apply_coupon" method="POST" class="mb-6 flex gap-3">
                <input type="text" name="coupon" placeholder="הזן קוד קופון להנחה..." class="bg-[#111827] border border-gray-800 p-3 rounded-xl flex-grow text-white text-sm focus:outline-none focus:border-blue-500">
                <button type="submit" class="bg-gray-800 hover:bg-gray-700 text-gray-200 px-6 py-3 rounded-xl font-bold text-sm transition">החל הנחה</button>
            </form>

            {% if discount > 0 %}
                <div class="bg-green-950/40 border border-green-800 text-green-400 p-3 rounded-xl text-xs font-bold mb-4">
                    🏷️ קופון פרימיום פעיל במערכת: {{ discount }}% הנחה הופחתו מהסל!
                </div>
            {% endif %}

            <div class="flex justify-between items-center border-t border-gray-800 pt-6 mb-8">
                <span class="text-gray-400 font-medium">סך הכל הסופי לתשלום:</span>
                <span class="text-3xl font-black text-transparent bg-clip-text bg-gradient-to-r from-green-400 to-emerald-400 font-mono">{{ total }}₪</span>
            </div>

            <hr class="border-gray-800 my-6">

            <h3 class="text-lg font-bold mb-4 text-gray-300 flex items-center gap-2">📝 פרטי לקוח למשלוח האספקה</h3>
            <form action="/checkout" method="POST" class="space-y-4">
                <div>
                    <label class="block text-xs text-gray-500 mb-1 font-medium">שם מלא של המקבל</label>
                    <input type="text" name="name" required class="w-full bg-[#111827] border border-gray-800 p-3 rounded-xl text-white text-sm focus:outline-none focus:border-blue-500">
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs text-gray-500 mb-1 font-medium">מספר טלפון נייד</label>
                        <input type="text" name="phone" required class="w-full bg-[#111827] border border-gray-800 p-3 rounded-xl text-white text-sm focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-xs text-gray-500 mb-1 font-medium">כתובת יעד מלאה</label>
                        <input type="text" name="address" required class="w-full bg-[#111827] border border-gray-800 p-3 rounded-xl text-white text-sm focus:outline-none focus:border-blue-500">
                    </div>
                </div>
                <button type="submit" class="w-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-3.5 rounded-2xl font-bold hover:from-blue-500 hover:to-indigo-500 transition shadow-lg shadow-blue-900/40 text-sm mt-4 cursor-pointer">💵 אישור הזמנה (מזומן לשליח / במעמד קבלה)</button>
            </form>
        {% endif %}
    </div>
</div>
"""

ADMIN_TEMPLATE = """
<div class="max-w-6xl mx-auto">
    <h2 class="text-3xl font-black mb-8 text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-400">📊 דאשבורד מנהל - אנליטיקה ורווחים</h2>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div class="bg-[#0f172a]/80 border border-gray-800 p-6 rounded-2xl neon-glow-green">
            <p class="text-xs font-bold text-gray-500 tracking-wider mb-1">מחזור הכנסות ברוטו</p>
            <p class="text-3xl font-black text-green-400 font-mono">{{ stats.rev }}₪</p>
        </div>
        <div class="bg-[#0f172a]/80 border border-gray-800 p-6 rounded-2xl">
            <p class="text-xs font-bold text-gray-500 tracking-wider mb-1">סך הוצאות תפעוליות</p>
            <p class="text-3xl font-black text-red-400 font-mono">{{ stats.exp }}₪</p>
        </div>
        <div class="bg-[#0f172a]/80 border border-gray-800 p-6 rounded-2xl neon-border">
            <p class="text-xs font-bold text-gray-500 tracking-wider mb-1">רווח פיננסי נקי</p>
            <p class="text-3xl font-black text-blue-400 font-mono">{{ stats.net }}₪</p>
        </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <div class="bg-[#0f172a]/80 border border-gray-800 p-6 rounded-3xl">
            <h3 class="text-sm font-bold text-gray-400 mb-4">📈 יחס הכנסות מול הוצאות עסקיות</h3>
            <div class="h-64"><canvas id="financialChart"></canvas></div>
        </div>
        <div class="bg-[#0f172a]/80 border border-gray-800 p-6 rounded-3xl">
            <h3 class="text-sm font-bold text-gray-400 mb-4">📊 התפלגות מוצרים מובילים במכירות</h3>
            <div class="h-64 flex justify-center"><canvas id="productsPieChart"></canvas></div>
        </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <div class="bg-[#0f172a]/80 border border-gray-800 p-6 rounded-2xl">
            <h3 class="font-bold text-sm text-gray-300 mb-4 flex items-center gap-2">📦 הוספת מוצר חדש למלאי</h3>
            <form action="/admin/add_product" method="POST" class="space-y-3">
                <input type="text" name="name" placeholder="שם המוצר הטכנולוגי" required class="w-full bg-[#111827] border border-gray-800 p-2.5 rounded-xl text-white text-sm focus:outline-none">
                <div class="grid grid-cols-2 gap-3">
                    <input type="number" step="0.1" name="price" placeholder="מחיר ברוטו" required class="w-full bg-[#111827] border border-gray-800 p-2.5 rounded-xl text-white text-sm focus:outline-none">
                    <input type="number" name="stock" placeholder="מלאי התחלתי" required class="w-full bg-[#111827] border border-gray-800 p-2.5 rounded-xl text-white text-sm focus:outline-none">
                </div>
                <button class="w-full bg-blue-600 hover:bg-blue-500 text-white p-2.5 rounded-xl text-xs font-bold transition">הוסף מוצר</button>
            </form>
        </div>
        <div class="bg-[#0f172a]/80 border border-gray-800 p-6 rounded-2xl">
            <h3 class="font-bold text-sm text-gray-300 mb-4 flex items-center gap-2">📉 רישום הוצאה מוכרת מיידית</h3>
            <form action="/admin/add_expense" method="POST" class="space-y-3">
                <input type="number" step="0.1" name="amount" placeholder="סכום ההוצאה בשקלים" required class="w-full bg-[#111827] border border-gray-800 p-2.5 rounded-xl text-white text-sm focus:outline-none">
                <input type="text" name="desc" placeholder="עבור מה? (ספקים, שיווק, שרתים...)" required class="w-full bg-[#111827] border border-gray-800 p-2.5 rounded-xl text-white text-sm focus:outline-none">
                <button class="w-full bg-red-600 hover:bg-red-500 text-white p-2.5 rounded-xl text-xs font-bold transition">רישום הוצאה</button>
            </form>
        </div>
    </div>

    <div class="bg-[#0f172a]/80 border border-gray-800 p-6 rounded-3xl">
        <h3 class="font-bold text-lg mb-4 text-gray-300">📋 ניהול ומעקב פניות והזמנות לקוחות</h3>
        <div class="overflow-x-auto">
            <table class="w-full text-right border-collapse text-sm">
                <thead>
                    <tr class="border-b border-gray-800 text-gray-400">
                        <th class="p-3">מזהה</th>
                        <th class="p-3">מוצרים שהוזמנו</th>
                        <th class="p-3">סכום הזמנה</th>
                        <th class="p-3">סטטוס שלב</th>
                        <th class="p-3 text-left">פעולות אוטומציה</th>
                    </tr>
                </thead>
                <tbody>
                    {% for o in orders %}
                    <tr class="border-b border-gray-800/60 hover:bg-gray-900/40 transition">
                        <td class="p-3 font-bold font-mono">#{{ o['id'] }}</td>
                        <td class="p-3 text-gray-300">{{ o['items'] }}</td>
                        <td class="p-3 font-bold text-blue-400 font-mono">{{ o['total'] }}₪</td>
                        <td class="p-3">
                            <span class="bg-blue-950 text-blue-400 px-2.5 py-1 rounded-lg text-xs font-semibold">{{ o['status'] }}</span>
                        </td>
                        <td class="p-3 text-left space-x-2 space-x-reverse">
                            <a href="/admin/approve/{{ o['id'] }}" class="inline-block bg-green-600/20 text-green-400 border border-green-500/30 px-3 py-1 rounded-lg text-xs font-bold hover:bg-green-600 hover:text-white transition">✅ הפק חשבונית PDF</a>
                            <a href="/admin/update_status/{{ o['id'] }}/🛵 שליח בדרך לקוח" class="inline-block bg-slate-800 text-gray-300 px-3 py-1 rounded-lg text-xs hover:bg-slate-700 transition">🛵 שלח שליח</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>

<script>
    // 1. Line Financial Analytics Chart
    const ctxFin = document.getElementById('financialChart').getContext('2d');
    new Chart(ctxFin, {
        type: 'line',
        data: {
            labels: ['תחילת קמפיין', 'שלב ב', 'שלב ג', 'היום'],
            datasets: [
                {
                    label: 'הכנסות',
                    data: [0, {{ stats.rev * 0.4 }}, {{ stats.rev * 0.75 }}, {{ stats.rev }}],
                    borderColor: '#22c55e',
                    backgroundColor: 'rgba(34, 197, 94, 0.1)',
                    fill: true,
                    tension: 0.3
                },
                {
                    label: 'הוצאות',
                    data: [0, {{ stats.exp * 0.3 }}, {{ stats.exp * 0.6 }}, {{ stats.exp }}],
                    borderColor: '#ef4444',
                    backgroundColor: 'rgba(239, 68, 68, 0.1)',
                    fill: true,
                    tension: 0.3
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { labels: { color: '#9ca3af' } } },
            scales: {
                x: { grid: { color: '#1f2937' }, ticks: { color: '#9ca3af' } },
                y: { grid: { color: '#1f2937' }, ticks: { color: '#9ca3af' } }
            }
        }
    });

    // 2. Pie Best Sellers Inventory Sales Matrix Chart
    const ctxPie = document.getElementById('productsPieChart').getContext('2d');
    new Chart(ctxPie, {
        type: 'pie',
        data: {
            labels: ['מחשוב פרימיום', 'אוזניות סאונד', 'לייף סטייל ושעונים', 'סמארטפונים'],
            datasets: [{
                data: [45, 25, 15, 15],
                backgroundColor: ['#3b82f6', '#6366f1', '#a855f7', '#ec4899'],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'bottom', labels: { color: '#9ca3af' } } }
        }
    });
</script>
"""

# --- 🌐 ROUTES & REST API CONTROLLERS ---
@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute("SELECT * FROM inventory WHERE stock > 0").fetchall()
    conn.close()
    
    full_html = BASE_TEMPLATE.replace('CHANNELS_CONTENT_PLACEHOLDER', CATALOG_TEMPLATE)
    return render_template_string(full_html, items=items)

# REST API קל לקבלת נתוני הסל בזמן אמת בלי רענון דף עבור מגירת ה-JS
@app.route('/api/cart-data')
def api_cart_data():
    if 'cart' not in session or not session['cart']:
        return jsonify({'items': {}, 'total_price': 0, 'total_qty': 0})
    
    conn = get_db_connection()
    cart_ids = session['cart']
    
    cart_items = {}
    subtotal = 0
    for cid in cart_ids:
        item = conn.execute("SELECT * FROM inventory WHERE id = ?", (cid,)).fetchone()
        if item:
            if item['name'] in cart_items:
                cart_items[item['name']]['qty'] += 1
            else:
                cart_items[item['name']] = {'price': item['price'], 'qty': 1}
            subtotal += item['price']
            
    discount = session.get('discount', 0)
    total = subtotal - (subtotal * discount / 100)
    conn.close()
    
    return jsonify({
        'items': cart_items,
        'total_price': total,
        'total_qty': len(cart_ids)
    })

@app.route('/add_to_cart_api/<int:item_id>')
def add_to_cart_api(item_id):
    if 'cart' not in session:
        session['cart'] = []
    cart = session['cart']
    cart.append(item_id)
    session['cart'] = cart
    return jsonify({'success': True, 'total_qty': len(cart)})

@app.route('/cart')
def cart():
    full_html = BASE_TEMPLATE.replace('CHANNELS_CONTENT_PLACEHOLDER', CART_TEMPLATE)
    
    if 'cart' not in session or not session['cart']:
        return render_template_string(full_html, cart_items={}, total=0, discount=0)
    
    conn = get_db_connection()
    cart_ids = session['cart']
    
    cart_items = {}
    subtotal = 0
    for cid in cart_ids:
        item = conn.execute("SELECT * FROM inventory WHERE id = ?", (cid,)).fetchone()
        if item:
            if item['name'] in cart_items:
                cart_items[item['name']]['qty'] += 1
            else:
                cart_items[item['name']] = {'price': item['price'], 'qty': 1}
            subtotal += item['price']
            
    discount = session.get('discount', 0)
    total = subtotal - (subtotal * discount / 100)
    conn.close()
    
    return render_template_string(full_html, cart_items=cart_items, total=total, discount=discount)

@app.route('/apply_coupon', methods=['POST'])
def apply_coupon():
    code = request.form.get('coupon', '').strip().upper()
    conn = get_db_connection()
    res = conn.execute("SELECT discount_percent FROM coupons WHERE code = ?", (code,)).fetchone()
    if res:
        session['discount'] = res['discount_percent']
        session['coupon_code'] = code
    else:
        # קופון ברירת מחדל לבדיקה של לקוחות פיקטיביים שיעבוד תמיד בשואוקייס
        if code == "PROMO10":
            session['discount'] = 10
            session['coupon_code'] = code
    conn.close()
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['POST'])
def checkout():
    if 'cart' not in session or not session['cart']: return redirect(url_for('index'))
    
    name = request.form.get('name')
    phone = request.form.get('phone')
    address = request.form.get('address')
    
    conn = get_db_connection()
    cart_ids = session['cart']
    
    summary = {}
    subtotal = 0
    for cid in cart_ids:
        item = conn.execute("SELECT * FROM inventory WHERE id = ?", (cid,)).fetchone()
        if item:
            summary[item['name']] = summary.get(item['name'], 0) + 1
            subtotal += item['price']
            conn.execute("UPDATE inventory SET stock = stock - 1 WHERE id = ?", (cid,))
            
    discount = session.get('discount', 0)
    total = subtotal - (subtotal * discount / 100)
    items_str = ", ".join([f"{n} (x{q})" for n, q in summary.items()])
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (user_id, items, total, method, phone, address, coupon_used) VALUES (?, ?, ?, 'Cash', ?, ?, ?)",
                   (999, items_str, total, phone, address, session.get('coupon_code')))
    conn.commit()
    conn.close()
    
    session.pop('cart', None)
    session.pop('discount', None)
    session.pop('coupon_code', None)
    
    return f\"\"\"
    <div style='text-align:center; padding:100px 20px; font-family:sans-serif; background:#0b0f19; color:white; min-h:100vh;'>
        <h1 style='color:#3b82f6; font-size:3rem; margin-bottom:10px;'>⚡ TRANSACTION SECURED</h1>
        <h2>ההזמנה בוצעה ונרשמה במערכת בהצלחה!</h2>
        <p style='color:#9ca3af;'>תודה {name}. פנייתך הועברה לדאשבורד המנהלים לטיפול מיידי.</p>
        <br><br>
        <a href='/' style='background:#2563eb; color:white; padding:12px 24px; border-radius:12px; text-decoration:none; font-weight:bold;'>חזרה למערכת הראשית</a>
    </div>
    \"\"\"

# --- 🔐 ADMIN PAGES ---
@app.route('/admin')
def admin_panel():
    if not session.get('is_admin'):
        return '''
        <div style="text-align:center; padding-top:150px; font-family:sans-serif; background:#0b0f19; color:white; min-height:100vh; margin:0;">
            <form action="/admin/login" method="POST" style="display:inline-block; border:1px solid #1e293b; padding:40px; border-radius:24px; background:#0f172a; box-shadow:0 0 20px rgba(59,130,246,0.2);">
                <h2 style="color:#3b82f6; margin-bottom:5px;">🔐 SMARTBIZ ADMIN TERMINAL</h2>
                <p style="color:#64748b; font-size:0.85rem; margin-bottom:25px;">נא להקליד קוד גישה מאובטח לניהול האנליטיקה</p>
                <input type="password" name="pin" placeholder="קוד סודי (ברירת מחדל: 4444)" required style="padding:12px; width:250px; background:#111827; border:1px solid #334155; border-radius:12px; color:white; text-align:center; font-size:1.1rem; outline:none;"><br><br>
                <button type="submit" style="background:#2563eb; color:white; padding:12px 25px; border:none; border-radius:12px; font-weight:bold; cursor:pointer; width:100%; transition:0.2s;">התחבר למערכת</button>
            </form>
        </div>
        '''
    conn = get_db_connection()
    orders = conn.execute("SELECT * FROM orders ORDER BY id DESC").fetchall()
    
    rev = conn.execute("SELECT SUM(total) FROM orders WHERE status NOT LIKE '%מבוטל%'").fetchone()[0] or 0
    exp = conn.execute("SELECT SUM(amount) FROM expenses").fetchone()[0] or 0
    stats = {'rev': rev, 'exp': exp, 'net': rev - exp}
    conn.close()
    
    full_html = BASE_TEMPLATE.replace('CHANNELS_CONTENT_PLACEHOLDER', ADMIN_TEMPLATE)
    return render_template_string(full_html, orders=orders, stats=stats)

@app.route('/admin/login', methods=['POST'])
def admin_login():
    if request.form.get('pin') == CORRECT_PIN:
        session['is_admin'] = True
    return redirect(url_for('admin_panel'))

@app.route('/admin/add_product', methods=['POST'])
def add_product():
    if not session.get('is_admin'): return redirect(url_for('admin_panel'))
    name = request.form.get('name')
    price = float(request.form.get('price'))
    stock = int(request.form.get('stock'))
    conn = get_db_connection()
    conn.execute("INSERT INTO inventory (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    conn.commit()
    conn.close()
    return redirect(url_for('admin_panel'))

@app.route('/admin/add_expense', methods=['POST'])
def add_expense():
    if not session.get('is_admin'): return redirect(url_for('admin_panel'))
    amount = float(request.form.get('amount'))
    desc = request.form.get('desc')
    conn = get_db_connection()
    conn.execute("INSERT INTO expenses (amount, description) VALUES (?, ?)", (amount, desc))
    conn.commit()
    conn.close()
    return redirect(url_for('admin_panel'))

@app.route('/admin/approve/<int:order_id>')
def approve_order(order_id):
    if not session.get('is_admin'): return redirect(url_for('admin_panel'))
    conn = get_db_connection()
    order = conn.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()
    conn.execute("UPDATE orders SET status = 'שולם ואושר ✅' WHERE id = ?", (order_id,))
    conn.commit()
    conn.close()
    
    pdf_path = generate_pdf_invoice(order_id, "Customer Port", order['items'], order['total'], order['date'][:16])
    return send_file(pdf_path, as_attachment=True)

@app.route('/admin/update_status/<int:order_id>/<string:status>')
def update_status(order_id, status):
    if not session.get('is_admin'): return redirect(url_for('admin_panel'))
    conn = get_db_connection()
    conn.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
    conn.commit()
    conn.close()
    return redirect(url_for('admin_panel'))

if __name__ == '__main__':
    # 🚀 הרצה על פורט 5001 - מוכן להצגה מטורפת ב-Termux!
    app.run(host='0.0.0.0', port=5001, debug=True)

