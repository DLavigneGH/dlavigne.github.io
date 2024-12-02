# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wad_item_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_wadInfo(object):
    def setupUi(self, wadInfo):
        if not wadInfo.objectName():
            wadInfo.setObjectName(u"wadInfo")
        wadInfo.resize(731, 1069)
        self.verticalLayoutWidget = QWidget(wadInfo)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 731, 1061))
        self.wadItemLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.wadItemLayout.setObjectName(u"wadItemLayout")
        self.wadItemLayout.setContentsMargins(0, 0, 0, 0)
        self.idLabel_2 = QLabel(self.verticalLayoutWidget)
        self.idLabel_2.setObjectName(u"idLabel_2")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.idLabel_2.setFont(font)

        self.wadItemLayout.addWidget(self.idLabel_2)

        self.idLabel = QLabel(self.verticalLayoutWidget)
        self.idLabel.setObjectName(u"idLabel")
        font1 = QFont()
        font1.setPointSize(10)
        self.idLabel.setFont(font1)

        self.wadItemLayout.addWidget(self.idLabel)

        self.titleLabel_2 = QLabel(self.verticalLayoutWidget)
        self.titleLabel_2.setObjectName(u"titleLabel_2")
        self.titleLabel_2.setFont(font)

        self.wadItemLayout.addWidget(self.titleLabel_2)

        self.titleLabel = QLabel(self.verticalLayoutWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setFont(font1)

        self.wadItemLayout.addWidget(self.titleLabel)

        self.filenameLabel_2 = QLabel(self.verticalLayoutWidget)
        self.filenameLabel_2.setObjectName(u"filenameLabel_2")
        self.filenameLabel_2.setFont(font)

        self.wadItemLayout.addWidget(self.filenameLabel_2)

        self.filenameLabel = QLabel(self.verticalLayoutWidget)
        self.filenameLabel.setObjectName(u"filenameLabel")
        self.filenameLabel.setFont(font1)

        self.wadItemLayout.addWidget(self.filenameLabel)

        self.authorLabel_2 = QLabel(self.verticalLayoutWidget)
        self.authorLabel_2.setObjectName(u"authorLabel_2")
        self.authorLabel_2.setFont(font)

        self.wadItemLayout.addWidget(self.authorLabel_2)

        self.authorLabel = QLabel(self.verticalLayoutWidget)
        self.authorLabel.setObjectName(u"authorLabel")
        self.authorLabel.setFont(font1)

        self.wadItemLayout.addWidget(self.authorLabel)

        self.dateLabel_2 = QLabel(self.verticalLayoutWidget)
        self.dateLabel_2.setObjectName(u"dateLabel_2")
        self.dateLabel_2.setFont(font)

        self.wadItemLayout.addWidget(self.dateLabel_2)

        self.dateLabel = QLabel(self.verticalLayoutWidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setFont(font1)

        self.wadItemLayout.addWidget(self.dateLabel)

        self.sizeLabel_2 = QLabel(self.verticalLayoutWidget)
        self.sizeLabel_2.setObjectName(u"sizeLabel_2")
        self.sizeLabel_2.setFont(font)

        self.wadItemLayout.addWidget(self.sizeLabel_2)

        self.sizeLabel = QLabel(self.verticalLayoutWidget)
        self.sizeLabel.setObjectName(u"sizeLabel")
        self.sizeLabel.setFont(font1)

        self.wadItemLayout.addWidget(self.sizeLabel)

        self.ratingLabel_2 = QLabel(self.verticalLayoutWidget)
        self.ratingLabel_2.setObjectName(u"ratingLabel_2")
        self.ratingLabel_2.setFont(font)

        self.wadItemLayout.addWidget(self.ratingLabel_2)

        self.ratingLabel = QLabel(self.verticalLayoutWidget)
        self.ratingLabel.setObjectName(u"ratingLabel")
        self.ratingLabel.setFont(font1)

        self.wadItemLayout.addWidget(self.ratingLabel)

        self.votesLabel_2 = QLabel(self.verticalLayoutWidget)
        self.votesLabel_2.setObjectName(u"votesLabel_2")
        self.votesLabel_2.setFont(font)

        self.wadItemLayout.addWidget(self.votesLabel_2)

        self.votesLabel = QLabel(self.verticalLayoutWidget)
        self.votesLabel.setObjectName(u"votesLabel")
        self.votesLabel.setFont(font1)

        self.wadItemLayout.addWidget(self.votesLabel)

        self.urlLabel_2 = QLabel(self.verticalLayoutWidget)
        self.urlLabel_2.setObjectName(u"urlLabel_2")
        self.urlLabel_2.setFont(font)

        self.wadItemLayout.addWidget(self.urlLabel_2)

        self.urlLabel = QLabel(self.verticalLayoutWidget)
        self.urlLabel.setObjectName(u"urlLabel")
        self.urlLabel.setFont(font1)
        self.urlLabel.setOpenExternalLinks(True)

        self.wadItemLayout.addWidget(self.urlLabel)

        self.descriptionLabel_2 = QLabel(self.verticalLayoutWidget)
        self.descriptionLabel_2.setObjectName(u"descriptionLabel_2")
        self.descriptionLabel_2.setFont(font)
        self.descriptionLabel_2.setWordWrap(True)

        self.wadItemLayout.addWidget(self.descriptionLabel_2)

        self.descriptionLabel = QLabel(self.verticalLayoutWidget)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setFont(font1)
        self.descriptionLabel.setWordWrap(True)

        self.wadItemLayout.addWidget(self.descriptionLabel)

        self.visitedCheckBox = QCheckBox(self.verticalLayoutWidget)
        self.visitedCheckBox.setObjectName(u"visitedCheckBox")
        self.visitedCheckBox.setEnabled(False)

        self.wadItemLayout.addWidget(self.visitedCheckBox)

        self.textFile = QTextBrowser(self.verticalLayoutWidget)
        self.textFile.setObjectName(u"textFile")

        self.wadItemLayout.addWidget(self.textFile)


        self.retranslateUi(wadInfo)

        QMetaObject.connectSlotsByName(wadInfo)
    # setupUi

    def retranslateUi(self, wadInfo):
        wadInfo.setWindowTitle(QCoreApplication.translate("wadInfo", u"Dialog", None))
        self.idLabel_2.setText(QCoreApplication.translate("wadInfo", u"Id:", None))
        self.idLabel.setText("")
        self.titleLabel_2.setText(QCoreApplication.translate("wadInfo", u"Title:", None))
        self.titleLabel.setText("")
        self.filenameLabel_2.setText(QCoreApplication.translate("wadInfo", u"Filename:", None))
        self.filenameLabel.setText("")
        self.authorLabel_2.setText(QCoreApplication.translate("wadInfo", u"Author:", None))
        self.authorLabel.setText("")
        self.dateLabel_2.setText(QCoreApplication.translate("wadInfo", u"Date:", None))
        self.dateLabel.setText("")
        self.sizeLabel_2.setText(QCoreApplication.translate("wadInfo", u"Size:", None))
        self.sizeLabel.setText("")
        self.ratingLabel_2.setText(QCoreApplication.translate("wadInfo", u"Rating:", None))
        self.ratingLabel.setText("")
        self.votesLabel_2.setText(QCoreApplication.translate("wadInfo", u"Votes:", None))
        self.votesLabel.setText("")
        self.urlLabel_2.setText(QCoreApplication.translate("wadInfo", u"URL:", None))
        self.urlLabel.setText("")
        self.descriptionLabel_2.setText(QCoreApplication.translate("wadInfo", u"Description:", None))
        self.descriptionLabel.setText("")
        self.visitedCheckBox.setText(QCoreApplication.translate("wadInfo", u"Visited", None))
    # retranslateUi

