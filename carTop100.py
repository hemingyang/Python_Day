import requests
from lxml import etree
from selenium import webdriver
import time

# 设置 User-Agent 和代理 IP
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
proxy = {"http": "http://username:password@ip:port", "https": "https://username:password@ip:port"}

# 使用 Selenium 模拟浏览器行为
driver = webdriver.Chrome()
driver.get("http://www.autohome.com.cn/grade/carhtml/A.html")
time.sleep(5) # 等待页面加载
html = driver.page_source
driver.quit()

# 解析 HTML 页面
tree = etree.HTML(html)

brand_names = tree.xpath("//h4[@class='toolong']/a[@class='greylink']//text()")


print(brand_names)