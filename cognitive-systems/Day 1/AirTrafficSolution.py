# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#pip install beautifulsoup4 if needed

from bs4 import BeautifulSoup
import requests

def get(url):
    headers={}
    resp = requests.get(url, headers=headers)
    if resp.ok:
        return resp.text
    
#Extract the main content from each web url
def colcontent(url):
    data2 = get(url)
    soup = BeautifulSoup(data2,  "html.parser")
    maindiv = soup.find("div", {"class":"sf_main_content tp"})
    if maindiv:
        return (maindiv.text)

website = "https://www.airport-technology.com/suppliers/air-traffic-control/"
data = get(website)

#Access all the relevant urls and store them in a list
soup = BeautifulSoup(data,"html.parser")
alltags = soup.findAll("a")

urls = []
names = []
for a_tag in alltags:
    href = a_tag.get("href")
    if href and href != "" and "contractors" in href:
        span_tag = a_tag.find("span", {"class": "companyaz_name"})
        if span_tag:
            clean = span_tag.text.strip(',')
            names.append(clean)
            urls.append(href)
            
       
totalCount = 5       
file = open("Air Traffic Control Solutions.txt","w")

for item in urls[:totalCount]:
    contents=colcontent(item)
    file.write(names[urls.index(item)])
    file.write(contents)
    print (names[urls.index(item)]+" downloaded.")

file.close()