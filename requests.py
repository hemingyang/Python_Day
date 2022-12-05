import requests as rs


url="http://www.baidu.com"
root=rs.get(url,)
##print(root.text)
##print(root.headers)
##print(root.json)
print(root.cookies)