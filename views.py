# --- 🛍️ ENTERPRISE BENTO CATALOG TEMPLATE ---
CATALOG_TEMPLATE = """
<div class="max-w-6xl mx-auto animate-fade-in space-y-10">
    
    <div class="text-center py-16 space-y-4 relative overflow-hidden rounded-3xl bg-gradient-to-br from-slate-900/40 via-[#070b18]/60 to-purple-950/20 border border-white/5 bento-glow-blue">
        <div class="absolute top-0 right-0 w-48 h-48 bg-blue-500/10 rounded-full blur-3xl pointer-events-none"></div>
        <h1 class="text-4xl md:text-6xl font-black tracking-tight text-white">
            הדור הבא של <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400">חנויות הדיגיטל</span>
        </h1>
        <p class="text-slate-400 max-w-xl mx-auto text-xs md:text-sm">
            חוויית קנייה מהירה קצה לקצה, ממשק משתמש אולטרה-מודרני ומערכת המלצות חכמה מבוססת בינה מלאכותית.
        </p>
        
        <div class="max-w-md mx-auto pt-6 px-4">
            <div class="relative">
                <span class="absolute inset-y-0 right-0 flex items-center pr-4 text-slate-500 text-sm">🔍</span>
                <input type="text" id="live-search" onkeyup="filterCatalog()" placeholder="חפש מוצרים, מותגים או טכנולוגיות במלאי..." 
                       class="w-full bg-slate-950/80 border border-slate-800 rounded-2xl py-3.5 pr-11 pl-4 text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 focus:ring-4 focus:ring-blue-950/30 transition text-xs">
            </div>
        </div>
    </div>

    <div class="flex flex-wrap justify-center gap-2 px-2">
        <button onclick="filterCategory('all')" class="cat-btn bg-blue-600 text-white px-5 py-2 rounded-xl text-xs font-bold transition cursor-pointer shadow-lg shadow-blue-950">כל המוצרים</button>
        <button onclick="filterCategory('מחשבים')" class="cat-btn bg-slate-900 border border-white/5 hover:border-slate-700 text-slate-300 px-5 py-2 rounded-xl text-xs font-bold transition cursor-pointer">💻 מחשבי עילית</button>
        <button onclick="filterCategory('סאונד')" class="cat-btn bg-slate-900 border border-white/5 hover:border-slate-700 text-slate-300 px-5 py-2 rounded-xl text-xs font-bold transition cursor-pointer">🎧 אוזניות וסאונד</button>
        <button onclick="filterCategory('סמארטפונים')" class="cat-btn bg-slate-900 border border-white/5 hover:border-slate-700 text-slate-300 px-5 py-2 rounded-xl text-xs font-bold transition cursor-pointer">📱 סמארטפונים</button>
        <button onclick="filterCategory('לייף סטייל')" class="cat-btn bg-slate-900 border border-white/5 hover:border-slate-700 text-slate-300 px-5 py-2 rounded-xl text-xs font-bold transition cursor-pointer">⌚ לייף סטייל</button>
    </div>

    <div id="products-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {% for item in items %}
        <div class="product-card glass-panel rounded-3xl p-6 transition duration-300 flex flex-col justify-between group relative overflow-hidden" 
             data-name="{{ item['name'].lower() }} {{ item['description'].lower() }}" data-category="{{ item['category'] }}">
            
            <div class="absolute top-0 left-0 bg-blue-500/10 text-blue-400 text-[9px] px-3 py-1 rounded-br-2xl font-black tracking-wider border-b border-r border-white/5 font-mono-cyber">
                {{ item['category'].upper() }}
            </div>
            
            <div class="pt-4 flex-grow">
                <h3 class="text-base font-bold text-slate-100 group-hover:text-blue-400 transition duration-300 mb-1.5 mt-2">{{ item['name'] }}</h3>
                <p class="text-slate-400 text-[11px] leading-relaxed mb-4 font-light">{{ item['description'] }}</p>
            </div>
            
            <div>
                <p class="text-[10px] text-slate-500 flex items-center gap-1 mb-4 font-medium">
                    📦 סטטוס מלאי זמין: <span class="text-slate-300 font-bold font-mono-cyber">{{ item['stock'] }} פריטים</span>
                </p>
                <div class="flex justify-between items-center pt-4 border-t border-slate-900">
                    <span class="text-xl font-black text-white font-mono-cyber">{{ item['price'] }}₪</span>
                    <button onclick="addToCartApi({{ item['id'] }}, '{{ item['name'] }}')" class="bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 text-white px-4 py-2.5 rounded-xl text-[11px] font-bold hover:opacity-90 shadow-md shadow-blue-950 transition cursor-pointer">➕ הוסף לסל</button>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>

<script>
    let currentCategory = 'all';

    function filterCategory(cat) {
        currentCategory = cat;
        // עדכון כפתורי העיצוב
        document.querySelectorAll('.cat-btn').forEach(btn => {
            btn.className = "cat-btn bg-slate-900 border border-white/5 hover:border-slate-700 text-slate-300 px-5 py-2 rounded-xl text-xs font-bold transition cursor-pointer";
        });
        event.currentTarget.className = "cat-btn bg-blue-600 text-white px-5 py-2 rounded-xl text-xs font-bold transition cursor-pointer shadow-lg shadow-blue-950";
        executeFilters();
    }

    function filterCatalog() {
        executeFilters();
    }

    function executeFilters() {
        const query = document.getElementById('live-search').value.toLowerCase();
        const cards = document.querySelectorAll('.product-card');
        
        cards.forEach(card => {
            const nameAndDesc = card.getAttribute('data-name');
            const cat = card.getAttribute('data-category');
            
            const matchesSearch = nameAndDesc.includes(query);
            const matchesCategory = (currentCategory === 'all' || cat === currentCategory);
            
            if(matchesSearch && matchesCategory) {
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
                    showToast(`המוצר "${name}" התווסף לסל הקניות בהצלחה!`, 'success');
                    document.getElementById('cart-badge').innerText = data.total_qty;
                    if(!document.getElementById('cart-drawer').classList.contains('hidden')) {
                        updateDrawerCart();
                    }
                }
            });
    }
</script>
"""


