# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testManager.ui'
#
# Created: Wed Nov 26 20:31:44 2008
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 507)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.trywebView = QtWebKit.QWebView(self.centralwidget)
        self.trywebView.setGeometry(QtCore.QRect(30, 10, 731, 401))
        self.trywebView.setUrl(QtCore.QUrl("about:blank"))
        self.trywebView.setObjectName("trywebView")
        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(30, 420, 90, 27))
        self.backButton.setObjectName("backButton")
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(790, 70, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(680, 420, 90, 27))
        self.nextButton.setObjectName("nextButton")
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(800, 130, 98, 23))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(800, 170, 98, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(800, 210, 98, 23))
        self.radioButton_3.setObjectName("radioButton_3")
        self.runButton = QtGui.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(790, 20, 101, 31))
        self.runButton.setObjectName("runButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 29))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Load_Test = QtGui.QAction(MainWindow)
        self.action_Load_Test.setObjectName("action_Load_Test")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Load_Test)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("MainWindow", "Previous Test", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Report Bug", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("MainWindow", "Next Test", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "Test OK", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "Test FAIL", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("MainWindow", "Waiting", None, QtGui.QApplication.UnicodeUTF8))
        self.runButton.setText(QtGui.QApplication.translate("MainWindow", "Run Scripts", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Load_Test.setText(QtGui.QApplication.translate("MainWindow", "&Load Test", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
