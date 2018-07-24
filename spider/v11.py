from urllib import request
import chardet

if __name__ == '__main__':

    url = "http://lol.qq.com/web201310/personal.shtml?id=2931971641&area=22&showDiv=1"

    rsp = request.urlopen(url)

    html = rsp.read()

    cs = chardet.detect(html)

    html = html.decode(cs.get("encoding", "gbk"))


    with open("rsp.html", "w") as f:
        f.write(html)
