from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

rp = RobotFileParser()
rp.set_url('https://www.jianshu.com/robots.txt')
# rp = RobotFileParser('https://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','https://www.jianshu.com/p/b67554025d7d/'))
print(rp.can_fetch('*','https://www.jianshu.com'))

'''
rp = RobotFileParser()
rp.parse(urlopen('https://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))

print(rp.can_fetch('*','https://www.jianshu.com/p/b67554025d7d/'))
print(rp.can_fetch('*','https://www.jianshu.com'))
'''