# Chinese2Audio
~~非常抽象的~~语音合成实现

<h2>效果截图(真的很抽象)</h2></p>

![screenshot](image/screenshot.png)


<h2>（一）环境要求</h2>
Python 3.x即可

<h2>（二）安装依赖</h2>
使用如下命令安装pypinyin和pydub</p>

```
pip install pypinyin pydub
```
<h2>（三）Enjoy it!</h2>
克隆本仓库，然后进入<code>Chinese2Audio</code>目录，执行如下命令：</p>

```
python audio.py
```
如果要启动webUI,请安装以下依赖

```
pip install flask sounddevice scipy pyaudio
```

**安装不了pyaudio的请自行查找解决办法**


启动WebUI

```
python web_demo.py
```

这会在http://127.0.0.1:5000上开启一个webUI

**Windows下请以管理员身份运行**

</p></p>
<strong>目前仅支持中文、英文字母、数字、小数点、加减乘除符号的朗读，英文单词朗读暂不支持</strong>
