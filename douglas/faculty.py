from .request_utils import requests_get
from .request_utils import bs
import re

class faculty:
    def __init__(self,url):
        self.url=url
    def parse(self):
        req = requests_get(self.url)
        soup= bs(req.content)
        data =[]
        plainText = soup.prettify()
        searchByName = soup.findAll("a", attrs={'href':re.compile('[^<>]@douglascollege.ca')})
        for a in searchByName:
            teacher = {}
            if a.text: 
                teacher['email'] = a['href'].replace('mailto:','')
                teacher['name'] = a.text
            data.append(teacher)
        #print(data)
        return data
        #depDivss = soup.findAll("span")
        #print(data)
        
        
