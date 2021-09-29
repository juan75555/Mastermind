from requests.sessions import session
from requests_html import HTMLSession
import time

url = "https://www.pccomponentes.com/msi-geforce-rtx-3070-gaming-z-trio-lhr-8gb-gddr6"

while True:
    session = HTMLSession()
    r = session.get(url)
    buy_zone = r.html.find("#btnsWishAddBuy")

    if len(buy_zone) > 0:
        print("HAY STOCK!!!!!")
    else:
        print("Sigue sin haber stock :(")
    
    time.sleep(30)
