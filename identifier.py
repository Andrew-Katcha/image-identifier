
import httplib, urllib, base64
import os, json
import cloudinary, cloudinary.uploader, cloudinary.api
from pprint import pprint
from subprocess import call
import pyttsx
from clarifai import rest
from clarifai.rest import ClarifaiApp

from appendDataToHtml import AppendDataToHTML
import config

#TODO add Cloudinary Cloudname, API Key, and API Secret here
cloudinary.config( 
  cloud_name = config.CloudinaryCloudName, 
  api_key = config.CloudinaryApiKey, 
  api_secret = config.CloudinaryApiSecret 
)

url = ""
#TODO ADD YOUR PATH to index.html. Apache Default is /var/www/html/index.html
htmlPagePath = config.IndexHtmlPath
tags = ""

#TODO: CHange this to take as many pictures as you would like!
for x in range(0, 1):
    file_name = "web-cam-shot" + str(x) + ".jpg"
    os.system("fswebcam -r 640x480 --jpeg 85 -D 1 " + file_name)

    
    path = str(os.getcwd()) + "/" + file_name
    result = cloudinary.uploader.upload(path)
    url = result['url']
    body = { "url": url }
    try:
        #TODO ADD YOUR CLARIFY API KEY AND API SECRET
        app = ClarifaiApp(config.ClarifaiApiKey, config.ClarifaiApiSecret)
        model = app.models.get("general-v1.3")       
        data = model.predict_by_url(url)
    except Exception as e:
        continue
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    appendDataToHtml = AppendDataToHTML()
    f = open(htmlPagePath,'a+')
    tags = appendDataToHtml.filterTags(tags, data)
    message = appendDataToHtml.appendToHTML(tags, url)
    f.write(message)
    f.close()

