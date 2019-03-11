import requests
from requests_html import HTMLSession
session = HTMLSession()
from bs4 import BeautifulSoup
import json
import time
import os
import html
import string
import base64
starti = time.time()
import argparse
parser = argparse.ArgumentParser()
l=[]
ls=[]
pots=[]
imgss=[]
vides=[]
answw=[]
query=None
location=None
lang=None
countrycode=None
uulu=None
nfpr=None
tbm=None
tbs=None
fillter=None
safesearch=None
start=None
noofresults=None
device=None
#query="coffee"  parser.add_argument("-v", "--verbose", action="store_true"
parser.add_argument('-q',"--query",type=str)
parser.add_argument( '-l',"--lang",type=str)
parser.add_argument( '-p',"--location",type=str)
parser.add_argument( '-c',"--countrycode",type=str)
parser.add_argument( '-u',"--uulu",type=str)
parser.add_argument( '-nf',"--nfpr",type=str)
parser.add_argument( '-tm',"--tbm",type=str)
parser.add_argument( '-ts',"--tbs",type=str)
parser.add_argument( '-f',"--fillter",type=str)
parser.add_argument( '-s',"--safesearch",type=str)
parser.add_argument( '-st',"--start",type=str)
parser.add_argument( '-n',"--noofresults",type=str)
parser.add_argument( '-R',"--device",type=str)
args = parser.parse_args()
string=args.location
try:
    vt=len(string)
    encoded = base64.b64encode(string.encode())
    encoded=str(encoded)
    encoded=(((encoded.split("'"))[1]).split("="))[0]
    if(vt==4):
        encoded="E"+encoded
    if(vt==5):
        encoded="F"+encoded
    if(vt==6):
        encoded="G"+encoded
    if(vt==7):
        encoded="H"+encoded
    if(vt==8):
        encoded="I"+encoded
    if(vt==9):
        encoded="J"+encoded
    if(vt==10):
        encoded="K"+encoded
    if(vt==11):
        encoded="L"+encoded
    if(vt==12):
        encoded="M"+encoded
    if(vt==13):
        encoded="N"+encoded
    if(vt==14):
        encoded="O"+encoded
    if(vt==15):
        encoded="P"+encoded
    if(vt==16):
        encoded="Q"+encoded
    if(vt==17):
        encoded="R"+encoded
    if(vt==18):
        encoded="S"+encoded
    if(vt==19):
        encoded="T"+encoded
    if(vt==20):
        encoded="U"+encoded
    if(vt==21):
        encoded="V"+encoded
    if(vt==22):
        encoded="W"+encoded
    if(vt==23):
        encoded="X"+encoded
    if(vt==24):
        encoded="Y"+encoded
    if(vt==25):
        encoded="Z"+encoded
    if(vt==26):
        encoded="a"+encoded
    if(vt==27):
        encoded="b"+encoded
    if(vt==28):
        encoded="c"+encoded
    if(vt==29):
        encoded="d"+encoded
    if(vt==30):
        encoded="e"+encoded
    if(vt==31):
        encoded="f"+encoded
    if(vt==32):
        encoded="g"+encoded
    if(vt==33):
        encoded="h"+encoded
    if(vt==34):
        encoded="i"+encoded
    if(vt==35):
        encoded="j"+encoded
    if(vt==36):
        encoded="k"+encoded
    if(vt==37):
        encoded="l"+encoded
    if(vt==38):
        encoded="m"+encoded
    if(vt==39):
        encoded="n"+encoded
    if(vt==40):
        encoded="o"+encoded
    if(vt==41):
        encoded="p"+encoded
    if(vt==42):
        encoded="q"+encoded
    if(vt==43):
        encoded="r"+encoded
    if(vt==44):
        encoded="s"+encoded
    if(vt==45):
        encoded="t"+encoded
    if(vt==46):
        encoded="u"+encoded
    if(vt==47):
        encoded="v"+encoded
    if(vt==48):
        encoded="w"+encoded
    if(vt==49):
        encoded="x"+encoded
    if(vt==50):
        encoded="y"+encoded
    if(vt==51):
        encoded="z"+encoded
    if(vt==52):
        encoded="0"+encoded
    if(vt==53):
        encoded="1"+encoded
    if(vt==54):
        encoded="2"+encoded
    if(vt==55):
        encoded="3"+encoded
    if(vt==56):
        encoded="4"+encoded
    if(vt==57):
        encoded="5"+encoded
    if(vt==58):
        encoded="6"+encoded
    if(vt==59):
        encoded="7"+encoded
    if(vt==60):
        encoded="8"+encoded
    if(vt==61):
        encoded="9"+encoded
    if(vt==62):
        encoded="--"+encoded
    if(vt==63):
        encoded="-"+encoded
    if(vt==64):
        encoded="A"+encoded
    if(vt==65):
        encoded="B"+encoded
    if(vt==66):
        encoded="C"+encoded
    if(vt==67):
        encoded="D"+encoded
    if(vt==68):
        encoded="E"+encoded
    if(vt==69):
        encoded="F"+encoded
    if(vt==70):
        encoded="G"+encoded
    if(vt==71):
        encoded="H"+encoded
    if(vt==72):
        encoded="I"+encoded
    if(vt==73):
        encoded="J"+encoded
    if(vt==74):
        encoded="K"+encoded
    if(vt==75):
        encoded="L"+encoded
    if(vt==76):
        encoded="M"+encoded
    if(vt==77):
        encoded="N"+encoded
    if(vt==78):
        encoded="O"+encoded
    if(vt==79):
        encoded="P"+encoded
    if(vt==80):
        encoded="Q"+encoded
    if(vt==81):
        encoded="R"+encoded
    if(vt==82):
        encoded="S"+encoded
    if(vt==83):
        encoded="T"+encoded   
    if(vt==89):
        encoded="L"+encoded  
