
# # from selenium import webdriver
# from django.dispatch import receiver
# from django.shortcuts import render
# from .models import *
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup as bs
# from selenium.webdriver.common.by import By
# import time
# from django.db.models.signals import post_migrate


# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument(f"user-agent={headers['User-Agent']}")

# # Start driver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# prod_1="https://www.flipkart.com/apple-iphone-se-black-64-gb/p/itm4d3d5718a5c95?pid=MOBFWQ6BR3MK7AUG&lid=LSTMOBFWQ6BR3MK7AUGEJNZLF&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=nmenu_sub_Electronics_0_iPhone%20SE&fm=neo%2Fmerchandising&iid=49e95733-5cfe-4159-9b26-c4b0ec4609a4.MOBFWQ6BR3MK7AUG.SEARCH&ppt=pp&ppn=pp&ssid=yse3smkv5s0000001745149704810"
# prod_2= "https://www.flipkart.com/samsung-galaxy-f06-5g-lit-violet-128-gb/p/itm140da3412b73b?pid=MOBH9AS4FA5RUHSY"
# prod_3="https://www.flipkart.com/xiaomi-14-civi-shadow-black-256-gb/p/itmdf7287cef4f11?pid=MOBHFGU7EJXG5M4M&fm=organic&ppt=pp&ppn=pp&ssid=k052hui0ts0000001745148835448"
# prod_4="https://www.flipkart.com/infinix-note-50x-5g-enchanted-purple-128-gb/p/itm094fc01ad674b?pid=MOBHAYMDWKHTQ4US&lid=LSTMOBHAYMDWKHTQ4USZANA5I&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_2&otracker=browse&fm=neo%2Fmerchandising&iid=fdb6a505-a557-4bbf-9506-a98ace9fa32e.MOBHAYMDWKHTQ4US.SEARCH&ppt=pp&ppn=pp&ssid=pqtit2oy9c0000001745149837967"
# prod_5="https://www.flipkart.com/apple-iphone-13-starlight-128-gb/p/itmc9604f122ae7f?pid=MOBG6VF5ADKHKXFX&lid=LSTMOBG6VF5ADKHKXFX4LCPEV&marketplace=FLIPKART&q=apple+mobiles&store=tyy%2F4io&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&fm=search-autosuggest&iid=1f20d18c-af54-4e8e-abc5-de73be625d69.MOBG6VF5ADKHKXFX.SEARCH&ppt=sp&ppn=sp&ssid=o5uht1ro9c0000001745149965102&qH=cb603b9543d774e1"
# product_url=[prod_2,prod_2,prod_3,prod_4,prod_5]

# @receiver(post_migrate)
# def run_after_server(sender, **kwargs):
#     for item in product_url:
#         driver.get(item)
#         time.sleep(3)
        
#         soup = bs(driver.page_source, "html.parser")


#         try:
#             product_name = soup.find("span", {"class": "VU-ZEz"}).text.strip()
#         except:
#             product_name = "Unknown Product"

#         print("Product Name:", product_name)
#         product_obj, _ = Product.objects.get_or_create(productname=product_name)
#         reviews = []

#         ratings = soup.find_all("div", class_="XQDdHH Ga3i8K")
#         titles = soup.find_all("div", class_="cPHDOP")
#         bodies = soup.find_all("div", class_="ZmyHeo")
        
#         for i in range(len(ratings)):
#          try:
#              rating = ratings[i].text.strip()
#              title = titles[i].text.strip() if i < len(titles) else ''
#              body = bodies[i].div.text.strip() if bodies[i].div else ''
#              reviews.append({
#             "rating": rating,
#             "title": title,
#             "review": body
#         })
#              Reviews.objects.create(
#                     product=product_obj,
#                     rating=rating,
#                     review=body,
#                     created_by=None,  
#                     updated_by=None
#                 )
#          except:
#            continue

#         driver.quit()


#         for r in reviews:
#           print(r)
    
    