import requests
import json
  
class postData:
  def __init__(self,dataSet):
    self.dataSet = dataSet
  def post(self):
    # defining the api-endpoint  
    API_ENDPOINT = "https://douglas-api.angeloking.dev/professors"
      
    # your API key here 
    API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiaWF0IjoxNTkzNDE3OTk2LCJleHAiOjE1OTYwMDk5OTZ9.vuSyM4JDyGHvy2x7mkfxT6sVG_3HaSAK37fwo-9Rfj0"
    # sending post request and saving response as response object 
    headers = {'token':API_KEY}
    # data to be sent to api 
    for data in self.dataSet:
      r = requests.post(API_ENDPOINT, data=data, headers=headers)
      print(r)