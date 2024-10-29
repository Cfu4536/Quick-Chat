# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 612)
        MainWindow.setMinimumSize(QtCore.QSize(600, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1400, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 728, 414))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.user_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.user_input.setFont(font)
        self.user_input.setStyleSheet("background-color: #f0f0f0;\n"
"border-radius: 10px; \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(100, 100, 100);\n"
"\n"
"\n"
"")
        self.user_input.setPlainText("")
        self.user_input.setObjectName("user_input")
        self.horizontalLayout.addWidget(self.user_input)
        self.sent_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sent_btn.sizePolicy().hasHeightForWidth())
        self.sent_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.sent_btn.setFont(font)
        self.sent_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sent_btn.setStyleSheet("QPushButton{\n"
"\n"
"background-color: #66929ff5;\n"
"border-radius: 10px; \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"font-family: \'华文细黑\', Arial, sans-serif;\n"
"color: #929ff5;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #44929ff5;\n"
"border-radius: 10px; \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"font-family: \'华文细黑\', Arial, sans-serif;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #11929ff5;\n"
"border-radius: 10px; \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"font-family: \'华文细黑\', Arial, sans-serif;\n"
"}\n"
"\n"
"QPushButton:released{\n"
"background-color: #66929ff5;\n"
"border-radius: 10px; \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"font-family: \'华文细黑\', Arial, sans-serif;\n"
"}\n"
"\n"
"\n"
"")
        self.sent_btn.setFlat(False)
        self.sent_btn.setObjectName("sent_btn")
        self.horizontalLayout.addWidget(self.sent_btn)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_tokens = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.label_tokens.setFont(font)
        self.label_tokens.setObjectName("label_tokens")
        self.horizontalLayout_2.addWidget(self.label_tokens)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_role = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.label_role.setFont(font)
        self.label_role.setObjectName("label_role")
        self.horizontalLayout_2.addWidget(self.label_role)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.input_length = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.input_length.setFont(font)
        self.input_length.setObjectName("input_length")
        self.horizontalLayout_2.addWidget(self.input_length)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 10px; \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(100, 100, 100);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2.setStretch(5, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_4 = QtWidgets.QMenu(self.menu)
        self.menu_4.setObjectName("menu_4")
        self.menu_11 = QtWidgets.QMenu(self.menu)
        self.menu_11.setObjectName("menu_11")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_12 = QtWidgets.QMenu(self.menu_3)
        self.menu_12.setObjectName("menu_12")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menu_5)
        self.menu_6.setObjectName("menu_6")
        self.menu_8 = QtWidgets.QMenu(self.menu_5)
        self.menu_8.setObjectName("menu_8")
        self.menu_7 = QtWidgets.QMenu(self.menu_5)
        self.menu_7.setObjectName("menu_7")
        self.menu_9 = QtWidgets.QMenu(self.menu_5)
        self.menu_9.setObjectName("menu_9")
        self.menu_10 = QtWidgets.QMenu(self.menu_5)
        self.menu_10.setObjectName("menu_10")
        self.menu_13 = QtWidgets.QMenu(self.menu_5)
        self.menu_13.setObjectName("menu_13")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.new_2 = QtWidgets.QAction(MainWindow)
        self.new_2.setObjectName("new_2")
        self.open_2 = QtWidgets.QAction(MainWindow)
        self.open_2.setObjectName("open_2")
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.actionupdate = QtWidgets.QAction(MainWindow)
        self.actionupdate.setObjectName("actionupdate")
        self.actionstart = QtWidgets.QAction(MainWindow)
        self.actionstart.setObjectName("actionstart")
        self.actionasd_2 = QtWidgets.QAction(MainWindow)
        self.actionasd_2.setObjectName("actionasd_2")
        self.actionada = QtWidgets.QAction(MainWindow)
        self.actionada.setObjectName("actionada")
        self.actionda = QtWidgets.QAction(MainWindow)
        self.actionda.setObjectName("actionda")
        self.action_md = QtWidgets.QAction(MainWindow)
        self.action_md.setObjectName("action_md")
        self.action_html = QtWidgets.QAction(MainWindow)
        self.action_html.setObjectName("action_html")
        self.actionGPT = QtWidgets.QAction(MainWindow)
        self.actionGPT.setObjectName("actionGPT")
        self.actiontongyi = QtWidgets.QAction(MainWindow)
        self.actiontongyi.setObjectName("actiontongyi")
        self.actionwenxin = QtWidgets.QAction(MainWindow)
        self.actionwenxin.setObjectName("actionwenxin")
        self.actionxunfei = QtWidgets.QAction(MainWindow)
        self.actionxunfei.setObjectName("actionxunfei")
        self.actiongamma = QtWidgets.QAction(MainWindow)
        self.actiongamma.setObjectName("actiongamma")
        self.actionwpsAI = QtWidgets.QAction(MainWindow)
        self.actionwpsAI.setObjectName("actionwpsAI")
        self.actiontianyin = QtWidgets.QAction(MainWindow)
        self.actiontianyin.setObjectName("actiontianyin")
        self.actionlibulibu = QtWidgets.QAction(MainWindow)
        self.actionlibulibu.setObjectName("actionlibulibu")
        self.actionbaiduwendang = QtWidgets.QAction(MainWindow)
        self.actionbaiduwendang.setObjectName("actionbaiduwendang")
        self.actionai_bot = QtWidgets.QAction(MainWindow)
        self.actionai_bot.setObjectName("actionai_bot")
        self.actionmidjourney = QtWidgets.QAction(MainWindow)
        self.actionmidjourney.setObjectName("actionmidjourney")
        self.actionBing_DALLE3 = QtWidgets.QAction(MainWindow)
        self.actionBing_DALLE3.setObjectName("actionBing_DALLE3")
        self.actionaliyun = QtWidgets.QAction(MainWindow)
        self.actionaliyun.setObjectName("actionaliyun")
        self.actiongettokens = QtWidgets.QAction(MainWindow)
        self.actiongettokens.setObjectName("actiongettokens")
        self.actiondonation = QtWidgets.QAction(MainWindow)
        self.actiondonation.setObjectName("actiondonation")
        self.actioncancelstartup = QtWidgets.QAction(MainWindow)
        self.actioncancelstartup.setObjectName("actioncancelstartup")
        self.actionconfig = QtWidgets.QAction(MainWindow)
        self.actionconfig.setObjectName("actionconfig")
        self.actionzhushou = QtWidgets.QAction(MainWindow)
        self.actionzhushou.setObjectName("actionzhushou")
        self.actionzhongyiying = QtWidgets.QAction(MainWindow)
        self.actionzhongyiying.setObjectName("actionzhongyiying")
        self.actionyingyizhong = QtWidgets.QAction(MainWindow)
        self.actionyingyizhong.setObjectName("actionyingyizhong")
        self.actionlunwenrunse = QtWidgets.QAction(MainWindow)
        self.actionlunwenrunse.setObjectName("actionlunwenrunse")
        self.actionnvninvyou = QtWidgets.QAction(MainWindow)
        self.actionnvninvyou.setObjectName("actionnvninvyou")
        self.actionxuninanyou = QtWidgets.QAction(MainWindow)
        self.actionxuninanyou.setObjectName("actionxuninanyou")
        self.actionpython = QtWidgets.QAction(MainWindow)
        self.actionpython.setObjectName("actionpython")
        self.actionjava = QtWidgets.QAction(MainWindow)
        self.actionjava.setObjectName("actionjava")
        self.actionwebqianduan = QtWidgets.QAction(MainWindow)
        self.actionwebqianduan.setObjectName("actionwebqianduan")
        self.actionusername = QtWidgets.QAction(MainWindow)
        self.actionusername.setObjectName("actionusername")
        self.actionzhanan = QtWidgets.QAction(MainWindow)
        self.actionzhanan.setObjectName("actionzhanan")
        self.actiondeeplearning = QtWidgets.QAction(MainWindow)
        self.actiondeeplearning.setObjectName("actiondeeplearning")
        self.actionhiden = QtWidgets.QAction(MainWindow)
        self.actionhiden.setObjectName("actionhiden")
        self.action_docx = QtWidgets.QAction(MainWindow)
        self.action_docx.setObjectName("action_docx")
        self.action_txt = QtWidgets.QAction(MainWindow)
        self.action_txt.setObjectName("action_txt")
        self.action_pdf = QtWidgets.QAction(MainWindow)
        self.action_pdf.setObjectName("action_pdf")
        self.actionAPIkey = QtWidgets.QAction(MainWindow)
        self.actionAPIkey.setObjectName("actionAPIkey")
        self.actiontongyiqianwen = QtWidgets.QAction(MainWindow)
        self.actiontongyiqianwen.setObjectName("actiontongyiqianwen")
        self.actionsuno = QtWidgets.QAction(MainWindow)
        self.actionsuno.setObjectName("actionsuno")
        self.actiontishijinglin = QtWidgets.QAction(MainWindow)
        self.actiontishijinglin.setObjectName("actiontishijinglin")
        self.actionChatGPT_SC = QtWidgets.QAction(MainWindow)
        self.actionChatGPT_SC.setObjectName("actionChatGPT_SC")
        self.actionc_zhuanjai = QtWidgets.QAction(MainWindow)
        self.actionc_zhuanjai.setObjectName("actionc_zhuanjai")
        self.actionwebhouduan = QtWidgets.QAction(MainWindow)
        self.actionwebhouduan.setObjectName("actionwebhouduan")
        self.actionlinux = QtWidgets.QAction(MainWindow)
        self.actionlinux.setObjectName("actionlinux")
        self.actionmachine = QtWidgets.QAction(MainWindow)
        self.actionmachine.setObjectName("actionmachine")
        self.menu_4.addAction(self.action_md)
        self.menu_4.addAction(self.action_html)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.action_docx)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.action_txt)
        self.menu_4.addAction(self.action_pdf)
        self.menu_11.addAction(self.actionzhushou)
        self.menu_11.addSeparator()
        self.menu_11.addAction(self.actionzhongyiying)
        self.menu_11.addAction(self.actionyingyizhong)
        self.menu_11.addAction(self.actionlunwenrunse)
        self.menu_11.addSeparator()
        self.menu_11.addAction(self.actionnvninvyou)
        self.menu_11.addAction(self.actionxuninanyou)
        self.menu_11.addAction(self.actionzhanan)
        self.menu_11.addSeparator()
        self.menu_11.addAction(self.actionc_zhuanjai)
        self.menu_11.addAction(self.actionjava)
        self.menu_11.addAction(self.actionpython)
        self.menu_11.addAction(self.actionwebqianduan)
        self.menu_11.addAction(self.actionwebhouduan)
        self.menu_11.addAction(self.actionlinux)
        self.menu_11.addAction(self.actiondeeplearning)
        self.menu_11.addAction(self.actionmachine)
        self.menu.addAction(self.new_2)
        self.menu.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.actionhiden)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_11.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.actiongettokens)
        self.menu_2.addAction(self.actionhelp)
        self.menu_2.addAction(self.actionupdate)
        self.menu_2.addAction(self.actionaliyun)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actiondonation)
        self.menu_12.addAction(self.actionusername)
        self.menu_3.addAction(self.menu_12.menuAction())
        self.menu_3.addAction(self.actionada)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionstart)
        self.menu_3.addAction(self.actioncancelstartup)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionAPIkey)
        self.menu_6.addAction(self.actionGPT)
        self.menu_6.addAction(self.actionwenxin)
        self.menu_6.addAction(self.actionxunfei)
        self.menu_6.addAction(self.actiontongyiqianwen)
        self.menu_8.addAction(self.actiontianyin)
        self.menu_8.addAction(self.actionsuno)
        self.menu_7.addAction(self.actiongamma)
        self.menu_7.addAction(self.actionbaiduwendang)
        self.menu_9.addAction(self.actionlibulibu)
        self.menu_9.addAction(self.actionBing_DALLE3)
        self.menu_10.addAction(self.actionai_bot)
        self.menu_13.addAction(self.actiontishijinglin)
        self.menu_13.addAction(self.actionChatGPT_SC)
        self.menu_5.addAction(self.menu_6.menuAction())
        self.menu_5.addAction(self.menu_7.menuAction())
        self.menu_5.addAction(self.menu_9.menuAction())
        self.menu_5.addAction(self.menu_8.menuAction())
        self.menu_5.addAction(self.menu_13.menuAction())
        self.menu_5.addAction(self.menu_10.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sent_btn.setText(_translate("MainWindow", "➤"))
        self.label_tokens.setText(_translate("MainWindow", "tockens："))
        self.label.setText(_translate("MainWindow", "|"))
        self.label_role.setText(_translate("MainWindow", "Role:"))
        self.label_3.setText(_translate("MainWindow", "|"))
        self.input_length.setText(_translate("MainWindow", "0/2000"))
        self.label_2.setText(_translate("MainWindow", "按住我可拖拽"))
        self.menu.setTitle(_translate("MainWindow", "开始"))
        self.menu_4.setTitle(_translate("MainWindow", "导出对话内容"))
        self.menu_11.setTitle(_translate("MainWindow", "角色"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.menu_3.setTitle(_translate("MainWindow", "选项"))
        self.menu_12.setTitle(_translate("MainWindow", "个性化"))
        self.menu_5.setTitle(_translate("MainWindow", "效率"))
        self.menu_6.setTitle(_translate("MainWindow", "大语言"))
        self.menu_8.setTitle(_translate("MainWindow", "音乐"))
        self.menu_7.setTitle(_translate("MainWindow", "文档"))
        self.menu_9.setTitle(_translate("MainWindow", "图像生成"))
        self.menu_10.setTitle(_translate("MainWindow", "其他"))
        self.menu_13.setTitle(_translate("MainWindow", "提示词"))
        self.new_2.setText(_translate("MainWindow", "新建对话"))
        self.open_2.setText(_translate("MainWindow", "打开对话"))
        self.save.setText(_translate("MainWindow", "保存对话"))
        self.actionhelp.setText(_translate("MainWindow", "使用文档"))
        self.actionupdate.setText(_translate("MainWindow", "检查更新"))
        self.actionstart.setText(_translate("MainWindow", "设置开机自启"))
        self.actionasd_2.setText(_translate("MainWindow", "asd"))
        self.actionada.setText(_translate("MainWindow", "模型切换"))
        self.actionda.setText(_translate("MainWindow", "最大/最小化窗口"))
        self.action_md.setText(_translate("MainWindow", ".md"))
        self.action_html.setText(_translate("MainWindow", ".html"))
        self.actionGPT.setText(_translate("MainWindow", "GPT"))
        self.actiontongyi.setText(_translate("MainWindow", "tongyi"))
        self.actionwenxin.setText(_translate("MainWindow", "文心一言"))
        self.actionxunfei.setText(_translate("MainWindow", "讯飞星火"))
        self.actiongamma.setText(_translate("MainWindow", "gamma"))
        self.actionwpsAI.setText(_translate("MainWindow", "wpsAI"))
        self.actiontianyin.setText(_translate("MainWindow", "网易天音"))
        self.actionlibulibu.setText(_translate("MainWindow", "libulibu"))
        self.actionbaiduwendang.setText(_translate("MainWindow", "百度文档助手"))
        self.actionai_bot.setText(_translate("MainWindow", "ai-bot"))
        self.actionmidjourney.setText(_translate("MainWindow", "midjourney"))
        self.actionBing_DALLE3.setText(_translate("MainWindow", "Bing-DALLE3"))
        self.actionaliyun.setText(_translate("MainWindow", "阿里云服务"))
        self.actiongettokens.setText(_translate("MainWindow", "获取token"))
        self.actiondonation.setText(_translate("MainWindow", "赞助"))
        self.actioncancelstartup.setText(_translate("MainWindow", "取消开机自启"))
        self.actionconfig.setText(_translate("MainWindow", "config"))
        self.actionzhushou.setText(_translate("MainWindow", "AI问答助手"))
        self.actionzhongyiying.setText(_translate("MainWindow", "中译英"))
        self.actionyingyizhong.setText(_translate("MainWindow", "英译中"))
        self.actionlunwenrunse.setText(_translate("MainWindow", "论文润色"))
        self.actionnvninvyou.setText(_translate("MainWindow", "虚拟女友"))
        self.actionxuninanyou.setText(_translate("MainWindow", "虚拟男友"))
        self.actionpython.setText(_translate("MainWindow", "python高手"))
        self.actionjava.setText(_translate("MainWindow", "java高手"))
        self.actionwebqianduan.setText(_translate("MainWindow", "web前端高手"))
        self.actionusername.setText(_translate("MainWindow", "自定义昵称"))
        self.actionzhanan.setText(_translate("MainWindow", "渣男"))
        self.actiondeeplearning.setText(_translate("MainWindow", "深度学习专家"))
        self.actionhiden.setText(_translate("MainWindow", "隐藏"))
        self.action_docx.setText(_translate("MainWindow", ".docx"))
        self.action_txt.setText(_translate("MainWindow", ".txt"))
        self.action_pdf.setText(_translate("MainWindow", ".pdf"))
        self.actionAPIkey.setText(_translate("MainWindow", "API Key"))
        self.actiontongyiqianwen.setText(_translate("MainWindow", "通义千问"))
        self.actionsuno.setText(_translate("MainWindow", "suno"))
        self.actiontishijinglin.setText(_translate("MainWindow", "提示精灵"))
        self.actionChatGPT_SC.setText(_translate("MainWindow", "ChatGPT_SC"))
        self.actionc_zhuanjai.setText(_translate("MainWindow", "c++高手"))
        self.actionwebhouduan.setText(_translate("MainWindow", "web后端高手"))
        self.actionlinux.setText(_translate("MainWindow", "linux高手"))
        self.actionmachine.setText(_translate("MainWindow", "机器学习专家"))