import requests
import json

HOST = "http://localhost:8001"
TOKEN = "j19ksi1mim1lksm12213"

data = {}
# data["chatId"] = "6285878554150" + "@c.us"
data["chatId"] = "6282245405673" + "@c.us"
# data["chatId"] = "628568855504" + "@c.us"

data["body"] = "Assalamu'alaikum bapak/ ibu di mohon kehadirannya dalam acara yudisium tugas akhir.\n" \
               "Yang diadakan pada:\n" \
               "Jumat, 10 Juli 2020, pk 08.30.\n" \
               "Zoom id: 983 9042 8008\n" \
               "Atas perhatian dan kehadirannya disampaikan terima kasih.\n\n" \
               "Ttd\n" \
               "Panitia Tugas Akhir\n\n" \
               "*Sent by system*"

# data["body"] = "Assalamu'alaikum bapak/ ibu di mohon kehadirannya dalam acara yudisium tugas akhir.\n" \
#                "Yang diadakan pada:\n" \
#                "Jumat, 10 Juli 2020, pk 08.30.\n" \
#                "Bertempat d LSI 2, gd. Sipil lt.6 sayap Timur.\n" \
#                "Atas perhatian dan kehadirannya disampaikan terima kasih.\n\n" \
#                "Ttd\n" \
#                "Panitia Tugas Akhir"



print(data)
url = HOST + "/83430/sendMessage?token=" + TOKEN
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
