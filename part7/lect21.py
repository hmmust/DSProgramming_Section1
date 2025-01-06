import requests
import pandas as pd
get_result = requests.get(url="https://raw.githubusercontent.com/hmmust/DSProgramming_Section1/refs/heads/main/part6/students1.json")
print(get_result.status_code)
print(get_result.text)
print(get_result.url)
std1 = pd.DataFrame(get_result.json())
print(std1)