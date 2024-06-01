# encoding:utf-8
import requests 

# 接口地址
url = "https://api.map.baidu.com/geocoding/v3"

# 此处填写你在控制台-应用管理-创建应用后获取的AK
ak = "GU4BZ-NEXWW-XOHRW-OFHTX-QHFCV-GTF2W"

params = {
    "address":    "北京市昌平区龙跃苑4区31号楼1-501",
    "output":    "json",
    "ak":       ak,
}

response = requests.get(url=url, params=params)
if response:
    print(response.json())