except:
    pass
#url="https://www.google.co.in/search?q=coffee"
if(args.query!=None):
    url="https://www.google.com/search?q="+args.query+"&oq="+args.query
if(args.uulu!=None):
    url=url+"&uule="+uulu
else:
    try:
        url="https://www.google.com/search?q="+args.query+"&oq="+args.query+"&uule=w+CAIQICI"+encoded
    except:
        url=url
if(args.lang!=None):
    url=url+"&hl="+args.lang
if(args.countrycode!=None):
    url=url+"&gl="+args.countrycode
if(args.noofresults!=None):
    url=url+"&num="+args.noofresults
if(args.safesearch!=None):
    url=url+"&safe="+args.safesearch
if(args.nfpr!=None):
    url=url+"&nfpr="+args.nfpr
if(args.tbm!=None):
    url=url+"&tbm="+args.tbm
if(args.tbs!=None):
    url=url+"&tbs="+args.tbs
if(args.start!=None):
    url=url+"&start="+args.start
if(args.fillter!=None):
    url=url+"&filter="+args.fillter
if(args.device!=None):
    url=url+"&sourceid=chrome&ie=UTF-8"   
htmlsource = session.get(url)
htmlsource = htmlsource.text

with open("pags.html", "w", encoding="utf-8") as f:
    f.write(htmlsource)
peop=[]
sitelinks="0"
topstories="0"
imagepack="0"
adwords_top="0"
adwords_bottom="0"
shoppingresults="0"
brandknowledgegraph="0"
videos="0"
tweetsbox="0"
peopleaskfor="0"
richanswer="0"
richsnippet="0"
topcarousel="0"
localpack="0"
answerbox="0"
chachedurl=None             
similarurl=None
top_stories=None
pvideos=None
timagepack=None
tpeople=None
value=None
locationa={}
endtt = time.time()

