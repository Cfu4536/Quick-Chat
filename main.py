import os
import sys
import psutil
import uuid
import webbrowser
from PyQt5.QtWidgets import QApplication

from main_win import main_win


def check_files(path: str):
    file_list = os.listdir(path)
    if "user.json" not in file_list:
        return False
    else:
        return True


def init():
    # 没有user文件夹 新建
    user_path = os.path.expanduser('~')  # user文件夹路径
    if not os.path.exists(os.path.join(user_path, ".quickChart")):  # 创建quickchart文件夹
        os.mkdir(os.path.join(user_path, ".quickChart"))
    if not os.path.exists(os.path.join(user_path, ".quickChart", "map.cf")):  # 创建路径映射
        with open(os.path.join(user_path, ".quickChart", "map.cf"), mode="w", encoding='utf-8') as f:
            f.write(os.path.abspath("./"))
        webbrowser.open_new_tab(os.path.abspath("src/html/help.html"))
    # 设置工作路径
    with open(os.path.join(user_path, ".quickChart", "map.cf"), mode="r", encoding='utf-8') as f:
        path = f.read()  # 读取map.cf设置为工作路径
        if os.path.exists(path) and check_files(path):  # 工作路径是否有效防止被移动
            os.chdir(path)
        else:  # 更新映射
            with open(os.path.join(user_path, ".quickChart", "map.cf"), mode="w", encoding='utf-8') as f:
                f.write(os.path.abspath("./"))
    print("当前工作路径：", os.path.abspath("./"))
    uuid1 = str(uuid.uuid1())
    device_id = uuid1.split('-')[2] + uuid1.split('-')[4]  # 设备号
    print("设备id", device_id)
    with open(os.path.join(user_path, ".quickChart", "uuid.html"), mode='w', encoding='utf-8') as f:
        f.write(str(device_id))
    # 是否已经运行
    Qchat_cnt = 0
    for proc in psutil.process_iter(['pid', 'name']):
        if "Qchat.exe" == proc.info['name']:
            Qchat_cnt += 1
    if Qchat_cnt > 2:
        sys.exit()


if __name__ == '__main__':
    init()
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化窗口
    main_win = main_win(app)
    main_win.resize(1000, 750)  # 设置窗体的宽为800像素，高为600像素
    # 显示ui界面
    main_win.show()
    # 创建系统托盘
    main_win.create_tray_icon()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
