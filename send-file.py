import requests
import json

HOST = "http://localhost:8001"
TOKEN = "j19ksi1mim1lksm12213"

data = {}
# data["phone"] = "6285878554150" + "@c.us"
# data["phone"] = "6282245405673" + "@c.us"
data["chatId"] = "6285878554150" + "@c.us"
data["body"] = "/Users/od3ng/PycharmProjects/wa-blash/resources/Undangan.png"  # file
data["filename"] = "Undangan Kamis.png"  # file name
data["caption"] = "W2API - Best REST API for WhatsApp"
print(data)
url = HOST + "/83430/sendFile?token=" + TOKEN
headers = {
    'Content-Type': 'application/json'
}
js = json.dumps(data)
print(js)
# http://localhost:8001/83430/sendMessage?token=j19ksi1mim1lksm12213
resp = requests.post(url=url, headers=headers, data=js)
print(resp.status_code)
if resp.status_code == 200:
    print(resp.text)
