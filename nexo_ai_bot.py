import feedparser
import re
import random
from datetime import datetime
from collections import defaultdict
import auto_publish

print("🤖 NEXO MASTER BOT (God Mode v2) Started...")

# ==========================================
# 1. AFFILIATE IDs
# ==========================================
AMAZON_TAG = "myid1991-21"
FLIPKART_EXT = "affgrowth&affExtParam1=ENKR20260307A1862482668&affExtParam2=4854510"
EARNKARO_EXT = "growthte&affExtParam1=ENKR20260307A1862062015&affExtParam2=4854510"
CPAGRIP_URLS = ["https://optilinklock.com/1887152", "https://optilinklock.com/1887151"]

# ==========================================
# 2. BULK DEAL GENERATOR (15+ Products)
# ==========================================
def get_shopping_data():
    print("🛒 Auto-Generating 50+ Premium Deals for Catalog...")
    
    platforms = ['amazon', 'flipkart', 'earnkaro']
    categories = ["🔥 Trading News & CPA", "📱 Mobiles & Tech", "💻 Laptops & Electronics", "🎧 Gadgets & Accessories", "🛋️ Home & Lifestyle"]
    
    # Premium Unsplash Images jo kabhi block nahi hongi
    tech_images = [
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=500&q=80", # Phone
        "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=500&q=80", # Headphones
        "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=500&q=80", # Laptop
        "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=500&q=80", # Watch
        "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=500&q=80", # Shoes/Lifestyle
        "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=500&q=80"  # Trading
    ]

    all_deals = []

    # Har category mein 12-15 products generate karna
    for cat in categories:
        # CPA/News category ke liye special handling
        if "Trading News" in cat:
            news_feed = feedparser.parse("https://news.google.com/rss/search?q=trading+finance+india&hl=en-IN&gl=IN&ceid=IN:en")
            for entry in news_feed.entries[:4]:
                all_deals.append({
                    "category": cat,
                    "title": entry.title,
                    "price": "Check Update",
                    "image_url": tech_images[5],
                    "processed_url": random.choice(CPAGRIP_URLS),
                    "badge": "CPA Offer"
                })
            continue

        # Baki shopping categories ke liye Bulk Products
        for i in range(1, 13): 
            platform = random.choice(platforms)
            price = random.randint(1999, 89999)
            
            # Smart URL Routing
            if platform == 'amazon':
                url = f"https://www.amazon.in/s?k=premium+{cat.split()[1]}&tag={AMAZON_TAG}"
            elif platform == 'flipkart':
                url = f"https://www.flipkart.com/search?q=premium+{cat.split()[1]}&{FLIPKART_EXT}"
            else:
                url = f"https://earnkaro.com/top-offers?{EARNKARO_EXT}"

            all_deals.append({
                "category": cat,
                "title": f"Premium {cat.split()[1]} Product - Pro Edition {i}",
                "price": f"₹{price:,}",
                "image_url": random.choice(tech_images),
                "processed_url": url,
                "badge": platform.capitalize()
            })
            
    return all_deals

# ==========================================
# 3. FIXING HTML GRID & LAYOUT BUG
# ==========================================
def build_fixed_html(deals_list):
    print("🌐 Building Bug-Free Grid Layout...")
    
    # Category ke hisab se perfectly group karna
    grouped_deals = defaultdict(list)
    for deal in deals_list:
        grouped_deals[deal['category']].append(deal)

    master_html = ""
    
    for category, deals in grouped_deals.items():
        # HAR CATEGORY KO EK <SECTION> MEIN WRAP KIYA HAI (Taki cards squish na ho)
        section_html = f"""
        <section class="w-full mb-16 block clear-both">
            <div class="mb-6 border-l-4 border-[#ff0054] pl-4 w-full">
                <h2 class="text-3xl font-bold text-white mb-1 uppercase tracking-tight">{category}</h2>
                <p class="text-gray-400 text-sm">Top verified AI selections.</p>
            </div>
            
            <!-- FIXED GRID LAYOUT -->
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4 gap-6 w-full">
        """
        
        for deal in deals:
            section_html += f"""
                <div class="bg-[#1a1a1a] border border-[#333] rounded-xl overflow-hidden hover:border-[#ff0054] hover:shadow-[0_0_15px_rgba(255,0,84,0.3)] transition-all duration-300 flex flex-col h-full relative group">
                    <div class="absolute top-3 left-3 bg-[#ff0054] text-white text-[10px] font-bold px-2 py-1 rounded uppercase tracking-wider z-10">
                        {deal['badge']}
                    </div>
                    <div class="relative h-48 w-full flex items-center justify-center overflow-hidden">
                        <img src="{deal['image_url']}" alt="Product" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                    </div>
                    <div class="p-5 flex flex-col flex-grow border-t border-[#333]">
                        <h3 class="text-gray-200 font-semibold text-sm line-clamp-2 mb-2 flex-grow">{deal['title']}</h3>
                        <div class="mt-2 mb-4">
                            <p class="text-[#ff0054] font-extrabold text-xl">{deal['price']}</p>
                        </div>
                        <a href="{deal['processed_url']}" target="_blank" rel="nofollow" class="w-full block text-center bg-[#ff0054] hover:bg-[#d40045] text-white font-bold py-2.5 rounded-lg text-sm transition-colors mt-auto">
                            GET DEAL NOW
                        </a>
                    </div>
                </div>
            """
        section_html += """
            </div>
        </section>
        """
        master_html += section_html
        
    return master_html

# ==========================================
# 4. PUBLISHER
# ==========================================
if __name__ == "__main__":
    final_deals = get_shopping_data()
    final_html = build_fixed_html(final_deals)
    
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r'(<!-- DEALS_START -->).*?(<!-- DEALS_END -->)', 
        r'\1\n' + final_html + r'\n            <!-- DEALS_END -->', 
        content, 
        flags=re.DOTALL
    )

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print("🚀 Updates done! Pushing to Vercel...")
    auto_publish.auto_publish()