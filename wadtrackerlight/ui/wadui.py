# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wadui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_wadList(object):
    def setupUi(self, wadList):
        if not wadList.objectName():
            wadList.setObjectName(u"wadList")
        wadList.resize(1416, 684)
        self.pushRandomize = QPushButton(wadList)
        self.pushRandomize.setObjectName(u"pushRandomize")
        self.pushRandomize.setGeometry(QRect(10, 20, 100, 28))
        self.scrollAreaLevels = QScrollArea(wadList)
        self.scrollAreaLevels.setObjectName(u"scrollAreaLevels")
        self.scrollAreaLevels.setGeometry(QRect(10, 60, 1411, 621))
        self.scrollAreaLevels.setFrameShape(QFrame.NoFrame)
        self.scrollAreaLevels.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollAreaLevels.setWidgetResizable(True)
        self.scrollAreaLevels_Content = QWidget()
        self.scrollAreaLevels_Content.setObjectName(u"scrollAreaLevels_Content")
        self.scrollAreaLevels_Content.setGeometry(QRect(0, 0, 1411, 621))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaLevels_Content.sizePolicy().hasHeightForWidth())
        self.scrollAreaLevels_Content.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(self.scrollAreaLevels_Content)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, 1401, 601))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaLevels.setWidget(self.scrollAreaLevels_Content)
        self.pushSaveJson = QPushButton(wadList)
        self.pushSaveJson.setObjectName(u"pushSaveJson")
        self.pushSaveJson.setEnabled(False)
        self.pushSaveJson.setGeometry(QRect(260, 20, 100, 28))
        self.pushDownload = QPushButton(wadList)
        self.pushDownload.setObjectName(u"pushDownload")
        self.pushDownload.setEnabled(False)
        self.pushDownload.setGeometry(QRect(120, 20, 100, 28))
        self.pushDownload.setFocusPolicy(Qt.StrongFocus)

        self.retranslateUi(wadList)

        QMetaObject.connectSlotsByName(wadList)
    # setupUi

    def retranslateUi(self, wadList):
        wadList.setWindowTitle(QCoreApplication.translate("wadList", u"WADdomizer", None))
        self.pushRandomize.setText(QCoreApplication.translate("wadList", u"Randomize!", None))
        self.pushSaveJson.setText(QCoreApplication.translate("wadList", u"Record to JSON", None))
        self.pushDownload.setText(QCoreApplication.translate("wadList", u"Download WAD", None))
    # retranslateUi

