# -*- coding: utf-8 -*-
#
# Copyright (C) 2005-2009, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#
#PyQt4 Stuff
from PyQt4 import QtGui
from PyQt4.QtCore import QString
from PyQt4.QtGui import QMessageBox

import subprocess,os, dbus

#Context Stuff
import kaptan.screens.context as ctx
from kaptan.screens.context import *
from kaptan.plugins import Desktop

from kaptan.screen import Screen
from kaptan.screens.ui_scrSummary import Ui_summaryWidget

# import other widgets to get the latest configuration
import kaptan.screens.scrWallpaper as wallpaperWidget
import kaptan.screens.scrMouse as mouseWidget
import kaptan.screens.scrStyle as styleWidget
import kaptan.screens.scrMenu as menuWidget
import kaptan.screens.scrSmolt  as smoltWidget
import kaptan.screens.scrAvatar  as avatarWidget

from kaptan.tools import tools

class Widget(QtGui.QWidget, Screen):
    title = i18n("Summary")
    desc = i18n("Save Your Settings")

    def __init__(self, *args):
        QtGui.QWidget.__init__(self,None)
        self.ui = Ui_summaryWidget()
        self.ui.setupUi(self)

    def shown(self):
        self.wallpaperSettings = wallpaperWidget.Widget.screenSettings
        self.mouseSettings = mouseWidget.Widget.screenSettings
        self.menuSettings = menuWidget.Widget.screenSettings
        self.styleSettings = styleWidget.Widget.screenSettings
        self.smoltSettings = smoltWidget.Widget.screenSettings
        self.avatarSettings = avatarWidget.Widget.screenSettings

        subject = "<p><li><b>%s</b></li><ul>"
        item    = "<li>%s</li>"
        end     = "</ul></p>"
        content = QString("")

        content.append("""<html><body><ul>""")

        # Mouse Settings
        content.append(subject % i18n("Mouse Settings"))

        content.append(item % i18n("Selected Mouse configuration: <b>%s</b>") % self.mouseSettings["summaryMessage"]["selectedMouse"])
        content.append(item % i18n("Selected clicking behavior: <b>%s</b>")% self.mouseSettings["summaryMessage"]["clickBehavior"])
        content.append(end)

        # Menu Settings
        content.append(subject % i18n("Menu Settings"))
        content.append(item % i18n("Selected Menu: <b>%s</b>") % self.menuSettings["summaryMessage"])
        content.append(end)

        # Wallpaper Settings
        content.append(subject % i18n("Wallpaper Settings"))
        if not self.wallpaperSettings["hasChanged"]:
            content.append(item % i18n("You haven't selected any wallpaper."))
        else:
            content.append(item % i18n("Selected Wallpaper: <b>%s</b>") % os.path.basename(str(self.wallpaperSettings["selectedWallpaper"])))
        content.append(end)

        # Style Settings
        content.append(subject % i18n("Style Settings"))

        if not self.styleSettings["hasChanged"]:
            content.append(item % i18n("You haven't selected any style."))
        else:
            content.append(item % i18n("Selected Style: <b>%s</b>") % unicode(self.styleSettings["summaryMessage"]))

        content.append(end)

        # Smolt Settings
        try:
            if self.smoltSettings["summaryMessage"]:
                content.append(subject %i18n("Smolt Settings"))
                content.append(item % i18n("Send my profile: <b>%s</b>") % self.smoltSettings["summaryMessage"])
                #content.append(i18n("(<i><u>Warning:</u> Sending profile requires to set up communication with Smolt server and can take between 30 seconds to a minute. Kaptan may freeze during this time.</i>)"))
                content.append(end)
        except:
            print "WARNING: Your Smolt profile is already sent."

        content.append("""</ul></body></html>""")
        self.ui.textSummary.setHtml(content)

    def killPlasma(self):
        try:
            p = subprocess.Popen(["pidof", "-s", "plasma-desktop"], stdout=subprocess.PIPE)
            out, err = p.communicate()
            pidOfPlasma = int(out)

            try:
                os.kill(pidOfPlasma, 15)
            except OSError, e:
                print 'WARNING: failed os.kill: %s' % e
                print "Trying SIGKILL"
                os.kill(pidOfPlasma, 9)

            finally:
                self.startPlasma()
        except:
            QMessageBox.critical(self, i18n("Error"), i18n("Cannot restart plasma-desktop. Kaptan will now shutdown."))
            kdeui.KApplication.kApplication().quit()

    def startPlasma(self):
        p = subprocess.Popen(["plasma-desktop"], stdout=subprocess.PIPE)


    def execute(self):

        # Wallpaper Settings
        Desktop.wallpaper.setWallpaper(self.wallpaperSettings["selectedWallpaper"],self.wallpaperSettings["hasChanged"])

        # Menu Settings
        Desktop.menu.setMenuSettings(self.menuSettings["selectedMenu"], self.menuSettings["hasChanged"])

        def removeFolderViewWidget():
            desktop.removeFolderViewWidget()

        # Desktop Type
        if self.styleSettings["hasChangedDesktopType"]:
            hasChanged = True
            desktop.setDesktopType()

        # Number of Desktops
        if self.styleSettings["hasChangedDesktopNumber"]:
            hasChanged = True
            desktop.setDesktopNumber()


        def deleteIconCache():
            try:
                os.remove("/var/tmp/kdecache-%s/icon-cache.kcache" % os.environ.get("USER"))
            except:
                pass

            desktop.deleteIconCache()

        # Theme Settings
        if self.styleSettings["hasChanged"]:
            if self.styleSettings["iconChanged"]:
                hasChanged = True
                desktop.setThemeSettings()

                # Change Icon theme
                desktop.changeIconTheme()
                deleteIconCache()
            if self.styleSettings["styleChanged"]:
                hasChanged = True
                desktop.setStyleSettings()

                # Change Icon theme
                desktop.changeIconTheme()
                deleteIconCache()


                desktop.deleteIconCache()

                # Change widget style & color
                desktop.setChangeWidget()
                desktop.emitChangeStyle()

                desktop.configPlasmarc()
                desktop.setPlasma()
                desktop.configKwinRC()

            session = dbus.SessionBus()

            try:
                proxy = session.get_object('org.kde.kwin', '/KWin')
                proxy.reconfigure()
            except dbus.DBusException:
                pass

        # Smolt Settings
        if self.smoltSettings["profileSend"]:
            self.procSettings = QProcess()
            command = "smoltSendProfile"
            arguments = ["-a", "--submitOnly"]
            self.procSettings.startDetached(command, arguments)

        # Avatar Settings
        if self.avatarSettings["hasChanged"]:
            self.killPlasma()

        return True
