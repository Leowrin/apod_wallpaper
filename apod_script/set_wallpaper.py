#from https://stackoverflow.com/a/21213504

import get_desktop_environment as gde
import os, sys



def set_wallpaper(file_loc, first_run):
    # Note: There are two common Linux desktop environments where
    # I have not been able to set the desktop background from
    # command line: KDE, Enlightenment
    desktop_env = gde.get_desktop_environment()

    if desktop_env!="windows":
        from gi.repository import Gio

    try:
        if desktop_env in ["unity", "cinnamon"]:
            uri = "file://%s" % file_loc
            try:
                SCHEMA = "org."+desktop_env+".desktop.background"
                KEY = "picture-uri"
                gsettings = Gio.Settings.new(SCHEMA)
                gsettings.set_string(KEY, uri)
            except:
                args = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", uri]
                subprocess.Popen(args)

        elif desktop_env=="gnome":
            try:
                file_loc = "file://" + file_loc
                commandToDo = "gsettings set org.gnome.desktop.background picture-uri-dark " + file_loc
                os.system(commandToDo)
            except:
                pass
    
        elif desktop_env=="mate":
                try: # MATE >= 1.6
                    # info from http://wiki.mate-desktop.org/docs:gsettings
                    args = ["gsettings", "set", "org.mate.background", "picture-filename", "'%s'" % file_loc]
                    subprocess.Popen(args)
                except: # MATE < 1.6
                    # From https://bugs.launchpad.net/variety/+bug/1033918
                    args = ["mateconftool-2","-t","string","--set","/desktop/mate/background/picture_filename",'"%s"' %file_loc]
                    subprocess.Popen(args)
        elif desktop_env=="gnome2": # Not tested
            # From https://bugs.launchpad.net/variety/+bug/1033918
            args = ["gconftool-2","-t","string","--set","/desktop/gnome/background/picture_filename", '"%s"' %file_loc]
            subprocess.Popen(args)
        ## KDE4 is difficult
        ## see http://blog.zx2c4.com/699 for a solution that might work
        elif desktop_env in ["kde3", "trinity"]:
            # From http://ubuntuforums.org/archive/index.php/t-803417.html
            args = 'dcop kdesktop KBackgroundIface setWallpaper 0 "%s" 6' % file_loc
            subprocess.Popen(args,shell=True)
        elif desktop_env=="xfce4":
            #From http://www.commandlinefu.com/commands/view/2055/change-wallpaper-for-xfce4-4.6.0
            if first_run:
                args0 = ["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/image-path", "-s", file_loc]
                args1 = ["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/image-style", "-s", "3"]
                args2 = ["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/image-show", "-s", "true"]
                subprocess.Popen(args0)
                subprocess.Popen(args1)
                subprocess.Popen(args2)
            args = ["xfdesktop","--reload"]
            subprocess.Popen(args)

        elif desktop_env in ["fluxbox","jwm","openbox","afterstep"]:
            #http://fluxbox-wiki.org/index.php/Howto_set_the_background
            # used fbsetbg on jwm too since I am too lazy to edit the XML configuration
            # now where fbsetbg does the job excellent anyway.
            # and I have not figured out how else it can be set on Openbox and AfterSTep
            # but fbsetbg works excellent here too.
            try:
                args = ["fbsetbg", file_loc]
                subprocess.Popen(args)
            except:
                sys.stderr.write("ERROR: Failed to set wallpaper with fbsetbg!\n")
                sys.stderr.write("Please make sre that You have fbsetbg installed.\n")
        elif desktop_env=="icewm":
            # command found at http://urukrama.wordpress.com/2007/12/05/desktop-backgrounds-in-window-managers/
            args = ["icewmbg", file_loc]
            subprocess.Popen(args)
        elif desktop_env=="blackbox":
            # command found at http://blackboxwm.sourceforge.net/BlackboxDocumentation/BlackboxBackground
            args = ["bsetbg", "-full", file_loc]
            subprocess.Popen(args)
        elif desktop_env=="lxde":
            args = "pcmanfm --set-wallpaper %s --wallpaper-mode=scaled" % file_loc
            subprocess.Popen(args,shell=True)
        elif desktop_env=="windowmaker":
            # From http://www.commandlinefu.com/commands/view/3857/set-wallpaper-on-windowmaker-in-one-line
            args = "wmsetbg -s -u %s" % file_loc
            subprocess.Popen(args,shell=True)
        ## NOT TESTED BELOW - don't want to mess things up ##
        #elif desktop_env=="enlightenment": # I have not been able to make it work on e17. On e16 it would have been something in this direction
        #    args = "enlightenment_remote -desktop-bg-add 0 0 0 0 %s" % file_loc
        #    subprocess.Popen(args,shell=True)
        elif desktop_env=="windows": #Not tested since I do not run this on Windows
            #From https://stackoverflow.com/questions/1977694/change-desktop-background
            import ctypes
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_loc , 0)                                  #changed A to W for python 3.5
        elif desktop_env=="mac": #Not tested since I do not have a mac
            #From https://stackoverflow.com/questions/431205/how-can-i-programatically-change-the-background-in-mac-os-x
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
        else:
            if first_run: #don't spam the user with the same message over and over again
                sys.stderr.write("Warning: Failed to set wallpaper. Your desktop environment is not supported.")
                sys.stderr.write("You can try manually to set Your wallpaper to %s" % file_loc)
            return False
        return True
    except:
        sys.stderr.write("ERROR: Failed to set wallpaper. There might be a bug.\n")
        return False


def get_home_dir():
    if sys.platform == "cygwin":
        home_dir = os.getenv('HOME')
    else:
        home_dir = os.getenv('USERPROFILE') or os.getenv('HOME')
    if home_dir is not None:
        return os.path.normpath(home_dir)
    else:
        raise KeyError("Neither USERPROFILE or HOME environment variables set.")
