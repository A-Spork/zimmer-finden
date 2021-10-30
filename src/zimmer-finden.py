import requests
from bs4 import BeautifulSoup
import argparse

"""
First Experiment with WG-Gesucht website

Missing : other related websites
"""

pm_argparse = argparse.ArgumentParser()

# argument and parameter directive #
pm_argparse.add_argument( '--startDate' , type=str  , help='date of desired move in DD.MM.YEAR format' )
pm_argparse.add_argument( '--price',  type=int , help='maximum price')
pm_argparse.add_argument( '--poi', type=int, help='location of point of interest')

# read argument and parameters #
pm_args = pm_argparse.parse_args()

# wg-gesucht websites (WG Query)
url1 = "https://www.wg-gesucht.de/wg-zimmer-und-1-zimmer-wohnungen-und-wohnungen-und-haeuser-in-Munster.91.0+1+2+3.1.0.html?offer_filter=1&city_id=91&noDeact=1&categories%5B%5D=0&categories%5B%5D=1&categories%5B%5D=2&categories%5B%5D=3&rent_types%5B%5D=2%2C1"

url2 = "https://www.wg-gesucht.de/wg-zimmer-und-1-zimmer-wohnungen-und-wohnungen-und-haeuser-in-Munster.91.0+1+2+3.1.1.html?categories=0%2C1%2C2%2C3&city_id=91&rent_types%5B0%5D=2&rent_types%5B1%5D=1&noDeact=1&img=1"

def wggesucht(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    
    # main cards for iteration
    announce_card = soup.find_all('div', class_= 'col-sm-8 card_body')
    span_card = soup.find_all('div', class_= 'col-xs-11')

    link = []
    price = []
    info = []

    for announce in announce_card:
        
        announce_link = announce.a.text.replace(' ', '').replace('\n', '')
        announce_price = announce.b.text.replace(' ', '')

        link.append(announce_link)
        price.append(announce_price)

    for subannounce in span_card:

        announce_info = subannounce.span.text.replace('                        ', '').replace('|', '').replace('\n','').replace('               ', ',').replace('        ', ',').replace(' ', ',').replace(',,,,,,', '')

        info.append(announce_info)

    # clear announcement
    if (len(link) == len(price) == len(info)) == False :

        link = link[1: ]
        price = price[1: ]

        print('\n add removed \n')

    print('\n', link, '\n', price, '\n', info, '\n')

wggesucht(url1)
wggesucht(url2)

    # remove old posts
    # option : moving day
    # option : price
    # geocode
    # option : distance to point
    # prelimanry plot before leaflet (or other)

