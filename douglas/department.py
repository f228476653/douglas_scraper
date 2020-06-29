from .request_utils import requests_get
from .request_utils import bs
import re

class department:
    # def __init__(self,url):
    #     self.url=url
    # def parse(self):
    #     req = requests_get(self.url)
    #     data = []
    #     depsName = ""
    #     soup= bs(req.content)
    #     #plainText = soup.prettify()
    #     depDivs = soup.findAll("a", attrs={'href':re.compile('^\/programs-courses\/faculties')})
    #     #depDivss = soup.findAll("span")
    #     print(depDivs)
    #     course= []
    #     for dep in depDivs:
    #         depCourse= link.replace("/programs-courses/faculties/","").split("/")
    #         depsName = depCourse[0]
    #         course.append(dep.text)
    #         if depsName == depCourse[0]:
    #             course.append(dep.text)
    #         else:
    #             pass


         #return data
        
