#1. 未实现多线程 2. 中文乱码  有待完善
import re
import os
import os.path
import time
import requests
import sys
import os
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
dstDir = 'JiBing2'
if not os.path.isdir(dstDir):
    os.mkdir(dstDir)
startUrl = r'http://www.zgzbao.com/yq.asp?bigclass=%D6%B2%CE%EF%B2%A1%BA%A6%C7%F8'
content = requests.get(startUrl).text
# print(content)

# # 提取并遍历链接
pattern = r'<td width="874" height="25" align="left"><a href="(.+)" class="b2">(.+)</a></td>'
result = re.findall(pattern, content)
for item in result:
    perUrl, name = item
    # 测试是否获取信息
    print(perUrl)
    print(item)
    # 这里根据初爬结果进行改进
    name = name.replace('<h3>', '').replace('</h3>', '')
    name = os.path.join(dstDir, name)
    perUrl = r'http://www.zgzbao.com/' + perUrl
    content = requests.get(perUrl).text
    #     print(content)
    pattern = r'<p>(.+?)</p>'
    result = re.findall(pattern, content)
    imagePattern = r'<img src="(.+?)" width height'
    imageresult = re.findall(imagePattern, content)

    if imageresult:
        content = requests.get("http://www.zgzbao.com/" + imageresult[0]).content
        #         print(content.content)
        with open(name + '.jpg', 'wb') as fp:
            fp.write(content)

    if result:
        intro = re.sub('(<a.+</a>)|(&ensp;)|(&nbsp;)', '', '\n'.join(result))
        with open(name + '.txt', 'w', encoding='gb18030') as fp:
            fp.write(intro)