#import unicodedata
#htmlsource = ''.join(c for c in unicodedata.normalize('NFC', str(htmlsource)) if c <= '\uFFFF')
soup = BeautifulSoup(htmlsource, "html.parser")
try:
    maplink = soup.find("div",{"id":"hdtb-msb"})
    maplink =maplink.findAll("a")
    for a in maplink:
        if("Maps" in str(a)):
            valururl=a['href']
    htmlsource = session.get(valururl)
    data =str(htmlsource.text)
    data=((data.split('<meta content="https://maps.google.com/maps/api/staticmap?center='))[1]).split('&amp;zoom=12&amp;size=200x200&amp;')[0]
    locations=data.split("%2C")
except:
    pass
endtty = time.time()
resultStats = soup.find("div",{"id":"resultStats"})
try:
    resultStats=resultStats.getText()
except:
    resultStats = soup.find("div",{"id":"topabar"})
    resultStats=resultStats.getText()
    
resultsearches=(resultStats.split("("))[0]
vakk=(((resultStats.split("("))[1]).split(")"))[0]

allclasses = soup.findAll("div", {"class": "e2BEnf"})
for a in allclasses:
    if("Videos" in str(a)):
        videos="1"
    if("Top stories" in str(a)):
        topstories="1"
    if("Images" in str(a)):
        imagepack="1"     

vids=soup.findAll("div", {"class": "y8AWGd llvJ5e"})
for i in vids:
    url=i.find('a', href=True)
    title=i.find("div", {"class": "mB12kf JRhSae ZyAH8d nDgy9d"})
    ownby=i.find("div", {"class": "zECGdd RgAZAc"})    
    y={
        "video title":title.getText(),
        "video link":url['href'],
        "video by":ownby.getText()
       } 
    vides.append(y)
                
position=int(0)

