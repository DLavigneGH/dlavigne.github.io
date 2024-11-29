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
        wadInfo.resize(731, 835)
        self.verticalLayoutWidget = QWidget(wadInfo)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 731, 831))
        self.wadItemLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.wadItemLayout.setObjectName(u"wadItemLayout")
        self.wadItemLayout.setContentsMargins(0, 0, 0, 0)
        self.idLabel = QLabel(self.verticalLayoutWidget)
        self.idLabel.setObjectName(u"idLabel")

        self.wadItemLayout.addWidget(self.idLabel)

        self.titleLabel = QLabel(self.verticalLayoutWidget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.wadItemLayout.addWidget(self.titleLabel)

        self.filenameLabel = QLabel(self.verticalLayoutWidget)
        self.filenameLabel.setObjectName(u"filenameLabel")

        self.wadItemLayout.addWidget(self.filenameLabel)

        self.authorLabel = QLabel(self.verticalLayoutWidget)
        self.authorLabel.setObjectName(u"authorLabel")

        self.wadItemLayout.addWidget(self.authorLabel)

        self.dateLabel = QLabel(self.verticalLayoutWidget)
        self.dateLabel.setObjectName(u"dateLabel")

        self.wadItemLayout.addWidget(self.dateLabel)

        self.sizeLabel = QLabel(self.verticalLayoutWidget)
        self.sizeLabel.setObjectName(u"sizeLabel")

        self.wadItemLayout.addWidget(self.sizeLabel)

        self.ratingLabel = QLabel(self.verticalLayoutWidget)
        self.ratingLabel.setObjectName(u"ratingLabel")

        self.wadItemLayout.addWidget(self.ratingLabel)

        self.votesLabel = QLabel(self.verticalLayoutWidget)
        self.votesLabel.setObjectName(u"votesLabel")

        self.wadItemLayout.addWidget(self.votesLabel)

        self.urlLabel = QLabel(self.verticalLayoutWidget)
        self.urlLabel.setObjectName(u"urlLabel")

        self.wadItemLayout.addWidget(self.urlLabel)

        self.descriptionLabel = QLabel(self.verticalLayoutWidget)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
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
        self.idLabel.setText(QCoreApplication.translate("wadInfo", u"Id:", None))
        self.titleLabel.setText(QCoreApplication.translate("wadInfo", u"Title:", None))
        self.filenameLabel.setText(QCoreApplication.translate("wadInfo", u"Filename:", None))
        self.authorLabel.setText(QCoreApplication.translate("wadInfo", u"Author:", None))
        self.dateLabel.setText(QCoreApplication.translate("wadInfo", u"Date:", None))
        self.sizeLabel.setText(QCoreApplication.translate("wadInfo", u"Size:", None))
        self.ratingLabel.setText(QCoreApplication.translate("wadInfo", u"Rating:", None))
        self.votesLabel.setText(QCoreApplication.translate("wadInfo", u"Votes:", None))
        self.urlLabel.setText(QCoreApplication.translate("wadInfo", u"URL:", None))
        self.descriptionLabel.setText(QCoreApplication.translate("wadInfo", u"Description:", None))
        self.visitedCheckBox.setText(QCoreApplication.translate("wadInfo", u"Visited", None))
    # retranslateUi

