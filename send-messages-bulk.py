import requests
import json
import time

HOST = "http://localhost:8001"
TOKEN = "j19ksi1mim1lksm12213"

phones = "62811361847,6283115524109,628123313847,628557698615,6281252497711,6281944819792,628179646264,6285731311476,6281333873680,6281259668854,6285655104757,6282245483111,6285695836204,628113200670,6281252537493,6285233139738,628563026274,6285369199997,6283840811400,6282245405673,628113615482,6281330966644,6281381476586,6289669379888,6281336657220,628123399764,6282233725411,628123383910,6282143246664,6282143964396,6285755023455,628563302542,6281217828672"
# phones = "6285878554150,6282245405673,628568855504"
for phone in phones.split(","):
    data = {}
    data["chatId"] = phone + "@c.us"

    data["body"] = "Assalamu'alaikum bapak/ ibu di mohon kehadirannya dalam acara yudisium tugas akhir.\n" \
                   "Yang diadakan pada:\n" \
                   "Jumat, 10 Juli 2020, pk 08.30.\n" \
                   "Zoom id: 983 9042 8008\n" \
                   "Atas perhatian dan kehadirannya disampaikan terima kasih.\n\n" \
                   "Ttd\n" \
                   "Panitia Tugas Akhir"

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
    time.sleep(0.25)