allcla = soup.findAll("div", {"class": "bkWMgd"})
for c in allcla:
    brandknowledgegraphs = c.findAll("h2", {"class": "bNg8Rb"})
    for a in brandknowledgegraphs:
        if("Featured snippet from the web" in str(a)):
            answerbox="1"
        if("Knowledge result" in str(a)):
            brandknowledgegraph="1"
        b=a.getText()
        if(b=="Local results"):
            localpack="1"
            try:
                loca=c.find("div", {"class": "xERobd"})
                url=loca.find('a')
                url=url['href']
                val=(((url.split("lag="))[1]).split("&"))[0]
                val=val.split(",")
                image=loca.find('img')
                image=image['src']
                locationa={
                    "link":url,
                    "gps coordinates":{
                    "latitude":locations[0],
                    "longitude":locations[1],
                    "altitude":val[2]
                    },
                     "image":image
                }
            except:
                pass
    brandknowledgegraphs = c.findAll("h3", {"class": "bNg8Rb"})
    for a in brandknowledgegraphs:
        if("Featured snippet from the web" in str(a)):
            answerbox="1"
        if("Knowledge result" in str(a)):
            brandknowledgegraph="1"
        b=a.getText()
        if(b=="Local results"):
            localpack="1"
            try:
                loca=c.find("div", {"class": "xERobd"})
                url=loca.find('a')
                url=url['href']
                val=(((url.split("lag="))[1]).split("&"))[0]
                val=val.split(",")
                image=loca.find('img')
                image=image['src']
                locationa={
                    "link":url,
                    "gps coordinates":{
                    "latitude":locations[0],
                    "longitude":locations[1],
                    "altitude":val[2]
                    },
                     "image":image
                }
            except:
                pass
    people = soup.findAll("h2", {"class": "XS4Rbf"})
    for pep in people:
        if("People also ask" in str(pep)):
            peopleaskfor="1"
            
    people = soup.findAll("h2", {"class": "JolIg"})
    for pep in people:
        if("People also ask" in str(pep)):
            peopleaskfor="1"
            
    try:
        if(peopleaskfor=="1"):
            allca = c.findAll("div", {"class": "related-question-pair"})
            if(len(allca)!=0):
                for a in allca:
                    alca = a.find("div", {"class": "match-mod-horizontal-padding cbphWd"})
                    question=alca.getText()
                    ala = a.find("div", {"class": "di3YZe"})
                    if(ala==None):
                        ala = a.find("div", {"class": "LGOjhe"})
                    answer=ala.getText()
                    ala = a.find("a")
                    link=ala['href']
                    title=a.find("h3", {"class": "LC20lb"})
                    title=title.getText()
                    sitename=a.find("cite", {"class": "iUh30"})
                    sitename=sitename.getText()
                    y={
                      "question":question,
                      "answer":answer,
                      "title":title,
                      "displayurl":sitename,
                      "link":link
                     }
                    peop.append(y)
    except:
        pass
    if("Top stories" in str(c)):
        top_stories=position
    if("Videos" in str(c)):
        pvideos=position
    if("AX4s9b kno-ibrg" in str(c)):
        timagepack=position
    if("People also ask" in str(c)):
        tpeople=position
    allclass = c.findAll("div", {"class": "g"})
    for a in allclass:
        import unicodedata
        a = ''.join(c for c in unicodedata.normalize('NFC', str(a)) if c <= '\uFFFF')
        a = BeautifulSoup(a, "html.parser")
        value=a.findAll("a", {"class": "fl"})
        chachedurl=None             
        similarurl=None
        for a in value:
            if("Cached" in str(a)):
                chachedurl=a['href']              
            if("Similar" in str(a)):
                similarurl=a['href']
        
    for a in allclass:        
        ls=[]
        allliks = a.findAll("div", {"class": "sld vsc"})
        for b in allliks:
            try:
                tie=b.find("h3", {"class": "r"})
                url=b.find('a', href=True)
                maint=b.find("div", {"class": "st"})
                p={
                  "title":tie.text,
                  "url":url['href'],
                  "description":maint.text
                   }
                sitelinks="1"
                ls.append(p)
            except:
                pass
    allclass = c.findAll("div", {"class": "g"})       
    for a in allclass:
        import unicodedata
        a = ''.join(c for c in unicodedata.normalize('NFC', str(a)) if c <= '\uFFFF')
        a = BeautifulSoup(a, "html.parser")
        alllks = a.findAll("div", {"class": "osl"})
        for b in alllks:
            try:
                maint=b.findAll("a")
                for main in maint:
                    p={
                      "title":main.text,
                      "url":main['href']
                      }
                    sitelinks="1"
                    ls.append(p)
            except:
                pass    
        tweerreults=a.find("div", {"class": "DOqJne"})
        rank=position+1
        if(tweerreults!=None):
            url=a.find('a', href=True)
            title=a.find("h3", {"class": "r"})
            sitename=a.find("cite", {"class": "ellip D5gSDf iUh30"})
            vale=a.find("div", {"class": "st"})
            y={}
            if(rank!=None):
                y['position']=rank
            if((title.text)!=None):
                y['title']=title.getText()
            if((sitename.text)!=None):
                y['displayurl']=sitename.text 
            if((url['href'])!=None):
                y['url']=url['href']
            if(val!=None):
                y['description']=val
            if(pots!=None):
                y['starrating']=pots
                richsnippet="1"
            if(len(ls)!=0):
                y['sitelinksls']=ls
            if(chachedurl!=None):
                y['similarur']=chachedurl
            if(similarurl!=None):
                y['similarurl']=similarurl
            l.append(y)
            position=position+1
        richsnip="0"
        title=a.find("h3", {"class": "LC20lb"})
        sitename=a.find("cite", {"class": "iUh30"})
        url=a.find('a', href=True)
        try:
            vale=a.find("span", {"class": "st"})
            val=vale.text
            #allclass = c.findAll("div", {"class": "g"})
            value=a.find("div", {"class": "slp f"})
            try:
                if(value!=None):
                    pots=[]
                    richsnip=value.getText()
                    rating=(richsnip.split("-"))[0]
                    review=(((richsnip.split("\u200e"))[1]).split(" "))[0]
                    y={
                       "rating":rating,
                       "review":review
                       }
                    pots.append(y)      
            except:
                richsnip="0"   
            y={}
            if(rank!=None):
                y['position']=rank     
            if((title.text)!=None):
                y['title']=title.getText()    
            if((sitename.text)!=None):
                y['displayurl']=sitename.text    
            if((url['href'])!=None):
                y['url']=url['href']     
            if(val!=None):
                y['description']=val    
            if(pots!=None):
                y['starrating']=pots
                richsnippet="1"
            if(len(ls)!=0):
                y['sitelinksls']=ls     
            if(chachedurl!=None):
                y['similarur']=chachedurl    
            if(similarurl!=None):
                y['similarurl']=similarurl     
            l.append(y)
            position=position+1
        except:
            pass
        

