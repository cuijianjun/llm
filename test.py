#coding:utf-8
import requests
import json
import time
time_start = time.time()  # 记录开始时间
# function()   执行的程序


API_KEY = "zxgxhN3QtqW2YyLn5cKfJRfs"
SECRET_KEY = "HLjJIG9iMK6In6GBbM9g7lRxtwIZ5hzQ"

def main():
        
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": 
                """
请帮我解析以下任务，获取今天日期，并根据您的理解，需要输出格式化后的时间，格式为年-月-日 时:分 ,地址需要补全为省市县区街道小区门牌号，如无可忽略，请直接返回结果，不需要分析，最后输出的格式为
【时间】XX
【地址】XX
【任务】XX
以下为内容：
1. . 15:30 日常3小时，丰台，角东门，临泓路37号院8号楼3单元703室，自带工具，90

2. 16.00 檫玻璃12平米含纱窗 朝阳，绿城沁园(建设中)1号楼二单元1504，自带工具 120
                """
            },
            {
                "role": "user",
                "content": 
                """
1. . 15:30   日常3小时，丰台，角东门，临泓路37号院8号楼3单元703室，自带工具，90

2. 16.00 檫玻璃12平米含纱窗  朝阳，绿城沁园(建设中)1号楼二单元1504，自带工具 120
                """
            }
        ],
        "temperature": 0.95,
        "top_p": 0.8,
        "penalty_score": 1,
        "disable_search": False,
        "enable_citation": False,
        "response_format": "text",
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    time_end = time.time()  # 记录结束时间
    time_sum = time_end - time_start  # 计算的时间差为程序的执行时间，单位为秒/s
    print(time_sum)
    print(response.text)
    

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main()

