[en](./README.md)

# Build.python-ftgl

　PythonでFTGLを使うライブラリをビルドする。

# デモ

![demo](doc/demo.png)

# 開発環境

* <time datetime="2020-04-28T16:14:52+0900">2020-04-28</time>
* [Raspbierry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 4 Model B Rev 1.2
* [Raspbian](https://ja.wikipedia.org/wiki/Raspbian) buster 10.0 2019-09-26 <small>[setup](http://ytyaru.hatenablog.com/entry/2019/12/25/222222)</small>
* bash 5.0.3(1)-release
* Python 2.7.16
* Python 3.7.3
* freetype
* FTGL

```sh
$ uname -a
Linux raspberrypi 4.19.97-v7l+ #1294 SMP Thu Jan 30 13:21:14 GMT 2020 armv7l GNU/Linux
```

# インストール

```sh
sudo apt -y install libftgl-dev
```
```sh
git clone https://github.com/mugwort-rc/python-ftgl
cd python-ftgl
python setup.py build
python3 setup.py build
sudo python setup.py install
sudo python3 setup.py install
```

# 使い方

```sh
git clone https://github.com/ytyaru/Build.python-ftgl.20200428161725
cd Build.python-ftgl.20200428161725/src
./run.sh
```

　フォントパスは任意の値を指定する。

run.sh
```sh
python example.py /usr/share/fonts/truetype/vlgothic/VL-Gothic-Regular.ttf
python3 example.py /usr/share/fonts/truetype/vlgothic/VL-Gothic-Regular.ttf
```

　フォント一覧取得コマンドは以下。

```sh
fc-list
```

# 著者

　ytyaru

* [![github](http://www.google.com/s2/favicons?domain=github.com)](https://github.com/ytyaru "github")
* [![hatena](http://www.google.com/s2/favicons?domain=www.hatena.ne.jp)](http://ytyaru.hatenablog.com/ytyaru "hatena")
* [![mastodon](http://www.google.com/s2/favicons?domain=mstdn.jp)](https://mstdn.jp/web/accounts/233143 "mastdon")

# ライセンス

　このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

　ビルド元コードは以下。感謝。

* https://github.com/mugwort-rc/python-ftgl
* https://github.com/umlaeute/pyftgl