if(len(ls)!=None):
    sitelinks="1"
tweetsb = soup.findAll("h2", {"class": "vwfsqc"})
if(len(tweetsb)>0):
    tweetsbox="1"                   
adwords_t = soup.findAll("div", {"id": "tads"})
if(len(adwords_t)>0):
    adwords_top="1"
adwords_b = soup.findAll("div", {"id": "tadsb"})
if(len(adwords_b)>0):
    adwords_bottom="1"
shoppingresult = soup.findAll("div", {"class": "cu-container"})
if(len(shoppingresult)>0):
    shoppingresults="1"
carousel = soup.findAll("div", {"class": "abup"})
if(len(carousel)>0):
    topcarousel="1"              
richanswerd = soup.findAll("div", {"class": "NFQFxe viOShc LKPcQc EfDVh mod"})
if(len(richanswerd)>0):
    richanswer="1"
richanswerk = soup.findAll("div", {"class": "g knavi obcontainer NFQFxe mod"})
if(len(richanswerk)>0):
    richanswer="1"        
adwor = soup.findAll("div", {"class": "BmP5tf"})
for a in adwor:
    if("w-answer" in str(a)):
        richanswer="1"       
adwr = soup.findAll("div", {"class": "g knavi obcontainer mod"})
if(len(adwr)>0):
    richanswer="1"

if(answerbox=="1"):
    done="0"
    adr = soup.find("div", {"class": "xpdopen"})
    ifvideo=adr.find("div", {"class": "L2AgXb"})
    if(ifvideo!=None):
        url=adr.find("div", {"class": "r"})
        url=url.find('a')
        scr=adr.find('img')['src']
        sitename=adr.find("cite", {"class": "iUh30"})
        vale=adr.find("div", {"class": "LC20lb"})
        y={
        "title":url.getText(),
        "image url":scr,
        "displayurl":sitename.text,
        "url":url['href'],
         } 
        answw.append(y)
        done="1"
    try:
        title=adr.find("div", {"class": "co8aDb gsrt"})
        vale=adr.find("div", {"class": "RqBzHd"})
        url=adr.find("div", {"class": "r"})
        url=url.find('a')
        sitename=adr.find("cite", {"class": "iUh30"})
        scr=adr.find('img')['src']
        if(done!="1"):
            y={
               "title":title.getText(),
               "description":vale.getText(),
               "image url":scr,
               "displayurl":sitename.text,
               "url":url['href'],
               } 
            answw.append(y)
    except:
        vale=adr.find("span", {"class": "ILfuVd"})       
        title=adr.find("h3", {"class": "LC20lb"})
        url=adr.find("div", {"class": "r"})
        url=url.find('a') 
        sitename=adr.find("cite", {"class": "iUh30"})
        if(done!="1"):
            y={
               "title":title.text,
               "description":vale.getText(),
               "displayurl":sitename.text,
               "url":url['href'],
               } 
            answw.append(y)

if(imagepack=="1"):
    imgs=soup.findAll("div", {"class": "vsqVBf rg_el ivg-i"})
    for i in imgs:
        url=i.find('a', href=True)
        scr=i.find('img')['src']
        y={
          "image url":url['href'],
          "image link":scr
          } 
        imgss.append(y)
