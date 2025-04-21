from django.core.management.base import BaseCommand
from user.models import Product, Reviews
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import time

class Command(BaseCommand):
    help = "Scrapes product reviews from Flipkart and stores them in the DB"

    def handle(self, *args, **kwargs):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"user-agent={headers['User-Agent']}")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        product_urls = [
            "https://www.flipkart.com/samsung-galaxy-f06-5g-lit-violet-128-gb/p/itm140da3412b73b?pid=MOBH9AS4FA5RUHSY",
            "https://www.flipkart.com/xiaomi-14-civi-shadow-black-256-gb/p/itmdf7287cef4f11?pid=MOBHFGU7EJXG5M4M",
            "https://www.flipkart.com/infinix-note-50x-5g-enchanted-purple-128-gb/p/itm094fc01ad674b?pid=MOBHAYMDWKHTQ4US",
            "https://www.flipkart.com/apple-iphone-13-starlight-128-gb/p/itmc9604f122ae7f?pid=MOBG6VF5ADKHKXFX"
        ]

        for item in product_urls:
            try:
                driver.get(item)
                time.sleep(3)
                soup = bs(driver.page_source, "html.parser")

                try:
                    product_name = soup.find("span", {"class": "VU-ZEz"}).text.strip()
                except:
                    product_name = "Unknown Product"

                self.stdout.write(self.style.SUCCESS(f"Scraping: {product_name}"))

                product_obj, _ = Product.objects.get_or_create(productname=product_name)

                ratings = soup.find_all("div", class_="XQDdHH Ga3i8K")
                titles = soup.find_all("div", class_="cPHDOP")
                bodies = soup.find_all("div", class_="ZmyHeo")

                for i in range(len(ratings)):
                    try:
                        rating = ratings[i].text.strip()
                        title = titles[i].text.strip() if i < len(titles) else ''
                        body = bodies[i].div.text.strip() if bodies[i].div else ''

                        Reviews.objects.create(
                            product=product_obj,
                            rating=rating,
                            review=body,
                            created_by=None,
                            updated_by=None
                        )
                    except Exception as e:
                        continue

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error scraping {item}: {e}"))

        driver.quit()
        self.stdout.write(self.style.SUCCESS("✅ Scraping completed successfully."))
