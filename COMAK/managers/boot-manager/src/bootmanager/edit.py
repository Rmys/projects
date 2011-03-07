#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2009 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

# PyQt
from PyQt4 import QtCore
from PyQt4 import QtGui


# UI
from bootmanager.ui_edit import Ui_EditWidget
from context import *

class EditWidget(QtGui.QWidget, Ui_EditWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.id = None
        self.type = None
        #Kernel button signal connect
        self.connect(self.toolButton, QtCore.SIGNAL("clicked()"),self.slotFileDialog)
        #Ramdisk button signal connect
        self.connect(self.toolButton_2, QtCore.SIGNAL("clicked()"),self.slotRamDialog)
    def isNew(self):
        return self.id == None

    def reset(self):
        self.id = None
        self.type = None
        self.setTitle("")
        self.setDisk("")
        self.setKernel("")
        self.setRamdisk("")
        self.setOptions("")
        self.showTitle()
        self.showDisk()
        self.showKernel()
        self.showRamdisk()
        self.showOptions()

    def setId(self, id_):
        self.id = id_

    def getId(self):
        return self.id

    def setType(self, type_):
        self.type_ = type_

    def getType(self):
        return self.type_

    def hideTitle(self):
        self.lineTitle.setEnabled(False)

    def showTitle(self):
        self.lineTitle.setEnabled(True)

    def hideDisk(self):
        self.widgetDisk.hide()

    def showDisk(self):
        self.widgetDisk.show()

    def hideKernel(self):
        self.widgetKernel.hide()

    def showKernel(self):
        self.widgetKernel.show()

    def hideOptions(self):
        self.widgetOptions.hide()

    def showOptions(self):
        self.widgetOptions.show()

    def hideRamdisk(self):
        self.widgetRamdisk.hide()

    def showRamdisk(self):
        self.widgetRamdisk.show()

    def setTitle(self, title):
        self.lineTitle.setText(unicode(title))

    def getTitle(self):
        return unicode(self.lineTitle.text())

    def setDisk(self, disk):
        self.lineDisk.clear()
        if type(disk) == list:
            self.lineDisk.addItem('')
            self.lineDisk.addItems(disk)
        else:
            self.lineDisk.addItem(unicode(disk))

    def getDisk(self):
        return unicode(self.lineDisk.currentText())

    def setKernel(self, kernel):
        self.lineKernel.setText(unicode(kernel))

    def getKernel(self):
        return unicode(self.lineKernel.text())

    def setRamdisk(self, ramdisk):
        self.lineRamdisk.setText(unicode(ramdisk))

    def getRamdisk(self):
        return unicode(self.lineRamdisk.text())

    def setOptions(self, options):
        self.lineOptions.setText(unicode(options))

    def getOptions(self):
        return unicode(self.lineOptions.text()).replace('\n', ' ')

    #Get file name from file dialog
    def slotFileDialog(self):
        filename=str(QtGui.QFileDialog.getOpenFileName(self,i18n("File System"),"",i18n("All Files")))
        if filename:
            #Set file name
            self.setFile(filename)
    def setFile(self,filename):
        EditWidget.setKernel(self,filename)
    #Get file name from RamFile dialog
    def slotRamDialog(self):
        #set ram name
        ramname=str(QtGui.QFileDialog.getOpenFileName(self,i18n("File System"),"",i18n("All Files")))
        if ramname:
            self.setRam(ramname)
    def setRam(self,ramname):
        EditWidget.setRamdisk(self,ramname)
