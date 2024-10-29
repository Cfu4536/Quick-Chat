import hashlib
import time
import uuid

from PyQt5.QtWidgets import QApplication
from tools import *
from openai import OpenAI


class GPT3_5_turbo():
    def __init__(self):
        self.messages = []
        self.conversation_count = 0  # 对话轮数
        self.tocken_count = 0
        self.keys = []
        self.keys_num = 1
        self.key_index = 0
        self.client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key="sk-rt2LCZmZpik01x7YEU79SbwJLvHEoc7Bjj2xJ3FMjIt6eLca",
            base_url="https://api.chatanywhere.tech/v1"
        )

    def call_with_stream(self, messages, TextEdit, scrollArea):
        role = 'assistant'
        full_content = ''  # with incrementally we need to merge output.
        try:
            stream = self.client.chat.completions.create(
                model='gpt-3.5-turbo-1106',
                messages=messages,
                stream=True,
                temperature = 1, #number 可选 默认 1;数字0~2之间数字越大，答案越随机，开放，比如1.8数字越小，答案越固定，聚焦，比如0.2建议不要同时和top_p修改

            )
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    full_content += chunk.choices[0].delta.content
                    self.tocken_count += 2
                    print(chunk.choices[0].delta.content, end="")
                    TextEdit.setMarkdown(full_content)
                    TextEdit.setFixedHeight(TextEdit.height() + TextEdit.verticalScrollBar().maximum())  # 动态更新容器高度
                    QApplication.processEvents()  # 刷新窗口
                    scrollArea.verticalScrollBar().setValue(scrollArea.verticalScrollBar().maximum())  # 置低
                else:
                    TextEdit.setFixedHeight(TextEdit.height() + TextEdit.verticalScrollBar().maximum())  # 动态更新容器高度
                    QApplication.processEvents()  # 刷新窗口
                    scrollArea.verticalScrollBar().setValue(scrollArea.verticalScrollBar().maximum())  # 置低
                    print("over")
            return True, role, full_content
        except:
            return False, None, None

    def check_auth(self):
        uuid1 = str(uuid.uuid1())
        device_id = uuid1.split('-')[2] + uuid1.split('-')[4]  # 设备号
        # 创建md5对象
        hash_md5 = hashlib.md5()
        hash_md5.update(device_id.encode('utf-8'))
        encrypted_str = hash_md5.hexdigest()
        with(open(os.path.abspath("./user.json"), mode="r", encoding='utf8')) as f:
            data = json.loads(f.read())
            code = data["code"]
        print('使用的激活码', code)
        print('加密后的设备码', encrypted_str)
        return code == encrypted_str

    def conversation_with_messages(self, user_input, TextEdit, scrollArea):
        if (not self.check_auth()):  # 检查是否激活
            TextEdit.setMarkdown(f"申请激活，作者QQ：2778297606")
            TextEdit.setFixedHeight(TextEdit.height() + TextEdit.verticalScrollBar().maximum())  # 动态更新容器高度
            QApplication.processEvents()  # 刷新窗口
            scrollArea.verticalScrollBar().setValue(scrollArea.verticalScrollBar().maximum())  # 置低
            return
        self.tocken_count = 0
        self.messages.append({'role': 'user', 'content': user_input})
        # print(self.messages)
        self.choice_key()
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
            TextEdit.setMarkdown(
                f"[error]可能的原因：网络连接错误/限制访问/无效的api_key:{self.keys[self.key_index - 1]}")
            TextEdit.setFixedHeight(TextEdit.height() + TextEdit.verticalScrollBar().maximum())  # 动态更新容器高度
            QApplication.processEvents()  # 刷新窗口
            scrollArea.verticalScrollBar().setValue(scrollArea.verticalScrollBar().maximum())  # 置低
        return self.tocken_count

    def clear_conversation(self):
        self.messages = self.messages[:1]
        self.conversation_count = 0  # 对话轮数

    def choice_key(self):
        '''
        循环使用所有的key
        :return:
        '''
        print(os.getcwd())
        with open("./conf/gpt_keys.txt", "r") as f:
            for line in f.readlines():
                self.keys.append(line.strip())
        if len(self.keys) == 0:
            self.keys.append("sk-rt2LCZmZpik01x7YEU79SbwJLvHEoc7Bjj2xJ3FMjIt6eLca")
        self.keys_num = len(self.keys)
        print("use api:", self.keys[self.key_index])
        self.client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key=self.keys[self.key_index],
            base_url="https://api.chatanywhere.tech/v1"
        )
        self.key_index += 1
        if (self.key_index >= self.keys_num):
            self.key_index = 0

    def set_system(self, SYSTEM="你是一个乐于助人的助手，尽量简明扼要地回答"):
        self.messages.clear()
        self.messages.append({'role': "system", 'content': SYSTEM})

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