posi=1
rema=[]
extensi=[]
address=None
description=None
extensions=None
pric=None
typed=None
localresults=[]
image=None
localresults=soup.findAll("div", {"class": "VkpGBb"})
for local in localresults:
    try:
        try:
            image=local.find("img")
            image=image['src']
        except:
            pass
        title=local.find("div", {"class": "dbg0pd"})
        titl=local.find("span", {"class": "rllt__details lqhpac"})
        localresuls=titl.findAll("div")
        description=localresuls[1].getText()
        address=localresuls[2].getText()
        if("rllt__wrapped" in str(localresuls[2])):
            address=None
        extensions=local.find("div", {"class": "Wewxse"})
        extensions=local.findAll("span", {"class": "UGaK9c"})
        try:
            for val in extensions:
                y=val.getText()
                extensi.appened(y)
        except:
            pass  
        data=titl.getText()
        try:
            if("$" in str(data)):
                price=data.split("·")
                for pe in price:
                    if("$" in str(pe)):
                        pric=pe
        except:
            pass
        rating=(data.split("("))[0]
        reviews=(((data.split("("))[1]).split(")"))[0]
        data=localresuls[0].getText()
        typed=(data.split("·"))[-1]
        y={}
        if(posi!=None):
            y['position']=posi
        if(title!=None):
            y['title']=title.getText()
        if(typed!=None):
            y['type']=typed  
        if(rating!=None):
            y['rating']=rating
        if(reviews!=None):
            y['reviews']=reviews
        if(pric!=None):
            y['price']=pric  
        if(len(description)!=0):
            y['description']=description
        if(address!=None):
            y['address']=address
        if(extensions!=None):
            y['extensions']=extensi
        if(image!=None):
            y['thumbnail']=image 
        posi=posi+1
        rema.append(y)
    except:
        pass
if(len(rema)!=0):
   localpack="1"
   
simil=[]
similarentities=soup.findAll("div", {"class": "kno-fb-ctx MRfBrb kno-vrt-t"})
for simi in similarentities:
    url=simi.find('a')
    scr=simi.find('img')['src']
    y={
        "title":simi.getText(),
        "image":scr,
        "url":url['href'],
    } 
    simil.append(y)




sil=[]
similarsearch=soup.findAll("p", {"class": "nVcaUb"})
for simi in similarsearch:
    url=simi.find('a')
    y={
        "title":simi.getText(),
        "url":url['href'],
    } 
    sil.append(y)



j={
    "search information": [{
        "search results": resultsearches,
        "time": vakk,
        "query": args.query
    }],
    "location(local map)":locationa,
    "local names":rema,
    "no_of_results":str(len(l)),
    "search results":l,
    "relatated_questions":peop,
    "availabledata": {
         "sitelinks": sitelinks,
         "topstories": topstories,
         "Imagepack": imagepack,
         "adwords_top":adwords_top,
         "adwords_bottom":adwords_bottom,
         "shoppingresults":shoppingresults,
         "brandknowledgegraph":brandknowledgegraph,
         "videos":videos,
         "tweetsbox":tweetsbox,
         "peopleaskfor":peopleaskfor,
         "richanswer":richanswer,
         "richsnippet":richsnippet,
         "topcarousel":topcarousel,
         "localpack":localpack,
         "answerbox":answerbox,
    },
    "topstories": {"after_pos": top_stories,},
    "Videos": {"after_pos": pvideos,},
    "people also ask for": {"after_pos": tpeople,},
    "imagepos": {"after_pos": timagepack,},
    "imagepack":imgss,
    "videospack":vides,
    "answerdetails":answw,
    "simalrqueries":sil,
    "simalarentities":simil
 }
r = json.dumps(j)
print(str(r))
'''f=open("result.txt","a+")
f.write(r)
f.close()
print("scraping time:")
print(endtt - starti)
try:
    print("location:")
    print(endtty - starti)
except:
    pass
end = time.time()
print("total time:")
print(end - starti)'''
