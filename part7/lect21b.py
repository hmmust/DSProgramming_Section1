import requests
import pandas as pd
get_result = requests.get(url="https://www.google.com/search",params={"q":"Qais"})
if get_result:
    print(get_result.text)
else:
    print("error")
