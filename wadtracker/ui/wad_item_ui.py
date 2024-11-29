# -*- coding: utf-8 -*-
# fmt: off
################################################################################
## Form generated from reading UI file 'wad_item_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
                               QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(585, 733)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 361, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.idLabel = QLabel(self.verticalLayoutWidget)
        self.idLabel.setObjectName("idLabel")

        self.verticalLayout.addWidget(self.idLabel)

        self.titleLabel = QLabel(self.verticalLayoutWidget)
        self.titleLabel.setObjectName("titleLabel")

        self.verticalLayout.addWidget(self.titleLabel)

        self.filenameLabel = QLabel(self.verticalLayoutWidget)
        self.filenameLabel.setObjectName("filenameLabel")

        self.verticalLayout.addWidget(self.filenameLabel)

        self.authorLabel = QLabel(self.verticalLayoutWidget)
        self.authorLabel.setObjectName("authorLabel")

        self.verticalLayout.addWidget(self.authorLabel)

        self.dateLabel = QLabel(self.verticalLayoutWidget)
        self.dateLabel.setObjectName("dateLabel")

        self.verticalLayout.addWidget(self.dateLabel)

        self.sizeLabel = QLabel(self.verticalLayoutWidget)
        self.sizeLabel.setObjectName("sizeLabel")

        self.verticalLayout.addWidget(self.sizeLabel)

        self.ratingLabel = QLabel(self.verticalLayoutWidget)
        self.ratingLabel.setObjectName("ratingLabel")

        self.verticalLayout.addWidget(self.ratingLabel)

        self.votesLabel = QLabel(self.verticalLayoutWidget)
        self.votesLabel.setObjectName("votesLabel")

        self.verticalLayout.addWidget(self.votesLabel)

        self.urlLabel = QLabel(self.verticalLayoutWidget)
        self.urlLabel.setObjectName("urlLabel")

        self.verticalLayout.addWidget(self.urlLabel)

        self.descriptionLabel = QLabel(self.verticalLayoutWidget)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.descriptionLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.descriptionLabel)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.idLabel.setText(QCoreApplication.translate("Form", "Id:", None))
        self.titleLabel.setText(QCoreApplication.translate("Form", "Title:", None))
        self.filenameLabel.setText(
            QCoreApplication.translate("Form", "Filename:", None)
        )
        self.authorLabel.setText(QCoreApplication.translate("Form", "Author:", None))
        self.dateLabel.setText(QCoreApplication.translate("Form", "Date:", None))
        self.sizeLabel.setText(QCoreApplication.translate("Form", "Size:", None))
        self.ratingLabel.setText(QCoreApplication.translate("Form", "Rating:", None))
        self.votesLabel.setText(QCoreApplication.translate("Form", "Votes:", None))
        self.urlLabel.setText(QCoreApplication.translate("Form", "URL:", None))
        self.descriptionLabel.setText(
            QCoreApplication.translate("Form", "Description:", None)
        )

    # retranslateUi
