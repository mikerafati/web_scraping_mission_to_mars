from splinter import Browser
from bs4 import BeautifulSoup
import pandas as  pd

import time

def init_browser():
    exec_path = {'executable_path':"chromedriver.exe"}
    return Browser('chrome', headless=True, **exec_path)

def scrape():
    browser = init_browser()
    mars_collection = {}
    url1 = 'https://mars.nasa.gov/news/'
    browser.visit(url1)
    nasa_html = browser.html
    nasa_soup = BeautifulSoup(nasa_html, 'html.parser')

    news_title = nasa_soup.find("div",class_="content_title").text
    news_paragraph = nasa_soup.find("div", class_="article_teaser_body").text

    mars_collection['news_title'] = news_title

    mars_collection['news_p'] = news_paragraph
    #..................................................  

    browser = init_browser()
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(url2)
    jpl_html = browser.html
    
    jpl_soup = BeautifulSoup(jpl_html, 'html.parser')
    image = jpl_soup.find("img", class_="thumb")["src"]
    img_url = "https://jpl.nasa.gov"+image
    mars_collection["feature_image_src"] = img_url
    
#  ............................................................... 
    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)
    
    html_weather = browser.html
    soup = BeautifulSoup(html_weather, "html.parser")
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
   
    mars_collection['mars_weather'] = mars_weather

# ................................................................

    url4 = 'http://space-facts.com/mars/'
    browser.visit(url4)
    table = pd.read_html(url4)
    table[0]
    df_mars = table[0]

    df_mars.columns = ["Parameter", "Values"]
    df_mars.set_index(["Parameter"])
    mars_html_table = df_mars.to_html()
    mars_html_table = mars_html_table.replace("\n", "")
    mars_html_table

    mars_collection['mars_facts'] = mars_html_table
# ........................................................................................

# ..................................................................................
    
    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url5)
    mars_hemis=[]

    for i in range (4):
        time.sleep(5)
    images = browser.find_by_tag('h3')
    images[i].click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    partial = soup.find("img", class_="wide-image")["src"]
    img_title = soup.find("h2",class_="title").text
    img_url = 'https://astrogeology.usgs.gov'+ partial
    dictionary={"title":img_title,"img_url":img_url}
    mars_hemis.append(dictionary)
    mars_collection["hemisphere_imgs"] = dictionary
    browser.back()

    return mars_collection

