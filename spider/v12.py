from urllib import request
import chardet

if __name__ == '__main__':

    url = "http://lol.qq.com/web201310/personal.shtml?id=2931971641&area=22&showDiv=1"

    headers = {
        "Cookie":"pgv_pvi=5933122560; eas_sid=s1e5Z3X2D2X458a8A2i207f270; pgv_si=s5255909376; pgv_pvid=1707706593; pgv_info=pgvReferrer=&ssid=s5677944436; gpmtips_cfg=%7B%22iSendApi%22%3A0%2C%22iShowCount%22%3A0%2C%22iOnlineCount%22%3A0%2C%22iSendOneCount%22%3A0%2C%22iShowAllCount%22%3A0%2C%22iHomeCount%22%3A0%7D; ptisp=ctc; ptui_loginuin=986205094; pt2gguin=o0986205094; uin=o0986205094; skey=@6TlKdpqri; RK=SDzM7KplYO; ptcz=299325c835b089512abc1fe07ec9772fa7e317ce28c8f1c7b73d7bc1a5002765; IED_LOG_INFO2=userUin%3D986205094%26nickName%3D%2525E5%252591%2525B5%2525E5%252591%2525B5%26userLoginTime%3D1532248840; LOL_API_W2013_USER_986205094=2931971641%2C22%2C%25E8%258D%2594%25E6%259E%259Dsalad%2C85%2C2094%2C4221%2C250%2C5346%2C0%2CGOLD; LOL_API_W2013_USER_986205094Area=22; ue_uk=b5e696f9bab28ddd8623ff829058cc08; ue_uid=86fd3266d9f31d9d382f3837039a4416; ied_rf=lol.qq.com/webplat/info/news_version3/152/4579/4580/m3106/201806/734510.shtml; ue_ts=1532250010; ue_skey=4e51ec994ffd9da5f43d17252b1d92b0"
    }

    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read()

    cs = chardet.detect(html)

    html = html.decode(cs.get("encoding", "gbk"))

    with open("rsp1.html", "w") as f:
        f.write(html)