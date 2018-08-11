# 获取ｃｏｏｋｉｅｓ
import requests
'''
r = requests.get('https://www.baidu.com')
print(r.cookies)
for key, value in r.cookies.items():
    print(key+'='+value)
'''
# 使用cookies来维持登录状态
headers = {
    'Cookie':'_zap=4d53cd38-c197-4083-a191-9cfb1c7bdeb7; _xsrf=7dfmqgLoLKPfuodkfgqrpY5U8qF22x2u;'
             ' q_c1=3986d273149645aaa30b7047460738b3|1533802827000|1533802827000; d_c0="AHCkUB-FBw6PTrJPSTaYwtbDUojejkxOu48=|1533802827"; '
             'l_n_c=1; l_cap_id="NmM2MDUzOWEwOGJmNDVlYTgzMjMwMzNmZWZkYjdhNzE=|1533802834|0d5d87c33ddd38c2389ea98a3ed44a66dc6c35bb"; '
             'r_cap_id="NTM3ZTViMjhjNjUxNDY0OTk1ZTJiYjEzMjkyNTE2M2Y=|1533802834|b3513399659759d625b8521064803f447fcd3749"; '
             'cap_id="YTE0MjczYmE4ZDc0NGIxZmE2YzdhM2NhOGZmMTBlMDI=|1533802834|89b9cfeb20e225e5d6aee984e53a08f9464f3440"; n_c=1; '
             '__utmc=51854390; tgw_l7_route=7139e401481ef2f46ce98b22af4f4bed; capsion_ticket="2|1:0|10:1533805433|14:capsion_ticket|44:YzAzZmViN2I5MzhmNGU1ZWExNDQ3MGJmYTk4ODVmMDc=|3d9f24797b969c8d6888f9c635891c9ff459c651830f1bd6a4eeb25fed3d2da7";'
             ' z_c0="2|1:0|10:1533805461|4:z_c0|92:Mi4xQW5ZaENRQUFBQUFBY0tSUUg0VUhEaVlBQUFCZ0FsVk5sVkZaWEFDM2o2NExTZEVCM0VlNlEtLU9JN1pKeFpsSXF3|92c5dcce7e8eba5ea98ae550a30736211435fdd82cc649cb39109cda99211872"; unlock_ticket="ALBuzQqnhg0mAAAAYAJVTZ0KbFvAOR5pySAJgU2MjK2BeW40abndIA=="; '
             '__utma=51854390.767169631.1533802838.1533802838.1533805497.2; __utmb=51854390.0.10.1533805497;'
             ' __utmz=51854390.1533805497.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/explore; __utmv=51854390.100--|2=registration_date=20180501=1^3=entry_date=20180501=1',
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
}
r = requests.get('http://www.zhihu.com', headers=headers)
print(r.text)