import requests
from bs4 import BeautifulSoup
import smtplib
import time


url = [
    'https://www.amazon.com.mx/gp/product/B07CZ9NPKV/ref=ox_sc_saved_title_2?smid=AVDBXBAVVSXLQ&psc=1',
    'https://www.amazon.com.mx/gp/product/B08B3L2KCK/ref=ox_sc_saved_title_1?smid=APIF988DI4NGP&psc=1',
    'https://www.amazon.com.mx/gp/product/B08HJRGQ8V/ref=ox_sc_saved_title_2?smid=A1XRLO0K6AXY1I&psc=1',
    'https://www.amazon.com.mx/gp/product/B00TXVEQ8Y/ref=ox_sc_saved_title_3?smid=AFLGKHW1ZCQVN&psc=1',
    'https://www.amazon.com.mx/Xiaomi-Celular-Redmi-Black-128Gb/dp/B08GP297M1/ref=sr_1_1?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=redmi+note+9&qid=1603945775&sr=8-1'
]
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

username = "tamagochihaxx@gmail.com"
the_password = 'xfbmocjqrjxdbgse'

def run_program():
    while True:
        print("""
1.- Log In
2.- Register
3.- Skip
4.- Quit
        """)
        option = input("> ")
        if option == "3":
            print("Getting information about the products...")
            get_products()
            send_email()
        if option != "3":
            print("Try again")
        if option == "4":
            break


def login():


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
        #print(f"Getting information about", product_title, "with current price at: $", converted_price, ". Link: ", products)
        message = (f"{product_title} is currently at ${converted_price}.\n Link: {products}\n\n---------------------------------------")
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

    print("####################################")
    print("#                                  #")
    print("#       EMAIL HAS BEEN SENT        #")
    print("#                                  #")
    print("####################################")
    server.quit()

run_program()