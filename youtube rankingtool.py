import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import time
import os
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
l=[]
ls=[]
imgss=[]
vides=[]
answw=[]
chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox') # Bypass OS security model
chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
chrome_options.add_argument('start-maximized') # 
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument("--disable-extensions")
url="https://www.youtube.com/results?search_query=tv9 live"
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
driver.get(url)
time.sleep(5)
htmlsource = driver.page_source
with open("pags.txt", "w", encoding="utf-8") as f:
    f.write(htmlsource)   
driver.quit()
yty=None
pos=0
soup = BeautifulSoup(htmlsource, "html.parser")


content= soup.find("div", {"class": "style-scope ytd-item-section-renderer","id":"contents"})
alld=content.find_all("yt-img-shadow")
for a in alld:
    if("style-scope ytd-channel-renderer no-transition" in str(a)):
        position=pos
    pos=pos+1



allclasses = soup.findAll("ytd-video-renderer", {"class": "style-scope ytd-vertical-list-renderer"})
for a in allclasses:
    url=a.find('a')
    scr=a.find('img',{"class":"style-scope yt-img-shadow"})
    title=a.find("h3",{"class":"title-and-badge style-scope ytd-video-renderer"})
    description=a.find("yt-formatted-string",{"class":"style-scope ytd-video-renderer"})
    badge=a.find("span",{"class":"style-scope ytd-badge-supported-renderer"})
    if(badge!=None):
        badge=badge.getText()
    if(badge==None):
        badge="-"    
    #badge=a.find("ytd-badge-supported-renderer",{"class":"style-scope ytd-video-renderer"})
    try:
        y={
        "title":(title.getText()).strip(),
        "thumbnail_img_url":scr['src'],
        "link":url['href'],
        "description":description.getText(),
        "type":badge
        }
        l.append(y)
    except:
        pass




allclasses = soup.findAll("ytd-video-renderer", {"class": "style-scope ytd-item-section-renderer"})
for a in allclasses:
    url=a.find('a')
    scr=a.find('img',{"class":"style-scope yt-img-shadow"})
    title=a.find("h3",{"class":"title-and-badge style-scope ytd-video-renderer"})
    description=a.find("yt-formatted-string",{"class":"style-scope ytd-video-renderer"})
    badge=a.find("span",{"class":"style-scope ytd-badge-supported-renderer"})
    if(badge!=None):
        badge=badge.getText()
    if(badge==None):
        badge="-"
    try:
        y={
        "title":(title.getText()).strip(),
        "thumbnail_img_url":scr['src'],
        "link":url['href'],
        "description":description.getText(),
        "type":badge
        }
        l.append(y)
    except:
        pass


allclasses = soup.findAll("ytd-channel-renderer", {"class": "style-scope ytd-item-section-renderer"})
for a in allclasses:
    url=a.find('a')
    scr=a.find('img',{"class":"style-scope yt-img-shadow"})
    title=a.find("h3",{"class":"style-scope ytd-channel-renderer"})
    description=a.find("yt-formatted-string",{"class":"style-scope ytd-channel-renderer"})
    subscribers=a.find("span",{"id":"subscribers"})  
    videos=a.find("span",{"id":"video-count"})
    yty={
        "title":(title.getText()).strip(),
        "thumbnail_img_url":scr['src'],
        "link":url['href'],
        "description":description.getText(),
        "subscribers":subscribers.getText(),
        "videos":videos.getText(),
        "after_pos":position,
       }

j={
    "no_of_results":str(len(l)),
    "search results":l,
    "channel_snippet":yty, 
 }
r = json.dumps(j)
print(r)
