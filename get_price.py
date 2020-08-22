import requests
from bs4 import BeautifulSoup
import smtplib

def get_price():
    url = 'https://www.amazon.de/Quantum-Einstein-Debate-Nature-Reality/dp/1848310358/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=quantum+manjit+kumar&qid=1598102114&sr=8-1'
    headers = {
    "User-Agent": 'Your User Agent'
    }
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'lxml')
    price = soup.find('span', class_='a-size-medium a-color-price offer-price a-text-normal').get_text().strip()
    raw_price = price[0:5]
    converted_price = float(raw_price.replace(',', '.'))
    if converted_price < 9.0:
        print(converted_price)
        send_email()
    else:
        print('The book is still not affordable!')

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email@gmail.com', 'password')
    subject = 'Quantum by Manjit Kumar is now in your budget!'
    body = "Check the amazon link, as Quantum by Manjit Kumar is now in your budget. https://www.amazon.de/Quantum-Einstein-Debate-Nature-Reality/dp/1848310358/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=quantum+manjit+kumar&qid=1598102114&sr=8-1"
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('email@gmail.com', 'email@gmail.com', msg)
    print('Price has dropped, email sent')
    server.quit()
get_price()