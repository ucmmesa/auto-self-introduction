# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'button.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("傻瓜式自我介绍生成器")
        MainWindow.resize(895, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 540, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 351, 203))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.prize_number_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.prize_number_2.setObjectName("prize_number_2")
        self.gridLayout.addWidget(self.prize_number_2, 1, 1, 1, 1)
        self.prize_number = QtWidgets.QLineEdit(self.layoutWidget)
        self.prize_number.setObjectName("prize_number")
        self.gridLayout.addWidget(self.prize_number, 0, 1, 1, 1)
        self.prize_number_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.prize_number_5.setObjectName("prize_number_5")
        self.gridLayout.addWidget(self.prize_number_5, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.prize_number_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.prize_number_6.setObjectName("prize_number_6")
        self.gridLayout.addWidget(self.prize_number_6, 5, 1, 1, 1)
        self.prize_number_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.prize_number_3.setObjectName("prize_number_3")
        self.gridLayout.addWidget(self.prize_number_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.prize_number_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.prize_number_4.setObjectName("prize_number_4")
        self.gridLayout.addWidget(self.prize_number_4, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.toStart = QtWidgets.QPushButton(self.centralwidget)
        self.toStart.setGeometry(QtCore.QRect(380, 290, 93, 28))
        self.toStart.setObjectName("toStart")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 331, 771, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(400, 20, 351, 203))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)
        self.hobby_number_1 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.hobby_number_1.setObjectName("hobby_number_1")
        self.gridLayout_2.addWidget(self.hobby_number_1, 1, 1, 1, 1)
        self.hobby_number = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.hobby_number.setObjectName("hobby_number")
        self.gridLayout_2.addWidget(self.hobby_number, 0, 1, 1, 1)
        self.hobby_number_4 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.hobby_number_4.setObjectName("hobby_number_4")
        self.gridLayout_2.addWidget(self.hobby_number_4, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.hobby_number_5 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.hobby_number_5.setObjectName("hobby_number_5")
        self.gridLayout_2.addWidget(self.hobby_number_5, 5, 1, 1, 1)
        self.hobby_number_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.hobby_number_2.setObjectName("hobby_number_2")
        self.gridLayout_2.addWidget(self.hobby_number_2, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 1)
        self.hobby_number_3 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.hobby_number_3.setObjectName("hobby_number_3")
        self.gridLayout_2.addWidget(self.hobby_number_3, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "傻瓜式自我介绍生成器 by Karshilov"))
        self.pushButton.setText(_translate("MainWindow", "关闭"))
        self.label_3.setText(_translate("MainWindow", "奖项2"))
        self.label_6.setText(_translate("MainWindow", "奖项5"))
        self.prize_number_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>奖项数</p></body></html>"))
        self.prize_number.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>奖项数</p></body></html>"))
        self.prize_number_5.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>奖项数</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "奖项1"))
        self.prize_number_6.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>奖项数</p></body></html>"))
        self.prize_number_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>奖项数</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "奖项3"))
        self.label_5.setText(_translate("MainWindow", "奖项4"))
        self.prize_number_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>奖项数</p></body></html>"))
        self.label.setText(_translate("MainWindow", "奖项数"))
        self.toStart.setText(_translate("MainWindow", "开始生成"))
        self.label_7.setText(_translate("MainWindow", "爱好2"))
        self.label_8.setText(_translate("MainWindow", "爱好5"))
        self.hobby_number_1.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>奖项数</p></body></html>"))
        self.hobby_number.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>奖项数</p></body></html>"))
        self.hobby_number_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>奖项数</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "爱好1"))
        self.hobby_number_5.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>奖项数</p></body></html>"))
        self.hobby_number_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>奖项数</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "爱好3"))
        self.label_11.setText(_translate("MainWindow", "爱好4"))
        self.hobby_number_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>奖项数</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "爱好数"))