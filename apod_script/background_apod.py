import urllib.request, os, sys
from bs4 import BeautifulSoup
import set_wallpaper as sw
import get_desktop_environment as gde
#from gi.repository import Gio
import getpass



retrieved=False
user= getpass.getuser()   #recupere user system

if gde.get_desktop_environment(user)=='mac':
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://apod.nasa.gov/apod/astropix.html'
script_path = os.getcwd()   #recupere apod_script folder path

try:
    content = urllib.request.urlopen(url, timeout=1).read()
    if gde.get_desktop_environment(user)=='mac' or 'windows':
        soup = BeautifulSoup(content,features="html.parser")
    else :
        soup = BeautifulSoup(content, features="lxml")
except:
    sw.set_wallpaper(user, script_path+'/alternative.jpg', True)
    exit()


for link in soup.find_all('a'):
    if link.get('href')[0:5]=="image":
        image_url = "https://apod.nasa.gov/apod/" + link.get('href')

        with open(script_path+'/apod.jpg', 'wb') as f:
            f.write(urllib.request.urlopen(image_url).read())
        retrieved=True

if retrieved==True:
    sw.set_wallpaper(user, script_path+'/apod.jpg', True)
else :
    sw.set_wallpaper(user, script_path+'/alternative.jpg', True)
