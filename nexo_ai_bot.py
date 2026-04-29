import re
import auto_publish

print("🤖 NEXO MASTER BOT: ANTI-BLOCK MODE STARTED...")
print("✅ Fixing Images and Affiliate Link Redirects...")

# ==========================================
# 1. YOUR REAL AFFILIATE IDs
# ==========================================
AMAZON_TAG = "myid1991-21"
FLIPKART_EXT = "affgrowth&affExtParam1=ENKR20260307A1862482668&affExtParam2=4854510"

# ==========================================
# 2. THE ANTI-BLOCK PRODUCT DATABASE
# (Using Un-blockable High-Quality Images)
# ==========================================
def get_real_shopping_data():
    raw_products = [
        # --- 📱 MOBILES & TECH ---
        {
            "category": "📱 Mobiles & Tech",
            "title": "Apple iPhone 15 (128 GB) - Black",
            "price": "₹69,900",
            "base_url": "https://www.amazon.in/dp/B0CHX1W1XY",
            "platform": "amazon",
            "image_url": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?auto=format&fit=crop&w=500&q=80" # Unblockable iPhone
        },
        {
            "category": "📱 Mobiles & Tech",
            "title": "OnePlus 12R (8GB RAM, 128GB)",
            "price": "₹39,999",
            "base_url": "https://www.amazon.in/dp/B0CQPTMNWT",
            "platform": "amazon",
            "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=500&q=80"
        },
        {
            "category": "📱 Mobiles & Tech",
            "title": "Samsung Galaxy S24 Ultra 5G",
            "price": "₹1,29,999",
            "base_url": "https://www.amazon.in/dp/B0CS3XHBBW",
            "platform": "amazon",
            "image_url": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?auto=format&fit=crop&w=500&q=80"
        },
        {
            "category": "📱 Mobiles & Tech",
            "title": "Nothing Phone (2a) 5G - White",
            "price": "₹25,999",
            "base_url": "https://www.flipkart.com/nothing-phone-2a-5g-white-128-gb/p/itme119e71ec26de",
            "platform": "flipkart",
            "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?auto=format&fit=crop&w=500&q=80"
        },

        # --- 💻 LAPTOPS & ELECTRONICS ---
        {
            "category": "💻 Laptops & Electronics",
            "title": "Apple MacBook Air Laptop M1 chip",
            "price": "₹74,990",
            "base_url": "https://www.amazon.in/dp/B08N5W4NNB",
            "platform": "amazon",
            "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=500&q=80"
        },
        {
            "category": "💻 Laptops & Electronics",
            "title": "Sony WH-1000XM5 Wireless Headphones",
            "price": "₹26,990",
            "base_url": "https://www.amazon.in/dp/B0A42V7B9V",
            "platform": "amazon",
            "image_url": "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?auto=format&fit=crop&w=500&q=80"
        },
        {
            "category": "💻 Laptops & Electronics",
            "title": "Samsung 43 inches Crystal iSmart 4K TV",
            "price": "₹28,990",
            "base_url": "https://www.amazon.in/dp/B0C1QG8RFW",
            "platform": "amazon",
            "image_url": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?auto=format&fit=crop&w=500&q=80"
        },
        {
            "category": "💻 Laptops & Electronics",
            "title": "Apple iPad (10th Generation)",
            "price": "₹34,900",
            "base_url": "https://www.amazon.in/dp/B0BJLXV3R9",
            "platform": "amazon",
            "image_url": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?auto=format&fit=crop&w=500&q=80"
        },

        # --- 🛋️ HOME & LIFESTYLE ---
        {
            "category": "🛋️ Home & Lifestyle",
            "title": "Philips Digital Air Fryer HD9252/90",
            "price": "₹8,999",
            "base_url": "https://www.amazon.in/dp/B0977N91P9",
            "platform": "amazon",
            "image_url": "https://images.unsplash.com/photo-1628840042765-356cda07504e?auto=format&fit=crop&w=500&q=80"
        },
        {
            "category": "🛋️ Home & Lifestyle",
            "title": "Xiaomi Robot Vacuum Cleaner 2Pro",
            "price": "₹24,999",
            "base_url": "https://www.amazon.in/dp/B0B6PC85B1",
            "platform": "amazon",
            "image_url": "https://images.unsplash.com/photo-1589923188900-85dae523342b?auto=format&fit=crop&w=500&q=80"
        },
        {
            "category": "🛋️ Home & Lifestyle",
            "title": "Puma Men's Sneakers",
            "price": "₹1,499",
            "base_url": "https://www.amazon.in/dp/B0BM9C9B4Z",
            "platform": "amazon",
            "image_url": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?auto=format&fit=crop&w=500&q=80"
        },
        {
            "category": "🛋️ Home & Lifestyle",
            "title": "Premium Ergonomic Office Chair",
            "price": "₹8,990",
            "base_url": "https://www.amazon.in/dp/B08RD8F965",
            "platform": "amazon",
            "image_url": "https://images.unsplash.com/photo-1505843490538-5133c6c7d0e1?auto=format&fit=crop&w=500&q=80"
        }
    ]

    processed_deals = []
    
    for deal in raw_products:
        url = deal['base_url']
        
        # Affiliate links perfectly constructed
        if deal['platform'] == 'amazon':
            url += f"?tag={AMAZON_TAG}" if '?' not in url else f"&tag={AMAZON_TAG}"
        elif deal['platform'] == 'flipkart':
            url += f"?{FLIPKART_EXT}" if '?' not in url else f"&{FLIPKART_EXT}"

        processed_deals.append({
            "category": deal['category'],
            "title": deal['title'],
            "price": deal['price'],
            "image_url": deal['image_url'],
            "processed_url": url,
            "badge": deal['platform'].capitalize()
        })
        
    return processed_deals

