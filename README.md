# Quick-Chat

***——欢迎使用quickChart***

## 界面

<img src="help.assets/image-20231205151332823.png" alt="image-20231205151332823" style="zoom:67%;" />

<img src="help.assets/aaa.png" alt="image-aaa" style="zoom:67%;" />

## 快捷键

* 推荐和鼓励使用快捷键，这将大大提高你的使用效率

### alt+w(window)

* 快速**调出**和**隐藏**本工具 

### alt+q(question) / ctrl+enter

* 快速**发送**输入框问题 

### alt+c(clear)

* **清空对话**内容

## 配置

### 获取api key

* 本项目使用开源的国内镜像的gpt3.5 API项目，使用github认证即可**领取一个免费key**，链接如下：
* [chatanywhere/GPT_API_free: Free ChatGPT API Key，免费ChatGPT API，支持GPT4 API（免费），ChatGPT国内可用免费转发API，直连无需代理。可以搭配ChatBox等软件/插件使用，极大降低接口使用成本。国内即可无限制畅快聊天。](https://github.com/chatanywhere/GPT_API_free/tree/main)

### 修改配置文件

* 在./conf/gpt_keys.txt中输入获取的key，可以输多个，不要有多余的空行，程序会循环调用key

```
sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx1
sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx2
sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx3
sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx4
```

* 用户信息配置./user.json配置信息

``` json
{
  "name": "cfu223", #用户名
  "use-tokens": 0, #用了多少taken了
  "code": "6a5850bb5b37aae985b0ffba6d8e70a3" #点击“开始”->“获取token”，获取设备码，用项目中./tools/生成序列号.py，生成后序列号后，填入。（release中懒得砍掉这个功能了，以后再说，白嫖就自己研究一下吧，）
}
```

## 基础使用

### 开始

<img src="help.assets/image-20231203202813389.png" alt="image-20231203202813389" style="zoom:67%;" />

<img src="help.assets/image-20231203202830895.png" alt="image-20231203202830895" style="zoom:67%;" />

#### 新建对话

* 清空先前的对话内容，开始一段全新的对话，可以使用快捷键**alt+c(clear)**提高效率。

#### 导出对话内容

* 可以将当前的对话内容以多种格式导出。
* 需要注意的是，清除历史对话内容后，或者到达对话轮数上限后，之前的内容就没了。
* 推荐使用md格式导出，模型的数据返回就是markdown格式的。也可以利用其他更成熟的markdown编辑器导出想要的格式
* 如果要使用doc pdf导出请使用pandoc.exe

#### 隐藏

* 隐藏本工具，可用全局快捷键**alt+w**隐藏和呼出，或在系统托盘打开。

#### 角色

* 设置提示词，扮演指定的角色

#### 获取tocken

* 查看设备id，用 tools/激活码生成.py 生成激活码，填入config文件中（如果有商业需求的话）

### 选项

![image-20231203203622503](help.assets/image-20231203203622503.png)

#### 个性化

* 暂不支持

#### 模型切换

* 暂不支持

#### 设置开机自启

* 字面意思，软件可以挂在后台，快捷键alt+w(window)可以唤醒和隐藏。
* 如果开机自启不生效，可以前往用户文件夹删除**map.cf**映射文件然后重新设置开机自启。当然还有另一种可能就是**安全软件**禁止了开机自启的行为。
* map文件路径：C:\\Users\\{你的用户名}\\.quickChart

<img src="help.assets/image-20231203204334488.png" alt="image-20231203204334488" style="zoom:67%;" />

#### 取消开机自启

* 顾名思义。

### 效率

![image-20231203204555419](help.assets/image-20231203204555419.png)

### 帮助

![image-20231203204715290](help.assets/image-20231203204715290.png)

#### 使用教程

* 打开你现在在看的文档。

#### 检查更新

* 下载新版的软件，或者我的其他软件。

#### 阿里云服务

* 通义千问的API，使用自己的API key来调用，使用Qwen.py可以使用通义千问的API（不免费了，就不用了）

#### 赞助

* 可以给我打钱。

## 其他

### 页面调整

<img src="help.assets/image-20231205151708234.png" alt="image-20231205151708234" style="zoom:67%;" />

<img src="help.assets/image-20231205151810778.png" alt="image-20231205151810778" style="zoom:67%;" />

## 交流

* QQ：2778297606

  
