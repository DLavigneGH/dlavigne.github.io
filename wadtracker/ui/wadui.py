# -*- coding: utf-8 -*-
# fmt: off
################################################################################
## Form generated from reading UI file 'wadui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QRadioButton,
                               QScrollArea, QSizePolicy, QTabWidget,
                               QVBoxLayout, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(1577, 1106)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QRect(0, 40, 1391, 911))
        self.tabLevels = QWidget()
        self.tabLevels.setObjectName("tabLevels")
        self.scrollAreaLevels = QScrollArea(self.tabLevels)
        self.scrollAreaLevels.setObjectName("scrollAreaLevels")
        self.scrollAreaLevels.setGeometry(QRect(0, 10, 1371, 861))
        self.scrollAreaLevels.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollAreaLevels.setWidgetResizable(True)
        self.scrollAreaLevels_Content = QWidget()
        self.scrollAreaLevels_Content.setObjectName("scrollAreaLevels_Content")
        self.scrollAreaLevels_Content.setGeometry(QRect(0, 0, 1369, 859))
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollAreaLevels_Content.sizePolicy().hasHeightForWidth()
        )
        self.scrollAreaLevels_Content.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(self.scrollAreaLevels_Content)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 821, 591))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaLevels.setWidget(self.scrollAreaLevels_Content)
        self.tabWidget.addTab(self.tabLevels, "")
        self.tabMegawads = QWidget()
        self.tabMegawads.setObjectName("tabMegawads")
        self.scrollAreaMegawads = QScrollArea(self.tabMegawads)
        self.scrollAreaMegawads.setObjectName("scrollAreaMegawads")
        self.scrollAreaMegawads.setGeometry(QRect(0, 0, 1371, 861))
        self.scrollAreaMegawads.setWidgetResizable(True)
        self.scrollAreaMegawads_Content = QWidget()
        self.scrollAreaMegawads_Content.setObjectName("scrollAreaMegawads_Content")
        self.scrollAreaMegawads_Content.setGeometry(QRect(0, 0, 1369, 859))
        self.scrollAreaMegawads.setWidget(self.scrollAreaMegawads_Content)
        self.tabWidget.addTab(self.tabMegawads, "")
        self.radioDoom = QRadioButton(Dialog)
        self.radioDoom.setObjectName("radioDoom")
        self.radioDoom.setGeometry(QRect(10, 10, 89, 20))
        self.radioDoom2 = QRadioButton(Dialog)
        self.radioDoom2.setObjectName("radioDoom2")
        self.radioDoom2.setGeometry(QRect(90, 10, 90, 20))
        self.radioDoom2.setChecked(True)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabLevels),
            QCoreApplication.translate("Dialog", "Levels", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabMegawads),
            QCoreApplication.translate("Dialog", "Megawads", None),
        )
        self.radioDoom.setText(QCoreApplication.translate("Dialog", "Doom I", None))
        self.radioDoom2.setText(QCoreApplication.translate("Dialog", "Doom II", None))

    # retranslateUi
