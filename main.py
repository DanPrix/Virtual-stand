from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem, QDesktopWidget, QDialog

import res_rc

class Ui_Dialog0(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowState(QtCore.Qt.WindowMaximized)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        Dialog.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, screen_width, int(screen_height*0.915)))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(40, 40, 40, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_3.addWidget(self.graphicsView)

        image_path2 = ":метод.png"
        pixmap = QPixmap(image_path2)
        item = QGraphicsPixmapItem(pixmap)
        
        self.graphicsScene = QtWidgets.QGraphicsScene(self.graphicsView)
        self.graphicsView.setScene(self.graphicsScene)
        self.graphicsScene.addItem(item)

        
        
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(40, 20, 40, 20)
        self.horizontalLayout_2.setSpacing(300)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ExitB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.ExitB.setFont(font)
        self.ExitB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitB.setDefault(False)
        self.ExitB.setObjectName("ExitB")
        self.horizontalLayout_2.addWidget(self.ExitB)
        self.ExitB.clicked.connect(self.back)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Методические материалы"))
        self.ExitB.setText(_translate("Dialog", "Закрыть"))

    def back(self):
        Dialog0.hide()

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog.setObjectName("Dialog1")
        Dialog.setWindowState(QtCore.Qt.WindowMaximized)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, screen_width, int(screen_height*0.9)))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(40, 40, 40, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PlanTB = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.PlanTB.setFont(font)
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.RightB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.RightB.setMinimumSize(QtCore.QSize(214, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.RightB.setFont(font)
        self.RightB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RightB.setObjectName("RightB")
        self.RightB.clicked.connect(self.next_window)
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
        self.MetodB_2.clicked.connect(self.openMethod)
        self.StartB_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.StartB_2.setFont(font)
        self.StartB_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartB_2.setObjectName("StartB_2")
        self.StartB_2.clicked.connect(self.start_window)
        self.horizontalLayout_2.addWidget(self.StartB_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog1", "ИССЛЕДОВАНИЕ МНОГОФАЗНЫХ СХЕМ ВЫПРЯМЛЕНИЯ"))
        self.PlanTB.setHtml(_translate("Dialog1",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\';\">Данная программа является виртуальной лабораторной работой «Исследование многофазных схем выпрямления». Ознакомьтесь с планом работы перейдя по «стрелке». Перед началом работы на стенде внимательно ознакомьтесь с методическими указаниями. Для работы на стенде нажмите «Старт».</span></p></body></html>"))
        self.RightB.setText(_translate("Dialog1", "-->"))
        self.MetodB_2.setText(_translate("Dialog1", "Методические указания"))
        self.StartB_2.setText(_translate("Dialog1", "Старт"))
    def next_window(self):
        Dialog.hide()
        Dialog1.show()

    def start_window(self):
        Dialog.hide()
        Dialog5.show()
    
    def openMethod(self):
        Dialog0.show()
        


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowState(QtCore.Qt.WindowMaximized)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        Dialog.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, screen_width, int(screen_height*0.9)))
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
        self.LeftB.clicked.connect(self.prev_window)
        self.horizontalLayout_6.addWidget(self.LeftB)
        self.RightB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.RightB.setFont(font)
        self.RightB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RightB.setObjectName("RightB")
        self.RightB.clicked.connect(self.next_window)
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
        self.MetodB_2.clicked.connect(self.openMethod)
        self.StartB_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.StartB_2.setFont(font)
        self.StartB_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartB_2.setObjectName("StartB_2")
        self.StartB_2.clicked.connect(self.start_window)
        self.horizontalLayout_2.addWidget(self.StartB_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ИССЛЕДОВАНИЕ МНОГОФАЗНЫХ СХЕМ ВЫПРЯМЛЕНИЯ"))
        self.PlanTB.setHtml(_translate("Dialog",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                       "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:16pt;\">1. ЦЕЛЬ РАБОТЫ</span></p>\n"
                                       "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:8pt;\"> </span></p>\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt;\">   Ознакомиться с принципом действия, режимами работы и параметрами многофазных схем выпрямления. Экспериментальное исследование работы трех многофазных схем выпрямления на нагрузку индуктивного характера и определение их основных параметров.</span></p>\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:8pt;\"> </span></p>\n"
                                       "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:16pt;\">2. ПОРЯДОК ВЫПОЛНЕНИЕЯ РАБОТЫ</span></p>\n"
                                       "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:8pt;\"> </span></p>\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:8pt;\">     </span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt;\">1. Снять внешние характеристики U</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt; vertical-align:sub;\">н</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt;\"> = f(I</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:11pt; vertical-align:sub;\">н</span><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt;\">) при U<span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt; vertical-align:sub;\">с</span> = const трёхфазной, шестифазной и мостовой схем выпрямления.</span></p>\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt;\">    2. Определить внутренние сопротивления выпрямителей r.</span></p>\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt;\">    3. Определить коэффициенты пульсаций выпрямленного напряжения K<span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt; vertical-align:sub;\">n</span>.</span></p>\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt;\">    4. Определить КПД (η) и коэффициент мощности (χ) исследуемых схем выпрямления.</span></p>\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt;\">    5. Для каждой из схемвыпрямления определить габаритную мощность первичной (S<span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt; vertical-align:sub;\">1</span>) и вторичной (S<span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt; vertical-align:sub;\">2</span>) обмотки, а также габаритную мощностью трансформатора (S<span style=\" font-family:\'Times New Roman,Times,serif\'; font-size:15pt; vertical-align:sub;\">тр</span>).</span></p>\n</body></html>"))
        self.LeftB.setText(_translate("Dialog", "<--"))
        self.RightB.setText(_translate("Dialog", "-->"))
        self.MetodB_2.setText(_translate("Dialog", "Методические указания"))
        self.StartB_2.setText(_translate("Dialog", "Старт"))

    def next_window(self):
        Dialog1.hide()
        Dialog2.show()

    def prev_window(self):
        Dialog1.hide()
        Dialog.show()

    def start_window(self):
        Dialog1.hide()
        Dialog5.show()
    
    def openMethod(self):
        Dialog0.show()

class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowState(QtCore.Qt.WindowMaximized)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, screen_width, int(screen_height*0.9)))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(40, 40, 40, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.QuestTB = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.QuestTB.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.QuestTB.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.QuestTB.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.QuestTB.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.QuestTB.setTabStopWidth(40)
        self.QuestTB.setObjectName("QuestTB")
        self.horizontalLayout_3.addWidget(self.QuestTB)
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
        self.LeftB.clicked.connect(self.prev_window)
        self.horizontalLayout_6.addWidget(self.LeftB)
        self.RightB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.RightB.setFont(font)
        self.RightB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RightB.setObjectName("RightB")
        self.RightB.clicked.connect(self.next_window)
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
        self.MetodB_2.clicked.connect(self.openMethod)
        self.StartB_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.StartB_2.setFont(font)
        self.StartB_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartB_2.setObjectName("StartB_2")
        self.StartB_2.clicked.connect(self.start_window)
        self.horizontalLayout_2.addWidget(self.StartB_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ИССЛЕДОВАНИЕ МНОГОФАЗНЫХ СХЕМ ВЫПРЯМЛЕНИЯ"))
        self.QuestTB.setHtml(_translate("Dialog",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Пользуясь методическими указаниями подготовьте ответы на вопросы и получите допуск к работе на стенде от</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">преподавателя.</p>\n"
                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Вопросы к допуску для выполнения лабораторной работы.</p>\n"
                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1. Пояcнить назначение устройств и основные функции.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2. Последовательность выполнение работ на стенде.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3. Типы опытов.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    4. Сущность проводимых опытов.</p></body></html>"))
        self.LeftB.setText(_translate("Dialog", "<--"))
        self.RightB.setText(_translate("Dialog", "-->"))
        self.MetodB_2.setText(_translate("Dialog", "Методические указания"))
        self.StartB_2.setText(_translate("Dialog", "Старт"))

    def next_window(self):
        Dialog2.hide()
        Dialog3.show()

    def prev_window(self):
        Dialog2.hide()
        Dialog1.show()

    def start_window(self):
        Dialog2.hide()
        Dialog5.show()

    def openMethod(self):
        Dialog0.show()

class Ui_Dialog4(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowState(QtCore.Qt.WindowMaximized)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, screen_width, int(screen_height*0.9)))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(40, 40, 40, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.StrucTB = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.StrucTB.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.StrucTB.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.StrucTB.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.StrucTB.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.StrucTB.setTabStopWidth(40)
        self.StrucTB.setObjectName("StrucTB")
        self.horizontalLayout_3.addWidget(self.StrucTB)
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
        self.LeftB.clicked.connect(self.prev_window)
        self.horizontalLayout_6.addWidget(self.LeftB)
        self.RightB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.RightB.setFont(font)
        self.RightB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RightB.setObjectName("RightB")
        self.RightB.clicked.connect(self.next_window)
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
        self.MetodB_2.clicked.connect(self.openMethod)
        self.StartB_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.StartB_2.setFont(font)
        self.StartB_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartB_2.setObjectName("StartB_2")
        self.StartB_2.clicked.connect(self.start_window)
        self.horizontalLayout_2.addWidget(self.StartB_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ИССЛЕДОВАНИЕ МНОГОФАЗНЫХ СХЕМ ВЫПРЯМЛЕНИЯ"))
        self.StrucTB.setHtml(_translate("Dialog",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">СОДЕРЖАНИЕ ОТЧЕТА</span></p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"> </span></p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1. Цель и план проведения лабораторной работы.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2. Структурно-функциональную схему.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3. Электрическую принципиальную схему.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    4. Таблицы с результатами измерений и расчетов.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    5. Графические зависимости в соответствии c требованиями и экспериментальные результаты.</p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    6. Выводы.</p></body></html>"))
        self.LeftB.setText(_translate("Dialog", "<--"))
        self.RightB.setText(_translate("Dialog", "-->"))
        self.MetodB_2.setText(_translate("Dialog", "Методические указания"))
        self.StartB_2.setText(_translate("Dialog", "Старт"))

    def next_window(self):
        Dialog3.hide()
        Dialog4.show()

    def prev_window(self):
        Dialog3.hide()
        Dialog2.show()

    def start_window(self):
        Dialog3.hide()
        Dialog5.show()

    def openMethod(self):
        Dialog0.show()

class Ui_Dialog5(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowState(QtCore.Qt.WindowMaximized)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, screen_width, int(screen_height*0.9)))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(40, 40, 40, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.StrucTB = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.StrucTB.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.StrucTB.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.StrucTB.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.StrucTB.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.StrucTB.setTabStopWidth(40)
        self.StrucTB.setObjectName("StrucTB")
        self.horizontalLayout_3.addWidget(self.StrucTB)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(40, 10, 40, 10)
        self.horizontalLayout_6.setSpacing(600)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.LeftB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.LeftB.setMinimumSize(QtCore.QSize(214, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.LeftB.setFont(font)
        self.LeftB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LeftB.setDefault(False)
        self.LeftB.setFlat(False)
        self.LeftB.setObjectName("LeftB")
        self.LeftB.clicked.connect(self.prev_window)
        self.horizontalLayout_6.addWidget(self.LeftB)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
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
        self.MetodB_2.clicked.connect(self.openMethod)
        self.StartB_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.StartB_2.setFont(font)
        self.StartB_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartB_2.setObjectName("StartB_2")
        self.StartB_2.clicked.connect(self.start_window)
        self.horizontalLayout_2.addWidget(self.StartB_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ИССЛЕДОВАНИЕ МНОГОФАЗНЫХ СХЕМ ВЫПРЯМЛЕНИЯ"))
        self.StrucTB.setHtml(_translate("Dialog",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Программа по изучению многофазных схем выпрямления составлена студентами 4-го курса, группы БЗС2001:<br>Безяев Д.С.<br>Севрюков С.И.<br>Руководители:<br>Шакиров К.Ф.<br>Яблочников С.Л.</p></body></html>"))
        self.LeftB.setText(_translate("Dialog", "<--"))
        self.MetodB_2.setText(_translate("Dialog", "Методические указания"))
        self.StartB_2.setText(_translate("Dialog", "Старт"))

    def prev_window(self):
        Dialog4.hide()
        Dialog3.show()

    def start_window(self):
        Dialog4.hide()
        Dialog5.show()

    def openMethod(self):
        Dialog0.show()

class Ui_Dialog6(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowState(QtCore.Qt.WindowMaximized)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, screen_width, int(screen_height*0.9)))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(40, 20, 40, 20)
        self.horizontalLayout_2.setSpacing(300)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MetodB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.MetodB.setFont(font)
        self.MetodB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MetodB.setDefault(False)
        self.MetodB.setObjectName("MetodB")
        self.horizontalLayout_2.addWidget(self.MetodB)
        self.MetodB.clicked.connect(self.openMethod)
        self.StartMenuB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.StartMenuB.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.StartMenuB.setFont(font)
        self.StartMenuB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartMenuB.setObjectName("StartMenuB")
        self.StartMenuB.clicked.connect(self.start_window)
        self.horizontalLayout_2.addWidget(self.StartMenuB)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(10, 5, 10, 5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_4.addWidget(self.lcdNumber)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_11.addWidget(self.label_8)
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.verticalLayout_11.addWidget(self.lcdNumber_6)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_5.addWidget(self.lcdNumber_2)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.verticalLayout_6.addWidget(self.lcdNumber_3)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.verticalLayout_7.addWidget(self.lcdNumber_4)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.verticalLayout_3.addWidget(self.lcdNumber_5)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(5, 10, 5, 10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        self.frame = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.frame.setObjectName("frame")
        self.verticalLayout_9.addWidget(self.frame)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.Sai1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Sai1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Sai1.setChecked(True)
        self.Sai1.setObjectName("Sai1")
        self.verticalLayout_9.addWidget(self.Sai1)
        self.Sai2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Sai2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Sai2.setObjectName("Sai2")
        self.verticalLayout_9.addWidget(self.Sai2)
        self.Sai3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Sai3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Sai3.setObjectName("Sai3")
        self.verticalLayout_9.addWidget(self.Sai3)
        self.Sai1.clicked.connect(self.sai)
        self.Sai2.clicked.connect(self.sai)
        self.Sai3.clicked.connect(self.sai)
        self.Q1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.Q1.setObjectName("Q1")
        self.Q1.clicked.connect(self.check_key)
        self.verticalLayout_9.addWidget(self.Q1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)

        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_6.addWidget(self.graphicsView)

        image_path = ":стенд.png"
        pixmap = QPixmap(image_path)
        image_path1 = ":1.png"
        pixmap1 = QPixmap(image_path1)
        self.item1 = QGraphicsPixmapItem(pixmap1)
        image_path2 = ":2.png"
        pixmap2 = QPixmap(image_path2)
        self.item2 = QGraphicsPixmapItem(pixmap2)
        

        self.graphicsScene = QtWidgets.QGraphicsScene(self.graphicsView)
        self.graphicsView.setScene(self.graphicsScene)
        item = QGraphicsPixmapItem(pixmap)
        self.graphicsScene.addItem(item)

        self.graphicsScene1 = QtWidgets.QGraphicsScene(self.frame)
        self.frame.setScene(self.graphicsScene1)
        self.graphicsScene1.addItem(self.item1)

        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(5, 10, 5, 10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_12.addWidget(self.label_9)
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.verticalLayout_12.addWidget(self.lcdNumber_7)
        self.verticalLayout_10.addLayout(self.verticalLayout_12)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.dial_2 = QtWidgets.QDial(self.verticalLayoutWidget)
        self.dial_2.setObjectName("dial_2")
        self.dial_2.valueChanged.connect(self.r_dial)
        self.verticalLayout_10.addWidget(self.dial_2)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_8)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ИССЛЕДОВАНИЕ МНОГОФАЗНЫХ СХЕМ ВЫПРЯМЛЕНИЯ"))
        self.MetodB.setText(_translate("Dialog", "Методические указания"))
        self.StartMenuB.setText(_translate("Dialog", "Стартовый экран"))
        self.label.setText(_translate("Dialog", "V1"))
        self.label_8.setText(_translate("Dialog", "V2"))
        self.label_2.setText(_translate("Dialog", "A1"))
        self.label_3.setText(_translate("Dialog", "A2"))
        self.label_4.setText(_translate("Dialog", "Vн"))
        self.label_5.setText(_translate("Dialog", "Aн"))
        self.Q1.setText(_translate("Dialog", "QFF1"))
        self.label_9.setText(_translate("Dialog", "W"))
        self.label_7.setText(_translate("Dialog", "Rн"))
        self.Sai1.setText(_translate("Dialog", "SAI (1)"))
        self.Sai2.setText(_translate("Dialog", "SAI (2)"))
        self.Sai3.setText(_translate("Dialog", "SAI (3)"))


    def check_key(self):
        if self.Q1.isChecked():
            self.recalc()
        else:
            self.clear()

    def start_window(self):
        Dialog5.hide()
        Dialog.show()

    def r_dial(self, value):
        if self.Q1.isChecked():
            self.recalc()
        else:
            self.clear()

    def sai(self):
        if self.Q1.isChecked():
            self.recalc()
        else:
            self.clear()
        if self.Sai1.isChecked():
            self.graphicsScene1.removeItem(self.item2)
            self.graphicsScene1.addItem(self.item1)
        elif self.Sai2.isChecked():
            self.graphicsScene1.removeItem(self.item1)
            self.graphicsScene1.addItem(self.item2)
        else:
            self.graphicsScene1.removeItem(self.item1)
            self.graphicsScene1.addItem(self.item2)

    def recalc(self):
        n = self.dial_2.value()
        if self.Sai1.isChecked():
            res = 0.006*n - 1.322e-19*n*n + 4.41e-22*n*n*n
            self.lcdNumber_5.display(round(res, 2))     #In
            res = 48.9 - 0.6733 * n + 0.0146 * n * n - 0.0001547 * n * n * n + 5.76e-07 * n * n * n * n
            self.lcdNumber_4.display(round(res, 2))     #Un
            res = 0.4 + 0.5487*n - 0.01532*n*n + 0.0001749*n*n*n - 7.04e-07*n*n*n*n
            self.lcdNumber.display(round(res, 2))       #U1
            res = 36 - 0.04 * n
            self.lcdNumber_6.display(round(res, 2))     #U2
            res = 0.45 + 0.0031 * n - 7.533e-05 * n * n + 1.44e-06 * n * n * n - 7.467e-09 * n * n * n * n
            self.lcdNumber_2.display(round(res, 2))     #I1
            res = 0.01 + 0.005433*n - 0.0003767*n*n + 7.307e-06*n*n*n - 3.733e-08*n*n*n*n
            self.lcdNumber_3.display(round(res, 2))     #I2
            res = 2 + 0.14*n - 0.003467*n*n + 4.8e-05*n*n*n - 2.133e-07*n*n*n*n
            self.lcdNumber_7.display(round(res, 2))     #W
        elif self.Sai2.isChecked():
            res = 0.01 * n
            self.lcdNumber_5.display(round(res, 2))  # In
            res = 86 - 0.7847 * n + 0.01365 * n * n - 0.0001653 * n * n * n + 6.827e-07 * n * n * n * n
            self.lcdNumber_4.display(round(res, 2))  # Un
            res = 1.05 + 0.2578 * n - 0.007737 * n * n + 8.827e-05 * n * n * n - 3.573e-07 * n * n * n * n
            self.lcdNumber.display(round(res, 2))  # U1
            res = 36 - 0.1933 * n + 0.0016 * n * n - 1.067e-05 * n * n * n
            self.lcdNumber_6.display(round(res, 2))  # U2
            res = 0.45 + 0.004633 * n + 0.0001847 * n * n - 2.933e-06 * n * n * n + 1.173e-08 * n * n * n * n
            self.lcdNumber_2.display(round(res, 2))  # I1
            res = 0.01 - 0.02047 * n + 0.001196 * n * n - 1.621e-05 * n * n * n + 7.04e-08 * n * n * n * n
            self.lcdNumber_3.display(round(res, 2))  # I2
            res = 2 + 0.29 * n - 0.0042 * n * n + 6.4e-05 * n * n * n - 3.2e-07 * n * n * n * n
            self.lcdNumber_7.display(round(res, 2))  # W
        else:
            res = 0.006333 * n + 5.333e-05 * n * n - 8.533e-07 * n * n * n + 4.267e-09 * n * n * n * n
            self.lcdNumber_5.display(round(res, 2))  # In
            res = 49 - 0.2113 * n + 0.001133 * n * n - 1.067e-06 * n * n * n - 2.133e-08 * n * n * n * n
            self.lcdNumber_4.display(round(res, 2))  # Un
            res = 0.42 + 0.1073 * n - 0.003093 * n * n + 2.987e-05 * n * n * n - 9.387e-08 * n * n * n * n
            self.lcdNumber.display(round(res, 2))  # U1
            res = 36 + 0.03333 * n - 0.0016 * n * n + 1.067e-05 * n * n * n
            self.lcdNumber_6.display(round(res, 2))  # U2
            res = 0.45 - 0.0007 * n + 0.000154 * n * n - 2.08e-06 * n * n * n + 9.6e-09 * n * n * n * n
            self.lcdNumber_2.display(round(res, 2))  # I1
            res = 0.01 - 0.001433 * n + 0.0001447 * n * n - 3.467e-06 * n * n * n + 2.453e-08 * n * n * n * n
            self.lcdNumber_3.display(round(res, 2))  # I2
            res = 2 + 0.16 * n - 0.003467 * n * n + 4.8e-05 * n * n * n - 2.133e-07 * n * n * n * n
            self.lcdNumber_7.display(round(res, 2))  # W

    def clear(self):
        self.lcdNumber_5.display(0)
        self.lcdNumber.display(0)
        self.lcdNumber_4.display(0)
        self.lcdNumber_3.display(0)
        self.lcdNumber_6.display(0)
        self.lcdNumber_2.display(0)
        self.lcdNumber_7.display(0)

    def openMethod(self):
        Dialog0.show()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    desktop = QDesktopWidget()
    screen_rect = desktop.screenGeometry()

    # Получаем ширину и высоту экрана
    screen_width = screen_rect.width()
    screen_height = screen_rect.height()

    Dialog0 = QtWidgets.QDialog()
    Dialog = QtWidgets.QDialog()
    Dialog1 = QtWidgets.QDialog()
    Dialog2 = QtWidgets.QDialog()
    Dialog3 = QtWidgets.QDialog()
    Dialog4 = QtWidgets.QDialog()
    Dialog5 = QtWidgets.QDialog()
    Dialog6 = QtWidgets.QDialog()


    ui0 = Ui_Dialog0()
    ui1 = Ui_Dialog1()
    ui2 = Ui_Dialog2()
    ui3 = Ui_Dialog3()
    ui4 = Ui_Dialog4()
    ui5 = Ui_Dialog5()
    ui6 = Ui_Dialog6()

    ui0.setupUi(Dialog0)
    ui1.setupUi(Dialog)
    ui2.setupUi(Dialog1)
    ui3.setupUi(Dialog2)
    ui4.setupUi(Dialog3)
    ui5.setupUi(Dialog4)
    ui6.setupUi(Dialog5)

    Dialog0.setStyleSheet("""
        QWidget {
            background-color: #2E2E2E;  /* Темно-серый цвет фона */
        }
        QTextBrowser {
            background-color: #505050;  /* Темно-серый цвет фона текстового поля */
            border: 2px solid #2E2E2E;  /* Темно-серый цвет границы текстового поля */
            border-radius: 10px;  /* Скругление углов текстового поля */
            color: #FFFFFF;  /* Белый цвет текста в текстовом поле */
        }
        QPushButton {
            background-color: #4CAF50; /* Зеленый цвет фона кнопки */
            color: white; /* Белый цвет текста на кнопке */
            border: 2px solid #4CAF50; /* Зеленый цвет границы кнопки */
            border-radius: 5px; /* Скругление углов кнопки */
            padding: 10px 20px; /* Поля вокруг текста на кнопке */
        }
        QPushButton:hover {
            background-color: #45a049; /* Темно-зеленый цвет фона при наведении */
        }
    """)

    Dialog.setStyleSheet("""
        QWidget {
            background-color: #2E2E2E;  /* Темно-серый цвет фона */
        }
        QTextBrowser {
            background-image: url(:back2.png);  /* Темно-серый цвет фона текстового поля */
            border: 2px solid #2E2E2E;  /* Темно-серый цвет границы текстового поля */
            border-radius: 10px;  /* Скругление углов текстового поля */
            color: #FFFFFF;  /* Белый цвет текста в текстовом поле */
            padding: 40px;
        }
        QPushButton {
            background-color: #4CAF50; /* Зеленый цвет фона кнопки */
            color: white; /* Белый цвет текста на кнопке */
            border: 2px solid #4CAF50; /* Зеленый цвет границы кнопки */
            border-radius: 5px; /* Скругление углов кнопки */
            padding: 10px 20px; /* Поля вокруг текста на кнопке */
        }
        QPushButton:hover {
            background-color: #45a049; /* Темно-зеленый цвет фона при наведении */
        }
    """)
    Dialog1.setStyleSheet("""
        QWidget {
            background-color: #2E2E2E;  /* Темно-серый цвет фона */
        }
        QTextBrowser {
            background-image: url(:back2.png);  /* Темно-серый цвет фона текстового поля */
            border: 2px solid #2E2E2E;  /* Темно-серый цвет границы текстового поля */
            border-radius: 10px;  /* Скругление углов текстового поля */
            color: #FFFFFF;  /* Белый цвет текста в текстовом поле */
            padding: 40px;
        }
        QPushButton {
            background-color: #4CAF50; /* Зеленый цвет фона кнопки */
            color: white; /* Белый цвет текста на кнопке */
            border: 2px solid #4CAF50; /* Зеленый цвет границы кнопки */
            border-radius: 5px; /* Скругление углов кнопки */
            padding: 10px 20px; /* Поля вокруг текста на кнопке */
        }
        QPushButton:hover {
            background-color: #45a049; /* Темно-зеленый цвет фона при наведении */
        }
    """)
    Dialog2.setStyleSheet("""
        QWidget {
            background-color: #2E2E2E;  /* Темно-серый цвет фона */
        }
        QTextBrowser {
            background-image: url(:back2.png);  /* Темно-серый цвет фона текстового поля */
            border: 2px solid #2E2E2E;  /* Темно-серый цвет границы текстового поля */
            border-radius: 10px;  /* Скругление углов текстового поля */
            color: #FFFFFF;  /* Белый цвет текста в текстовом поле */
            padding: 40px;
        }
        QPushButton {
            background-color: #4CAF50; /* Зеленый цвет фона кнопки */
            color: white; /* Белый цвет текста на кнопке */
            border: 2px solid #4CAF50; /* Зеленый цвет границы кнопки */
            border-radius: 5px; /* Скругление углов кнопки */
            padding: 10px 20px; /* Поля вокруг текста на кнопке */
        }
        QPushButton:hover {
            background-color: #45a049; /* Темно-зеленый цвет фона при наведении */
        }
    """)
    Dialog3.setStyleSheet("""
        QWidget {
            background-color: #2E2E2E;  /* Темно-серый цвет фона */
        }
        QTextBrowser {
            background-image: url(:back2.png);  /* Темно-серый цвет фона текстового поля */
            border: 2px solid #2E2E2E;  /* Темно-серый цвет границы текстового поля */
            border-radius: 10px;  /* Скругление углов текстового поля */
            color: #FFFFFF;  /* Белый цвет текста в текстовом поле */
            padding: 40px;
        }
        QPushButton {
            background-color: #4CAF50; /* Зеленый цвет фона кнопки */
            color: white; /* Белый цвет текста на кнопке */
            border: 2px solid #4CAF50; /* Зеленый цвет границы кнопки */
            border-radius: 5px; /* Скругление углов кнопки */
            padding: 10px 20px; /* Поля вокруг текста на кнопке */
        }
        QPushButton:hover {
            background-color: #45a049; /* Темно-зеленый цвет фона при наведении */
        }
    """)
    Dialog4.setStyleSheet("""
        QWidget {
            background-color: #2E2E2E;  /* Темно-серый цвет фона */
        }
        QTextBrowser {
            background-image: url(:back2.png);  /* Темно-серый цвет фона текстового поля */
            border: 2px solid #2E2E2E;  /* Темно-серый цвет границы текстового поля */
            border-radius: 10px;  /* Скругление углов текстового поля */
            color: #FFFFFF;  /* Белый цвет текста в текстовом поле */
            padding: 40px;
        }
        QPushButton {
            background-color: #4CAF50; /* Зеленый цвет фона кнопки */
            color: white; /* Белый цвет текста на кнопке */
            border: 2px solid #4CAF50; /* Зеленый цвет границы кнопки */
            border-radius: 5px; /* Скругление углов кнопки */
            padding: 10px 20px; /* Поля вокруг текста на кнопке */
        }
        QPushButton:hover {
            background-color: #45a049; /* Темно-зеленый цвет фона при наведении */
        }
    """)
    Dialog5.setStyleSheet("""
        QWidget {
            background-color: #2E2E2E;  /* Темно-серый цвет фона */
        }
        QTextBrowser {
            background-color: #505050;  /* Темно-серый цвет фона текстового поля */
            border: 2px solid #2E2E2E;  /* Темно-серый цвет границы текстового поля */
            border-radius: 10px;  /* Скругление углов текстового поля */
            color: #FFFFFF;  /* Белый цвет текста в текстовом поле */
        }
        QPushButton {
            background-color: #4CAF50; /* Зеленый цвет фона кнопки */
            color: white; /* Белый цвет текста на кнопке */
            border: 2px solid #4CAF50; /* Зеленый цвет границы кнопки */
            border-radius: 5px; /* Скругление углов кнопки */
            padding: 10px 20px; /* Поля вокруг текста на кнопке */
        }
        QPushButton:hover {
            background-color: #45a049; /* Темно-зеленый цвет фона при наведении */
        }
        QLabel {
            color: white;
        }
        QCheckBox {
            color: white;
            font: 20px;
        }
        QCheckBox::indicator:unchecked {
            image: url(":off.png");
        }
        QCheckBox::indicator:checked {
            image: url(":on.png");
        }
        QCheckBox::indicator{
            width: 150px;
            height: 60px;
        }
        QRadioButton{
            margin-left: 40px;
            color: white;
            font: 20px;
            margin-bottom: 15px;
        }
        #frame{
            max-width: 210px;            
        }
        
    """)

    Dialog.show()


    sys.exit(app.exec_())