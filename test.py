import requests

result = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=%E6%B7%B1%E5%9C%B3")
print(result.content)