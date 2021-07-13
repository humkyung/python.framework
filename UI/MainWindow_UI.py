# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import Resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1089, 903)
        MainWindow.setBaseSize(QSize(0, 300))
        font = QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/AViewer.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon1)
        font1 = QFont()
        self.actionOpen.setFont(font1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actioncoffee = QAction(MainWindow)
        self.actioncoffee.setObjectName(u"actioncoffee")
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon3 = QIcon()
        icon3.addFile(u":/images/Exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.actionTheme = QAction(MainWindow)
        self.actionTheme.setObjectName(u"actionTheme")
        self.actionLanguage = QAction(MainWindow)
        self.actionLanguage.setObjectName(u"actionLanguage")
        self.actionExit_2 = QAction(MainWindow)
        self.actionExit_2.setObjectName(u"actionExit_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidgetOutputWnd = QDockWidget(MainWindow)
        self.dockWidgetOutputWnd.setObjectName(u"dockWidgetOutputWnd")
        self.dockWidgetOutputWnd.setMinimumSize(QSize(267, 202))
        self.dockWidgetOutputWnd.setBaseSize(QSize(0, 202))
        self.dockWidgetOutputWnd.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetOutputWnd.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.gridLayout_5 = QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.listWidgetLog = QListWidget(self.dockWidgetContents_3)
        self.listWidgetLog.setObjectName(u"listWidgetLog")

        self.gridLayout_5.addWidget(self.listWidgetLog, 2, 0, 1, 1)

        self.dockWidgetOutputWnd.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dockWidgetOutputWnd)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1089, 22))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTheme = QMenu(self.menuFile)
        self.menuTheme.setObjectName(u"menuTheme")
        icon4 = QIcon()
        icon4.addFile(u":/images/Theme.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuTheme.setIcon(icon4)
        self.menuLanguage = QMenu(self.menuFile)
        self.menuLanguage.setObjectName(u"menuLanguage")
        icon5 = QIcon()
        icon5.addFile(u":/images/Language.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuLanguage.setIcon(icon5)
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.menuTheme.menuAction())
        self.menuFile.addAction(self.menuLanguage.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(tooltip)
        self.actionOpen.setToolTip(QCoreApplication.translate("MainWindow", u"Open(Ctrl + O)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"Save(Ctrl + S)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actioncoffee.setText(QCoreApplication.translate("MainWindow", u"coffee", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.actionHelp.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionHelp.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionTheme.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.actionLanguage.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.actionExit_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.dockWidgetOutputWnd.setWindowTitle(QCoreApplication.translate("MainWindow", u"Output Window", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

