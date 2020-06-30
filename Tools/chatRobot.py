import hashlib
import random
import string
import time
from urllib.parse import quote
import requests


def curl_md5(src):
    """进行MD5加密运算"""
    md = hashlib.md5(src.encode('UTF-8'))
    # 将得到的md5值所有字符串转换成大写
    return md.hexdigest().upper()


def get_params(question):
    # 请求时间戳（秒级），防止请求重放
    time_stamp = int(time.time())
    # 请求随机字符串，保证签名不可预测
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    # 应用标志
    app_id = 2110645471
    app_key = 'vHdDvhqnLwPMKvCG'
    params = {
        'app_id': app_id,
        'time_stamp': time_stamp,
        'nonce_str': nonce_str,
        'session': '10000',
        'question': question,
    }
    sign_before = ''
    # 对key排序再拼接，获取签名信息
    for key in sorted(params):
        # 键值对拼接过程，部分值需要bs64编码
        sign_before += '{}={}&'.format(key, quote(str(params[key]), safe=''))
    # 将应用密钥拼接到sign_before末尾
    sign_before += 'app_key={}'.format(app_key)
    # 对sign_before进行MD5加密运算，得到接口请求签名
    sign = curl_md5(sign_before)
    params['sign'] = sign
    # print(params)
    return params


def get_content(question):
    # 聊天的api接口
    url = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'
    # 获取请求参数
    question = question.decode('utf-8')
    payload = get_params(question)
    response = requests.post(url, data=payload)
    return response.json()['data']['answer']


def run(Name):
    Temp = "Science"
    c = 1
    Lst = ['告诉我你最近的心情吧～',
           '我想和你聊聊你未来的打算，怎么样呢？',
           '唔，我有点困。【委屈】',
           '你工作了还是在学校呢？',
           '等等，我去倒杯水给你',
           '我之前谈了一个女朋友',
           '我还是听喜欢和你聊天的',
           '不知道新冠肺炎什么时候才好，唉……'
           '你喜欢打篮球吗？最近我迷上了篮球',
           '天苍苍，野茫茫，风吹草低见牛羊～',
           '我想诵诗，哈哈哈'
           ]
    while True:
        content = input(' >> ')
        c += 1
        if content == 'exit':
            print(" \t\t\t " + Name + " : " + "以后想聊天找我哦，我可以一直陪你～")
            break
        select = random.randint(0, len(Lst)+10)
        if select < 5:
            answer = Lst[select]
        else:
            answer = get_content(str(content).encode('utf-8'))
        print(" \t\t\t " + Name + " : " + answer)

