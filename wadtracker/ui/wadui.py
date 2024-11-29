# -*- coding: utf-8 -*-
# isort: skip_file
# fmt:off
################################################################################
## Form generated from reading UI file 'wadui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, Qt, QTime, QUrl

from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QApplication, QDialog, QPushButton, QRadioButton, QScrollArea, QSizePolicy, QTabWidget, QVBoxLayout, QWidget

class Ui_wadList(object):
    def setupUi(self, wadList):
        if not wadList.objectName():
            wadList.setObjectName("wadList")
        wadList.resize(1109, 963)
        self.tabWidget = QTabWidget(wadList)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QRect(0, 40, 851, 901))
        self.tabLevels = QWidget()
        self.tabLevels.setObjectName("tabLevels")
        self.scrollAreaLevels = QScrollArea(self.tabLevels)
        self.scrollAreaLevels.setObjectName("scrollAreaLevels")
        self.scrollAreaLevels.setGeometry(QRect(0, 10, 841, 861))
        self.scrollAreaLevels.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollAreaLevels.setWidgetResizable(True)
        self.scrollAreaLevels_Content = QWidget()
        self.scrollAreaLevels_Content.setObjectName("scrollAreaLevels_Content")
        self.scrollAreaLevels_Content.setGeometry(QRect(0, 0, 839, 859))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaLevels_Content.sizePolicy().hasHeightForWidth())
        self.scrollAreaLevels_Content.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(self.scrollAreaLevels_Content)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 821, 841))
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
        self.radioDoom = QRadioButton(wadList)
        self.radioDoom.setObjectName("radioDoom")
        self.radioDoom.setGeometry(QRect(10, 10, 89, 20))
        self.radioDoom2 = QRadioButton(wadList)
        self.radioDoom2.setObjectName("radioDoom2")
        self.radioDoom2.setGeometry(QRect(90, 10, 90, 20))
        self.radioDoom2.setChecked(True)
        self.pushRandomize = QPushButton(wadList)
        self.pushRandomize.setObjectName("pushRandomize")
        self.pushRandomize.setGeometry(QRect(190, 20, 93, 28))

        self.retranslateUi(wadList)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(wadList)

    # setupUi

    def retranslateUi(self, wadList):
        wadList.setWindowTitle(QCoreApplication.translate("wadList", "Dialog", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabLevels),
            QCoreApplication.translate("wadList", "Levels", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabMegawads),
            QCoreApplication.translate("wadList", "Megawads", None),
        )
        self.radioDoom.setText(QCoreApplication.translate("wadList", "Doom I", None))
        self.radioDoom2.setText(QCoreApplication.translate("wadList", "Doom II", None))
        self.pushRandomize.setText(
            QCoreApplication.translate("wadList", "Randomize!", None)
        )

    # retranslateUi
