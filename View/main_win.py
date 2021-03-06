# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import traceback
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel, QLineEdit, QComboBox, QPushButton

from View.MyQLabelImpl import MyQLabel
from View.add_win import AddPersonForm
from View.icon_label import ICON_label
from channel_dao_impl import ChannelDaoImpl
from model import Person
from person_dao_impl import PersonDaoImpl
from tools import readJPG2RGB, getKeyByValue


class Ui_main_win(object):
    def setupUi(self, main_win):
        main_win.setObjectName("main_win")
        main_win.resize(932, 468)
        self.centralwidget = QtWidgets.QWidget(main_win)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 911, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_tab = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.main_tab.setMouseTracking(False)
        self.main_tab.setObjectName("main_tab")
        self.monitor_tab = QtWidgets.QWidget()
        self.monitor_tab.setObjectName("monitor_tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.monitor_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 881, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.M_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.M_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.M_gridLayout.setSpacing(20)
        self.M_gridLayout.setObjectName("M_gridLayout")
        self.M_channel_info_vl = QtWidgets.QVBoxLayout()
        self.M_channel_info_vl.setObjectName("M_channel_info_vl")
        self.M_channel_choice_hl = QtWidgets.QHBoxLayout()
        self.M_channel_choice_hl.setObjectName("M_channel_choice_hl")
        self.M_channel_choice_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.M_channel_choice_label.setFont(font)
        self.M_channel_choice_label.setObjectName("M_channel_choice_label")
        self.M_channel_choice_hl.addWidget(self.M_channel_choice_label)
        self.M_channel_choice_combox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.M_channel_choice_combox.setEditable(False)
        self.M_channel_choice_combox.setObjectName("M_channel_choice_combox")
        self.M_channel_choice_hl.addWidget(self.M_channel_choice_combox)
        self.M_channel_choice_hl.setStretch(0, 1)
        self.M_channel_choice_hl.setStretch(1, 2)
        self.M_channel_info_vl.addLayout(self.M_channel_choice_hl)

        self.M_channel_name_vl = QtWidgets.QHBoxLayout()
        self.M_channel_name_vl.setObjectName("M_channel_name_vl")
        self.channel_name_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.channel_name_label.setFont(font)
        self.channel_name_label.setObjectName("channel_name_label")
        self.M_channel_name_vl.addWidget(self.channel_name_label)
        self.channel_name_show_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.channel_name_show_label.setObjectName("channel_name_show_label")
        self.M_channel_name_vl.addWidget(self.channel_name_show_label)
        self.M_channel_name_vl.setStretch(0, 1)
        self.M_channel_name_vl.setStretch(1, 2)
        self.M_channel_info_vl.addLayout(self.M_channel_name_vl)

        self.M_channel_area_vl = QtWidgets.QHBoxLayout()
        self.M_channel_area_vl.setObjectName("M_channel_area_vl")
        self.channel_area_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.channel_area_label.setFont(font)
        self.channel_area_label.setObjectName("channel_area_label")
        self.M_channel_area_vl.addWidget(self.channel_area_label)
        self.channel_area_show_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.channel_area_show_label.setObjectName("channel_area_show_label")
        self.M_channel_area_vl.addWidget(self.channel_area_show_label)
        self.M_channel_area_vl.setStretch(0, 1)
        self.M_channel_area_vl.setStretch(1, 2)
        self.M_channel_info_vl.addLayout(self.M_channel_area_vl)



        self.M_channel_model_vl = QtWidgets.QHBoxLayout()
        self.M_channel_model_vl.setObjectName("M_channel_model_vl")
        self.channel_mode_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.channel_mode_label.setFont(font)
        self.channel_mode_label.setObjectName("channel_mode_label")
        self.M_channel_model_vl.addWidget(self.channel_mode_label)
        self.channel_mode_show_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.channel_mode_show_label.setObjectName("channel_mode_show_label")
        self.M_channel_model_vl.addWidget(self.channel_mode_show_label)
        self.M_channel_model_vl.setStretch(0, 1)
        self.M_channel_model_vl.setStretch(1, 2)
        self.M_channel_info_vl.addLayout(self.M_channel_model_vl)



        self.M_channel_features_hl = QtWidgets.QHBoxLayout()
        self.M_channel_features_hl.setObjectName("M_channel_features_hl")
        self.M_channel_features_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.M_channel_features_label.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.M_channel_features_label.setFont(font)
        self.M_channel_features_label.setObjectName("M_channel_features_label")
        self.M_channel_features_hl.addWidget(self.M_channel_features_label)
        self.M_channel_features_show_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.M_channel_features_show_label.setObjectName("M_channel_features_show_label")
        self.M_channel_features_hl.addWidget(self.M_channel_features_show_label)
        self.M_channel_features_hl.setStretch(0, 1)
        self.M_channel_features_hl.setStretch(1, 2)
        self.M_channel_info_vl.addLayout(self.M_channel_features_hl)
        self.M_gridLayout.addLayout(self.M_channel_info_vl, 0, 0, 1, 1)

        self.M_gridLayout.setColumnStretch(0, 1)
        self.M_gridLayout.setColumnStretch(1, 2)
        self.main_tab.addTab(self.monitor_tab, "")
        self.class_tab = QtWidgets.QWidget()
        self.class_tab.setObjectName("class_tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.class_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 881, 361))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.C_gl = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.C_gl.setContentsMargins(0, 0, 0, 0)
        self.C_gl.setObjectName("C_gl")
        self.main_tab.addTab(self.class_tab, "")
        self.dorm_tab = QtWidgets.QWidget()
        self.dorm_tab.setObjectName("dorm_tab")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.dorm_tab)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 881, 361))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.DO_gl = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.DO_gl.setContentsMargins(0, 0, 0, 0)
        self.DO_gl.setObjectName("DO_gl")
        self.main_tab.addTab(self.dorm_tab, "")
        self.all_tab = QtWidgets.QWidget()
        self.all_tab.setObjectName("all_tab")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.all_tab)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 881, 361))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.A_gl = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.A_gl.setContentsMargins(0, 0, 0, 0)
        self.A_gl.setObjectName("A_gl")
        self.main_tab.addTab(self.all_tab, "")
        self.data_tab = QtWidgets.QWidget()
        self.data_tab.setObjectName("data_tab")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.data_tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 881, 361))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.D_gl = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.D_gl.setContentsMargins(0, 0, 0, 0)
        self.D_gl.setObjectName("D_gl")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.D_choice_channel_hl = QtWidgets.QHBoxLayout()
        self.D_choice_channel_hl.setObjectName("D_choice_channel_hl")
        self.D_choice_channel_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.D_choice_channel_label.setObjectName("D_choice_channel_label")
        self.D_choice_channel_hl.addWidget(self.D_choice_channel_label)
        self.D_choice_channel_combox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.D_choice_channel_combox.setEnabled(True)
        self.D_choice_channel_combox.setObjectName("D_choice_channel_combox")
        self.D_choice_channel_combox.addItem("")
        self.D_choice_channel_hl.addWidget(self.D_choice_channel_combox)
        self.D_choice_channel_hl.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.D_choice_channel_hl)
        self.D_choice_mode_hl = QtWidgets.QHBoxLayout()
        self.D_choice_mode_hl.setObjectName("D_choice_mode_hl")
        self.D_choice_mode_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.D_choice_mode_label.setObjectName("D_choice_mode_label")
        self.D_choice_mode_hl.addWidget(self.D_choice_mode_label)
        self.D_chioce_mode_combox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.D_chioce_mode_combox.setObjectName("D_chioce_mode_combox")
        self.D_chioce_mode_combox.addItem("")
        self.D_choice_mode_hl.addWidget(self.D_chioce_mode_combox)
        self.D_choice_mode_hl.setStretch(0, 1)
        self.D_choice_mode_hl.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.D_choice_mode_hl)
        self.D_chioce_features_hl = QtWidgets.QHBoxLayout()
        self.D_chioce_features_hl.setObjectName("D_chioce_features_hl")
        self.D_chioce_features_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.D_chioce_features_label.setObjectName("D_chioce_features_label")
        self.D_chioce_features_hl.addWidget(self.D_chioce_features_label)
        self.D_chioce_features_combox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.D_chioce_features_combox.setObjectName("D_chioce_features_combox")
        self.D_chioce_features_combox.addItem("")
        self.D_chioce_features_hl.addWidget(self.D_chioce_features_combox)
        self.D_chioce_features_hl.setStretch(0, 1)
        self.D_chioce_features_hl.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.D_chioce_features_hl)
        self.D_chioce_time_hl = QtWidgets.QHBoxLayout()
        self.D_chioce_time_hl.setObjectName("D_chioce_time_hl")
        self.D_chioce_time_checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.D_chioce_time_checkbox.setObjectName("D_chioce_time_checkbox")
        self.D_chioce_time_hl.addWidget(self.D_chioce_time_checkbox)
        self.D_chioce_time_timeedit = QtWidgets.QDateEdit(self.gridLayoutWidget_3)
        self.D_chioce_time_timeedit.setEnabled(False)
        self.D_chioce_time_timeedit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 4, 23), QtCore.QTime(0, 0, 0)))
        self.D_chioce_time_timeedit.setCalendarPopup(True)
        self.D_chioce_time_timeedit.setObjectName("D_chioce_time_timeedit")
        self.D_chioce_time_hl.addWidget(self.D_chioce_time_timeedit)
        self.D_chioce_time_hl.setStretch(0, 1)
        self.D_chioce_time_hl.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.D_chioce_time_hl)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.D_gl.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.D_data_scrollarea = QtWidgets.QScrollArea(self.gridLayoutWidget_3)
        self.D_data_scrollarea.setWidgetResizable(True)
        self.D_data_scrollarea.setObjectName("D_data_scrollarea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 653, 357))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.D_data_scrollarea.setWidget(self.scrollAreaWidgetContents)
        self.D_gl.addWidget(self.D_data_scrollarea, 0, 1, 1, 1)
        self.D_gl.setColumnStretch(0, 1)
        self.D_gl.setColumnStretch(1, 3)
        self.main_tab.addTab(self.data_tab, "")
        self.person_tab = QtWidgets.QWidget()
        self.person_tab.setObjectName("person_tab")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.person_tab)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 891, 371))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")

        # self.P_gl = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        # self.P_gl.setContentsMargins(0, 0, 0, 0)
        # self.P_gl.setObjectName("P_gl")
        # self.P_search_hl = QtWidgets.QHBoxLayout()
        # self.P_search_hl.setObjectName("P_search_hl")
        # spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.P_search_hl.addItem(spacerItem)
        # self.P_search_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        # self.P_search_label.setObjectName("P_search_label")
        # self.P_search_hl.addWidget(self.P_search_label)
        # self.P_search_lineedit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        # self.P_search_lineedit.setObjectName("P_search_lineedit")
        # self.P_search_hl.addWidget(self.P_search_lineedit)
        # self.P_search_btn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        # self.P_search_btn.setObjectName("P_search_btn")
        # self.P_search_hl.addWidget(self.P_search_btn)
        # spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.P_search_hl.addItem(spacerItem1)
        # self.P_search_hl.setStretch(0, 8)
        # self.P_search_hl.setStretch(1, 1)
        # self.P_search_hl.setStretch(2, 5)
        # self.P_search_hl.setStretch(3, 2)
        # self.P_search_hl.setStretch(4, 8)
        # self.P_gl.addLayout(self.P_search_hl, 0, 0, 1, 1)
        # self.P_data_table = QtWidgets.QTableWidget(self.gridLayoutWidget_4)
        # self.P_data_table.setObjectName("P_data_table")
        # self.P_data_table.setColumnCount(0)
        # self.P_data_table.setRowCount(0)
        # self.P_gl.addWidget(self.P_data_table, 1, 0, 1, 1)
        self.P_gl = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.P_gl.setContentsMargins(0, 0, 0, 0)
        self.P_gl.setObjectName("P_gl")
        self.P_search_hl = QtWidgets.QHBoxLayout()
        self.P_search_hl.setObjectName("P_search_hl")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.P_search_hl.addItem(spacerItem)
        self.P_search_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.P_search_label.setObjectName("P_search_label")
        self.P_search_hl.addWidget(self.P_search_label)
        self.P_search_lineedit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.P_search_lineedit.setObjectName("P_search_lineedit")
        self.P_search_hl.addWidget(self.P_search_lineedit)
        self.P_search_btn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.P_search_btn.setObjectName("P_search_btn")
        self.P_search_hl.addWidget(self.P_search_btn)
        self.P_add_btn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.P_add_btn.setObjectName("P_add_btn")
        self.P_search_hl.addWidget(self.P_add_btn)
        self.P_reset_btn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.P_reset_btn.setObjectName("P_reset_btn")
        self.P_search_hl.addWidget(self.P_reset_btn)
        self.P_search_hl.setStretch(0, 9)
        self.P_search_hl.setStretch(2, 5)
        self.P_search_hl.setStretch(3, 2)
        self.P_search_hl.setStretch(4, 2)
        self.P_search_hl.setStretch(5, 2)
        self.P_gl.addLayout(self.P_search_hl, 0, 0, 1, 1)
        self.P_data_table = QtWidgets.QTableWidget(self.gridLayoutWidget_4)
        self.P_data_table.setObjectName("P_data_table")
        self.P_data_table.setColumnCount(0)
        self.P_data_table.setRowCount(0)
        self.P_gl.addWidget(self.P_data_table, 1, 0, 1, 1)


        self.main_tab.addTab(self.person_tab, "")
        self.setting_tab = QtWidgets.QWidget()
        self.setting_tab.setObjectName("setting_tab")
        self.main_tab.addTab(self.setting_tab, "")
        self.verticalLayout.addWidget(self.main_tab)
        main_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_win)
        self.main_tab.setCurrentIndex(1)
        self.M_channel_choice_combox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_win)

    def retranslateUi(self, main_win):
        _translate = QtCore.QCoreApplication.translate
        main_win.setWindowTitle(_translate("main_win", "??????????????????"))
        self.M_channel_choice_label.setText(_translate("main_win", "???????????????"))

        self.channel_name_label.setText(_translate("main_win", "???????????????"))
        self.channel_name_show_label.setText(_translate("main_win", "??????"))

        self.channel_area_label.setText(_translate("main_win", "???????????????"))
        self.channel_area_show_label.setText(_translate("main_win", "??????"))

        self.channel_mode_label.setText(_translate("main_win", "???????????????"))
        self.channel_mode_show_label.setText(_translate("main_win", "????????????"))
        self.M_channel_features_label.setText(_translate("main_win", "???????????????"))
        self.M_channel_features_show_label.setText(_translate("main_win", "????????????"))

        self.main_tab.setTabText(self.main_tab.indexOf(self.monitor_tab), _translate("main_win", "????????????"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.class_tab), _translate("main_win", "??????????????????"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.dorm_tab), _translate("main_win", "??????????????????"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.all_tab), _translate("main_win", "??????????????????"))

        self.D_choice_channel_label.setText(_translate("main_win", "????????????"))
        self.D_choice_channel_combox.setItemText(0, _translate("main_win", "??????1"))
        self.D_choice_mode_label.setText(_translate("main_win", "????????????"))
        self.D_chioce_mode_combox.setItemText(0, _translate("main_win", "????????????"))
        self.D_chioce_features_label.setText(_translate("main_win", "????????????"))
        self.D_chioce_features_combox.setItemText(0, _translate("main_win", "??????????????????"))
        self.D_chioce_time_checkbox.setText(_translate("main_win", "????????????"))
        self.pushButton.setText(_translate("main_win", "??????"))
        self.pushButton_2.setText(_translate("main_win", "??????"))
        self.pushButton_3.setText(_translate("main_win", "????????????"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.data_tab), _translate("main_win", "????????????"))

        # self.P_search_label.setText(_translate("main_win", "??????"))
        # self.P_search_btn.setText(_translate("main_win", "??????"))
        self.P_search_label.setText(_translate("main_win", "??????"))
        self.P_search_btn.setText(_translate("main_win", "??????"))
        self.P_add_btn.setText(_translate("main_win", "????????????"))
        self.P_reset_btn.setText(_translate("main_win", "??????"))

        self.main_tab.setTabText(self.main_tab.indexOf(self.person_tab), _translate("main_win", "????????????"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.setting_tab), _translate("main_win", "????????????"))



