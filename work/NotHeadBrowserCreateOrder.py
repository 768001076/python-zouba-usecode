# 无头浏览器下单
import requests
from urllib import request

def CreateOrderMethod(param):
    result = requests.post(url="http://101.236.62.47:8000", json=param, timeout=60)
    print(result.status_code)
    print(result.headers)
    print(str(result.content.decode("utf-8")))

def ParamEncode():
    param = "%7b%22isAutoCreateOrder%22%3afalse%2c%22orderType%22%3a%22%22%2c%22queryLink%22%3a%22leftTicket%2fquery%22%2c%22getPayUrlFlag%22%3atrue%2c%22seatTypeOf12306%22%3a%22P%23tz_num%23%e7%89%b9%e7%ad%89%e5%ba%a7%40M%23zy_num%23%e4%b8%80%e7%ad%89%e5%ba%a7%40O%23ze_num%23%e4%ba%8c%e7%ad%89%e5%ba%a7%40F%23dw_num%23%e5%8a%a8%e5%8d%a7%40E%23qt_num%23%e7%89%b9%e7%ad%89%e8%bd%af%e5%ba%a7%40A%23qt_num%23%e9%ab%98%e7%ba%a7%e5%8a%a8%e5%8d%a7%409%23swz_num%23%e5%95%86%e5%8a%a1%e5%ba%a7%408%23ze_num%23%e4%ba%8c%e7%ad%89%e8%bd%af%e5%ba%a7%407%23zy_num%23%e4%b8%80%e7%ad%89%e8%bd%af%e5%ba%a7%406%23gr_num%23%e9%ab%98%e7%ba%a7%e8%bd%af%e5%8d%a7%404%23rw_num%23%e8%bd%af%e5%8d%a7%403%23yw_num%23%e7%a1%ac%e5%8d%a7%402%23rz_num%23%e8%bd%af%e5%ba%a7%401%23yz_num%23%e7%a1%ac%e5%ba%a7%400%23wz_num%23%e6%97%a0%e5%ba%a7%22%2c%22CustomerAccount%22%3afalse%2c%22from_station_name%22%3a%22%e9%a6%99%e6%a8%9f%e8%b7%af%22%2c%22dontBindingPassengers%22%3afalse%2c%22goAliOcs%22%3afalse%2c%22to_station_name%22%3a%22%e7%94%b0%e5%bf%83%e4%b8%9c%22%2c%22cookie%22%3a%22JSESSIONID%3d0A01E841600665A24B1EED7CD340EB785F5DCE1921%3b+BIGipServerotn%3d1105723658.24610.0000%3b+current_captcha_type%3dZ%3b+AccountVirtualCookie%3d1%22%2c%22passengers%22%3a%7b%22oldPassengerStr%22%3a%22%e7%8b%84%e9%9b%a8%e8%93%89%2c1%2c430624200003210821%2c1_%e5%91%a8%e5%ae%87%e8%88%aa%2c1%2c430202199904064010%2c1_%22%2c%22prices%22%3a%2214.0%4014.0%22%2c%22choose_seats%22%3a%22%22%2c%22zwcodes%22%3a%222%402%22%2c%22passengerTicketStr%22%3a%222%2c0%2c1%2c%e7%8b%84%e9%9b%a8%e8%93%89%2c1%2c430624200003210821%2c%2cN_2%2c0%2c1%2c%e5%91%a8%e5%ae%87%e8%88%aa%2c1%2c430202199904064010%2c%2cN%22%7d%2c%22to_station%22%3a%22KQQ%22%2c%22train_date%22%3a%222018-06-25%22%2c%22from_station%22%3a%22FNQ%22%2c%22loginPwd%22%3a%22asd123456%22%2c%22isBindingPassengers%22%3atrue%2c%22orderId%22%3a135400237%2c%22train_code%22%3a%22C7851%22%2c%22payMethod%22%3a2%2c%22loginName%22%3a%22chenwenmsafzvpuf%22%7d"
    par = request.unquote(param)
    print(par)



if __name__ == '__main__':
    param = "%7b%22isAutoCreateOrder%22%3afalse%2c%22orderType%22%3a%22%22%2c%22queryLink%22%3a%22leftTicket%2fquery%22%2c%22getPayUrlFlag%22%3atrue%2c%22seatTypeOf12306%22%3a%22P%23tz_num%23%e7%89%b9%e7%ad%89%e5%ba%a7%40M%23zy_num%23%e4%b8%80%e7%ad%89%e5%ba%a7%40O%23ze_num%23%e4%ba%8c%e7%ad%89%e5%ba%a7%40F%23dw_num%23%e5%8a%a8%e5%8d%a7%40E%23qt_num%23%e7%89%b9%e7%ad%89%e8%bd%af%e5%ba%a7%40A%23qt_num%23%e9%ab%98%e7%ba%a7%e5%8a%a8%e5%8d%a7%409%23swz_num%23%e5%95%86%e5%8a%a1%e5%ba%a7%408%23ze_num%23%e4%ba%8c%e7%ad%89%e8%bd%af%e5%ba%a7%407%23zy_num%23%e4%b8%80%e7%ad%89%e8%bd%af%e5%ba%a7%406%23gr_num%23%e9%ab%98%e7%ba%a7%e8%bd%af%e5%8d%a7%404%23rw_num%23%e8%bd%af%e5%8d%a7%403%23yw_num%23%e7%a1%ac%e5%8d%a7%402%23rz_num%23%e8%bd%af%e5%ba%a7%401%23yz_num%23%e7%a1%ac%e5%ba%a7%400%23wz_num%23%e6%97%a0%e5%ba%a7%22%2c%22CustomerAccount%22%3afalse%2c%22from_station_name%22%3a%22%e9%a6%99%e6%a8%9f%e8%b7%af%22%2c%22dontBindingPassengers%22%3afalse%2c%22goAliOcs%22%3afalse%2c%22to_station_name%22%3a%22%e7%94%b0%e5%bf%83%e4%b8%9c%22%2c%22cookie%22%3a%22JSESSIONID%3d0A01E841600665A24B1EED7CD340EB785F5DCE1921%3b+BIGipServerotn%3d1105723658.24610.0000%3b+current_captcha_type%3dZ%3b+AccountVirtualCookie%3d1%22%2c%22passengers%22%3a%7b%22oldPassengerStr%22%3a%22%e7%8b%84%e9%9b%a8%e8%93%89%2c1%2c430624200003210821%2c1_%e5%91%a8%e5%ae%87%e8%88%aa%2c1%2c430202199904064010%2c1_%22%2c%22prices%22%3a%2214.0%4014.0%22%2c%22choose_seats%22%3a%22%22%2c%22zwcodes%22%3a%222%402%22%2c%22passengerTicketStr%22%3a%222%2c0%2c1%2c%e7%8b%84%e9%9b%a8%e8%93%89%2c1%2c430624200003210821%2c%2cN_2%2c0%2c1%2c%e5%91%a8%e5%ae%87%e8%88%aa%2c1%2c430202199904064010%2c%2cN%22%7d%2c%22to_station%22%3a%22KQQ%22%2c%22train_date%22%3a%222018-06-25%22%2c%22from_station%22%3a%22FNQ%22%2c%22loginPwd%22%3a%22asd123456%22%2c%22isBindingPassengers%22%3atrue%2c%22orderId%22%3a135400237%2c%22train_code%22%3a%22C7851%22%2c%22payMethod%22%3a2%2c%22loginName%22%3a%22chenwenmsafzvpuf%22%7d"
    # CreateOrderMethod(param)
    ParamEncode()