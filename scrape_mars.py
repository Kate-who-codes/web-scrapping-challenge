

from splinter import Browser
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import pandas as pd
from chromedriver import executable_path
import time


def scrape_info():
    # Set up Splinter
    executable_path = {"executable_path" : "chromedriver.exe "}
    browser = Browser("chrome", **executable_path, headless=False)

    
    # define url 
    mars_news_url = "https://mars.nasa.gov/news/"
    browser.visit(mars_news_url)

    # create beautiful soup object 
    html = browser.html
    mars_news_soup = BeautifulSoup(html, 'html.parser')

    # find the first news title
        
    news_title = mars_news_soup.body.find("div", class_="content_title").text

    # find the paragraph associated with the first title
    news_paragraph = mars_news_soup.body.find("div", class_="article_teaser_body").text



# Check on class activities Day 3?
mars_web = {}
hemisphere_image_urls = []

def scrape_news():
    
    browser = init_browser()



    # What's next?
    url = 
    browser.visit(url)
    html = browser.html
    
    # html.parser?
    soup = bs(html, 'html.parser')
    latest_news_date = (soup.find_all('div', class_="list_date"))[0].get_text()
    latest_news_title = (soup.find_all('div', class_='content_title'))[0].get_text()
    latest_news_paragraph = (soup.find_all('div', class_='article_teaser_body'))[0].get_text()
    
    mars_web['latest_news_date'] = latest_news_date
    mars_web['latest_news_title'] = latest_news_title
    mars_web['latest_news_paragraph'] = latest_news_paragraph
   
    browser.quit()
    return mars_web

