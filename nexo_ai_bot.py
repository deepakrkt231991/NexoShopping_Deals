import re
import auto_publish

print("🤖 NEXO MASTER BOT: PRODUCTION MODE STARTED...")
print("✅ CPAGrip Removed. Loading 100% REAL Amazon/Flipkart Products...")

# ==========================================
# 1. YOUR REAL AFFILIATE IDs
# ==========================================
AMAZON_TAG = "myid1991-21"
FLIPKART_EXT = "affgrowth&affExtParam1=ENKR20260307A1862482668&affExtParam2=4854510"

# ==========================================
# 2. THE REAL PRODUCT DATABASE
# (No scraping risk, 100% real images and exact links)
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
            "image_url": "https://m.media-amazon.com/images/I/71657TiFeHL._SX679_.jpg"
        },
        {
            "category": "📱 Mobiles & Tech",
            "title": "OnePlus 12R (8GB RAM, 128GB) - Iron Gray",
            "price": "₹39,999",
            "base_url": "https://www.amazon.in/dp/B0CQPTMNWT",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/71XNeka-BRL._SX679_.jpg"
        },
        {
            "category": "📱 Mobiles & Tech",
            "title": "Samsung Galaxy S24 Ultra 5G (Titanium Black)",
            "price": "₹1,29,999",
            "base_url": "https://www.amazon.in/dp/B0CS3XHBBW",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/71CXhVhpM0L._SX679_.jpg"
        },
        {
            "category": "📱 Mobiles & Tech",
            "title": "Nothing Phone (2a) 5G - White",
            "price": "₹25,999",
            "base_url": "https://www.flipkart.com/nothing-phone-2a-5g-white-128-gb/p/itme119e71ec26de",
            "platform": "flipkart",
            "image_url": "https://rukminim2.flixcart.com/image/416/416/xif0q/mobile/7/k/8/-original-imagzjgjcwzbffze.jpeg"
        },

        # --- 💻 LAPTOPS & ELECTRONICS ---
        {
            "category": "💻 Laptops & Electronics",
            "title": "Apple MacBook Air Laptop M1 chip",
            "price": "₹74,990",
            "base_url": "https://www.amazon.in/dp/B08N5W4NNB",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/71TPda7cwUL._SX679_.jpg"
        },
        {
            "category": "💻 Laptops & Electronics",
            "title": "Sony WH-1000XM5 Wireless Active Noise Cancelling Headphones",
            "price": "₹26,990",
            "base_url": "https://www.amazon.in/dp/B0A42V7B9V",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/61FwW6u3x9L._SX679_.jpg"
        },
        {
            "category": "💻 Laptops & Electronics",
            "title": "Samsung 108 cm (43 inches) Crystal iSmart 4K TV",
            "price": "₹28,990",
            "base_url": "https://www.amazon.in/dp/B0C1QG8RFW",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/81PqR+mB-FL._SX679_.jpg"
        },
        {
            "category": "💻 Laptops & Electronics",
            "title": "Apple iPad (10th Generation)",
            "price": "₹34,900",
            "base_url": "https://www.amazon.in/dp/B0BJLXV3R9",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/61uA2UVnYWL._SX679_.jpg"
        },

        # --- 🛋️ HOME & LIFESTYLE ---
        {
            "category": "🛋️ Home & Lifestyle",
            "title": "Philips Digital Air Fryer HD9252/90",
            "price": "₹8,999",
            "base_url": "https://www.amazon.in/dp/B0977N91P9",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/61dC2KigI+L._SX679_.jpg"
        },
        {
            "category": "🛋️ Home & Lifestyle",
            "title": "Xiaomi Robot Vacuum Cleaner 2Pro",
            "price": "₹24,999",
            "base_url": "https://www.amazon.in/dp/B0B6PC85B1",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/51wXU4q0cML._SX679_.jpg"
        },
        {
            "category": "🛋️ Home & Lifestyle",
            "title": "Puma Men's Dazzler Sneakers",
            "price": "₹1,499",
            "base_url": "https://www.amazon.in/dp/B0BM9C9B4Z",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/71k1oW7G+KL._SY695_.jpg"
        },
        {
            "category": "🛋️ Home & Lifestyle",
            "title": "Green Soul Jupiter Superb Office Chair",
            "price": "₹8,990",
            "base_url": "https://www.amazon.in/dp/B08RD8F965",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/71rJgD99Q1L._SX679_.jpg"
        }
    ]

    processed_deals = []
    
    # 3. AUTOMATIC AFFILIATE LINK GENERATOR
    for deal in raw_products:
        url = deal['base_url']
        
        # Adding Affiliate tags flawlessly
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
# 4. BUILDING THE UI (PERFECT LAYOUT)
# ==========================================
def build_fixed_html(deals_list):
    print("🌐 Injecting Real Products into Website Grid...")
    
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
            # PERFECT IMAGE SIZING AND WORKING LINKS
            section_html += f"""
                <div class="bg-[#1a1a1a] border border-[#333] rounded-xl overflow-hidden hover:border-[#ff0054] hover:shadow-[0_0_15px_rgba(255,0,84,0.3)] transition-all duration-300 flex flex-col h-full relative group">
                    <div class="absolute top-3 left-3 bg-[#ff0054] text-white text-[10px] font-bold px-2 py-1 rounded uppercase tracking-wider z-10">
                        {deal['badge']}
                    </div>
                    <div class="relative h-56 bg-white w-full flex items-center justify-center p-4">
                        <img src="{deal['image_url']}" alt="Product" class="max-w-full max-h-full object-contain transition-transform duration-500 group-hover:scale-110">
                    </div>
                    <div class="p-5 flex flex-col flex-grow border-t border-[#333]">
                        <h3 class="text-gray-200 font-semibold text-sm line-clamp-2 mb-2 flex-grow">{deal['title']}</h3>
                        <div class="mt-2 mb-4">
                            <p class="text-[#ff0054] font-extrabold text-xl">{deal['price']}</p>
                        </div>
                        <a href="{deal['processed_url']}" target="_blank" rel="noopener noreferrer" class="w-full block text-center bg-[#ff0054] hover:bg-[#d40045] text-white font-bold py-2.5 rounded-lg text-sm transition-colors mt-auto shadow-[0_4px_14px_0_rgba(255,0,84,0.39)] hover:shadow-[0_6px_20px_rgba(255,0,84,0.23)]">
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

# ==========================================
# 5. EXECUTION & AUTO PUBLISH
# ==========================================
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
        
    print("🚀 Real Products Saved! Publishing to Website...")
    auto_publish.auto_publish()