# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\FELLab\Documents\GitHub\Interactivepg-waffle\interactivePG\curves\clickablePlotSettings.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LineSettingsDialog(object):
    def setupUi(self, LineSettingsDialog):
        LineSettingsDialog.setObjectName("LineSettingsDialog")
        LineSettingsDialog.resize(561, 466)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(LineSettingsDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(LineSettingsDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lwCurves = QtWidgets.QListWidget(self.splitter)
        self.lwCurves.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lwCurves.setObjectName("lwCurves")
        self.twCurveSettings = QtWidgets.QTabWidget(self.splitter)
        self.twCurveSettings.setObjectName("twCurveSettings")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sbLineWidth = SpinBox(self.groupBox)
        self.sbLineWidth.setObjectName("sbLineWidth")
        self.horizontalLayout.addWidget(self.sbLineWidth)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cbLineStyle = QtWidgets.QComboBox(self.groupBox_3)
        self.cbLineStyle.setObjectName("cbLineStyle")
        self.cbLineStyle.addItem("")
        self.cbLineStyle.addItem("")
        self.cbLineStyle.addItem("")
        self.cbLineStyle.addItem("")
        self.cbLineStyle.addItem("")
        self.cbLineStyle.addItem("")
        self.horizontalLayout_2.addWidget(self.cbLineStyle)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.colLine = ColorButton(self.groupBox_4)
        self.colLine.setText("")
        self.colLine.setObjectName("colLine")
        self.horizontalLayout_3.addWidget(self.colLine)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sbMarkerSize = SpinBox(self.groupBox_2)
        self.sbMarkerSize.setObjectName("sbMarkerSize")
        self.horizontalLayout_5.addWidget(self.sbMarkerSize)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cbMarkerStyle = QtWidgets.QComboBox(self.groupBox_6)
        self.cbMarkerStyle.setObjectName("cbMarkerStyle")
        self.cbMarkerStyle.addItem("")
        self.cbMarkerStyle.addItem("")
        self.cbMarkerStyle.addItem("")
        self.cbMarkerStyle.addItem("")
        self.cbMarkerStyle.addItem("")
        self.cbMarkerStyle.addItem("")
        self.cbMarkerStyle.addItem("")
        self.horizontalLayout_6.addWidget(self.cbMarkerStyle)
        self.horizontalLayout_4.addWidget(self.groupBox_6)
        self.colMarker = ColorButton(self.groupBox_5)
        self.colMarker.setText("")
        self.colMarker.setObjectName("colMarker")
        self.horizontalLayout_4.addWidget(self.colMarker)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout.addWidget(self.groupBox_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.twCurveSettings.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tXOffset = QtWidgets.QLineEdit(self.tab_2)
        self.tXOffset.setGeometry(QtCore.QRect(142, 40, 101, 21))
        self.tXOffset.setObjectName("tXOffset")
        self.tYOffset = QtWidgets.QLineEdit(self.tab_2)
        self.tYOffset.setGeometry(QtCore.QRect(192, 100, 81, 21))
        self.tYOffset.setObjectName("tYOffset")
        self.twCurveSettings.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.splitter)
        self.buttonBox = QtWidgets.QDialogButtonBox(LineSettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(LineSettingsDialog)
        self.twCurveSettings.setCurrentIndex(0)
        self.buttonBox.accepted.connect(LineSettingsDialog.accept)
        self.buttonBox.rejected.connect(LineSettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LineSettingsDialog)

    def retranslateUi(self, LineSettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        LineSettingsDialog.setWindowTitle(_translate("LineSettingsDialog", "Dialog"))
        self.groupBox_4.setTitle(_translate("LineSettingsDialog", "Line"))
        self.groupBox.setTitle(_translate("LineSettingsDialog", "Linewidth"))
        self.groupBox_3.setTitle(_translate("LineSettingsDialog", "Style"))
        self.cbLineStyle.setItemText(0, _translate("LineSettingsDialog", "None"))
        self.cbLineStyle.setItemText(1, _translate("LineSettingsDialog", "Solid"))
        self.cbLineStyle.setItemText(2, _translate("LineSettingsDialog", "Dashed"))
        self.cbLineStyle.setItemText(3, _translate("LineSettingsDialog", "Dotted"))
        self.cbLineStyle.setItemText(4, _translate("LineSettingsDialog", "Dash Dot"))
        self.cbLineStyle.setItemText(5, _translate("LineSettingsDialog", "Dash Dot Dot"))
        self.groupBox_5.setTitle(_translate("LineSettingsDialog", "Marker"))
        self.groupBox_2.setTitle(_translate("LineSettingsDialog", "Size"))
        self.groupBox_6.setTitle(_translate("LineSettingsDialog", "Style"))
        self.cbMarkerStyle.setItemText(0, _translate("LineSettingsDialog", "None"))
        self.cbMarkerStyle.setItemText(1, _translate("LineSettingsDialog", "o"))
        self.cbMarkerStyle.setItemText(2, _translate("LineSettingsDialog", "s"))
        self.cbMarkerStyle.setItemText(3, _translate("LineSettingsDialog", "t"))
        self.cbMarkerStyle.setItemText(4, _translate("LineSettingsDialog", "d"))
        self.cbMarkerStyle.setItemText(5, _translate("LineSettingsDialog", "+"))
        self.cbMarkerStyle.setItemText(6, _translate("LineSettingsDialog", "x"))
        self.twCurveSettings.setTabText(self.twCurveSettings.indexOf(self.tab), _translate("LineSettingsDialog", "Line Style"))
        self.twCurveSettings.setTabText(self.twCurveSettings.indexOf(self.tab_2), _translate("LineSettingsDialog", "Offset"))

from pyqtgraph import ColorButton, SpinBox