class MyMainForm(QMainWindow, Ui_main_win):
    def __init__(self, labelDict,CHANNEL_DICT,ChannelRefreshThreadDict,parent=None):
        super(MyMainForm, self).__init__(parent)
        # Label??????
        self.labelDict = labelDict
        self.setupUi(self)

        self.channelDict = CHANNEL_DICT
        self.ChannelRefreshThreadDict = ChannelRefreshThreadDict

        self.D_tab_curItemCount = 0

        self.CDI = ChannelDaoImpl()
        self.PDI = PersonDaoImpl()

        # ??????
        # ????????????
        self.P_data_table.setColumnCount(8)  # ????????????
        self.P_data_table.setHorizontalHeaderLabels(['??????ID', '????????????', '????????????', '????????????', '??????', '??????', '??????', '??????'])
        # ??????????????????
        self.P_table_widget_list = list()

        # ??????????????????
        self.glDict = dict()
        self.glDict["A_label"] = {
            "tab_gl":self.gridLayoutWidget_6,
            "label_gl":self.A_gl
        }
        self.glDict["class"] = {
            "tab_gl": self.gridLayoutWidget_2,
            "label_gl": self.C_gl
        }
        self.glDict["dorm"] = {
            "tab_gl": self.gridLayoutWidget_5,
            "label_gl": self.DO_gl
        }

        # ??????label
        self.setLabel()



    def setLabel(self):
        # ???????????????label
        self.M_frame_label = MyQLabel(self.gridLayoutWidget,channelDict=self.channelDict)
        self.M_frame_label.setObjectName("M_frame_label")
        self.M_gridLayout.addWidget(self.M_frame_label, 0, 1, 1, 1)

        self.labelDict["M_label"] = self.M_frame_label
        # ??????A_label
        self.setGLbyLabel("A_label")
        # ????????????
        self.setGLbyLabel("dorm")
        # ????????????
        self.setGLbyLabel("class")

        # ??????A_label

    # ??????Label????????????Gl
    def setGLbyLabel(self,clz):

        curRow = 0
        curCol = 0
        channelList = None
        count = 0
        labelBandStr = None
        # ?????????????????????
        if clz == "A_label":
           # ?????????????????????
           channelList = self.labelDict["labelClass"]["all"]
           count = len(channelList)
           print("???????????????{0}????????????{1}".format(count, channelList))
           labelBandStr = "A_label"
        elif clz == "class":# ?????????????????????
            channelList = self.labelDict["labelClass"]["class"]
            count = len(channelList)
            print("???????????????{0}????????????{1}".format(count,channelList))
            labelBandStr = "C_label"
        elif clz == "dorm":# ?????????????????????
            channelList = self.labelDict["labelClass"]["dormin"]
            for dormout in self.labelDict["labelClass"]["dormout"]:
                channelList.append(dormout)
            count = len(channelList)
            print("???????????????{0}????????????{1}".format(count, channelList))
            labelBandStr = "C_label"




        # ??????????????????
        if count == 0:
            label = MyQLabel(self.glDict[clz]["tab_gl"])
            self.glDict[clz]["label_gl"].addWidget(label,0, 0, 1, 1)
            label.setText("???????????????")
            return

        # ??????????????????
        # gl_width = self.glDict[clz]["label_gl"].width()
        # gl_height = self.glDict[clz]["label_gl"].height()

        # ??????????????????1
        if count == 1:
            label = MyQLabel(self.glDict[clz]["tab_gl"],channelID=channelList[0],channelDict=self.channelDict)
            self.glDict[clz]["label_gl"].addWidget(label,0, 0, 1, 1)
            label.setFixedSize(361 / count, 361 / count)
            self.labelDict[labelBandStr][channelList[0]] = label
            return



        # ??????
        for channelID in channelList:

            # ????????????

            # ????????????label
            label = MyQLabel(self.glDict[clz]["tab_gl"],channelID=channelList[0],channelDict=self.channelDict)
            # ???????????????
            self.glDict[clz]["label_gl"].addWidget(label,curRow,curCol,1,1)
            label.setFixedSize(881/count,881/count)
            curCol += 1
            if curCol == 8:
                curCol = 0
                curRow += 1

            #label.setText(label,channelID)
            # ???Labeldict?????????
            self.labelDict[labelBandStr][channelID] = label

    # ??????????????????
    def setChannel(self):
        self.set_M_tab()
        # ??????D_tab????????????
        self.setD_tab_content()
        # ??????????????????
        self.connect()

    # ??????D_tab????????????
    def setD_tab_content(self):

        self.P_table_widget_list.clear()
        self.P_data_table.clearContents()
        # ????????????
        # ????????????Item??????
        self.D_tab_curItemCount = len(self.channelDict["personForTabel"])
        self.P_data_table.setRowCount(self.D_tab_curItemCount)  # ????????????
        curRow = 0
        for personInfo in self.channelDict["personForTabel"]:
            # ????????????
            # ????????????Item??????ID
            person_id = personInfo[0]
            # ????????????
            #personImg = readJPG2RGB(personInfo[1])
            person_img = QImage(personInfo[1])
            # ????????????
            personName = personInfo[2]
            # ????????????
            personClz = personInfo[3]
            # ????????????
            personDorm = personInfo[4]
            # ????????????
            personGrade = personInfo[5]
            # ????????????
            # ??????ID
            person_id_lineEdit = QLineEdit(self)
            self.P_data_table.setCellWidget(curRow, 0, person_id_lineEdit)
            person_id_lineEdit.setText(str(person_id))
            person_id_lineEdit.setEnabled(False)

            size = QSize(20, 20)
            # ????????????
            # ??????label
            imageLabel = ICON_label(self,self.channelDict,None)
            # ????????????
            imageLabel.setFixedSize(size)
            # ??????
            self.P_data_table.setCellWidget(curRow, 1, imageLabel)
            # ????????????
            imageLabel.setPixmap(QPixmap.fromImage(person_img.scaled(size)))
            # ????????????
            person_name_lineEdit = QLineEdit(self)
            self.P_data_table.setCellWidget(curRow, 2, person_name_lineEdit)
            person_name_lineEdit.setText(personName)
            # ?????????????????? combox
            comboxCurTextFlag = 0
            comboxCurStuteFlag = False
            person_clz_combox = QComboBox(self)
            for key,values in self.channelDict["personClass"].items():
                person_clz_combox.addItem(values)
                if comboxCurStuteFlag == False:
                    if personClz == key:
                        comboxCurStuteFlag = True
                    else:
                        comboxCurTextFlag +=1
            person_clz_combox.setCurrentIndex(comboxCurTextFlag)
            self.P_data_table.setCellWidget(curRow, 3, person_clz_combox)

            # ????????????
            comboxCurTextFlag = 0
            comboxCurStuteFlag = False
            person_dorm_combox = QComboBox(self)
            for key, values in self.channelDict["addr_dorm"].items():
                person_dorm_combox.addItem(values)
                if comboxCurStuteFlag == False:
                    if personDorm == key:
                        comboxCurStuteFlag = True
                    else:
                        comboxCurTextFlag += 1
            person_dorm_combox.setCurrentIndex(comboxCurTextFlag)
            self.P_data_table.setCellWidget(curRow, 4, person_dorm_combox)
            # ????????????
            comboxCurTextFlag = 0
            comboxCurStuteFlag = False
            person_class_combox = QComboBox(self)
            for key, values in self.channelDict["addr_class"].items():
                person_class_combox.addItem(values)
                if comboxCurStuteFlag == False:
                    if personGrade == key:
                        comboxCurStuteFlag = True
                    else:
                        comboxCurTextFlag += 1
            person_class_combox.setCurrentIndex(comboxCurTextFlag)
            self.P_data_table.setCellWidget(curRow, 5, person_class_combox)
            # ??????????????????
            check_btn = QPushButton(self)
            check_btn.setText("??????")
            self.P_data_table.setCellWidget(curRow, 6, check_btn)
            # ??????????????????
            # ??????????????????
            delete_btn = QPushButton(self)
            delete_btn.setText("??????")
            self.P_data_table.setCellWidget(curRow, 7, delete_btn)


            # ?????????????????????
            widget_dict = dict()
            widget_dict["person_id_lineEdit"] = person_id_lineEdit
            widget_dict["imageLabel"] = imageLabel
            imageLabel.widgetDict = widget_dict
            widget_dict["person_name_lineEdit"] = person_name_lineEdit
            widget_dict["person_clz_combox"] = person_clz_combox
            widget_dict["person_dorm_combox"] = person_dorm_combox
            widget_dict["person_class_combox"] = person_class_combox
            widget_dict["check_btn"] = check_btn
            widget_dict["delete_btn"] = delete_btn
            # ?????????????????????
            widget_dict["imageChange"] = False
            # ??????????????????
            widget_dict["imagePath"] = ""
            # ??????????????????
            widget_dict["imageEncode"] = None

            self.P_table_widget_list.append(widget_dict)
            # ??????
            #index = curRow
            check_btn.clicked.connect(partial(self.P_tab_check_btn_click, curRow))
            # ??????????????????
            self.P_tab_set_enabled_false(curRow)
            curRow += 1

    # ????????????????????????
    def P_tab_check_btn_click(self,row):
        # ????????????
        if self.P_table_widget_list[row]["check_btn"].text() == "??????":
            self.P_table_widget_list[row]["check_btn"].setText("??????")
            self.P_tab_set_enabled_true(row)
        else:
            self.P_table_widget_list[row]["check_btn"].setText("??????")
            #?????????
            class_id = getKeyByValue(self.channelDict["personClass"],self.P_table_widget_list[row]["person_clz_combox"].currentText())
            dorm = getKeyByValue(self.channelDict["addr_dorm"],self.P_table_widget_list[row]["person_dorm_combox"].currentText())
            grade = getKeyByValue(self.channelDict["addr_class"],self.P_table_widget_list[row]["person_class_combox"].currentText())
            # ?????????
            # ????????????????????????
            if self.P_table_widget_list[row]["imageChange"]:# ??????????????????
                # ????????????
                enc = self.P_table_widget_list[row]["imageEncode"]
                # ????????????
                path = self.P_table_widget_list[row]["imagePath"]

                person = Person(enc, self.P_table_widget_list[row]["person_name_lineEdit"].text(), class_id, path)
                person.id = int(self.P_table_widget_list[row]["person_id_lineEdit"].text())
                self.PDI.updatePerson(person, int(dorm), int(grade))
                # ????????????
                self.P_table_widget_list[row]["imageEncode"] = None
                self.P_table_widget_list[row]["imagePath"] = ""
                self.P_table_widget_list[row]["imageChange"] = False
                # ????????????
                person_img = QImage(path)
                size = QSize(20, 20)
                self.P_table_widget_list[row]["imageLabel"].setPixmap(QPixmap.fromImage(person_img.scaled(size)))
                # ?????????????????????
                self.channelDict["DataGetThreadContent"].append("updateFaceLib")
                self.channelDict["DataGetThreadEvent"].set()
            else:
                # ????????????
                person = Person(None,self.P_table_widget_list[row]["person_name_lineEdit"].text(),class_id,None)
                person.id = int(self.P_table_widget_list[row]["person_id_lineEdit"].text())
                self.PDI.updatePerson(person,int(dorm),int(grade))


            self.P_table_widget_list[row]["check_btn"].setText("??????")
            self.P_tab_set_enabled_false(row)

    # ????????????????????????????????????
    def P_tab_set_enabled_false(self,row):


        self.P_table_widget_list[row]["imageLabel"].setEnabled(False)
        self.P_table_widget_list[row]["person_name_lineEdit"].setEnabled(False)
        self.P_table_widget_list[row]["person_clz_combox"].setEnabled(False)
        self.P_table_widget_list[row]["person_dorm_combox"].setEnabled(False)
        self.P_table_widget_list[row]["person_class_combox"].setEnabled(False)

        self.P_table_widget_list[row]["delete_btn"].setEnabled(True)

    # ????????????????????????????????????
    def P_tab_set_enabled_true(self,row):


        self.P_table_widget_list[row]["imageLabel"].setEnabled(True)
        self.P_table_widget_list[row]["person_name_lineEdit"].setEnabled(True)
        self.P_table_widget_list[row]["person_clz_combox"].setEnabled(True)
        self.P_table_widget_list[row]["person_dorm_combox"].setEnabled(True)
        self.P_table_widget_list[row]["person_class_combox"].setEnabled(True)

        self.P_table_widget_list[row]["delete_btn"].setEnabled(False)


    #????????????tab
    def set_M_tab(self):
        # ?????????combox??????
        channelList = self.labelDict["labelClass"]["all"]
        # ????????????
        for channelID in channelList:
            self.M_channel_choice_combox.addItem(str(channelID))
        self.M_channel_choice_combox.setCurrentIndex(0)
        self.lastComboxChannelID = int(self.M_channel_choice_combox.currentText())


    def connect(self):
        self.main_tab.currentChanged['int'].connect(self.tabfun)
        self.M_channel_choice_combox.currentIndexChanged.connect(self.M_tab_combox_change)
        self.P_add_btn.clicked.connect(self.P_add_person)


    # ??????M_tab_combox????????????
    def M_tab_combox_change(self):

        # ???????????????label
        self.ChannelRefreshThreadDict[self.lastComboxChannelID].setLabelFlag(2)

        # ???????????????index
        channelID = int(self.M_channel_choice_combox.currentText())
        self.ChannelRefreshThreadDict[channelID].setLabelFlag(1)

        self.lastComboxChannelID = channelID


        # ????????????
        # ??????name
        self.channel_name_show_label.setText(self.channelDict[channelID]["info"][0])
        # area
        self.channel_area_show_label.setText(self.channelDict[channelID]["info"][1])
        # mode
        self.channel_mode_show_label.setText(self.channelDict[channelID]["info"][4])
        # features
        featuresList = self.channelDict[channelID]["info"][5]
        if len(featuresList) == 0:
            self.M_channel_features_show_label.setText("????????????")
        else:
            str = ','
            self.M_channel_features_show_label.setText(str.join(featuresList))


    def tabfun(self,index):

        # ????????????
        if index == 0:
            # # ??????combox???????????????id
            # channelID = int(self.M_channel_choice_combox.currentText())
            # # ??????
            # self.ChannelRefreshThreadDict[channelID].setLabelFlag(1)
            self.M_tab_combox_change()
        elif index == 1:#????????????
            # ??????id??????
            channelIDList = self.labelDict["labelClass"]["class"]
            for channelID in channelIDList:
                self.ChannelRefreshThreadDict[channelID].setLabelFlag(2)
        elif index == 2:#????????????
            channelList = self.labelDict["labelClass"]["dormin"]
            for dormout in self.labelDict["labelClass"]["dormout"]:
                channelList.append(dormout)

            for channelID in channelList:
                self.ChannelRefreshThreadDict[channelID].setLabelFlag(2)

        elif index == 3:#????????????
            channelIDList = self.labelDict["labelClass"]["all"]
            for channelID in channelIDList:
                self.ChannelRefreshThreadDict[channelID].setLabelFlag(3)


    # p_tab
    # ????????????????????????
    def P_add_person(self):
        self.add_form = AddPersonForm(self.channelDict)
        self.add_form.show()




if __name__ == '__main__':

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # ?????????pyqt???????????????????????????QApplication?????????sys.argv??????????????????????????????
    app = QApplication(sys.argv)
    # ???????????????
    form = MyMainForm()
    # ?????????????????????????????????
    form.show()
    # ????????????????????????????????????????????????????????????
    sys.exit(app.exec_())