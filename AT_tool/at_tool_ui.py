# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'at_tool_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 252)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ser_bt_find = QtWidgets.QPushButton(self.layoutWidget)
        self.ser_bt_find.setObjectName("ser_bt_find")
        self.horizontalLayout.addWidget(self.ser_bt_find)
        self.ser_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.ser_comboBox.setObjectName("ser_comboBox")
        self.horizontalLayout.addWidget(self.ser_comboBox)
        self.ser_bt_open = QtWidgets.QPushButton(self.layoutWidget)
        self.ser_bt_open.setObjectName("ser_bt_open")
        self.horizontalLayout.addWidget(self.ser_bt_open)
        self.ser_bt_close = QtWidgets.QPushButton(self.layoutWidget)
        self.ser_bt_close.setObjectName("ser_bt_close")
        self.horizontalLayout.addWidget(self.ser_bt_close)
        self.at_bt_config = QtWidgets.QPushButton(self.layoutWidget)
        self.at_bt_config.setObjectName("at_bt_config")
        self.horizontalLayout.addWidget(self.at_bt_config)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.at_bt_join = QtWidgets.QPushButton(self.layoutWidget)
        self.at_bt_join.setMinimumSize(QtCore.QSize(0, 0))
        self.at_bt_join.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.at_bt_join.setObjectName("at_bt_join")
        self.verticalLayout.addWidget(self.at_bt_join)
        self.at_bt_id = QtWidgets.QPushButton(self.layoutWidget)
        self.at_bt_id.setObjectName("at_bt_id")
        self.verticalLayout.addWidget(self.at_bt_id)
        self.at_bt_send = QtWidgets.QPushButton(self.layoutWidget)
        self.at_bt_send.setObjectName("at_bt_send")
        self.verticalLayout.addWidget(self.at_bt_send)
        self.at_bt_statue = QtWidgets.QPushButton(self.layoutWidget)
        self.at_bt_statue.setObjectName("at_bt_statue")
        self.verticalLayout.addWidget(self.at_bt_statue)
        self.at_bt_set_cfg = QtWidgets.QPushButton(self.layoutWidget)
        self.at_bt_set_cfg.setObjectName("at_bt_set_cfg")
        self.verticalLayout.addWidget(self.at_bt_set_cfg)
        self.at_bt_save = QtWidgets.QPushButton(self.layoutWidget)
        self.at_bt_save.setObjectName("at_bt_save")
        self.verticalLayout.addWidget(self.at_bt_save)
        self.at_bt_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.at_bt_clear.setObjectName("at_bt_clear")
        self.verticalLayout.addWidget(self.at_bt_clear)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStatusTip("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ser_bt_find.setText(_translate("MainWindow", "串口搜索"))
        self.ser_bt_open.setText(_translate("MainWindow", "打开"))
        self.ser_bt_close.setText(_translate("MainWindow", "关闭"))
        self.at_bt_config.setText(_translate("MainWindow", "填写配置"))
        self.pushButton.setText(_translate("MainWindow", "修改按键"))
        self.at_bt_join.setText(_translate("MainWindow", "请求入网"))
        self.at_bt_id.setText(_translate("MainWindow", "获取信息"))
        self.at_bt_send.setText(_translate("MainWindow", "测试发包"))
        self.at_bt_statue.setText(_translate("MainWindow", "获取状态"))
        self.at_bt_set_cfg.setText(_translate("MainWindow", "修改配置"))
        self.at_bt_save.setText(_translate("MainWindow", "保存配置"))
        self.at_bt_clear.setText(_translate("MainWindow", "清空配置"))

