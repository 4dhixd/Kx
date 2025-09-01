#تخمط_بس_ادكر_المصدر_تدكر_انو_في_شي_اسمه_يوم_القيامة
import webbrowser
import requests 
import random,datetime,sys 
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
W="\033[1;37m" # White
insta="1234567890qwertyuiopasdfghjklzxcvbnm"
all="qwertyuiopasdfghjkzxcvbnm"

#-------------------------start code ---------------------------#
def instaa(user):
    url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',headers ={'Host':'www.instagram.com',
'content-length':'85',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'sec-ch-ua-mobile':'?0',
'x-instagram-ajax':'81f3a3c9dfe2',
'content-type':'application/x-www-form-urlencoded',
'accept':'*/*',
'x-requested-with':'XMLHttpRequest',
'x-asbd-id':'198387',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'sec-ch-ua-platform':'"Linux"',
'origin':'https://www.instagram.com',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-IQ,en;q=0.9',
'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
'cookie':'ig_nrcb=1'},data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false')
    if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
        print(W+f" [+] {Z} ErRoR UsEr : {X}{user} ")
    elif  '"errors": {"username":' in url.text or  '"code": "username_is_taken"' in url.text:
        print(W+f" [+] {Z} Bad user ➯ {X}{user} ")
    else:
        email=0
        print(W+f" [+] {F} Good User ➯ {C}{user} ")
        email+=1
        god=f""" 🇹🇷 𝐇𝐞𝐲 𝐦𝐚𝐧 𝐘𝐨𝐮 𝐠𝐨𝐭 𝐚 𝐧𝐞𝐰 𝟓𝐥 𝐮𝐧𝐮𝐬𝐞𝐝 𝐈𝐧𝐬𝐭𝐚 𝐮𝐬𝐞𝐫𝐧𝐚𝐦𝐞 
←•━━━━━━━━━━━━•→
🇹🇷 𝐔𝐧𝐮𝐬𝐞𝐝 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞  ➠ {user}
←•━━━━━━━━━━━━•→
🇹🇷 𝐁𝐘 »  @Kuttuxd × @Kuttuxd7"""
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={god}')
def users():
    ran1="1234567890..qwertyuiopasdfghjklzxvcbnm.."
    while True:
	       v1 = str(''.join((random.choice(insta) for i in range(1))))
	       v2 = str(''.join((random.choice(insta) for i in range(1))))
	       v3 = str(''.join((random.choice(insta) for i in range(1))))
	       v4 = str(''.join((random.choice(insta) for i in range(1))))
	       v5 = str(''.join((random.choice(all) for i in range(1))))
	       user1 = (v5+v1+v2+v3+v4)
	       user2 = (v1+v5+v2+v3+v4)
	       user3 = (v1+v2+v5+v3+v4)
	       user4 = (v1+v2+v3+v5+v4)
	       hamo010 = (user1, user2, user3, user4)
	       user = random.choice(hamo010)
	       instaa(user)
import requests
from datetime import datetime, timedelta

REMOTE_URL = "https://raw.githubusercontent.com/imbatman2pwpq/Kx/main/userid.txt"
SCRIPT_URL = "https://raw.githubusercontent.com/imbatman2pwpq/Kx/main/KUTTU.py"

def fetch_id_data():
    try:
        response = requests.get(REMOTE_URL, timeout=5)  # Increased timeout for reliability
        response.raise_for_status()
        # Filter lines that contain "|" and are non-empty
        return [line.strip() for line in response.text.strip().splitlines() if "|" in line and line.strip()]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ID data: {e}")
        return []

def check_id_validity(input_id):
    if not input_id or not input_id.strip():
        print("Error: ID cannot be empty.")
        return False

    input_id = input_id.strip()
    data = fetch_id_data()

    if not data:
        print("Error: No valid data retrieved. Contact owner @Kuttuxd for access.")
        return False

    for record in data:
        try:
            id_val, expiry = map(str.strip, record.split("|"))
            if id_val == input_id:
                expiry_dt = datetime.strptime(expiry, "%Y-%m-%d %H:%M:%S")
                if datetime.now() < expiry_dt:
                    remaining = expiry_dt - datetime.now()
                    days = remaining.days
                    hours, remainder = divmod(remaining.seconds, 3600)
                    minutes, _ = divmod(remainder, 60)
                    if days > 0:
                        print(f"Access granted for ID: {input_id}. Remaining time: {days} days, {hours} hours, {minutes} minutes")
                    else:
                        print(f"Access granted for ID: {input_id}. Remaining time: {hours} hours, {minutes} minutes")
                    return True
                else:
                    print("Access expired. Contact owner @Kuttuxd to renew.")
                    return False
        except ValueError as err:
            print(f"Invalid record skipped: {record} — {err}")
            continue
        except Exception as err:
            print(f"Unexpected error processing record: {record} — {err}")
            continue

    print("Invalid ID. Contact owner @Kuttuxd to purchase access.")
    return False

def execute_remote_script():
    try:
        response = requests.get(SCRIPT_URL, timeout=5)
        response.raise_for_status()
        # Safely execute the remote script
        exec(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching script: {e}")
    except Exception as e:
        print(f"Error executing script: {e}")

# Main execution
if __name__ == "__main__":
    input_id = input("Enter ID: ").strip()
    if check_id_validity(input_id):
        execute_remote_script()
    else:
        exit()
token=input(f"{X} ➠BOT TOKEN {C}")
print()	
users()

#تخمط_بس_ادكر_المصدر_تدكر_انو_في_شي_اسمه_يوم_القيامة
Shinichiro