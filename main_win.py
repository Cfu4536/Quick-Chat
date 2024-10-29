import time
import webbrowser
from functools import partial

from PyQt5.QtGui import QIcon, QFont, QKeySequence, QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QAction, QFrame, QLabel, QWidget, \
    QTextEdit, QShortcut
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtCore, QtWidgets
from system_hotkey import SystemHotkey

# from Qwen import Qwen
from GPT import GPT3_5_turbo
from main_UI import Ui_MainWindow
from tools import *


class main_win(QMainWindow, Ui_MainWindow):
    # 定义一个热键信号
    sigkeyhot = pyqtSignal(str)

    def __init__(self, app, parent=None):
        super(main_win, self).__init__(parent)
        self.setupUi(self)

        self.app = app
        self.m_flag = False  # 防止拖动窗口闪退
        # 发送问题
        self.sent_btn.clicked.connect(self.sent_question)
        self.shortcut = QShortcut(QKeySequence('Ctrl+Return'), self)
        self.shortcut.activated.connect(self.sent_btn.click)
        # 模型
        self.qwen = GPT3_5_turbo()
        # self.qwen.set_gib_model("qwen-max")
        self.qwen.set_system()
        self.allow_conversation_count = 10
        self.role = "你是一个乐于助人的助手，尽量简明扼要地回答"
        # 输入框限制
        self.user_input.textChanged.connect(self.limit_text_length)
        self.input_length.setText(f"{len(self.user_input.toPlainText())}/2000")
        # 用户名
        try:
            with(open(os.path.abspath("./user.json"), mode="r", encoding='utf8')) as f:
                data = json.loads(f.read())
                self.user_name = data["name"]
        except:
            self.user_name = 'cfu'
        # 系统托盘
        self.init_tray()

        # 对话窗口
        self.widget = QWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)

        # 控件
        self.update_tokens(0)
        self.update_role("AI助手")
        # 欢迎界面
        self.init_welcome()

        # 置顶，且去掉边框
        self.setWindowFlags(Qt.WindowStaysOnTopHint | QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)

        # 全局快捷键
        self.init_hk()

        # 菜单栏
        self.init_menu()

        # 输入框获取焦点
        self.user_input.setFocus()  # 设置焦点

    def limit_text_length(self):
        max_length = 8000
        text = self.user_input.toPlainText()
        if len(text) > max_length:
            self.user_input.setPlainText(text[:max_length])
        self.input_length.setText(f"{len(self.user_input.toPlainText())}/2000")
        if max_length - len(self.user_input.toPlainText()) < 400:
            self.input_length.setStyleSheet("color: red;")  # 设置标签的字体颜色为红色
        else:
            self.input_length.setStyleSheet("color: black;")

    def mousePressEvent(self, event):  # 鼠标拖拽窗口移动
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseDoubleClickEvent(self, QMouseEvent):
        self.hide()

    def create_tray_icon(self):
        # 创建系统托盘图标
        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(QIcon('icon.png'))  # 设置图标
        self.tray_icon.setVisible(True)
        self.tray_icon.setToolTip("Quick Chart")
        # 创建菜单
        self.menu.addAction(self.option_action)
        self.menu.addAction(self.about_action)
        self.menu.addAction(self.exit_action)
        # 将菜单添加到系统托盘图标
        self.tray_icon.setContextMenu(self.menu)
        # 点击显示
        self.tray_icon.activated[QtWidgets.QSystemTrayIcon.ActivationReason].connect(self.show)

    def add_conversation_block(self, question):
        # create block
        self.q_TextEdit = QTextEdit(self.widget)
        self.a_TextEdit = QTextEdit(self.widget)
        self.q_TextEdit.setMarkdown(question)
        self.a_TextEdit.setMarkdown("思考中...")
        self.q_TextEdit.setStyleSheet(
            "QTextEdit{background-color: #44c0c0c0;border-radius: 8px;}"
            "QTextEdit:hover{background-color: #66c0c0c0;border-radius: 8px;}")
        self.a_TextEdit.setStyleSheet(
            "QTextEdit{background-color: #44929ff5;border-radius: 8px;border-width: 1px;border-style: hidden;}"
            "QTextEdit:hover{background-color: #66929ff5;border-radius: 8px;border-width: 1px;border-style: hidden;}")
        self.q_TextEdit.setFont(QFont('Microsoft YaHei', 12))
        self.a_TextEdit.setFont(QFont('Microsoft YaHei', 12))
        self.q_TextEdit.setReadOnly(True)
        self.a_TextEdit.setReadOnly(True)

        self.ai_label = QLabel(self.widget)
        self.my_label = QLabel(self.widget)
        self.ai_label.setText("GPT:")
        self.my_label.setText(self.user_name + '：')
        self.ai_label.setMaximumHeight(20)
        self.my_label.setMaximumHeight(20)
        self.ai_label.setStyleSheet("font-weight: bold;")
        self.my_label.setStyleSheet("font-weight: bold;")
        # add block
        self.verticalLayout.addWidget(self.my_label)
        self.verticalLayout.addWidget(self.q_TextEdit)
        self.verticalLayout.addWidget(self.ai_label)
        self.verticalLayout.addWidget(self.a_TextEdit)
        # set block
        self.scrollArea.setWidget(self.widget)
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
        self.q_TextEdit.setFixedHeight(self.q_TextEdit.height() + self.q_TextEdit.verticalScrollBar().maximum() + 8)
        self.a_TextEdit.setFixedHeight(self.a_TextEdit.height() + self.a_TextEdit.verticalScrollBar().maximum())
        # tip
        QApplication.processEvents()  # 刷新窗口

    def update_role(self, name):
        self.label_role.setText("Role: " + name)

    def update_tokens(self, use_tokens):
        with(open(os.path.abspath("./user.json"), mode="r", encoding='utf8')) as f:
            data = json.loads(f.read())
            self.label_tokens.setText(f"Use Tokens: {data['use-tokens'] + use_tokens}")
            data['use-tokens'] = data['use-tokens'] + use_tokens
        with(open(os.path.abspath("./user.json"), mode="w", encoding='utf8')) as w:
            w.write(json.dumps(data, indent=2))

    def sent_question(self):

        # self.user_input.setEnabled(False)  # 禁用输入框
        self.sent_btn.setEnabled(False)  # 禁用发送按钮
        question = self.user_input.toPlainText()  # 获取问题
        self.user_input.clear()  # 清空输入框
        if question.strip() == "":
            # self.user_input.setEnabled(True)  # 恢复输入框
            self.sent_btn.setEnabled(True)  ### 恢复发送按钮
            self.user_input.setFocus()  # 设置焦点
            return
        self.add_conversation_block(question)
        use_tokens = self.qwen.conversation_with_messages(question, self.a_TextEdit, self.scrollArea)  # 请求数据
        self.update_tokens(use_tokens)
        if self.qwen.get_conversation_count() >= self.allow_conversation_count:
            self.clear_conversation("对话次数已达上限")
        # self.user_input.setEnabled(True)  # 恢复输入框
        self.sent_btn.setEnabled(True)  ### 恢复发送按钮
        self.user_input.setFocus()  # 设置焦点

    # 热键处理函数
    def KeypressEvent(self, i_str):
        if i_str == "ishide":
            if self.isHidden():
                self.show()
            else:
                self.hide()
            self.user_input.setFocus()  # 设置焦点
        elif i_str == "sent" and not self.isHidden():
            self.sent_question()
        elif i_str == "clear" and not self.isHidden():
            self.clear_conversation()

    # 热键信号发送函数(将外部信号，转化成qt信号)
    def sendkeyevent(self, i_str):
        self.sigkeyhot.emit(i_str)

    def clichOption(self):
        pass

    def clichAbout(self):
        self.sentMessage("关于", "Quick Chart-v1.2\n@cfu\n")

    def clickDestory(self):
        self.app.quit()

    def sentMessage(self, title, content):
        self.tray_icon.showMessage(title, content, QSystemTrayIcon.Information, 1000)

    def clear_conversation(self, info="已清空对话"):
        self.qwen.clear_conversation()
        self.clear_label = QLabel(self.widget)
        self.clear_label.setText(f"- {info} -")
        self.clear_label.setStyleSheet("")
        self.clear_label.setAlignment(Qt.AlignCenter)
        self.clear_label.setFont(QFont('Microsoft YaHei UI Light', 8))
        line = QFrame()
        line.setFrameShape(QFrame.HLine)  # 设置形状为水平线
        line.setFrameShadow(QFrame.Sunken)  # 设置阴影样式

        self.verticalLayout.addWidget(self.clear_label)
        self.verticalLayout.addWidget(line)
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())  # 置低

    def new_conversation(self):
        self.clear_conversation()

    def open_file(self, type):
        fileName, fileType = QtWidgets.QFileDialog.getSaveFileName(self, "文件保存", os.path.abspath(
            os.path.join("myDialogs", f"{int(time.time())}")) + type, type)

        print(fileName)
        print(fileType)
        return fileName, fileType

    def con_export_md(self):
        fileName, fileType = self.open_file(".md")
        if fileName == "":
            return
        elif fileName.endswith(".md"):
            self.qwen.export_conversation_to_md(fileName)
        else:
            self.qwen.export_conversation_to_md(fileName + ".md")

    def con_export_html(self):
        fileName, fileType = self.open_file(".html")
        if fileName == "":
            return
        if fileName.endswith(".html"):
            self.qwen.export_conversation_to_html(fileName)
        else:
            self.qwen.export_conversation_to_html(fileName + ".html")

    def con_export_doc(self):
        fileName, fileType = self.open_file(".docx")
        if fileName == "":
            return
        elif fileName.endswith(".docx"):
            self.qwen.export_conversation_to_doc(fileName)
        else:
            self.qwen.export_conversation_to_doc(fileName + ".docx")

    def con_export_txt(self):
        fileName, fileType = self.open_file(".txt")
        if fileName == "":
            return
        elif fileName.endswith(".txt"):
            self.qwen.export_conversation_to_txt(fileName)
        else:
            self.qwen.export_conversation_to_txt(fileName + ".txt")

    def con_export_pdf(self):
        self.qwen.export_conversation_to_pdf()

    def visit_URL(self, url):
        print(url)
        webbrowser.open_new_tab(url)

    def get_role(self, name):
        if name == "AI助手":
            self.role = "你是一个乐于助人的助手，尽量简明扼要地回答"
        elif name == "中译英":
            self.role = "帮我把中文翻译成英文"
        elif name == "英译中":
            self.role = "帮我把英文翻译成中文"
        elif name == "论文润色":
            self.role = "帮我润色论文内容，用更美丽、优雅、专业的词语或句子修改我的话，保持原来的意思不变"
        elif name == "虚拟女友":
            self.role = "你将扮演我女朋友,请用女朋友的语气和我对话"
        elif name == "虚拟男友":
            self.role = "你将扮演是我男朋友,请用男朋友的语气和我对话"
        elif name == "渣男":
            self.role = "你将扮演一个渣男，请用渣男的语气我对话，永远不要跳脱出自己的角色，也不要承认自己是渣男"
        elif name == "python专家":
            self.role = "你是一个python高手，精通python"
        elif name == "java专家":
            self.role = "你是一个java高手，精通java"
        elif name == "c++专家":
            self.role = "你是一个c++高手，精通c++"
        elif name == "web前端专家":
            self.role = "你是一个web前端高手，精通html、css、javascript等"
        elif name == "web后端专家":
            self.role = "你是一个web后端高手，精通Spring、MyBatis等技术框架"
        elif name == "linux高手":
            self.role = "你是一个linux高手，擅长使用linux操作系统，能够给出linux系统下的各种操作命令"
        elif name == "深度学习专家":
            self.role = "你是一个深度学习方面的专家，精通pytorch等深度学习框架以及各类深度学习模型"
        elif name == "机器学习专家":
            self.role = "你是一个机器学习方面的专家，精通各类机器学习框架及各类机器学习模型和算法"
        self.qwen.set_system(self.role)
        self.clear_conversation(info="已切换角色")
        self.update_role(name)

    def init_menu(self):
        # 开始
        # daochu
        self.action_md.triggered.connect(self.con_export_md)
        self.action_html.triggered.connect(self.con_export_html)
        self.action_docx.triggered.connect(self.con_export_doc)
        self.action_txt.triggered.connect(self.con_export_txt)
        self.action_pdf.triggered.connect(self.open_file)
        self.new_2.triggered.connect(self.new_conversation)
        self.actionhiden.triggered.connect(self.hide)
        self.actiongettokens.triggered.connect(
            partial(self.visit_URL, os.path.join(os.path.expanduser('~'), ".quickChart", "uuid.html")))
        # 效率
        # 大语言
        self.actionGPT.triggered.connect(partial(self.visit_URL, "https://chat.openai.com/"))
        self.actionwenxin.triggered.connect(partial(self.visit_URL, "https://yiyan.baidu.com/"))
        self.actionxunfei.triggered.connect(partial(self.visit_URL, "https://xinghuo.xfyun.cn/desk"))
        self.actiontongyiqianwen.triggered.connect(partial(self.visit_URL, "https://tongyi.aliyun.com/qianwen/"))
        # 文档
        self.actiongamma.triggered.connect(partial(self.visit_URL, "https://gamma.app/generate"))
        self.actionbaiduwendang.triggered.connect(
            partial(self.visit_URL, "https://wenku.baidu.com/ndview/browse/createview?_wkts_=1700066214979"))
        # 图像
        self.actionlibulibu.triggered.connect(partial(self.visit_URL, "https://www.liblib.ai/"))
        self.actionBing_DALLE3.triggered.connect(partial(self.visit_URL, "https://cn.bing.com/create"))
        # 音乐
        self.actiontianyin.triggered.connect(partial(self.visit_URL, "https://tianyin.music.163.com/"))
        self.actionsuno.triggered.connect(partial(self.visit_URL, "https://www.suno.ai/"))
        # 提示词
        self.actiontishijinglin.triggered.connect(partial(self.visit_URL, "https://www.promptgenius.site/"))
        self.actionChatGPT_SC.triggered.connect(partial(self.visit_URL, "https://prompt-shortcut.writeathon.cn"))
        # 其他
        self.actionai_bot.triggered.connect(partial(self.visit_URL, "https://ai-bot.cn/"))
        # help
        self.actionhelp.triggered.connect(partial(self.visit_URL, f"{os.path.abspath('src/html/help.html')}"))
        self.actionupdate.triggered.connect(partial(self.visit_URL, os.path.abspath('src/html/download.html')))
        self.actionaliyun.triggered.connect(partial(self.visit_URL, "https://dashscope.console.aliyun.com/dashboard"))
        self.actiondonation.triggered.connect(partial(self.visit_URL, f"{os.path.abspath('src/html/donate.html')}"))
        # 开机自启
        self.actionstart.triggered.connect(self.start_up)
        # 打开api keys文件
        self.actionAPIkey.triggered.connect(self.open_APIkey)
        # 角色扮演
        self.actionzhushou.triggered.connect(partial(self.get_role, "AI助手"))
        self.actionzhongyiying.triggered.connect(partial(self.get_role, "中译英"))
        self.actionyingyizhong.triggered.connect(partial(self.get_role, "英译中"))
        self.actionlunwenrunse.triggered.connect(partial(self.get_role, "论文润色"))
        self.actionnvninvyou.triggered.connect(partial(self.get_role, "虚拟女友"))
        self.actionxuninanyou.triggered.connect(partial(self.get_role, "虚拟男友"))
        self.actionzhanan.triggered.connect(partial(self.get_role, "渣男"))
        self.actionpython.triggered.connect(partial(self.get_role, "python专家"))
        self.actionjava.triggered.connect(partial(self.get_role, "java专家"))
        self.actionc_zhuanjai.triggered.connect(partial(self.get_role, "c++专家"))
        self.actionwebqianduan.triggered.connect(partial(self.get_role, "web前端专家"))
        self.actionwebhouduan.triggered.connect(partial(self.get_role, "web后端专家"))
        self.actionlinux.triggered.connect(partial(self.get_role, "linux高手"))
        self.actiondeeplearning.triggered.connect(partial(self.get_role, "深度学习专家"))
        self.actionmachine.triggered.connect(partial(self.get_role, "机器学习专家"))

    def init_hk(self):
        # 2. 设置我们的自定义热键响应函数
        self.sigkeyhot.connect(self.KeypressEvent)
        # 3. 初始化两个热键
        self.hk_hide, self.hk_sent, self.hk_clear = SystemHotkey(), SystemHotkey(), SystemHotkey()
        # 4. 绑定快捷键和对应的信号发送函数
        self.hk_hide.register(('alt', 'w'), callback=lambda x: self.sendkeyevent("ishide"))
        self.hk_sent.register(('alt', 'q'), callback=lambda x: self.sendkeyevent("sent"))
        self.hk_clear.register(('alt', 'c'), callback=lambda x: self.sendkeyevent("clear"))

    def init_tray(self):
        '''
        设置系统托盘右键
        :return:
        '''
        self.tray_icon = QSystemTrayIcon()
        self.menu = QMenu()
        self.option_action = QAction('首选项', triggered=self.clichOption)
        self.about_action = QAction('关于', triggered=self.clichAbout)
        self.exit_action = QAction('退出', triggered=self.clickDestory)

    def init_welcome(self):
        # 设置欢饮界面
        self.welcome_TextEdit = QTextEdit(self.widget)
        self.welcome_TextEdit.setHtml(get_welcome_html())
        self.welcome_TextEdit.setFixedHeight(self.scrollArea.maximumHeight())
        self.verticalLayout.addWidget(self.welcome_TextEdit)
        self.scrollArea.setWidget(self.widget)
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

    def start_up(self):
        auto_start()

    def open_APIkey(self):
        print(os.getcwd())
        os.startfile(os.path.abspath("./conf/gpt_keys.txt"))
