from bs4 import BeautifulSoup
import requests
import lxml
import urllib

def GenerateMetaLogic(url):
    res = requests.get(url)
    content = res.text
    soup = BeautifulSoup(content, "lxml")
    error = ""
    for tag in soup.find_all("meta"):
        if tag.get("property") == "og:title" or tag.get("name") == "title":
            try:
                title =  tag.get("content", None)
            except: 
                error = "none"
        elif tag.get("property") == "og:description" or tag.get("name") == "description":
            try:
                description = tag.get("content", None)
            except:
                error = "none"
        elif tag.get("property", None) == "og:url":
            try:
                add = tag.get("content", None)    
            except:
                error = "none"   
        elif tag.get("name") == "keywords":
            try:
                keyword = tag.get("content", None)    
            except:
                error = "none"   

    a = soup.find_all("a","href") 
    page = soup.find('p').getText()

    return title, description, add, a, page
   
url = 'https://www.blogger.com/'
print(GenerateMetaLogic(url))


def findmeta():
    url = 'https://www.sigmasoftwares.org/'

    try:

         html=requests.get(url, timeout=60)

         soup = BeautifulSoup(html.text,"html.parser")

         metadesc = soup.findAll(attrs={"name":'description'})

         metakeywords= soup.findAll(attrs={"name":'keywords'})
         metatitle = soup.find('title').getText().strip()

         descList=[]
         keywordList=[]

         for link in metadesc:
              a=link.get("content")
              descList.append(a)

         for link in metakeywords:
              a=link.get("content")
              keywordList.append(a)

         meta2=str(metatitle)
         meta=str(descList)
         meta1=str(keywordList)

         data = f"\n url:{url}\n title:{meta2} \n description:{meta}\n keywords:{meta1}"
    
    except:
        pass

    return data

print(findmeta())
