#!/bin/bash
# json2sh.py `gui-config.json路径` `生成文件到` `本地命令，ss的sslocal程序路径`
rm -rf "ss/*"
python3 json2sh.py "gui-config.json" "ss/" "python shadowsocks/shadowsocks/local.py" "sh"
chmod +x *.sh