# ==========================================
# 3. HTML BUILDER (Fixed Link Logic)
# ==========================================
def build_fixed_html(deals_list):
    print("🌐 Rebuilding Grid with Clean Links & Images...")
    
    from collections import defaultdict
    grouped_deals = defaultdict(list)
    for deal in deals_list:
        grouped_deals[deal['category']].append(deal)

    master_html = ""
    
    for category, deals in grouped_deals.items():
        section_html = f"""
        <section class="w-full mb-16 block clear-both">
            <div class="mb-6 border-l-4 border-[#ff0054] pl-4 w-full">
                <h2 class="text-3xl font-bold text-white mb-1 uppercase tracking-tight">{category}</h2>
                <p class="text-gray-400 text-sm">Top verified AI selections.</p>
            </div>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4 gap-6 w-full">
        """
        
        for deal in deals:
            # FIXED: Removed 'noreferrer' so affiliate links track & open properly
            section_html += f"""
                <div class="bg-[#1a1a1a] border border-[#333] rounded-xl overflow-hidden hover:border-[#ff0054] hover:shadow-[0_0_15px_rgba(255,0,84,0.3)] transition-all duration-300 flex flex-col h-full relative group">
                    <div class="absolute top-3 left-3 bg-[#ff0054] text-white text-[10px] font-bold px-2 py-1 rounded uppercase tracking-wider z-10">
                        {deal['badge']}
                    </div>
                    <div class="relative h-56 bg-white w-full flex items-center justify-center overflow-hidden">
                        <img src="{deal['image_url']}" alt="{deal['title']}" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                    </div>
                    <div class="p-5 flex flex-col flex-grow border-t border-[#333]">
                        <h3 class="text-gray-200 font-semibold text-sm line-clamp-2 mb-2 flex-grow">{deal['title']}</h3>
                        <div class="mt-2 mb-4">
                            <p class="text-[#ff0054] font-extrabold text-xl">{deal['price']}</p>
                        </div>
                        <a href="{deal['processed_url']}" target="_blank" rel="nofollow" class="w-full block text-center bg-[#ff0054] hover:bg-[#d40045] text-white font-bold py-2.5 rounded-lg text-sm transition-colors mt-auto shadow-[0_4px_14px_0_rgba(255,0,84,0.39)] hover:shadow-[0_6px_20px_rgba(255,0,84,0.23)]">
                            BUY NOW
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

if __name__ == "__main__":
    final_deals = get_real_shopping_data()
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
        
    print("🚀 Fixes Applied! Pushing to Vercel...")
    auto_publish.auto_publish()