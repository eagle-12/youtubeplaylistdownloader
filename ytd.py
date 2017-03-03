import requests
from bs4 import BeautifulSoup
from pytube import YouTube
from pprint import pprint
print "INPUT LINK OF THE PLAYLIST:-"
playlist=raw_input()
r=requests.get(playlist)
soup=BeautifulSoup(r.content)
for link in soup.find_all('a'):
	if "watch?" in str(link["href"]):
		video_link = YouTube()
		video_link.url = "https://www.youtube.com" + str(link["href"])
		print "SELECT ONE OF THE AVAILABLE VIDEO QUALITIES"
		pprint(video_link.videos)
		print "input the type of video"
		type_ = raw_input()
		print "input the resolution of video"
		quality=raw_input()
		video = video_link.get(type_,quality)
		video.download("/home/nikhil/Downloads")#specify the address where to store the downloaded video
		print "SET THE FILENAME"
		video_link.filename=raw_input()
