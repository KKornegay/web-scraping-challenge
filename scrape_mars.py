#import dependencies

from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

#create function to initalize browser
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

#url to be scraped
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)

# Scrape page into Soup

    html = browser.html
    soup = bs(html, "html.parser")

