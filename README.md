# apod_wallpaper
A python script that retrieves the picture from the website https://apod.nasa.gov/apod/astropix.html and sets it as a wallpaper.

Script was written in Python3 and should work on most used Os, including macOs, windows, Linux: Cinnamon, Gnome, Mate...
Used Libraries :
 -os, sys, bs4 BeautifulSoup, urllib.request, appscript (macOs), ctypes (windows)
 
 How to use Script:
 place "set_apod_wallpaper.py" "get_desktop_environment.py" and "set_wallpaper.py" in the same folder. Execute "set_apod_wallpaper.py" with python3.
 Additionally, beacause apod's website sometimes has a video instead of a picture, you can add an "alternative.jpg" in the same folder as "set_apod_wallpaper.py" which will be used if impossible to retrive apod.
 
 How to use App:
 I used pyinstaller to develop an executable for windows and macOs, place the executable where you want, disable your antivirus, and execute. 
 
 
 Thanks to :
 stackoverflow community, and especially links commented in .py files.
