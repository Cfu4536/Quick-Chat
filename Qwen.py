import time
from http import HTTPStatus

from PyQt5.QtWidgets import QApplication
from dashscope import Generation
from dashscope.api_entities.dashscope_response import Role
import dashscope
from tools import *


class Qwen():
    def __init__(self):
        self.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxx" # your api key
        self.messages = []
        self.conversation_count = 0  # 对话轮数
        self.tocken_count = 0
        self.stream_box = None
        self.big_model = Generation.Models.qwen_max
        dashscope.api_key = self.api_key

    def call_with_stream(self, messages, TextEdit, scrollArea):
        role = ""
        responses = Generation.call(
            self.big_model,
            messages=messages,
            result_format='message',  # set the result to be "message" format.
            stream=True,
            incremental_output=True  # get streaming output incrementally
        )
        full_content = ''  # with incrementally we need to merge output.
        try:
            for response in responses:
                if response.status_code == HTTPStatus.OK:
                    full_content += response.output.choices[0]['message']['content']
                    role = response.output.choices[0]['message']['role']
                    self.tocken_count += response.usage.input_tokens
                    print(response.output.choices[0]['message']['content'], end="")
                    TextEdit.setMarkdown(full_content)
                    TextEdit.setFixedHeight(TextEdit.height() + TextEdit.verticalScrollBar().maximum())  # 动态更新容器高度
                    QApplication.processEvents()  # 刷新窗口
                    scrollArea.verticalScrollBar().setValue(scrollArea.verticalScrollBar().maximum())  # 置低
                else:
                    print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                        response.request_id, response.status_code,
                        response.code, response.message
                    ))
            return True, role, full_content
        except:
            return False, None, None

    def conversation_with_messages(self, user_input, TextEdit, scrollArea):
        self.tocken_count = 0
        self.messages.append({'role': Role.USER, 'content': user_input})
        print(self.messages)
        status, role, full_content = self.call_with_stream(self.messages, TextEdit, scrollArea)
        TextEdit.setFixedHeight(TextEdit.height() + 5)  # 增加一点容器高度
        if status:
            print("\n")
            # append result to messages.
            self.messages.append({'role': role,
                                  'content': full_content})
            self.conversation_count += 1
            print(self.tocken_count)
        else:
            print("error")
            TextEdit.setMarkdown("网络连接错误！")
            TextEdit.setFixedHeight(TextEdit.height() + TextEdit.verticalScrollBar().maximum())  # 动态更新容器高度
            QApplication.processEvents()  # 刷新窗口
            scrollArea.verticalScrollBar().setValue(scrollArea.verticalScrollBar().maximum())  # 置低
        return self.tocken_count

    def clear_conversation(self):
        self.messages = self.messages[:1]
        self.conversation_count = 0  # 对话轮数

    def set_gib_model(self, name):
        if name == "qwen-max":  # 通义千问2.0千亿级别超大规模语言模型，支持中文英文等不同语言输入。//暂时免费
            self.big_model = Generation.Models.qwen_max
        elif name == "qwen-plus":  # 通义千问超大规模语言模型增强版，支持中文英文等不同语言输入。
            self.big_model = Generation.Models.qwen_plus
        elif name == "qwen-turbo":  # 通义千问超大规模语言模型，支持中文英文等不同语言输入。
            self.big_model = Generation.Models.qwen_turbo

    def set_system(self, SYSTEM="你是一个乐于助人的助手，尽量简明扼要地回答"):
        self.messages.clear()
        self.messages.append({'role': Role.SYSTEM, 'content': SYSTEM})

    def save_conversation(self):
        with open(f"./myDialogs/{time.time()}.dlg", mode="w", encoding="utf-8") as f:
            json.dump(self.messages, f)

    def load_conversation(self, file_name):
        with open(f"./myDialogs/{file_name}.dlg", mode="r", encoding="utf-8") as f:
            self.messages = json.load(f)

    def export_conversation_to_md(self, file_path):
        # file_path = os.path.abspath(os.path.join(path, f"{int(time.time())}_" + file_name))
        with open(file_path, mode="w", encoding='utf8') as w:
            w.write(export_to_md(self.messages))
        try:
            os.startfile(file_path)
        except:
            pass

    def export_conversation_to_html(self, file_path):
        # file_path = os.path.abspath(os.path.join(path, f"{int(time.time())}_" + file_name))
        with open(file_path, mode="w", encoding='utf8') as w:
            w.write(export_to_html(self.messages))
        try:
            os.startfile(file_path)
        except:
            pass

    def export_conversation_to_doc(self, file_path):
        # file_path = os.path.abspath(os.path.join(path, f"{int(time.time())}_" + file_name))
        export_to_doc(file_path, self.messages)
        try:
            os.startfile(file_path)
        except:
            pass

    def export_conversation_to_txt(self, file_path):
        # file_path = os.path.abspath(os.path.join(path, f"{int(time.time())}_" + file_name))
        export_to_txt(file_path, self.messages)
        try:
            os.startfile(file_path)
        except:
            pass

    def export_conversation_to_pdf(self, file_path):
        # file_path = os.path.abspath(os.path.join(path, f"{int(time.time())}_" + file_name))
        export_to_pdf(file_path, self.messages)
        try:
            os.startfile(file_path)
        except:
            pass

    def get_conversation_count(self):
        return self.conversation_count
