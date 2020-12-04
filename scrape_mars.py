#import dependencies

from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
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

#find title
    mars_soup_title = soup.find_all("div", class_= "content_title")    
    title= mars_soup_title[1].get_text()

#find paragraph
    mars_soup_paragraph = soup.find_all("div", class_= "article_teaser_body")
    paragraph= mars_soup_paragraph[0].get_text()

#next url to be scraped
    url1 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url1)
    time.sleep(2)

#find and click links
    browser.links.find_by_partial_text("FULL IMAGE")[0].click()
    browser.links.find_by_partial_text("more info")[0].click()

#use text under figure to find image
    text_soup = soup.find_all("figure", class_= "lede")
    figure= text_soup[0]
    image_soup = figure.find_all("a", href = True)
    image_soup[0]["href"]

#define feature image url
    featured_image_url = "https://www.jpl.nasa.gov" + image_soup[0]["href"]



