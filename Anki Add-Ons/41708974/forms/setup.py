# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/setup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(759, 478)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/person/icons/person.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout_6 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tabAccount = QtWidgets.QWidget()
        self.tabAccount.setObjectName("tabAccount")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabAccount)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.gl1 = QtWidgets.QGridLayout()
        self.gl1.setObjectName("gl1")
        self.login_info = QtWidgets.QLabel(self.tabAccount)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_info.setFont(font)
        self.login_info.setObjectName("login_info")
        self.gl1.addWidget(self.login_info, 2, 0, 1, 1)
        self.delete_username = QtWidgets.QLineEdit(self.tabAccount)
        self.delete_username.setText("")
        self.delete_username.setObjectName("delete_username")
        self.gl1.addWidget(self.delete_username, 6, 0, 1, 1)
        self.login_username = QtWidgets.QLineEdit(self.tabAccount)
        self.login_username.setText("")
        self.login_username.setObjectName("login_username")
        self.gl1.addWidget(self.login_username, 3, 0, 1, 1)
        self.create_username = QtWidgets.QLineEdit(self.tabAccount)
        self.create_username.setText("")
        self.create_username.setMaxLength(15)
        self.create_username.setObjectName("create_username")
        self.gl1.addWidget(self.create_username, 1, 0, 1, 1)
        self.create_info = QtWidgets.QLabel(self.tabAccount)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.create_info.setFont(font)
        self.create_info.setObjectName("create_info")
        self.gl1.addWidget(self.create_info, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tabAccount)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gl1.addWidget(self.label, 7, 0, 1, 1)
        self.delete_info = QtWidgets.QLabel(self.tabAccount)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.delete_info.setFont(font)
        self.delete_info.setObjectName("delete_info")
        self.gl1.addWidget(self.delete_info, 5, 0, 1, 1)
        self.delete_button = QtWidgets.QPushButton(self.tabAccount)
        self.delete_button.setAutoDefault(False)
        self.delete_button.setObjectName("delete_button")
        self.gl1.addWidget(self.delete_button, 6, 1, 1, 1)
        self.login_info_2 = QtWidgets.QLabel(self.tabAccount)
        font = QtGui.QFont()
        font.setItalic(True)
        self.login_info_2.setFont(font)
        self.login_info_2.setObjectName("login_info_2")
        self.gl1.addWidget(self.login_info_2, 4, 0, 1, 1)
        self.create_button = QtWidgets.QPushButton(self.tabAccount)
        self.create_button.setAutoDefault(False)
        self.create_button.setDefault(False)
        self.create_button.setObjectName("create_button")
        self.gl1.addWidget(self.create_button, 1, 1, 1, 1)
        self.login_button = QtWidgets.QPushButton(self.tabAccount)
        self.login_button.setAutoDefault(False)
        self.login_button.setDefault(False)
        self.login_button.setObjectName("login_button")
        self.gl1.addWidget(self.login_button, 3, 1, 1, 1)
        self.statusMsg = QtWidgets.QTextEdit(self.tabAccount)
        self.statusMsg.setObjectName("statusMsg")
        self.gl1.addWidget(self.statusMsg, 8, 0, 1, 1)
        self.statusButton = QtWidgets.QPushButton(self.tabAccount)
        self.statusButton.setToolTip("")
        self.statusButton.setCheckable(False)
        self.statusButton.setChecked(False)
        self.statusButton.setAutoDefault(False)
        self.statusButton.setObjectName("statusButton")
        self.gl1.addWidget(self.statusButton, 8, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gl1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabAccount, "")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tabSettings)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox = QtWidgets.QGroupBox(self.tabSettings)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LB_DeckBrowser = QtWidgets.QCheckBox(self.groupBox)
        self.LB_DeckBrowser.setObjectName("LB_DeckBrowser")
        self.verticalLayout.addWidget(self.LB_DeckBrowser)
        self.lb_focus = QtWidgets.QCheckBox(self.groupBox)
        self.lb_focus.setObjectName("lb_focus")
        self.verticalLayout.addWidget(self.lb_focus)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.maxUsers_Label = QtWidgets.QLabel(self.groupBox)
        self.maxUsers_Label.setObjectName("maxUsers_Label")
        self.horizontalLayout.addWidget(self.maxUsers_Label)
        self.maxUsers = QtWidgets.QSpinBox(self.groupBox)
        self.maxUsers.setMaximum(99999)
        self.maxUsers.setObjectName("maxUsers")
        self.horizontalLayout.addWidget(self.maxUsers)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_9.addWidget(self.groupBox, 1, 0, 2, 2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tabSettings)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.country = QtWidgets.QComboBox(self.groupBox_5)
        self.country.setObjectName("country")
        self.country.addItem("")
        self.gridLayout_8.addWidget(self.country, 0, 0, 1, 1)
        self.gl3 = QtWidgets.QGridLayout()
        self.gl3.setObjectName("gl3")
        self.newday = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newday.sizePolicy().hasHeightForWidth())
        self.newday.setSizePolicy(sizePolicy)
        self.newday.setMaximum(23)
        self.newday.setObjectName("newday")
        self.gl3.addWidget(self.newday, 0, 1, 1, 1)
        self.Default_Tab = QtWidgets.QComboBox(self.groupBox_5)
        self.Default_Tab.setObjectName("Default_Tab")
        self.Default_Tab.addItem("")
        self.Default_Tab.addItem("")
        self.Default_Tab.addItem("")
        self.Default_Tab.addItem("")
        self.Default_Tab.addItem("")
        self.gl3.addWidget(self.Default_Tab, 2, 1, 1, 2)
        self.sortby_label = QtWidgets.QLabel(self.groupBox_5)
        self.sortby_label.setObjectName("sortby_label")
        self.gl3.addWidget(self.sortby_label, 1, 0, 1, 1)
        self.sortby = QtWidgets.QComboBox(self.groupBox_5)
        self.sortby.setObjectName("sortby")
        self.sortby.addItem("")
        self.sortby.addItem("")
        self.sortby.addItem("")
        self.sortby.addItem("")
        self.sortby.addItem("")
        self.gl3.addWidget(self.sortby, 1, 1, 1, 2)
        self.next_day_info2 = QtWidgets.QLabel(self.groupBox_5)
        self.next_day_info2.setObjectName("next_day_info2")
        self.gl3.addWidget(self.next_day_info2, 0, 2, 1, 1)
        self.next_day_info1 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_day_info1.sizePolicy().hasHeightForWidth())
        self.next_day_info1.setSizePolicy(sizePolicy)
        self.next_day_info1.setObjectName("next_day_info1")
        self.gl3.addWidget(self.next_day_info1, 0, 0, 1, 1)
        self.Defaul_Tab_Label = QtWidgets.QLabel(self.groupBox_5)
        self.Defaul_Tab_Label.setObjectName("Defaul_Tab_Label")
        self.gl3.addWidget(self.Defaul_Tab_Label, 2, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gl3, 1, 0, 1, 1)
        self.scroll = QtWidgets.QCheckBox(self.groupBox_5)
        self.scroll.setObjectName("scroll")
        self.gridLayout_8.addWidget(self.scroll, 2, 0, 1, 1)
        self.refresh = QtWidgets.QCheckBox(self.groupBox_5)
        self.refresh.setEnabled(True)
        self.refresh.setObjectName("refresh")
        self.gridLayout_8.addWidget(self.refresh, 3, 0, 1, 1)
        self.autosync = QtWidgets.QCheckBox(self.groupBox_5)
        self.autosync.setObjectName("autosync")
        self.gridLayout_8.addWidget(self.autosync, 4, 0, 1, 1)
        self.medals = QtWidgets.QCheckBox(self.groupBox_5)
        self.medals.setObjectName("medals")
        self.gridLayout_8.addWidget(self.medals, 5, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_5, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_9.addItem(spacerItem1, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tabSettings, "")
        self.tabGroup = QtWidgets.QWidget()
        self.tabGroup.setObjectName("tabGroup")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tabGroup)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tabGroup)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.manage_newRepeat = QtWidgets.QLineEdit(self.groupBox_4)
        self.manage_newRepeat.setText("")
        self.manage_newRepeat.setEchoMode(QtWidgets.QLineEdit.Password)
        self.manage_newRepeat.setPlaceholderText("")
        self.manage_newRepeat.setObjectName("manage_newRepeat")
        self.gridLayout_4.addWidget(self.manage_newRepeat, 4, 1, 1, 1)
        self.addAdmin_Label = QtWidgets.QLabel(self.groupBox_4)
        self.addAdmin_Label.setObjectName("addAdmin_Label")
        self.gridLayout_4.addWidget(self.addAdmin_Label, 5, 0, 1, 1)
        self.new_repeat_pwd_label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.new_repeat_pwd_label_2.setObjectName("new_repeat_pwd_label_2")
        self.gridLayout_4.addWidget(self.new_repeat_pwd_label_2, 4, 0, 1, 1)
        self.manageGroup = QtWidgets.QComboBox(self.groupBox_4)
        self.manageGroup.setObjectName("manageGroup")
        self.manageGroup.addItem("")
        self.gridLayout_4.addWidget(self.manageGroup, 0, 0, 1, 2)
        self.manage_newPwd = QtWidgets.QLineEdit(self.groupBox_4)
        self.manage_newPwd.setText("")
        self.manage_newPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.manage_newPwd.setPlaceholderText("")
        self.manage_newPwd.setObjectName("manage_newPwd")
        self.gridLayout_4.addWidget(self.manage_newPwd, 2, 1, 1, 1)
        self.manage_old_label = QtWidgets.QLabel(self.groupBox_4)
        self.manage_old_label.setObjectName("manage_old_label")
        self.gridLayout_4.addWidget(self.manage_old_label, 1, 0, 1, 1)
        self.new_pwd_label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.new_pwd_label_2.setObjectName("new_pwd_label_2")
        self.gridLayout_4.addWidget(self.new_pwd_label_2, 2, 0, 1, 1)
        self.oldPwd = QtWidgets.QLineEdit(self.groupBox_4)
        self.oldPwd.setText("")
        self.oldPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.oldPwd.setObjectName("oldPwd")
        self.gridLayout_4.addWidget(self.oldPwd, 1, 1, 1, 1)
        self.manageSave = QtWidgets.QPushButton(self.groupBox_4)
        self.manageSave.setAutoDefault(False)
        self.manageSave.setObjectName("manageSave")
        self.gridLayout_4.addWidget(self.manageSave, 6, 0, 1, 2)
        self.newAdmin = QtWidgets.QLineEdit(self.groupBox_4)
        self.newAdmin.setObjectName("newAdmin")
        self.gridLayout_4.addWidget(self.newAdmin, 5, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_4)
        self.gridLayout_7.addWidget(self.groupBox_4, 2, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabGroup)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.subject = QtWidgets.QComboBox(self.groupBox_2)
        self.subject.setObjectName("subject")
        self.subject.addItem("")
        self.verticalLayout_5.addWidget(self.subject)
        self.join_pwd_label = QtWidgets.QLabel(self.groupBox_2)
        self.join_pwd_label.setObjectName("join_pwd_label")
        self.verticalLayout_5.addWidget(self.join_pwd_label)
        self.joinPwd = QtWidgets.QLineEdit(self.groupBox_2)
        self.joinPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.joinPwd.setClearButtonEnabled(False)
        self.joinPwd.setObjectName("joinPwd")
        self.verticalLayout_5.addWidget(self.joinPwd)
        self.joinGroup = QtWidgets.QPushButton(self.groupBox_2)
        self.joinGroup.setAutoDefault(False)
        self.joinGroup.setObjectName("joinGroup")
        self.verticalLayout_5.addWidget(self.joinGroup)
        self.group_list = QtWidgets.QListWidget(self.groupBox_2)
        self.group_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.group_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.group_list.setObjectName("group_list")
        self.verticalLayout_5.addWidget(self.group_list)
        self.leaveGroup = QtWidgets.QPushButton(self.groupBox_2)
        self.leaveGroup.setAutoDefault(False)
        self.leaveGroup.setObjectName("leaveGroup")
        self.verticalLayout_5.addWidget(self.leaveGroup)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.gridLayout_7.addWidget(self.groupBox_2, 0, 0, 3, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_7.addItem(spacerItem2, 3, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabGroup)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.newRepeat = QtWidgets.QLineEdit(self.groupBox_3)
        self.newRepeat.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newRepeat.setPlaceholderText("")
        self.newRepeat.setObjectName("newRepeat")
        self.gridLayout.addWidget(self.newRepeat, 4, 1, 1, 1)
        self.newPwd = QtWidgets.QLineEdit(self.groupBox_3)
        self.newPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPwd.setObjectName("newPwd")
        self.gridLayout.addWidget(self.newPwd, 3, 1, 1, 1)
        self.add_newGroup = QtWidgets.QPushButton(self.groupBox_3)
        self.add_newGroup.setCheckable(False)
        self.add_newGroup.setChecked(False)
        self.add_newGroup.setAutoDefault(False)
        self.add_newGroup.setObjectName("add_newGroup")
        self.gridLayout.addWidget(self.add_newGroup, 5, 0, 1, 2)
        self.new_repeat_pwd_label = QtWidgets.QLabel(self.groupBox_3)
        self.new_repeat_pwd_label.setObjectName("new_repeat_pwd_label")
        self.gridLayout.addWidget(self.new_repeat_pwd_label, 4, 0, 1, 1)
        self.newGroup = QtWidgets.QLineEdit(self.groupBox_3)
        self.newGroup.setObjectName("newGroup")
        self.gridLayout.addWidget(self.newGroup, 0, 0, 3, 2)
        self.new_pwd_label = QtWidgets.QLabel(self.groupBox_3)
        self.new_pwd_label.setObjectName("new_pwd_label")
        self.gridLayout.addWidget(self.new_pwd_label, 3, 0, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout)
        self.gridLayout_7.addWidget(self.groupBox_3, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem3, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tabGroup, "")
        self.tabFriends = QtWidgets.QWidget()
        self.tabFriends.setObjectName("tabFriends")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabFriends)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gl4 = QtWidgets.QGridLayout()
        self.gl4.setObjectName("gl4")
        self.friends_list = QtWidgets.QListWidget(self.tabFriends)
        self.friends_list.setStyleSheet("")
        self.friends_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.friends_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.friends_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.friends_list.setObjectName("friends_list")
        self.gl4.addWidget(self.friends_list, 3, 0, 1, 1)
        self.friend_username = QtWidgets.QLineEdit(self.tabFriends)
        self.friend_username.setText("")
        self.friend_username.setObjectName("friend_username")
        self.gl4.addWidget(self.friend_username, 1, 0, 1, 1)
        self.vl1 = QtWidgets.QVBoxLayout()
        self.vl1.setObjectName("vl1")
        self.remove_friend_button = QtWidgets.QPushButton(self.tabFriends)
        self.remove_friend_button.setAutoDefault(False)
        self.remove_friend_button.setObjectName("remove_friend_button")
        self.vl1.addWidget(self.remove_friend_button)
        self.import_friends = QtWidgets.QPushButton(self.tabFriends)
        self.import_friends.setAutoDefault(False)
        self.import_friends.setObjectName("import_friends")
        self.vl1.addWidget(self.import_friends)
        self.export_friends = QtWidgets.QPushButton(self.tabFriends)
        self.export_friends.setAutoDefault(False)
        self.export_friends.setObjectName("export_friends")
        self.vl1.addWidget(self.export_friends)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vl1.addItem(spacerItem4)
        self.gl4.addLayout(self.vl1, 3, 1, 1, 1)
        self.add_friends_button = QtWidgets.QPushButton(self.tabFriends)
        self.add_friends_button.setAutoDefault(False)
        self.add_friends_button.setObjectName("add_friends_button")
        self.gl4.addWidget(self.add_friends_button, 1, 1, 1, 1)
        self.friend_list_info = QtWidgets.QLabel(self.tabFriends)
        self.friend_list_info.setObjectName("friend_list_info")
        self.gl4.addWidget(self.friend_list_info, 2, 0, 1, 1)
        self.add_friend_info = QtWidgets.QLabel(self.tabFriends)
        self.add_friend_info.setObjectName("add_friend_info")
        self.gl4.addWidget(self.add_friend_info, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gl4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabFriends, "")
        self.tabHiddenUsers = QtWidgets.QWidget()
        self.tabHiddenUsers.setObjectName("tabHiddenUsers")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabHiddenUsers)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.hiddenUsers = QtWidgets.QListWidget(self.tabHiddenUsers)
        self.hiddenUsers.setObjectName("hiddenUsers")
        self.verticalLayout_4.addWidget(self.hiddenUsers)
        self.unhideButton = QtWidgets.QPushButton(self.tabHiddenUsers)
        self.unhideButton.setObjectName("unhideButton")
        self.verticalLayout_4.addWidget(self.unhideButton)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabHiddenUsers, "")
        self.tabAbout = QtWidgets.QWidget()
        self.tabAbout.setObjectName("tabAbout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabAbout)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.about_text = QtWidgets.QTextBrowser(self.tabAbout)
        self.about_text.setStyleSheet("QTextEdit\n"
"{\n"
"    border: 0;\n"
"}")
        self.about_text.setOpenExternalLinks(True)
        self.about_text.setObjectName("about_text")
        self.verticalLayout_2.addWidget(self.about_text)
        self.tabWidget.addTab(self.tabAbout, "")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.create_username, self.create_button)
        Dialog.setTabOrder(self.create_button, self.login_username)
        Dialog.setTabOrder(self.login_username, self.login_button)
        Dialog.setTabOrder(self.login_button, self.delete_username)
        Dialog.setTabOrder(self.delete_username, self.delete_button)
        Dialog.setTabOrder(self.delete_button, self.statusMsg)
        Dialog.setTabOrder(self.statusMsg, self.statusButton)
        Dialog.setTabOrder(self.statusButton, self.country)
        Dialog.setTabOrder(self.country, self.newday)
        Dialog.setTabOrder(self.newday, self.sortby)
        Dialog.setTabOrder(self.sortby, self.Default_Tab)
        Dialog.setTabOrder(self.Default_Tab, self.scroll)
        Dialog.setTabOrder(self.scroll, self.refresh)
        Dialog.setTabOrder(self.refresh, self.autosync)
        Dialog.setTabOrder(self.autosync, self.medals)
        Dialog.setTabOrder(self.medals, self.LB_DeckBrowser)
        Dialog.setTabOrder(self.LB_DeckBrowser, self.lb_focus)
        Dialog.setTabOrder(self.lb_focus, self.maxUsers)
        Dialog.setTabOrder(self.maxUsers, self.subject)
        Dialog.setTabOrder(self.subject, self.joinPwd)
        Dialog.setTabOrder(self.joinPwd, self.joinGroup)
        Dialog.setTabOrder(self.joinGroup, self.group_list)
        Dialog.setTabOrder(self.group_list, self.leaveGroup)
        Dialog.setTabOrder(self.leaveGroup, self.newGroup)
        Dialog.setTabOrder(self.newGroup, self.newPwd)
        Dialog.setTabOrder(self.newPwd, self.newRepeat)
        Dialog.setTabOrder(self.newRepeat, self.add_newGroup)
        Dialog.setTabOrder(self.add_newGroup, self.manageGroup)
        Dialog.setTabOrder(self.manageGroup, self.oldPwd)
        Dialog.setTabOrder(self.oldPwd, self.manage_newPwd)
        Dialog.setTabOrder(self.manage_newPwd, self.manage_newRepeat)
        Dialog.setTabOrder(self.manage_newRepeat, self.newAdmin)
        Dialog.setTabOrder(self.newAdmin, self.manageSave)
        Dialog.setTabOrder(self.manageSave, self.friend_username)
        Dialog.setTabOrder(self.friend_username, self.add_friends_button)
        Dialog.setTabOrder(self.add_friends_button, self.friends_list)
        Dialog.setTabOrder(self.friends_list, self.remove_friend_button)
        Dialog.setTabOrder(self.remove_friend_button, self.import_friends)
        Dialog.setTabOrder(self.import_friends, self.export_friends)
        Dialog.setTabOrder(self.export_friends, self.hiddenUsers)
        Dialog.setTabOrder(self.hiddenUsers, self.unhideButton)
        Dialog.setTabOrder(self.unhideButton, self.about_text)
        Dialog.setTabOrder(self.about_text, self.tabWidget)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Leaderboard Config"))
        self.login_info.setText(_translate("Dialog", "Login:"))
        self.delete_username.setPlaceholderText(_translate("Dialog", "Username"))
        self.login_username.setPlaceholderText(_translate("Dialog", "Username"))
        self.create_username.setPlaceholderText(_translate("Dialog", "Username"))
        self.create_info.setText(_translate("Dialog", "Create Account:"))
        self.label.setText(_translate("Dialog", "Status:"))
        self.delete_info.setText(_translate("Dialog", "Delete Account:"))
        self.delete_button.setText(_translate("Dialog", "Delete Account"))
        self.login_info_2.setText(_translate("Dialog", "You are not logged in."))
        self.create_button.setText(_translate("Dialog", "Create Account"))
        self.login_button.setText(_translate("Dialog", "Login"))
        self.statusMsg.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.statusMsg.setPlaceholderText(_translate("Dialog", "A message that everyone can see when clicking on your username (max. 280 characters). You can use markdown to embed links."))
        self.statusButton.setText(_translate("Dialog", "Set Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAccount), _translate("Dialog", "Account"))
        self.groupBox.setTitle(_translate("Dialog", "Home screen"))
        self.LB_DeckBrowser.setText(_translate("Dialog", "Show the home screen leaderboard (only works with Anki 2.1.20+)"))
        self.lb_focus.setText(_translate("Dialog", "Focus on user"))
        self.maxUsers_Label.setText(_translate("Dialog", "Maximum number of users on the home screen Leaderboard:"))
        self.groupBox_5.setTitle(_translate("Dialog", "General"))
        self.country.setItemText(0, _translate("Dialog", "Country"))
        self.Default_Tab.setItemText(0, _translate("Dialog", "Global"))
        self.Default_Tab.setItemText(1, _translate("Dialog", "Friends"))
        self.Default_Tab.setItemText(2, _translate("Dialog", "Country"))
        self.Default_Tab.setItemText(3, _translate("Dialog", "Group"))
        self.Default_Tab.setItemText(4, _translate("Dialog", "League"))
        self.sortby_label.setText(_translate("Dialog", "Sort by:"))
        self.sortby.setItemText(0, _translate("Dialog", "Reviews"))
        self.sortby.setItemText(1, _translate("Dialog", "Time"))
        self.sortby.setItemText(2, _translate("Dialog", "Streak"))
        self.sortby.setItemText(3, _translate("Dialog", "Reviews past 31 days"))
        self.sortby.setItemText(4, _translate("Dialog", "Retention"))
        self.next_day_info2.setText(_translate("Dialog", "hours past midnight"))
        self.next_day_info1.setText(_translate("Dialog", "The next day starts"))
        self.Defaul_Tab_Label.setText(_translate("Dialog", "Default Leaderboard:"))
        self.scroll.setText(_translate("Dialog", "Automatically scroll to user"))
        self.refresh.setText(_translate("Dialog", "Refresh the Leaderboard every two minutes (beta, only for Anki 2.1.24+)\n"
"Sorting will be disabled"))
        self.autosync.setText(_translate("Dialog", "Sync when deck is finished (only works with Anki 2.1.20+)"))
        self.medals.setText(_translate("Dialog", "Show league medals next to username"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), _translate("Dialog", "Settings"))
        self.groupBox_4.setTitle(_translate("Dialog", "Manage groups"))
        self.addAdmin_Label.setText(_translate("Dialog", "Add admin:"))
        self.new_repeat_pwd_label_2.setText(_translate("Dialog", "Repeat password:"))
        self.manageGroup.setItemText(0, _translate("Dialog", "Select a group you\'re an admin of"))
        self.manage_old_label.setText(_translate("Dialog", "Old password:"))
        self.new_pwd_label_2.setText(_translate("Dialog", "New password"))
        self.oldPwd.setPlaceholderText(_translate("Dialog", "leave empty if it\'s currently not password protected"))
        self.manageSave.setText(_translate("Dialog", "Save"))
        self.groupBox_2.setTitle(_translate("Dialog", "Join/Leave group"))
        self.subject.setItemText(0, _translate("Dialog", "Join a group"))
        self.join_pwd_label.setText(_translate("Dialog", "If it\'s a private group, please enter the password:"))
        self.joinGroup.setText(_translate("Dialog", "Join group"))
        self.leaveGroup.setText(_translate("Dialog", "Leave group"))
        self.groupBox_3.setTitle(_translate("Dialog", "Request new group"))
        self.newPwd.setPlaceholderText(_translate("Dialog", "optional"))
        self.add_newGroup.setText(_translate("Dialog", "Request group"))
        self.new_repeat_pwd_label.setText(_translate("Dialog", "Repeat password:"))
        self.newGroup.setPlaceholderText(_translate("Dialog", "Group name"))
        self.new_pwd_label.setText(_translate("Dialog", "Password:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGroup), _translate("Dialog", "Groups"))
        self.friend_username.setPlaceholderText(_translate("Dialog", "Friend"))
        self.remove_friend_button.setText(_translate("Dialog", "Remove"))
        self.import_friends.setText(_translate("Dialog", "Import"))
        self.export_friends.setText(_translate("Dialog", "Export"))
        self.add_friends_button.setText(_translate("Dialog", "Add"))
        self.friend_list_info.setText(_translate("Dialog", "Your friends:"))
        self.add_friend_info.setText(_translate("Dialog", "Add friend:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFriends), _translate("Dialog", "Friends"))
        self.unhideButton.setText(_translate("Dialog", "Unhide"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHiddenUsers), _translate("Dialog", "Hidden Users"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAbout), _translate("Dialog", "About"))
from . import icons_rc
