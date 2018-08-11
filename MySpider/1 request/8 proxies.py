import requests
proxies = {
    'http':xxxxxxxx,
    'https':xxxxxxxx,
}
proxies = {
    'http':'http://user:password@host:post',
    'http':'http://user:password@10.10.1.10:3218',
}

requests.get('http://www.taobao.com', proxies=proxies)
