# encoding=utf8
import sys
import json
with open(sys.argv[1],'r') as load_f:
    load_dict = json.load(load_f)
    configs = load_dict['configs']
    for i in range(0, len(configs)):
        nowconf = configs[i]
        name = configs[i]["remarks"]
        name = sys.argv[2] + name.replace(" ", "")
        name1 = name + ".json"
        name2 = name + "." + sys.argv[4]
        shfile = sys.argv[3] + " -c " + name + ".json"
        with open(name1,"w") as f:
            print("# 创建文件：" + name1)
            print(nowconf)
            jsonstr = json.dumps(nowconf)
            print("文件内容：" + jsonstr)
            f.write(jsonstr)
        with open(name2,"w") as f2:
            print("# 创建文件：" + name2)
            print("文件内容：" + shfile)
            f2.write(shfile)