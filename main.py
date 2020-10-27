import requests
from bs4 import BeautifulSoup
import smtplib
import time


url = [
    'https://www.amazon.com.mx/gp/product/B07CZ9NPKV/ref=ox_sc_saved_title_2?smid=AVDBXBAVVSXLQ&psc=1',
    'https://www.amazon.com.mx/gp/product/B08B3L2KCK/ref=ox_sc_saved_title_1?smid=APIF988DI4NGP&psc=1',
    'https://www.amazon.com.mx/gp/product/B08HJRGQ8V/ref=ox_sc_saved_title_2?smid=A1XRLO0K6AXY1I&psc=1',
    'https://www.amazon.com.mx/gp/product/B00TXVEQ8Y/ref=ox_sc_saved_title_3?smid=AFLGKHW1ZCQVN&psc=1'
]
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

username = "tamagochihaxx@gmail.com"
the_password = 'xfbmocjqrjxdbgse'

def run_program():
    print("Getting information about the products...")


def get_products():
    global email_message
    email_message = []
    for products in (url):
        page = requests.get(products, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        #time.sleep(10)
        try:
            title = soup.find(id="productTitle").get_text()
        except:
            pass
        if soup.find(id) == "priceblock_ourprice" or "priceblock_dealprice":
            price = soup.find(id="priceblock_ourprice").get_text()
        converted_price = float(price.replace(',', '')[1:])
        product_title = title.strip()[:20]
        print(f"Getting information about", product_title, "with current price at: $", converted_price, ". Link: ", products)
        message = (f"{product_title} is currently at ${converted_price}. Link: {products}")
        email_message.append(message)

def send_email():
    message = "" ""
    for products in email_message:
        message += '\n\n' + products
    print(message)
    mail_setup(message)

def mail_setup(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, the_password)
    server.sendmail(username, 'officialkevinc@hotmail.com', message)

    print("####################################\n#\n#\n#        EMAIL HAS BEEN SENT\n#\n#\n####################################")
    server.quit()

run_program()
get_products()
send_email()