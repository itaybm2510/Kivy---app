# --- 🌐 MEGA-ENTERPRISE BASE STRUCTURAL MATRIX TEMPLATE ---

BASE_TEMPLATE = """
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SmartBiz Mega-OS • Next-Gen Digital Ecosystem</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;600;800&family=Rajdhani:wght@500;700&display=swap');
        
        body { 
            background-color: #030712; 
            font-family: 'Assistant', sans-serif;
            overflow-x: hidden;
        }
        .font-mono-cyber {
            font-family: 'Rajdhani', sans-serif;
        }
        /* אפקט זכוכית יוקרתי - Glassmorphism */
        .glass-panel {
            background: rgba(17, 24, 39, 0.55);
            backdrop-filter: blur(16px) saturate(180%);
            -webkit-backdrop-filter: blur(16px) saturate(180%);
            border: 1px solid rgba(255, 255, 255, 0.06);
        }
        .glass-panel:hover {
            border-color: rgba(59, 130, 246, 0.4);
            box-shadow: 0 0 30px rgba(59, 130, 246, 0.15);
        }
        /* Bento Grid Shadows */
        .bento-glow-green { box-shadow: 0 0 35px rgba(34, 197, 94, 0.12); }
        .bento-glow-blue { box-shadow: 0 0 35px rgba(59, 130, 246, 0.15); }
        .bento-glow-purple { box-shadow: 0 0 35px rgba(168, 85, 247, 0.12); }
        
        /* אנימציות חלקות */
        .drawer-transition {
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-fade-in {
            animation: fadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
    </style>
</head>
<body class="text-slate-100 min-h-screen flex flex-col relative selection:bg-blue-500/30 selection:text-blue-200">

    <div class="absolute top-0 left-1/4 w-96 h-96 bg-blue-600/10 rounded-full blur-[120px] pointer-events-none"></div>
    <div class="absolute bottom-10 right-1/4 w-96 h-96 bg-purple-600/10 rounded-full blur-[120px] pointer-events-none"></div>

    <nav class="border-b border-slate-900/80 bg-[#070b18]/70 backdrop-blur-xl sticky top-0 z-40 p-4 transition-all">
        <div class="container mx-auto flex justify-between items-center px-4 md:px-8">
            <a href="/" class="text-xl font-black tracking-wider text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400 select-none font-mono-cyber">
                💎 SMARTBIZ <span class="text-blue-400 text-xs px-2 py-0.5 border border-blue-500/20 rounded-lg bg-blue-500/5 tracking-normal">MEGA-OS v5</span>
            </a>
            <div class="flex items-center space-x-6 space-x-reverse">
                <a href="/" class="text-slate-300 hover:text-blue-400 transition text-sm font-semibold flex items-center gap-1.5">🛍️ <span class="hidden md:inline">קטלוג</span> פרימיום</a>
                <button onclick="toggleCartDrawer()" class="relative text-slate-300 hover:text-blue-400 transition text-sm font-semibold cursor-pointer flex items-center gap-1.5">
                    🛒 <span class="hidden md:inline">סל</span> קניות מהיר
                    <span id="cart-badge" class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white text-[10px] px-2 py-0.5 rounded-full font-bold shadow-md shadow-blue-900/50 font-mono-cyber">0</span>
                </button>
                <a href="/admin" class="bg-gradient-to-r from-blue-600 to-indigo-600 px-4 py-2 rounded-xl text-xs font-bold hover:from-blue-500 hover:to-indigo-500 shadow-lg shadow-blue-950/50 transition duration-300">⚙️ קונסולת ניהול</a>
            </div>
        </div>
    </nav>

    <main class="container mx-auto p-4 md:p-8 flex-grow z-10">
        CHANNELS_CONTENT_PLACEHOLDER
    </main>

    <div id="cart-drawer" class="fixed inset-0 z-50 hidden transition-opacity duration-300">
        <div class="absolute inset-0 bg-black/70 backdrop-blur-md transition-opacity" onclick="toggleCartDrawer()"></div>
        <div class="absolute inset-y-0 right-0 max-w-full flex">
            <div id="drawer-panel" class="w-screen max-w-md bg-[#050914] border-l border-slate-900/60 shadow-2xl flex flex-col p-6 transform translate-x-full drawer-transition">
                <div class="flex justify-between items-center mb-6 border-b border-slate-900 pb-4">
                    <h2 class="text-lg font-black text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-400">🛒 סל קניות מהיר</h2>
                    <button onclick="toggleCartDrawer()" class="text-slate-400 hover:text-white text-2xl cursor-pointer p-1 transition">&times;</button>
                </div>
                
                <div id="drawer-items-container" class="flex-grow overflow-y-auto space-y-3 pr-1">
                    </div>
                
                <div class="border-t border-slate-900/80 pt-4 mt-4 space-y-4">
                    <div class="flex justify-between items-center font-bold">
                        <span class="text-slate-400 text-sm">לתשלום זמני:</span>
                        <span id="drawer-total" class="text-xl font-black font-mono-cyber text-blue-400">0₪</span>
                    </div>
                    <a href="/cart" class="block text-center bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-3.5 rounded-xl font-bold hover:from-blue-500 hover:to-indigo-500 transition shadow-lg shadow-blue-950/50 text-xs">🔒 מעבר לקופה מאובטחת</a>
                </div>
            </div>
        </div>
    </div>

    <div class="fixed bottom-6 right-6 z-40">
        <button onclick="toggleAIChat()" class="bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 p-3.5 rounded-full shadow-2xl hover:scale-105 transition-all cursor-pointer border border-white/10 group">
            <span class="text-xl group-hover:rotate-12 block transition">🤖</span>
        </button>
    </div>

    <div id="ai-chat-window" class="fixed bottom-24 right-6 w-80 md:w-96 h-[450px] glass-panel rounded-3xl shadow-2xl z-40 hidden flex-col overflow-hidden animate-fade-in">
        <div class="bg-gradient-to-r from-blue-900/50 to-indigo-900/50 p-4 border-b border-white/5 flex justify-between items-center">
            <div>
                <h4 class="font-bold text-xs text-white">SmartBiz AI Assistant ⚡</h4>
                <p class="text-[10px] text-blue-400 font-medium">יועץ רכישות חכם ומחובר למלאי</p>
            </div>
            <button onclick="toggleAIChat()" class="text-slate-400 hover:text-white cursor-pointer">&times;</button>
        </div>
        <div id="ai-messages" class="flex-grow p-4 overflow-y-auto space-y-3 text-xs">
            <div class="bg-slate-900/60 p-3 rounded-2xl border border-white/5 text-slate-300 max-w-[85%] ml-auto">
                היי! אני עוזר ה-AI של איתי. אני מכיר את כל המלאי והמחירים בחנות בזמן אמת. תשאל אותי משהו כמו: "איזה מחשב יש לכם?" או "תמליץ לי על אוזניות".
            </div>
        </div>
        <div class="p-3 border-t border-white/5 bg-slate-950/40 flex gap-2">
            <input type="text" id="ai-input" placeholder="שאל את ה-AI על מוצרים או קופונים..." onkeypress="if(event.key==='Enter') sendAIMessage()" class="bg-slate-900 border border-slate-800 rounded-xl p-2.5 text-xs text-white flex-grow focus:outline-none focus:border-blue-500">
            <button onclick="sendAIMessage()" class="bg-blue-600 hover:bg-blue-500 px-3.5 rounded-xl font-bold text-xs transition cursor-pointer">🚀</button>
        </div>
    </div>

    <div id="toast-container" class="fixed bottom-6 left-6 z-50 space-y-2 max-w-sm w-full"></div>

    <footer class="border-t border-slate-950 p-5 text-center text-[11px] text-slate-600 mt-12 bg-[#02040a]">
        SmartBiz Corporation Global Ecosystem Architecture • Model 2026 Enterprise Framework v5.0
    </footer>

    <script>
        function toggleCartDrawer() {
            const drawer = document.getElementById('cart-drawer');
            const panel = document.getElementById('drawer-panel');
            
            if(drawer.classList.contains('hidden')) {
                drawer.classList.remove('hidden');
                setTimeout(() => { panel.classList.remove('translate-x-full'); }, 10);
                updateDrawerCart();
            } else {
                panel.classList.add('translate-x-full');
                setTimeout(() => { drawer.classList.add('hidden'); }, 300);
            }
        }

        function toggleAIChat() {
            const win = document.getElementById('ai-chat-window');
            win.classList.toggle('hidden');
            if(!win.classList.contains('hidden')) {
                document.getElementById('ai-input').focus();
            }
        }

        function sendAIMessage() {
            const input = document.getElementById('ai-input');
            const query = input.value.strip ? input.value.strip() : input.value.trim();
            if(!query) return;
            
            const container = document.getElementById('ai-messages');
            
            // הודעת משתמש
            container.innerHTML += `
                <div class="bg-blue-600/20 p-3 rounded-2xl border border-blue-500/20 text-blue-300 max-w-[85%] mr-auto font-semibold">
                    ${query}
                </div>
            `;
            input.value = '';
            container.scrollTop = container.scrollHeight;
            
            // פנייה לשרת לקבלת מענה מה-AI הפנימי
            fetch(`/api/ai-chat?q=${encodeURIComponent(query)}`)
                .then(res => res.json())
                .then(data => {
                    container.innerHTML += `
                        <div class="bg-slate-900/60 p-3 rounded-2xl border border-white/5 text-slate-300 max-w-[85%] ml-auto animate-fade-in">
                            ${data.response}
                        </div>
                    `;
                    container.scrollTop = container.scrollHeight;
                });
        }

        function showToast(message, type='info') {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            
            let themeClasses = "border-blue-500/30 bg-slate-900/95 text-blue-400 bento-glow-blue";
            if(type === 'success') { themeClasses = "border-green-500/30 bg-emerald-950/95 text-green-400 bento-glow-green"; }
            
            toast.className = `p-4 rounded-2xl border shadow-2xl backdrop-blur-md text-xs font-bold flex items-center justify-between transition-all duration-300 transform translate-y-4 opacity-0 ${themeClasses}`;
            toast.innerHTML = `<span>${message}</span><button onclick="this.parentElement.remove()" class="text-slate-500 hover:text-white mr-2 cursor-pointer text-sm">&times;</button>`;
            
            container.appendChild(toast);
            setTimeout(() => { toast.classList.remove('translate-y-4', 'opacity-0'); }, 10);
            
            setTimeout(() => {
                toast.classList.add('opacity-0', 'translate-y-2');
                setTimeout(() => { toast.remove(); }, 300);
            }, 3800);
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
                        container.innerHTML = '<div class="text-center py-12 text-slate-500 text-xs font-medium">הסל ריק. מוצרים שתבחר יופיעו כאן.</div>';
                        return;
                    }
                    
                    for (const [name, details] of Object.entries(data.items)) {
                        container.innerHTML += `
                            <div class="bg-slate-900/40 border border-slate-900 p-3 rounded-xl flex justify-between items-center transition hover:bg-slate-900/60">
                                <div>
                                    <h4 class="font-bold text-xs text-slate-200">${name}</h4>
                                    <p class="text-[10px] text-slate-500 mt-0.5">${details.price}₪ × ${details.qty}</p>
                                </div>
                                <span class="font-bold text-xs font-mono-cyber text-blue-400">${details.price * details.qty}₪</span>
                            </div>
                        `;
                    }
                });
        }
        
        document.addEventListener('DOMContentLoaded', () => {
            fetch('/api/cart-data').then(res=>res.json()).then(data=>{
                document.getElementById('cart-badge').innerText = data.total_qty;
            });
        });
    </script>
</body>
</html>
"""

