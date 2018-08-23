import requests

if __name__ == '__main__':
    filepath = "C:\Users\Administrator\Desktop\img\1524518711565.jpg"

    headers = {
        "accept":"text/xml;text/html",
        "Content-Type":"text/xml;charset=utf-8"
    }

    result = requests.request(url="http://api.pub.train.qunar.com/captcha/api/captcha.jsp?agentCode=hangt",method="POST",headers=headers)
    print(result.headers)
    print(result.text)
