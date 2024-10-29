import json
import os
import pypandoc
import markdown


def auto_start():
    # 实现开机自启
    # 重写路径映射
    user_path = os.path.expanduser('~')  # user文件夹路径
    cur_path = os.path.abspath("./")  # 获取当前工作路径
    with open(os.path.join(user_path, ".quickChart", "map.cf"), mode="w", encoding='utf-8') as f:
        f.write(cur_path)
    # 启动exe
    os.popen(os.path.abspath(r".\bin\auto-start.exe"))


def get_welcome_html():
    with open("src/html/welcome.html", mode="r", encoding="utf-8") as r:
        return r.read()


def export_to_md(msg):
    with(open(os.path.abspath("./user.json"), mode="r", encoding='utf8')) as f:
        data = json.loads(f.read())
        user_name = data['name']
    str_md = "# conversation\n"
    r = 1
    for data in msg:
        if data['role'] == "System":
            str_md += f"*system: {data['content']}*\n"
        elif data['role'] == "user":
            str_md += f"## {r}-{user_name}:\n"
            str_md += f"{data['content']}\n"
        elif data['role'] == "assistant":
            str_md += f"## {r}-AI:\n"
            str_md += f"{data['content']}\n"
            r += 1
    return str_md


def export_to_html(msg):
    md = export_to_md(msg)
    html = markdown.markdown(md, extensions=['markdown.extensions.toc', 'markdown.extensions.fenced_code',
                                             'markdown.extensions.tables'])
    return html


def export_to_doc(file_path, messages):
    html = export_to_html(messages)
    pypandoc.convert_text(html, 'docx', outputfile=file_path, format='html')


def export_to_txt(file_path, messages):
    html = export_to_html(messages)
    pypandoc.convert_text(html, 'textile', outputfile=file_path, format='html')


def export_to_pdf(file_path, messages):
    pass
