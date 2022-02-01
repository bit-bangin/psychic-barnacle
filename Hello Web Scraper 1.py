#Import urllib
import urllib
#Import urlopen() from urllibrequest module
from urllib.request import urlopen
#Define URL for scraping
url = "yoururlasastring.com"
#Pass variable url into urlopen() fx
page = urlopen(url)
#This returns an HTTPResponse object
#Extract HTML from page, use HTTPResp obj .read() method 
html_bytes = page.read()
#Decode returned bytes to a string of UTF-8
html = html_bytes.decode("utf-8")
#Display
print(html)