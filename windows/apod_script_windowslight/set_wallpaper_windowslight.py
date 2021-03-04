#from https://stackoverflow.com/a/21213504

import os, sys
import ctypes



def set_wallpaper(file_loc, first_run):
    # Note: There are two common Linux desktop environments where
    # I have not been able to set the desktop background from
    # command line: KDE, Enlightenment


    #From https://stackoverflow.com/questions/1977694/change-desktop-background
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_loc , 0)                                  #changed A to W for python 3.5
