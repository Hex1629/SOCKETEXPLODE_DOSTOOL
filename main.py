import json
import os
import requests
from cryptography.fernet import Fernet
import base64
from leak_gui import checker_login,PANEL_USE

running_new = None
cap = None
try:
    with open(os.path.dirname(__file__)+'/SETTING/captcha.txt', 'r') as f:
        outage = f.read()
    print("CAPTCHA [200 OK]")
    cap = False
except FileNotFoundError:
    print("FAILED")
    cap = True

passed_api = []
api_sxptool = ['https://www.google.com', 'https://sxptoolsapi.idkotherhex1629.repl.co/', 'https://ipwho.is/']

for api in api_sxptool:
    try:
        r = requests.get(api)
        if r.status_code == 200:
            if 'www.google.com' not in api:
                if api not in passed_api:
                    passed_api.append(api)
                print(f"{api} OK...")
            else:
                passed_api.append(f'{api}|CONNECTED')
                print(f"{api} OK...")
        else:
            print(f"{api} DOWN...")
    except Exception as e:
        print(f"{api} DOWN | {e}...")

if cap:
    try:
        with open(os.path.dirname(__file__)+'/SETTING/setting.json', 'r') as f:
            a = f.read()
        try:
            os.remove(os.path.dirname(__file__)+'/SETTING/setting.json')
            exit("RESTART NEW")
        except Exception as e:
            print(e)
            exit('OUTAGE PLS STOP ANOTHER PROCESS FOR EDIT setting.json')
    except FileNotFoundError:
        FERNET_KEYS = Fernet.generate_key()
        IP = ''
        for api_check in passed_api:
            if 'ipwho.is' in api_check:
                try:
                    r = requests.get(api_check)
                    j = json.loads(r.content)
                    IP = j["ip"]
                except Exception:
                    print("API IS FAILED 0.0.0.0")
                    exit('API IS FAILED 0.0.0.0')

        object_str = ['\\\\a|ROOT@ROOT', '\b|ADMIN@ADMIN', '\c|HEX@1629',
                      '\\\\i|https://raw.githubusercontent.com/Hex1629/SOCKETEXPLODE_DOSTOOL/main/update_log.txt',
                      '\\\\h|True', '\\\\g|TEST001', f'\d|{IP}']
        if len(passed_api) != 0:
            r = requests.get('https://raw.githubusercontent.com/Hex1629/SOCKETEXPLODE_DOSTOOL/main/payload_config.json')
            try:
                target_directory = os.path.join(os.path.dirname(__file__), 'SETTING/')
                os.makedirs(target_directory, exist_ok=True)
            except:
                pass
            with open(os.path.join(target_directory+'captcha.txt'), 'w') as f2:
                f2.write("CAPTCHA")
            with open(os.path.join(target_directory+'key.txt'), 'wb') as f3:
                f3.write(FERNET_KEYS)
            with open(os.path.join(target_directory+'setting.json'), 'w') as f:
                data = r.content.decode()
                for string_got in object_str:
                    put_data = string_got.split("|")
                    data = data.replace(put_data[0], put_data[1])
                f.write(data)
        else:
            print('[ -100 ] SXP.TOOLS CONNECT TO SERVER [ FAILED ]')
            exit('SXP.TOOLS CONNECT FAILED')
        running_new = False
else:
    if len(passed_api) == 0:
        print('[ -100 ] SXP.TOOLS CONNECT TO SERVER [ FAILED ]')
        exit('SXP.TOOLS CONNECT FAILED')
    running_new = True
    with open(os.path.dirname(__file__)+'/SETTING/key.txt', 'r') as f:
        a = f.read()
        try:
            FERNET_KEYS = a
            FERNET_ENC = Fernet(FERNET_KEYS)
            a = FERNET_ENC.encrypt(b'HI')
            a = FERNET_ENC.decrypt(a).decode()
            if a == 'HI':
                print("PASSED")
        except Exception as e:
            print(e)
            print("REPORT TO ME ( DISCORD ONLY --> discord.gg/g856k8CArH )")
            exit(e)

if running_new:
    shut = 0
    a_count = []
    for api_check in passed_api:
        try:
            a_proof = api_check.split('|')[1]
            if a_proof not in a_count:
                a_count.append(a_proof)
        except:
            pass

    for proof in a_count:
        if proof == 'CONNECTED':
            save_content = ''
            with open(os.path.dirname(__file__) + '/SETTING/setting.json', 'r') as f:
                save_content = f.read()
            j = json.loads(save_content)
            print(j['CHECK_UPDATE']['AUTO'])
            if j['CHECK_UPDATE'].get('AUTO',False):
                 print("Checking for updates...")
                 try:
                    r = requests.get(j['CHECK_UPDATE']['URL'])
                    conn_data = r.content.decode().replace('\n','').split('#')
                    if 'SHUTDOWN' == conn_data[0]:
                        save_content = save_content.replace('UPDATE', 'SHUTDOWN').replace('\\e', 'SHUTDOWN').replace('\\','')
                        print("SHUTDOWN . . .")
                        shut = 1
                    elif 'NORMAL' == conn_data[0]:
                        print("IT NORMAL NOW ^_^")
                    else:
                        if '\\e' in j['KEYS'] or 'SHUTDOWN' in j['KEYS']:
                            print("Performing update...")
                            r2 = requests.get(conn_data[2])
                            if r2.status_code == 200:
                                try:
                                    with open(os.path.join(os.path.dirname(__file__), conn_data[1]), 'w') as f:
                                        f.write(r2.content.decode())
                                except:
                                    try:
                                        with open(os.path.join(os.path.dirname(__file__), conn_data[1]), 'wb') as f:
                                            f.write(r2.content)
                                    except:
                                        print("FAILED TO UPDATE FILES")
                                        exit("REPORT TO HEX NOW")
                                print(f"{len(r2.content)} NEW CONTENT OF {conn_data[1]} FROM {conn_data[2]}")
                                save_content = save_content.replace('SHUTDOWN', 'UPDATE').replace('\\e', 'UPDATE').replace('\\','')
                            else:
                                print("GITHUB IT DOWN NOW LMAO ;-;")
                        else:
                            print("UPDATE IT DONE NOW ^_^")
                 except:
                    print("CONNECTION TO UPDATE AUTO FAILED [ -100 ]")
                    exit(1)

            with open(os.path.dirname(__file__) + '/SETTING/setting.json', 'w') as f:
                f.write(save_content)

            if shut == 1:
                print("LMAO SHUTDOWN . . .")
                exit("SYSTEM IS FAILED BY SHUTDOWN")
            else:
                print("RUNNING SXP.TOOLS MAIN . . .")
                checker_login()
else:
    print("restart program pls [ -001 ]")
    exit(1)
