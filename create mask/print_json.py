'''
json.load 用於讀取JSON檔案並將其轉換為Python數據
json.dump 用於將Python數據轉換為JSON格式並將其寫入檔案。
'''

import json

file = open("annotation/mask.json", "r")
data = json.load(file)
data = json.dumps(data, indent=4, ensure_ascii=False)
print(data)