# --- 🛒 GLASSMORPHISM CHECKOUT PAGE TEMPLATE ---
CART_TEMPLATE = """
<div class="max-w-2xl mx-auto my-6 animate-fade-in">
    <div class="glass-panel rounded-3xl p-8 shadow-2xl relative overflow-hidden">
        <div class="absolute top-0 left-0 w-32 h-32 bg-blue-500/5 rounded-full blur-2xl pointer-events-none"></div>
        <h2 class="text-xl font-black mb-6 text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-400">🛒 סיכום פריטים וקופה מאובטחת</h2>
        
        {% if not cart_items %}
            <div class="text-center py-16 space-y-4">
                <p class="text-slate-400 text-xs md:text-sm">סל הקניות הארגוני שלך ריק כרגע.</p>
                <a href="/" class="inline-block bg-blue-600 text-white px-6 py-2.5 rounded-xl font-bold hover:bg-blue-500 transition text-xs">🛍️ חזרה לקטלוג המוצרים</a>
            </div>
        {% else %}
            <div class="space-y-3 mb-6">
                {% for name, details in cart_items.items() %}
                <div class="bg-slate-950/50 border border-slate-900/60 p-4 rounded-2xl flex justify-between items-center transition hover:bg-slate-900/40">
                    <div>
                        <h3 class="text-sm font-bold text-slate-200">{{ name }}</h3>
                        <p class="text-[10px] text-slate-500 font-mono-cyber">UNIT PRICE: {{ details.price }}₪</p>
                    </div>
                    <div class="text-left flex items-center gap-4">
                        <span class="bg-slate-900 text-slate-400 text-[10px] px-2.5 py-1 rounded-lg font-mono-cyber font-bold border border-white/5">x{{ details.qty }}</span>
                        <span class="font-bold text-sm font-mono-cyber text-white">{{ details.price * details.qty }}₪</span>
                    </div>
                </div>
                {% endfor %}
            </div>

            <form action="/apply_coupon" method="POST" class="mb-6 flex gap-2">
                <input type="text" name="coupon" placeholder="הקלד קוד קופון הנחה תאגידי (למשל: VIP20)" class="bg-slate-950 border border-slate-800 p-3.5 rounded-xl flex-grow text-white text-xs focus:outline-none focus:border-blue-500 font-mono-cyber tracking-wider">
                <button type="submit" class="bg-slate-800 hover:bg-slate-700 text-slate-200 px-6 py-3.5 rounded-xl font-bold text-xs transition cursor-pointer">החל קוד</button>
            </form>

            {% if discount > 0 %}
                <div class="bg-emerald-950/30 border border-emerald-500/20 text-emerald-400 p-3.5 rounded-xl text-xs font-bold mb-4 animate-fade-in flex justify-between items-center">
                    <span>🏷️ קופון פרימיום הופעל במערכת!</span>
                    <span class="font-mono-cyber text-sm bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">-{ discount }%</span>
                </div>
            {% endif %}

            <div class="flex justify-between items-center border-t border-slate-900 pt-5 mb-6">
                <span class="text-slate-400 text-sm">סה"כ לתשלום סופי (כולל מע"מ):</span>
                <span class="text-2xl font-black text-emerald-400 font-mono-cyber tracking-tight">{{ total }}₪</span>
            </div>

            <hr class="border-slate-900/60 my-6">

            <h3 class="text-xs font-bold mb-4 text-slate-400 uppercase tracking-wider">📝 פרטי משלוח ויעד אספקה</h3>
            <form action="/checkout" method="POST" class="space-y-4">
                <input type="text" name="name" placeholder="שם מלא של המקבל" required class="w-full bg-slate-950 border border-slate-800 p-3.5 rounded-xl text-white text-xs focus:outline-none focus:border-blue-500">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <input type="text" name="phone" placeholder="מספר טלפון נייד ליצירת קשר" required class="w-full bg-slate-950 border border-slate-800 p-3.5 rounded-xl text-white text-xs focus:outline-none focus:border-blue-500">
                    <input type="text" name="address" placeholder="כתובת מלאה (עיר, רחוב, דירה)" required class="w-full bg-slate-950 border border-slate-800 p-3.5 rounded-xl text-white text-xs focus:outline-none focus:border-blue-500">
                </div>
                <button type="submit" class="w-full bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 text-white py-4 rounded-xl font-bold hover:opacity-95 transition shadow-lg shadow-blue-950/50 text-xs mt-2 cursor-pointer">💵 אישור מאובטח ושליחת הזמנה (מזומן לשליח)</button>
            </form>
        {% endif %}
    </div>
</div>
"""


