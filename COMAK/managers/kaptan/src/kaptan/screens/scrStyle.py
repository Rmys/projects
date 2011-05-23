#ifndef SCRSTYLE.PY
#define SCRSTYLE.PY
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

from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import QListWidgetItem

# Pds Stuff
import kaptan.screens.context as ctx
from kaptan.screens.context import *
from kaptan.plugins import Desktop

import os, sys, Image, dbus, glob

FOR_GNOME = ctx.Pds.session == ctx.pds.Gnome

from kaptan.screen import Screen

if FOR_GNOME:
    from kaptan.screens.ui_scrStyle_gnome import Ui_styleWidget
else:
    from kaptan.screens.ui_scrStyle import Ui_styleWidget

from kaptan.screens.styleItem import StyleItemWidget
from kaptan.tools.desktop_parser import DesktopParser
from ConfigParser import ConfigParser

class Widget(QtGui.QWidget, Screen):

    list_themes = []
    screenSettings = {}
    screenSettings["hasChanged"] = False
    screenSettings["iconChanged"] = False
    screenSettings["iconTheme"] = ""
    screenSettings["styleChanged"] = False
    screenSettings["hasChangedDesktopType"] = False
    screenSettings["hasChangedDesktopNumber"] = False

    # Set title and description for the information widget
    title = i18n("Themes")
    desc = i18n("Customize Your Desktop")


    def __init__(self, *args):
        QtGui.QWidget.__init__(self,None)
        self.ui = Ui_styleWidget()
        self.ui.setupUi(self)

        if not ctx.Pds.session.Name == "KDE":
            self.ui.listIcon.item(0).setHidden(1)
            self.ui.labelDesktopType.setVisible(False)
            self.ui.comboBoxDesktopType.setVisible(False)
        elif ctx.Pds.session.Name == "KDE":
            self.ui.listIcon.item(1).setHidden(1)

        self.ui.label.setText(str(ctx.Pds.session.Name)+" Themes")
        self.styleDetails = {}
        self.catLang = Desktop.common.getLanguage()
        defaultDesktopNumber = Desktop.style.getDesktopNumber()
        self.__class__.screenSettings["desktopNumber"]= defaultDesktopNumber
        self.ui.spinBoxDesktopNumbers.setValue(defaultDesktopNumber)
        if ctx.Pds.session.Name =="enlightenment":
            dir = QDir("/usr/share/enlightenment/data/themes")
            dir.setFilter( QDir.NoSymLinks | QDir.Files )
            a = QStringList()
            a.append("*.edj")
            dir.setNameFilters(a)
            lst2 = dir.entryList()
        elif ctx.Pds.session.Name == "fluxbox":
            dir = QDir("/usr/share/fluxbox/styles")
            lst2 =dir.entryList()
        elif ctx.Pds.session.Name == "gnome" or ctx.Pds.session.Name == "gnome3":
            #lst2=["Crux","Glider","HighContrast","Clearlooks","glossy","HighContrastInverse"]
            dir = QDir("/usr/share/themes")
            lst2 =dir.entryList()
        elif ctx.Pds.session.Name == "xfce":
            dir =QDir("/usr/share/themes")
            lst2= dir.entryList()
        elif ctx.Pds.session.Name == "LXDE":
            dir =QDir("/usr/share/themes")
            lst= dir.entryList()
            lst2=[]
            for previews in lst:
                if not previews=="Crux":
                    lst2.append(previews)
        else:
            dir = QtCore.QDir("/usr/share/themes")
            dir.setFilter(QtCore.QDir.Dirs| QtCore.QDir.NoDotAndDotDot)
            lst2 = dir.entryList()
        for themes in lst2:
            try:
                try:
                    StyleName = themes.split(".")[0]
                except :
                    StyleName = themes+"title"
                try:
                    StyleDesc = themes.split(".")[0]+"Desc"
                except:
                    StyleDesc = "unknown"
            except:
                print "Warning! Invalid syntax in ", themes
            ThemeFile = themes
            if ctx.Pds.session.Name == "xfce":
                a ="/usr/share//kaptan/kaptan/xfce_themes/"
                thumbFolder = a + themes + ".png"
            elif ctx.Pds.session.Name == "gnome" or  ctx.Pds.session.Name == "gnome3":
                a ="/usr/share/kaptan/kaptan/gnome_themes/"
                thumbFolder = a +themes+ ".png"
            else:
                a = "/usr/share/kaptan/kaptan/themes/"
                thumbFolder =a +themes+ ".png"

            if (os.path.exists(a+themes+".png")):
                self.list_themes.append(themes)
                styleThumb = thumbFolder
                item = QtGui.QListWidgetItem(self.ui.listStyles)
                widget = StyleItemWidget(unicode(StyleName),unicode(StyleDesc),thumbFolder,self.ui.listStyles)
                if ctx.Pds.session.Name == "KDE":
                    item.setSizeHint(QSize(120,170))
                else:
                    item.setSizeHint(QSize(130,160))
                self.ui.listStyles.setItemWidget(item,widget)
                item.setStatusTip(ThemeFile)
                self.styleDetails[StyleName] = {
                        "description":StyleDesc
                        }
            elif (os.path.exists("/usr/share/kaptan/kaptan/gnome_themes/"+themes+".png")):
                self.list_themes.append(themes)
                styleThumb = thumbFolder
                item = QtGui.QListWidgetItem(self.ui.listStyles)
                widget = StyleItemWidget(unicode(StyleName),unicode(StyleDesc),thumbFolder,self.ui.listStyles)
                item.setSizeHint(QSize(120,170))
                self.ui.listStyles.setItemWidget(item,widget)
                item.setStatusTip(ThemeFile)
                self.styleDetails[StyleName] = {
                        "description":StyleDesc
                        }

        self.ui.listStyles.connect(self.ui.listStyles, SIGNAL("itemSelectionChanged()"), self.setStyle)
        if ctx.Pds.session.Name =="fluxbox":
            self.ui.listIcon.setVisible(False)
            self.ui.iconContainer.hide()
            self.ui.label_3.hide()
        self.ui.listIcon.connect(self.ui.listIcon, SIGNAL("itemClicked(QListWidgetItem *)"), self.setIcon)
        #self.ui.comboBoxDesktopType.connect(self.ui.comboBoxDesktopType, SIGNAL("activated(const QString &)"), self.setDesktopType)
        #if ctx.Pds.session.Name =="gnome" or  ctx.Pds.session == ctx.pds.LXDE or ctx.Pds.session == ctx.pds.Gnome3:
        if ctx.Pds.session == ctx.pds.LXDE:
            self.ui.spinBoxDesktopNumbers.hide()
            self.ui.labelDesktopNumbers.hide()
        self.ui.spinBoxDesktopNumbers.connect(self.ui.spinBoxDesktopNumbers, SIGNAL("valueChanged(const QString &)"), self.addDesktop)
        #self.ui.previewButton.connect(self.ui.previewButton, SIGNAL("clicked()"), self.previewStyle)

    def ConfigSectionMap(self,section):
        dict1 = {}
        options = self.Config.options(section)
        for option in options:
            try:
                dict1[option] = self.Config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

    def addDesktop(self, numberOfDesktop):
        self.__class__.screenSettings["hasChangedDesktopNumber"] = True
        self.__class__.screenSettings["desktopNumber"] = str(numberOfDesktop)

    def setDesktopType(self):
        currentIndex = self.ui.comboBoxDesktopType.currentIndex()
        if currentIndex == 0:
            self.selectedType = 'desktop'
        else:
            self.selectedType = 'folderview'

        self.__class__.screenSettings["hasChangedDesktopType"] = True
        self.__class__.screenSettings["desktopType"] = self.selectedType

    def setStyle(self):
        styleName =  str(self.ui.listStyles.currentItem().statusTip())
        for wallpaper_index in range (self.ui.listStyles.count()):
            self.ui.listStyles.item(wallpaper_index).setBackground(Qt.gray);
            self.ui.listStyles.currentItem().setBackground(Qt.blue)


        self.__class__.screenSettings["summaryMessage"] = unicode(styleName)
        self.__class__.screenSettings["hasChanged"] = True
        self.__class__.screenSettings["styleChanged"] = True

        self.__class__.screenSettings["styleDetails"] = self.styleDetails
        self.__class__.screenSettings["styleName"] = styleName

    def setIcon(self):
        self.__class__.screenSettings["hasChanged"] = True
        self.iconTheme =  unicode(self.ui.listIcon.selectedItems()[0].text())
        self.iconTheme = str(self.iconTheme.split()[0]).lower()

        self.__class__.screenSettings["iconTheme"] = self.iconTheme
        self.__class__.screenSettings["summaryMessage"] = unicode(self.iconTheme)
        self.__class__.screenSettings["iconChanged"] = True


    def shown(self):
        pass

    def execute(self):
        return True


#endif // SCRSTYLE.PY
