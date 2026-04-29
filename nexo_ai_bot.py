import feedparser
import re
import random
from datetime import datetime
import auto_publish  # <--- BINGO! Direct connection banaya. Subprocess hata diya.

print("🤖 Nexo AI Bot Started: Fetching Real-Time Market Data...")

# ==========================================
# 1. AFFILIATE IDs & LINKS CONFIGURATION
# ==========================================
AMAZON_TAG = "myid1991-21"
FLIPKART_EXT = "affgrowth&affExtParam1=ENKR20260307A1862482668&affExtParam2=4854510"
EARNKARO_EXT = "growthte&affExtParam1=ENKR20260307A1862062015&affExtParam2=4854510"
CPAGRIP_URLS = ["https://optilinklock.com/1887152", "https://optilinklock.com/1887151"]

# ==========================================
# 2. REAL-TIME DATA SCRAPER (Google News API)
# ==========================================
def get_trading_news():
    print("📈 Scraping Daily Trading & Finance News...")
    news_feed = feedparser.parse("https://news.google.com/rss/search?q=trading+finance+offers+india&hl=en-IN&gl=IN&ceid=IN:en")
    
    news_deals = []
    for entry in news_feed.entries[:3]:
        cpa_link = random.choice(CPAGRIP_URLS)
        news_deals.append({
            "title": entry.title,
            "price": "Market Update",
            "image_url": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=400&q=80", 
            "processed_url": cpa_link,
            "badge": "Trading News"
        })
    return news_deals

# ==========================================
# 3. SHOPPING DEALS GENERATOR
# ==========================================
def get_shopping_deals():
    print("🛒 Generating E-Commerce Deals with Affiliate Tags...")
    
    raw_deals = [
        {
            "title": "Trending Smartphone 5G - Flash Sale",
            "price": "₹14,999",
            "base_url": "https://www.amazon.in/dp/B0BDHX8Z63",
            "platform": "amazon",
            "image_url": "https://m.media-amazon.com/images/I/71d7rfSl0wL._SX679_.jpg",
        },
        {
            "title": "Premium Wireless Earbuds",
            "price": "₹1,299",
            "base_url": "https://www.flipkart.com/search?q=earbuds",
            "platform": "flipkart",
            "image_url": "https://rukminim2.flixcart.com/image/416/416/xif0q/headphone/p/r/z/envy-mad-charge-fast-charging-bluetooth-original-imags5gyjrxxy6h6.jpeg",
        },
        {
            "title": "Mega EarnKaro Cashback Offer",
            "price": "Extra ₹500 Off",
            "base_url": "https://earnkaro.com/top-offers",
            "platform": "earnkaro",
            "image_url": "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?auto=format&fit=crop&w=400&q=80",
        }
    ]

    processed = []
    for deal in raw_deals:
        url = deal['base_url']
        
        if deal['platform'] == 'amazon':
            url += f"?tag={AMAZON_TAG}" if '?' not in url else f"&tag={AMAZON_TAG}"
        elif deal['platform'] == 'flipkart':
            url += f"?{FLIPKART_EXT}" if '?' not in url else f"&{FLIPKART_EXT}"
        elif deal['platform'] == 'earnkaro':
            url += f"?{EARNKARO_EXT}" if '?' not in url else f"&{EARNKARO_EXT}"

        processed.append({
            "title": deal['title'],
            "price": deal['price'],
            "image_url": deal['image_url'],
            "processed_url": url,
            "badge": deal['platform'].capitalize()
        })
    return processed

# ==========================================
# 4. HTML BUILDER & AUTO-PUBLISHER
# ==========================================
def update_website(all_deals):
    print("🌐 Updating index.html with Premium Dark/Pink UI...")
    html_cards = []
    
    for deal in all_deals:
        # Modern Dark Card with Neon Pink Accents matching your Figma design
        card = f"""
        <div class="bg-[#1a1a1a] border border-[#333] rounded-xl overflow-hidden hover:border-[#ff0054] hover:shadow-[0_0_15px_rgba(255,0,84,0.3)] transition-all duration-300 flex flex-col h-full relative group">
            <div class="absolute top-3 left-3 bg-[#ff0054] text-white text-[10px] font-bold px-2 py-1 rounded uppercase tracking-wider z-10">
                {deal['badge']}
            </div>
            
            <div class="relative h-48 bg-white p-4 w-full flex items-center justify-center">
                <img src="{deal['image_url']}" alt="{deal['title']}" class="max-w-full max-h-full object-contain transition-transform duration-500 group-hover:scale-110">
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
        html_cards.append(card)

    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Fixed the critical Regex bug here
    new_content = re.sub(
        r'(<!-- DEALS_START -->).*?(<!-- DEALS_END -->)', 
        r'\1\n' + "\n".join(html_cards) + r'\n            <!-- DEALS_END -->', 
        content, 
        flags=re.DOTALL
    )

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✅ Premium UI Applied Successfully!")

if __name__ == "__main__":
    trading_data = get_trading_news()
    shopping_data = get_shopping_deals()
    
    final_deals = trading_data + shopping_data
    update_website(final_deals)
    
    print("🚀 Triggering Auto-Publish to GitHub/Vercel...")
    
    # Ab hum file ko terminal se nahi, seedha Python Function se call kar rahe hain. 
    # Zero Crash Guarantee!
    auto_publish.auto_publish()