# -*- coding: utf-8 -*-
# isort: skip_file
################################################################################
## Form generated from reading UI file 'wad_item_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QDialog,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_wadInfo(object):
    def setupUi(self, wadInfo):
        if not wadInfo.objectName():
            wadInfo.setObjectName("wadInfo")
        wadInfo.resize(361, 621)
        self.verticalLayoutWidget = QWidget(wadInfo)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 361, 581))
        self.wadItemLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.wadItemLayout.setObjectName("wadItemLayout")
        self.wadItemLayout.setContentsMargins(0, 0, 0, 0)
        self.idLabel = QLabel(self.verticalLayoutWidget)
        self.idLabel.setObjectName("idLabel")

        self.wadItemLayout.addWidget(self.idLabel)

        self.titleLabel = QLabel(self.verticalLayoutWidget)
        self.titleLabel.setObjectName("titleLabel")

        self.wadItemLayout.addWidget(self.titleLabel)

        self.filenameLabel = QLabel(self.verticalLayoutWidget)
        self.filenameLabel.setObjectName("filenameLabel")

        self.wadItemLayout.addWidget(self.filenameLabel)

        self.authorLabel = QLabel(self.verticalLayoutWidget)
        self.authorLabel.setObjectName("authorLabel")

        self.wadItemLayout.addWidget(self.authorLabel)

        self.dateLabel = QLabel(self.verticalLayoutWidget)
        self.dateLabel.setObjectName("dateLabel")

        self.wadItemLayout.addWidget(self.dateLabel)

        self.sizeLabel = QLabel(self.verticalLayoutWidget)
        self.sizeLabel.setObjectName("sizeLabel")

        self.wadItemLayout.addWidget(self.sizeLabel)

        self.ratingLabel = QLabel(self.verticalLayoutWidget)
        self.ratingLabel.setObjectName("ratingLabel")

        self.wadItemLayout.addWidget(self.ratingLabel)

        self.votesLabel = QLabel(self.verticalLayoutWidget)
        self.votesLabel.setObjectName("votesLabel")

        self.wadItemLayout.addWidget(self.votesLabel)

        self.urlLabel = QLabel(self.verticalLayoutWidget)
        self.urlLabel.setObjectName("urlLabel")

        self.wadItemLayout.addWidget(self.urlLabel)

        self.descriptionLabel = QLabel(self.verticalLayoutWidget)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.descriptionLabel.setWordWrap(True)

        self.wadItemLayout.addWidget(self.descriptionLabel)

        self.visitedCheckBox = QCheckBox(self.verticalLayoutWidget)
        self.visitedCheckBox.setObjectName("visitedCheckBox")

        self.wadItemLayout.addWidget(self.visitedCheckBox)

        self.retranslateUi(wadInfo)

        QMetaObject.connectSlotsByName(wadInfo)

    # setupUi

    def retranslateUi(self, wadInfo):
        wadInfo.setWindowTitle(QCoreApplication.translate("wadInfo", "Dialog", None))
        self.idLabel.setText(QCoreApplication.translate("wadInfo", "Id:", None))
        self.titleLabel.setText(QCoreApplication.translate("wadInfo", "Title:", None))
        self.filenameLabel.setText(
            QCoreApplication.translate("wadInfo", "Filename:", None)
        )
        self.authorLabel.setText(QCoreApplication.translate("wadInfo", "Author:", None))
        self.dateLabel.setText(QCoreApplication.translate("wadInfo", "Date:", None))
        self.sizeLabel.setText(QCoreApplication.translate("wadInfo", "Size:", None))
        self.ratingLabel.setText(QCoreApplication.translate("wadInfo", "Rating:", None))
        self.votesLabel.setText(QCoreApplication.translate("wadInfo", "Votes:", None))
        self.urlLabel.setText(QCoreApplication.translate("wadInfo", "URL:", None))
        self.descriptionLabel.setText(
            QCoreApplication.translate("wadInfo", "Description:", None)
        )
        self.visitedCheckBox.setText(
            QCoreApplication.translate("wadInfo", "Visited", None)
        )

    # retranslateUi
