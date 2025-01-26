# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gun_detection_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(680, 800)
        Dialog.setMaximumSize(QSize(680, 800))
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.modelBrowseButton = QPushButton(Dialog)
        self.modelBrowseButton.setObjectName(u"modelBrowseButton")
        self.modelBrowseButton.setMinimumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.modelBrowseButton, 6, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 11, 1, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 6, 2, 1, 1)

        self.modelPathLine = QLineEdit(Dialog)
        self.modelPathLine.setObjectName(u"modelPathLine")
        self.modelPathLine.setReadOnly(True)

        self.gridLayout.addWidget(self.modelPathLine, 6, 1, 1, 1)

        self.mainImage = QLabel(Dialog)
        self.mainImage.setObjectName(u"mainImage")
        self.mainImage.setMinimumSize(QSize(600, 400))
        self.mainImage.setAutoFillBackground(False)
        self.mainImage.setStyleSheet(u"background-color: rgb(213, 213, 213);")
        self.mainImage.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.mainImage, 3, 1, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 9, 1, 1, 3)

        self.detectButton = QPushButton(Dialog)
        self.detectButton.setObjectName(u"detectButton")
        self.detectButton.setMinimumSize(QSize(400, 50))
        self.detectButton.setMaximumSize(QSize(400, 50))
        self.detectButton.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.detectButton, 10, 1, 1, 3, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 3)

        self.imageBrowseButton = QPushButton(Dialog)
        self.imageBrowseButton.setObjectName(u"imageBrowseButton")
        self.imageBrowseButton.setMinimumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.imageBrowseButton, 8, 3, 1, 1, Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 3)

        self.provideImageLabel = QLabel(Dialog)
        self.provideImageLabel.setObjectName(u"provideImageLabel")

        self.gridLayout.addWidget(self.provideImageLabel, 7, 1, 1, 1)

        self.imagePathLine = QLineEdit(Dialog)
        self.imagePathLine.setObjectName(u"imagePathLine")
        self.imagePathLine.setEnabled(True)
        self.imagePathLine.setReadOnly(True)

        self.gridLayout.addWidget(self.imagePathLine, 8, 1, 1, 1)

        self.provideModelLabel = QLabel(Dialog)
        self.provideModelLabel.setObjectName(u"provideModelLabel")

        self.gridLayout.addWidget(self.provideModelLabel, 5, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 1, 1, 3)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 8, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 0, 12, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.label, 1, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 4, 12, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.modelBrowseButton.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.mainImage.setText("")
        self.detectButton.setText(QCoreApplication.translate("Dialog", u"Detect Weapon", None))
        self.imageBrowseButton.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.provideImageLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" color:#aa0000;\">Please provide a path to a valid image (.png .jpg .jpeg)</span></p></body></html>", None))
        self.provideModelLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" color:#aa0000;\">Please provide a path to a valid gun detection model file (.pt .pth)</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">PB\u015a AI Gun Detection</span></p></body></html>", None))
    # retranslateUi

