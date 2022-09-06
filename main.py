import requests
from bs4 import BeautifulSoup
import smtplib
import lxml.html

amazon_paras = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

az_url = 'https://www.amazon.in/dp/B09VH3R875/ref=sspa_dk_detail_3?psc=1&pd_rd_i=B09VH3R875&pd_rd_w=HfmXO&content-id=amzn1.sym.5210e5d3-37e0-44be-93e0-eb50dad0d2ca&pf_rd_p=5210e5d3-37e0-44be-93e0-eb50dad0d2ca&pf_rd_r=2ZVTKBGQN1XFBV41SHZG&pd_rd_wg=J0FbS&pd_rd_r=9c1e9209-a91b-4be1-9852-4841b7bbe2fa&s=grocery'
target_price = 500
my_email = '*********'
my_password = '********'
to_email = '**************'


response = requests.get(az_url, headers=amazon_paras)

soup = BeautifulSoup(response.text, 'lxml')

price_tag = soup.find(class_= "a-price-whole").getText()

# The following also gets the same result, so either can be used
# price_tag = soup.find('span', {'class': "a-price-whole"}).getText()
# price_tag = soup.select(selector=".a-price-whole")

price = float(price_tag.split('.')[0])


if price < target_price:
    with smtplib.SMTP("smtp.gmail.com") as my_connection:
        my_connection.starttls()
        my_connection.login(user=my_email, password=my_password)
        my_connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject: Amazon Deal \n\n "
                                                                          f"Current Price: {price}"
                                                                          f"Click here - {az_url}")
