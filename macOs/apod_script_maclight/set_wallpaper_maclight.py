#from https://stackoverflow.com/a/21213504

import os, sys



def set_wallpaper(file_loc, first_run):

    try:
        from appscript import app, mactypes
        app('Finder').desktop_picture.set(mactypes.File(file_loc))
    except ImportError:
        #import subprocess
        SCRIPT = """/usr/bin/osascript<<END
        tell application "Finder" to
        set desktop picture to POSIX file "%s"
        end tell
        END"""
        subprocess.Popen(SCRIPT%file_loc, shell=True)
