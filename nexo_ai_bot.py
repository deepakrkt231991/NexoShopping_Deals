import feedparser
import re
import random
from datetime import datetime
import auto_publish  # <--- BINGO! Direct connection to push changes

print("🤖 NEXO MASTER BOT (God Mode) Started...")
print(f"🕒 Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ==========================================
# 1. AFFILIATE IDs & LINKS CONFIGURATION
# ==========================================
AMAZON_TAG = "myid1991-21"
FLIPKART_EXT = "affgrowth&affExtParam1=ENKR20260307A1862482668&affExtParam2=4854510"
EARNKARO_EXT = "growthte&affExtParam1=ENKR20260307A1862062015&affExtParam2=4854510"
CPAGRIP_URLS = ["https://optilinklock.com/1887152", "https://optilinklock.com/1887151"]

# ==========================================
# 2. DATA SOURCE (The Categorized Deals Engine)
# ==========================================

def get_news_source():
    """Fetches real trading news to monetize clicks with CPAGrip."""
    print("📈 Scraping Real-Time Trading & Finance News...")
    news_feed = feedparser.parse("https://news.google.com/rss/search?q=trading+finance+offers+india&hl=en-IN&gl=IN&ceid=IN:en")
    
    processed_news = []
    for entry in news_feed.entries[:3]: # Top 3 only
        # Generic high-tech images for modern feel
        news_images = [
            "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=400&q=80", # Trading chart
            "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=400&q=80", # Tech network
            "https://images.unsplash.com/photo-1526628953301-3e589a6a8b74?auto=format&fit=crop&w=400&q=80"  # Graphs
        ]
        cpa_link = random.choice(CPAGRIP_URLS)
        processed_news.append({
            "category": "Trading News",
            "title": entry.title,
            "price": "Market Update",
            "image_url": random.choice(news_images),
            "processed_url": cpa_link,
            "badge": "CPA Offer",
            "platform": "CPA"
        })
    return processed_news

def get_shopping_source():
    """Pre-loaded high-converting categorized deals."""
    print("🛒 Populating E-Commerce Deals List (Categorized)...")
    
    raw_shopping = [
        # --- CATEGORY: MOBILES ---
        {
            "category": "Mobiles",
            "title": "iPhone 15 (128 GB) - Blue (Pre-order / Deal)",
            "price": "₹69,900",
            "base_url": "https://www.amazon.in/dp/B0CHX1W1XY",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/71d7rfSl0wL._SX679_.jpg",
        },
        {
            "category": "Mobiles",
            "title": "Samsung Galaxy S24 Ultra (Titanium Black)",
            "price": "₹1,29,999",
            "base_url": "https://www.flipkart.com/search?q=samsung+s24+ultra",
            "platform": "flipkart",
            "image_url": "https://rukminim2.flixcart.com/image/416/416/xif0q/mobile/5/r/x/-original-imagx99ne9jhv26b.jpeg",
        },
        {
            "category": "Mobiles",
            "title": "Nothing Phone (2a) 5G - White",
            "price": "₹25,999",
            "base_url": "https://www.amazon.in/dp/B0CWPC6K33",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/71m67YJj3kL._SX679_.jpg",
        },
        
        # --- CATEGORY: ELECTRONICS ---
        {
            "category": "Electronics",
            "title": "MacBook Air M3 Chip - 13 inch",
            "price": "₹1,09,900",
            "base_url": "https://www.amazon.in/dp/B0CWPCNVDZ",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/71IsfK3zGML._SX679_.jpg",
        },
        {
            "category": "Electronics",
            "title": "PlayStation 5 Console (Slim model)",
            "price": "₹54,990",
            "base_url": "https://www.amazon.in/dp/B0D189Y47B",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/51w9h9fL3zL._SX679_.jpg",
        },
        {
            "category": "Electronics",
            "title": "Sony WH-1000XM5 Noise Cancelling Headphones",
            "price": "₹26,990",
            "base_url": "https://www.amazon.in/dp/B0A42V7B9V",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/61FwW6u3x9L._SX679_.jpg",
        },
        {
            "category": "Electronics",
            "title": "Dell XPS 13 Laptop - Core i7",
            "price": "₹1,45,000",
            "base_url": "https://www.flipkart.com/search?q=dell+xps+13",
            "platform": "flipkart",
            "image_url": "https://rukminim2.flixcart.com/image/416/416/xif0q/computer/v/l/l/-original-imagv4g6t6z4zyu7.jpeg",
        },

        # --- CATEGORY: HOME & LIFESTYLE ---
        {
            "category": "Home & Lifestyle",
            "title": "Premium Coffee Maker - Automatic",
            "price": "₹12,499",
            "base_url": "https://www.amazon.in/dp/B0A42Z5G9D",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/71F1L0PzWmL._SX679_.jpg",
        },
        {
            "category": "Home & Lifestyle",
            "title": "Robot Vacuum Cleaner with Mop",
            "price": "₹29,990",
            "base_url": "https://earnkaro.com/search?q=robot+vacuum",
            "platform": "earnkaro",
            "image_url": "https://rukminim2.flixcart.com/image/416/416/xif0q/vacuum-cleaner/f/h/b/-original-imagp8zzv3g3zv3d.jpeg",
        },
        {
            "category": "Home & Lifestyle",
            "title": "Ergonomic Office Chair - White",
            "price": "₹8,999",
            "base_url": "https://www.amazon.in/dp/B0D2C87V9X",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/61k8R+qN0jL._SX679_.jpg",
        },

        # --- CATEGORY: SPECIAL OFFERS ---
        {
            "category": "Special Offers",
            "title": "Exclusive EarnKaro Cashback Deal",
            "price": "GET CASHBACK",
            "base_url": "https://earnkaro.com/top-offers",
            "platform": "earnkaro",
            "image_url": "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?auto=format&fit=crop&w=400&q=80",
        }
    ]

    processed_shopping = []
    for deal in raw_shopping:
        url = deal['base_url']
        
        # AFFILIATE LINK LOGIC (Perfect handling as requested)
        if deal['platform'] == 'amazon':
            url += f"?tag={AMAZON_TAG}" if '?' not in url else f"&tag={AMAZON_TAG}"
        elif deal['platform'] == 'flipkart':
            url += f"?{FLIPKART_EXT}" if '?' not in url else f"&{FLIPKART_EXT}"
        elif deal['platform'] == 'earnkaro':
            url += f"?{EARNKARO_EXT}" if '?' not in url else f"&{EARNKARO_EXT}"

        processed_shopping.append({
            "category": deal['category'],
            "title": deal['title'],
            "price": deal['price'],
            "image_url": deal['image_url'],
            "processed_url": url,
            "badge": deal['platform'].capitalize(),
            "platform": deal['platform']
        })
    return processed_shopping

# ==========================================
# 3. HTML GRID GENERATOR & AUTO-CATEGORIZATION
# ==========================================
def generate_categorized_html(final_list):
    """Sorts deals and generates HTML with category headers."""
    print("🌐 Organizing deals by Category and generating UI...")
    
    # 1. Sort the list by Category to group them together
    final_list.sort(key=lambda x: x['category'])
    
    # 2. Determine unique categories to create headers
    current_category = ""
    category_html_block = ""
    current_grid_html = ""
    
    for deal in final_list:
        # Check if Category has changed to insert a header and start a new grid
        if deal['category'] != current_category:
            # If this isn't the first category, close the previous grid
            if current_category != "":
                current_grid_html += "</div>" # Closing div of the grid
                category_html_block += current_grid_html
                current_grid_html = "" # Reset grid for next category

            # Update current category
            current_category = deal['category']
            
            # Insert Premium Category Header (Matching mockup design)
            # Dhyan dein: `mb-2 mt-12` isliye hai taaki top navbar ke niche pehla section dabna na jaye,
            # aur har section ke baad thoda gap ho. Pehla header section-specific margins handle karega.
            first_margin_t = "mt-2" if current_category == "Trading News" else "mt-12"
            
            category_html_block += f"""
            <div class="mb-6 border-l-4 border-[#ff0054] pl-4 {first_margin_t} w-full flex-none">
                <h2 class="text-3xl font-bold text-white mb-1 uppercase tracking-tight">{current_category}</h2>
                <p class="text-gray-400 text-sm">Best hand-picked deals from top platforms via AI.</p>
            </div>
            """
            
            # Start a new Grid container for this category
            current_grid_html += '<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 mb-12">'
            
        # Standard Modern Dark Card Logic (As request: perfect images/details)
        # Handle News cards slightly differently (different image handling)
        image_styling = "object-contain" if deal['platform'] != "CPA" else "object-cover"
        white_bg_div = 'class="relative h-48 bg-white p-4 w-full flex items-center justify-center"' if deal['platform'] != "CPA" else 'class="relative h-48 w-full flex items-center justify-center"'
        
        card = f"""
        <div class="bg-[#1a1a1a] border border-[#333] rounded-xl overflow-hidden hover:border-[#ff0054] hover:shadow-[0_0_15px_rgba(255,0,84,0.3)] transition-all duration-300 flex flex-col h-full relative group">
            <div class="absolute top-3 left-3 bg-[#ff0054] text-white text-[10px] font-bold px-2 py-1 rounded uppercase tracking-wider z-10">
                {deal['badge']}
            </div>
            
            <div {white_bg_div}>
                <img src="{deal['image_url']}" alt="{deal['title']}" class="max-w-full max-h-full {image_styling} transition-transform duration-500 group-hover:scale-110">
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
        current_grid_html += card

    # Close the very last grid of the last category
    if current_grid_html != "":
        current_grid_html += "</div>"
        category_html_block += current_grid_html
        
    return category_html_block

# ==========================================
# 4. SITE UPDATER & PUBLISHER
# ==========================================
def update_full_nexo_platform():
    """Main execution pipeline."""
    # 1. Collect Data
    all_data = get_news_source() + get_shopping_source()
    
    # 2. Build Categorized HTML
    master_content_html = generate_categorized_html(all_data)
    
    # 3. Read index.html and update between markers
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    new_html_content = re.sub(
        r'(<!-- DEALS_START -->).*?(<!-- DEALS_END -->)', 
        r'\1\n' + master_content_html + r'\n            <!-- DEALS_END -->', 
        html_content, 
        flags=re.DOTALL
    )

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html_content)
    print("✅ Nexo Platform files updated on local computer!")

if __name__ == "__main__":
    update_full_nexo_platform()
    
    print("🚀 Auto-Publishing to GitHub/Vercel...")
    # Trigger the inherited publisher script
    auto_publish.auto_publish()
    print("🎊 God Mode Complete. Site should update in 1 minute.")