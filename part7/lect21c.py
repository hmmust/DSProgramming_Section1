import requests
get_result = requests.post(url="http://httpbin.org/post",params={"key":"Qais"})
if get_result:
    print(get_result.json())
else:
    print("error")
