import re

def process_deals(deals):
    processed_deals = []
    for deal in deals:
        url = deal['original_url']
        platform = deal['platform'].lower()

        # Adding Affiliate Tags
        if platform == 'amazon':
            if '?' in url:
                url += '&tag=myid1991-21'
            else:
                url += '?tag=myid1991-21'
        elif platform == 'cpagrip':
            if '?' in url:
                url += '&aff_id=2494241'
            else:
                url += '?aff_id=2494241'
        
        deal['processed_url'] = url
        processed_deals.append(deal)
    return processed_deals

def generate_html_cards(deals):
    html_cards = []
    for deal in deals:
        # Changed to match the exact CSS structure of your index.html
        card = f"""
        <div class="product-card">
            <img src="{deal['image_url']}" alt="{deal['title']}">
            <div class="product-card-content">
                <h3>{deal['title']}</h3>
                <p class="price">Price: {deal['price']}</p>
                <a href="{deal['processed_url']}" target="_blank">View Deal</a>
            </div>
        </div>
        """
        html_cards.append(card)
    return "".join(html_cards)


if __name__ == "__main__":
    # Dummy list of product deals
    product_deals = [
        {
            "title": "Amazon Echo Dot (3rd Gen)",
            "price": "$29.99",
            "original_url": "https://www.amazon.com/echo-dot-3rd-gen-charcoal/dp/B07FZ8S7FG",
            "image_url": "https://m.media-amazon.com/images/I/6182S7MYC2L._AC_SY200_.jpg",
            "platform": "amazon",
        },
        {
            "title": "Exclusive CPAGrip Trading Offer",
            "price": "FREE",
            "original_url": "https://www.cpagrip.com/offer?id=123",
            "image_url": "https://via.placeholder.com/150",
            "platform": "cpagrip",
        },
        {
            "title": "Smart Watch Deal",
            "price": "$50.00",
            "original_url": "https://www.amazon.com/some-other-product/dp/B08ABCD123",
            "image_url": "https://via.placeholder.com/150",
            "platform": "amazon",
        }
    ]

    # 1. Process the deals
    processed_deals = process_deals(product_deals)

    # 2. Generate matching HTML
    generated_html = generate_html_cards(processed_deals)

    # 3. Read the index.html file
    with open("index.html", "r", encoding="utf-8") as f:
        index_html_content = f.read()

    # 4. Replace the content using the correct Start and End markers
    updated_html_content = re.sub(
        r".*?",
        f"\n{generated_html}\n        ",
        index_html_content,
        flags=re.DOTALL,
    )

    # 5. Save the updated file
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(updated_html_content)

    print("✅ SUCCESS: deal_processor.py script executed successfully. index.html updated.")