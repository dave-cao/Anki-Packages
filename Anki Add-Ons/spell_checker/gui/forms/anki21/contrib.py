# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/contrib.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(352, 479)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.contribLayout = QtWidgets.QVBoxLayout()
        self.contribLayout.setContentsMargins(-1, 5, -1, 10)
        self.contribLayout.setObjectName("contribLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.labHeart = QtWidgets.QLabel(Dialog)
        self.labHeart.setText("")
        self.labHeart.setPixmap(QtGui.QPixmap(":/spell_checker/icons/heart.svg"))
        self.labHeart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labHeart.setObjectName("labHeart")
        self.horizontalLayout_3.addWidget(self.labHeart)
        self.fmtLabContrib = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fmtLabContrib.setFont(font)
        self.fmtLabContrib.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fmtLabContrib.setObjectName("fmtLabContrib")
        self.horizontalLayout_3.addWidget(self.fmtLabContrib)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.contribLayout.addLayout(self.horizontalLayout_3)
        self.fmtLabHeader = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fmtLabHeader.sizePolicy().hasHeightForWidth())
        self.fmtLabHeader.setSizePolicy(sizePolicy)
        self.fmtLabHeader.setWordWrap(True)
        self.fmtLabHeader.setOpenExternalLinks(False)
        self.fmtLabHeader.setObjectName("fmtLabHeader")
        self.contribLayout.addWidget(self.fmtLabHeader)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.contribLayout.addItem(spacerItem2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnCoffee = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCoffee.sizePolicy().hasHeightForWidth())
        self.btnCoffee.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/spell_checker/icons/coffee.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCoffee.setIcon(icon)
        self.btnCoffee.setIconSize(QtCore.QSize(32, 32))
        self.btnCoffee.setObjectName("btnCoffee")
        self.gridLayout.addWidget(self.btnCoffee, 2, 0, 1, 1)
        self.btnMail = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMail.sizePolicy().hasHeightForWidth())
        self.btnMail.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/spell_checker/icons/email.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMail.setIcon(icon1)
        self.btnMail.setIconSize(QtCore.QSize(32, 14))
        self.btnMail.setObjectName("btnMail")
        self.gridLayout.addWidget(self.btnMail, 2, 1, 1, 1)
        self.btnPatreon = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPatreon.sizePolicy().hasHeightForWidth())
        self.btnPatreon.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/spell_checker/icons/patreon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPatreon.setIcon(icon2)
        self.btnPatreon.setIconSize(QtCore.QSize(32, 32))
        self.btnPatreon.setObjectName("btnPatreon")
        self.gridLayout.addWidget(self.btnPatreon, 1, 0, 1, 2)
        self.contribLayout.addLayout(self.gridLayout)
        self.labFooter = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labFooter.sizePolicy().hasHeightForWidth())
        self.labFooter.setSizePolicy(sizePolicy)
        self.labFooter.setWordWrap(True)
        self.labFooter.setObjectName("labFooter")
        self.contribLayout.addWidget(self.labFooter)
        self.verticalLayout.addLayout(self.contribLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnCredits = QtWidgets.QPushButton(Dialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/spell_checker/icons/heart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCredits.setIcon(icon3)
        self.btnCredits.setObjectName("btnCredits")
        self.horizontalLayout_2.addWidget(self.btnCredits)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.btnPatreon, self.btnCoffee)
        Dialog.setTabOrder(self.btnCoffee, self.btnMail)
        Dialog.setTabOrder(self.btnMail, self.btnCredits)
        Dialog.setTabOrder(self.btnCredits, self.buttonBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Please support my work"))
        self.fmtLabContrib.setText(_translate("Dialog", "Love {ADDON_NAME}?"))
        self.fmtLabHeader.setText(_translate("Dialog", "<html><head/><body><p>Hi! <span style=\" font-weight:600;\">Glutanimate</span> here :). Thanks for checking out {ADDON_NAME} and some of my other add-ons. I hope you\'ve been enjoying them! </p><p>If <span style=\" font-weight:600;\">{ADDON_NAME}</span> or any of <a href=\"https://glutanimate.com/projects/\"><span style=\" text-decoration: underline; color:#2980b9;\">my other projects</span></a> has been a valuable asset in your studies, please do consider <span style=\" font-weight:600;\">supporting my work</span> through one of the methods below:</p></body></html>"))
        self.btnCoffee.setToolTip(_translate("Dialog", "Each coffee helps. Thank you!"))
        self.btnCoffee.setText(_translate("Dialog", "Fuel my work\n"
"with a coffee"))
        self.btnMail.setToolTip(_translate("Dialog", "<html>Feel free to send me an email with your idea – be it a new add-on or feature in an existing add-on – and we can work things out.</html>"))
        self.btnMail.setText(_translate("Dialog", "Hire me to work on\n"
"an add-on for you"))
        self.btnPatreon.setToolTip(_translate("Dialog", "Perks include access to Patron-only add-ons, <br>exclusive blog posts, mentions in the credits, and more!"))
        self.btnPatreon.setText(_translate("Dialog", "Become a Patron and receive \n"
"exclusive add-ons && other goodies!"))
        self.labFooter.setText(_translate("Dialog", "<html><head/><body><p>Each contribution is greatly appreciated and will help me <span style=\" font-weight:600;\">update and improve</span> my add-ons as time goes by! Thank you.</p></body></html>"))
        self.btnCredits.setText(_translate("Dialog", "Credits"))
