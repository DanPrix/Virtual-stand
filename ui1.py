# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1111, 530)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        Dialog.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 1111, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(40, 40, 40, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PlanTB = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.PlanTB.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.PlanTB.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.PlanTB.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlanTB.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.PlanTB.setTabStopWidth(40)
        self.PlanTB.setObjectName("PlanTB")
        self.horizontalLayout_3.addWidget(self.PlanTB)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(40, 10, 40, 10)
        self.horizontalLayout_6.setSpacing(600)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.LeftB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.LeftB.setFont(font)
        self.LeftB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LeftB.setDefault(False)
        self.LeftB.setFlat(False)
        self.LeftB.setObjectName("LeftB")
        self.horizontalLayout_6.addWidget(self.LeftB)
        self.RightB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.RightB.setFont(font)
        self.RightB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RightB.setObjectName("RightB")
        self.horizontalLayout_6.addWidget(self.RightB)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(40, 20, 40, 20)
        self.horizontalLayout_2.setSpacing(300)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MetodB_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.MetodB_2.setFont(font)
        self.MetodB_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MetodB_2.setDefault(False)
        self.MetodB_2.setObjectName("MetodB_2")
        self.horizontalLayout_2.addWidget(self.MetodB_2)
        self.StartB_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.StartB_2.setFont(font)
        self.StartB_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartB_2.setObjectName("StartB_2")
        self.horizontalLayout_2.addWidget(self.StartB_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.PlanTB.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:14pt;\">1. ЦЕЛЬ РАБОТЫ</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt;\">    Изучить принцип действия и особенности импульсных источников питания. Ознакомится с принципом действия релейных стабилизаторов.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:8pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:14pt;\">2. ПЛАН РАБОТЫ</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:8pt;\">    </span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt;\">1. Снять внешнюю характеристику стабилизатора U</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt; vertical-align:sub;\">н</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt;\">=f(I</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt; vertical-align:sub;\">н</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt;\">) при постоянном напряжении питания.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt;\">    2. Снять нагрузочную характеристику стабилизатора U</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt; vertical-align:sub;\">н</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt;\">=f(I</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt; vertical-align:sub;\">н</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt;\">) при постоянном токе нагрузки I</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt; vertical-align:sub;\">н</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt;\">=const.</span></p></body></html>"))
        self.LeftB.setText(_translate("Dialog", "<--"))
        self.RightB.setText(_translate("Dialog", "-->"))
        self.MetodB_2.setText(_translate("Dialog", "Методические указания"))
        self.StartB_2.setText(_translate("Dialog", "Старт"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
