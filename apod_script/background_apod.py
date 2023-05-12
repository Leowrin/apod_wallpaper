#!/usr/bin/python3

#version 1.3 corrected directories for image save

import urllib.request, os, sys, datetime
from bs4 import BeautifulSoup
import set_wallpaper as sw
import get_desktop_environment as gde
#from gi.repository import Gio

date = str(datetime.datetime.now().day) + "." + str(datetime.datetime.now().month)

scriptDirectory = os.path.dirname(os.path.realpath(__file__))


with open(scriptDirectory+'/settings.txt', 'r') as f:
    lastDay = f.readline()
    if lastDay == date :
        exit()
    pass

with open(scriptDirectory+'/settings.txt', 'w') as f:
    f.write(date)
    pass



retrieved=False   #recupere user system

if gde.get_desktop_environment()=='mac':
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://apod.nasa.gov/apod/astropix.html'




try:
    content = urllib.request.urlopen(url, timeout=1).read()
    if gde.get_desktop_environment()=='mac' or 'windows':
        soup = BeautifulSoup(content,features="html.parser")
    else :
        soup = BeautifulSoup(content, features="lxml")
except:
    sw.set_wallpaper(scriptDirectory+'/alternative.jpg', True)
    exit()


for link in soup.find_all('a'):
    if link.get('href')[0:5]=="image":
        image_url = "https://apod.nasa.gov/apod/" + link.get('href')

        with open(scriptDirectory+'/apod.jpg', 'w+b') as f:
            f.write(urllib.request.urlopen(image_url).read())
        retrieved=True

if retrieved==True:
    sw.set_wallpaper(scriptDirectory+'/apod.jpg', True)
else :
    sw.set_wallpaper(scriptDirectory+'/alternative.jpg', True)
