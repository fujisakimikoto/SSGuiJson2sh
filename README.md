# ssjson2sh
将从 ss 服务商下载的 sswin 配置文件 gui-config.json 转换为单个的 json 文件和 sh 脚本，便于服务器等纯 CUI 环境临时快速选择接入点进行连接。

# 环境要求
python3 UTF-8

# 使用方法
修改 json2sh.sh 里面的相关参数，以下是默认值，根据需要修改：
- `gui-config.json`: gui-config.json路径
- `ss/`: 生成文件的目标文件夹
- `python shadowsocks/shadowsocks/local.py`: sslocal 命令
- `sh`: 扩展名，给 Windows 用的话改成 `bat`

如果打算在 Windows 中运行，把 `json2sh.sh` 按 bat 文件的书写格式写个 bat 文件就行了。

## 脚本将会
- 把 `gui-config.json` 拆分成一个节点一个 json 文件。
- 根据设置的参数为每个节点的 json 文件创建一个相应的执行脚本。

# 生成的文件夹结构示例
```
$ ls ss
台湾节点1.json		美国节点5.json
日本节点1.json		香港节点5.json
美国节点1.json		日本节点5.sh
英国节点1.json		美国节点5.sh
荷兰节点1.json		香港节点5.sh
韩国节点1.json		日本节点6.json
香港节点1.json		美国节点6.json
台湾节点1.sh		香港节点6.json
日本节点1.sh		日本节点6.sh
美国节点1.sh		美国节点6.sh
英国节点1.sh		香港节点6.sh
荷兰节点1.sh		日本节点7.json
韩国节点1.sh		美国节点7.json
香港节点1.sh		香港节点7.json
香港节点10.json		日本节点7.sh
香港节点10.sh		美国节点7.sh
香港节点11.json		香港节点7.sh
香港节点11.sh		日本节点8.json
香港节点12.json		美国节点8.json
香港节点12.sh		香港节点8.json
香港节点13.json		日本节点8.sh
香港节点13.sh		美国节点8.sh
香港节点14.json		香港节点8.sh
香港节点14.sh		日本节点9.json
香港节点15.json		美国节点9.json
香港节点15.sh		香港节点9.json
香港节点16.json		日本节点9.sh
香港节点16.sh		美国节点9.sh
台湾节点2.json		香港节点9.sh
日本节点2.json		新加坡节点1.json
美国节点2.json		新加坡节点1.sh
英国节点2.json		新加坡节点2.json
韩国节点2.json		新加坡节点2.sh
香港节点2.json		新加坡节点3.json
台湾节点2.sh		新加坡节点3.sh
日本节点2.sh		中国标准节点1.json
美国节点2.sh		日本标准节点1.json
英国节点2.sh		美国标准节点1.json
韩国节点2.sh		香港标准节点1.json
香港节点2.sh		中国标准节点1.sh
台湾节点3.json		日本标准节点1.sh
日本节点3.json		美国标准节点1.sh
美国节点3.json		香港标准节点1.sh
香港节点3.json		中国标准节点2.json
台湾节点3.sh		日本标准节点2.json
日本节点3.sh		美国标准节点2.json
美国节点3.sh		香港标准节点2.json
香港节点3.sh		中国标准节点2.sh
台湾节点4.json		日本标准节点2.sh
日本节点4.json		美国标准节点2.sh
美国节点4.json		香港标准节点2.sh
香港节点4.json		香港标准节点3.json
台湾节点4.sh		香港标准节点3.sh
日本节点4.sh		香港标准节点4.json
美国节点4.sh		香港标准节点4.sh
香港节点4.sh		香港标准节点5.json
日本节点5.json		香港标准节点5.sh
```