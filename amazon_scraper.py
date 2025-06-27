# amazon_scraper.py

from playwright.sync_api import sync_playwright

def get_amazon_product_details(product_id):
    url = f"https://www.amazon.in/dp/{product_id}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/114.0.0.0 Safari/537.36"
            )
        )
        page = context.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_selector("#productTitle", timeout=10000)

        title = page.locator("#productTitle").inner_text().strip()
        price = page.locator(".a-price-whole").first.inner_text().strip()
        rating = page.locator(".a-icon-alt").first.inner_text().strip()
        img = page.locator("#imgTagWrapperId img").get_attribute("src")

        browser.close()

        result = {
            "title": title,
            "price": f"₹ {price}",
            "rating": rating,
            "img": img
        }

        return result, None  # Second value for compatibility with your Flask code