# --- 📊 EXECUTIVE ADMIN BENTO PANEL TEMPLATE ---
ADMIN_TEMPLATE = """
<div class="max-w-5xl mx-auto animate-fade-in space-y-8">
    <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border-b border-slate-900 pb-4">
        <div>
            <h2 class="text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400">📊 קונסולת ניהול עסק - אנליטיקה ו-CRM</h2>
            <p class="text-[11px] text-slate-500">מחובר כעת בתפקיד: מנהל מערכת ראשי (Admin Node)</p>
        </div>
        <div class="flex gap-2">
            <span class="bg-slate-900 text-slate-400 border border-white/5 text-[10px] px-3 py-1.5 rounded-xl font-bold font-mono-cyber">SERVER STATUS: ONLINE</span>
        </div>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="glass-panel p-6 rounded-3xl bento-glow-green relative overflow-hidden">
            <div class="absolute -right-4 -bottom-4 text-6xl opacity-5 pointer-events-none">💰</div>
            <p class="text-[10px] font-bold text-slate-500 tracking-wider mb-1 uppercase">מחזור הכנסות ברוטו</p>
            <p class="text-2xl font-black text-emerald-400 font-mono-cyber">{{ stats.rev }}₪</p>
        </div>
        <div class="glass-panel p-6 rounded-3xl relative overflow-hidden">
            <div class="absolute -right-4 -bottom-4 text-6xl opacity-5 pointer-events-none">📉</div>
            <p class="text-[10px] font-bold text-slate-500 tracking-wider mb-1 uppercase">סך הוצאות תפעוליות</p>
            <p class="text-2xl font-black text-rose-500 font-mono-cyber">{{ stats.exp }}₪</p>
        </div>
        <div class="glass-panel p-6 rounded-3xl bento-glow-blue relative overflow-hidden">
            <div class="absolute -right-4 -bottom-4 text-6xl opacity-5 pointer-events-none">⚡</div>
            <p class="text-[10px] font-bold text-slate-500 tracking-wider mb-1 uppercase">רווח נקי לחברה</p>
            <p class="text-2xl font-black text-blue-400 font-mono-cyber">{{ stats.net }}₪</p>
        </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="glass-panel p-6 rounded-3xl">
            <h3 class="text-xs font-bold text-slate-400 mb-4 tracking-wider uppercase">📈 מגמות רווחיות (הכנסות מול הוצאות)</h3>
            <div class="h-60"><canvas id="financialChart"></canvas></div>
        </div>
        <div class="glass-panel p-6 rounded-3xl">
            <h3 class="text-xs font-bold text-slate-400 mb-4 tracking-wider uppercase">📊 התפלגות פלח מכירות וביקוש במלאי</h3>
            <div class="h-60 flex justify-center"><canvas id="productsPieChart"></canvas></div>
        </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="glass-panel p-6 rounded-3xl">
            <h3 class="font-bold text-xs text-slate-300 mb-4 uppercase tracking-wider">📦 עדכון מלאי - הוספת מוצר חדש לחנות</h3>
            <form action="/admin/add_product" method="POST" class="space-y-3">
                <div class="grid grid-cols-2 gap-3">
                    <input type="text" name="name" placeholder="שם מוצר טכנולוגי" required class="w-full bg-slate-950 border border-slate-800 p-2.5 rounded-xl text-white text-xs focus:outline-none">
                    <input type="text" name="category" placeholder="קטגוריה (מחשבים, סאונד)" required class="w-full bg-slate-950 border border-slate-800 p-2.5 rounded-xl text-white text-xs focus:outline-none">
                </div>
                <div class="grid grid-cols-2 gap-3">
                    <input type="number" step="0.1" name="price" placeholder="מחיר פריט ברוטו" required class="w-full bg-slate-950 border border-slate-800 p-2.5 rounded-xl text-white text-xs focus:outline-none">
                    <input type="number" name="stock" placeholder="מלאי התחלתי" required class="w-full bg-slate-950 border border-slate-800 p-2.5 rounded-xl text-white text-xs focus:outline-none">
                </div>
                <input type="text" name="description" placeholder="תיאור קצר ומילות מפתח עבור מנוע ה-AI..." required class="w-full bg-slate-950 border border-slate-800 p-2.5 rounded-xl text-white text-xs focus:outline-none">
                <button class="w-full bg-blue-600 hover:bg-blue-500 text-white p-3 rounded-xl text-xs font-bold transition cursor-pointer">הוסף פריט למסד הנתונים</button>
            </form>
        </div>
        
        <div class="glass-panel p-6 rounded-3xl">
            <h3 class="font-bold text-xs text-slate-300 mb-4 uppercase tracking-wider">📉 רישום והזנת הוצאה תפעולית מבוקרת</h3>
            <form action="/admin/add_expense" method="POST" class="space-y-3">
                <input type="number" step="0.1" name="amount" placeholder="סכום ההוצאה בש"₪ required class="w-full bg-slate-950 border border-slate-800 p-2.5 rounded-xl text-white text-xs focus:outline-none">
                <input type="text" name="desc" placeholder="תיאור סעיף ההוצאה (שיווק, שרתים, רכש, משכורות)" required class="w-full bg-slate-950 border border-slate-800 p-2.5 rounded-xl text-white text-xs focus:outline-none">
                <button class="w-full bg-rose-600 hover:bg-rose-500 text-white p-3 rounded-xl text-xs font-bold transition cursor-pointer">רשום הוצאה בספרים</button>
            </form>
        </div>
    </div>

    <div class="glass-panel p-6 rounded-3xl overflow-hidden">
        <h3 class="font-bold text-sm mb-4 text-slate-300">📋 מעקב צבר הזמנות לקוחות (CRM System)</h3>
        <div class="overflow-x-auto">
            <table class="w-full text-right border-collapse text-xs">
                <thead>
                    <tr class="border-b border-slate-800 text-slate-500 font-bold uppercase tracking-wider">
                        <th class="p-3.5">מזהה</th>
                        <th class="p-3.5">פירוט הפריטים בסל</th>
                        <th class="p-3.5">סה"כ לגבייה</th>
                        <th class="p-3.5">כתובת משלוח</th>
                        <th class="p-3.5">סטטוס זרימה</th>
                        <th class="p-3.5 text-left">פקודות אוטומציה</th>
                    </tr>
                </thead>
                <tbody>
                    {% for o in orders %}
                    <tr class="border-b border-slate-900 hover:bg-white/5 transition">
                        <td class="p-3.5 font-bold font-mono-cyber">#{{ o['id'] }}</td>
                        <td class="p-3.5 text-slate-300 font-medium">{{ o['items'] }}</td>
                        <td class="p-3.5 font-bold text-blue-400 font-mono-cyber">{{ o['total'] }}₪</td>
                        <td class="p-3.5 text-slate-400">{{ o['address'] }} <br><span class="text-[10px] text-slate-500 font-mono-cyber">{{ o['phone'] }}</span></td>
                        <td class="p-3.5">
                            <span class="bg-blue-950/80 text-blue-400 border border-blue-800/30 px-2.5 py-1 rounded-lg text-[10px] font-bold">{{ o['status'] }}</span>
                        </td>
                        <td class="p-3.5 text-left space-x-2 space-x-reverse flex items-center justify-end">
                            <a href="/admin/approve/{{ o['id'] }}" class="inline-block bg-emerald-600/10 text-emerald-400 border border-emerald-500/20 px-3 py-1.5 rounded-xl font-bold hover:bg-emerald-600 hover:text-white transition">✅ אשר והפק PDF</a>
                            <a href="/admin/update_status/{{ o['id'] }}/🛵 יצא עם שליח" class="inline-block bg-slate-800 text-slate-300 px-3 py-1.5 rounded-xl hover:bg-slate-700 transition">🛵 שלח שליח</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>

<script>
    // 1. אתחול גרף פיננסי לינארי (הכנסות מול הוצאות)
    const ctxFin = document.getElementById('financialChart').getContext('2d');
    new Chart(ctxFin, {
        type: 'line',
        data: {
            labels: ['Q1 Start', 'Q2 Milestone', 'Q3 Pipeline', 'Current Node'],
            datasets: [
                {
                    label: 'הכנסות ברוטו',
                    data: [0, {{ stats.rev * 0.45 }}, {{ stats.rev * 0.8 }}, {{ stats.rev }}],
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16, 185, 129, 0.04)',
                    fill: true,
                    tension: 0.35
                },
                {
                    label: 'הוצאות תפעול',
                    data: [0, {{ stats.exp * 0.35 }}, {{ stats.exp * 0.7 }}, {{ stats.exp }}],
                    borderColor: '#f43f5e',
                    backgroundColor: 'rgba(244, 63, 94, 0.04)',
                    fill: true,
                    tension: 0.35
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { labels: { color: '#94a3b8', font: { size: 11, family: 'Assistant' } } } },
            scales: {
                x: { grid: { color: 'rgba(255,255,255,0.02)' }, ticks: { color: '#64748b', font: { family: 'Rajdhani', size: 11 } } },
                y: { grid: { color: 'rgba(255,255,255,0.02)' }, ticks: { color: '#64748b', font: { family: 'Rajdhani', size: 11 } } }
            }
        }
    });

    // 2. אתחול גרף פלח עוגה (קטגוריות מלאי נמכר)
    const ctxPie = document.getElementById('productsPieChart').getContext('2d');
    new Chart(ctxPie, {
        type: 'pie',
        data: {
            labels: ['💻 מחשבים', '🎧 סאונד', '⌚ לייף סטייל', '📱 סמארטפונים'],
            datasets: [{
                data: [45, 20, 20, 15],
                backgroundColor: ['#2563eb', '#4f46e5', '#9333ea', '#db2777'],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'bottom', labels: { color: '#94a3b8', font: { size: 11, family: 'Assistant' } } } }
        }
    });
</script>
"""

