import os,platform

TYPE_COMMAND = ['pip install|INSTALL','python -m pip install|INSTALL']

def scan(path):
    allFiles = []
    for home, sub_files, file_list_s in os.walk(path):
        for name_files in file_list_s:
            print(name_files)
            allFiles.append(os.path.join(home, name_files))
    return allFiles

try:
    with open(os.path.join(os.path.dirname(__file__),'SETUP.config'),'r') as f:
        data = f.read()
        if data == 'INSTALLER':
           print("YOU NEED UNINSTALLER ?")
           type = input("Y OR N ?")
           if type.upper() == 'Y' or type.upper() == 'YES':
              print('TRYING UNINSTALL')
              if platform.system().upper() == 'WINDOWS' or platform.system().upper() == 'LINUX':
                path = os.path.dirname(__file__)
                files_os = scan(path)
                for a in files_os:
                   try:
                      os.remove(f'[REMOVE] FILES --> {a}')
                   except:
                      print(f"{a} FAILED REMOVE . . .")
                if platform.system().upper() == 'WINDOWS':
                   os.system('del SOCKETEXPLODE_DOSTOOL')
                   os.system('start https://github.com/Hex1629/SOCKETEXPLODE_DOSTOOL')
                   os.system('echo WEBSITE STARTING . . . ^_^')
                else:
                   os.system('rm -rf SOCKETEXPLODE_DOSTOOL')
                   os.system('git clone https://github.com/Hex1629/SOCKETEXPLODE_DOSTOOL')
                   os.system('echo GIT CLONE RUNNING ^_^')
              else:
                 print("IDK HOW TO UNINSTALL IN YOU SYSTEM ( OS )")
           else:
              print("OK I GONNA CLOSE NOW LMAO")
              exit(1)
except:
    return_check = None
    while True:
     try:
        import socks
        import cryptography
        import requests
        import discord_webhook
        import colorsys
        import colorama
        import colored
        import pybase64
        import ipaddress
        import paramiko
        import undetected_chromedriver
        if return_check == True:
           break
        elif return_check == None:
           return_check = True
     except ModuleNotFoundError as e:
      return_check = True
      a = f'{e}'.replace("No module named '","").replace("'","")
      for TYPE in TYPE_COMMAND:
        PIP_LOAD = TYPE.split('|')
        if a == 'discord_webhook':
           a = 'discord-webhook'
        elif a == 'colored':
           a = 'colored==1.4.4'
        elif a == 'socks':
           a = 'PySocks'
        print(f'[{PIP_LOAD[0]}] --> {a}')
        os.system(f'{PIP_LOAD[0]} {a}')
        break
    with open(os.path.join(os.path.dirname(__file__),'SETUP.config'),'w') as f:
        f.write('INSTALLER')
    print("! PASSED ! [ NEXT PLS RUNNING MY TOOLS WITH python main.py ]")
    os.system(f"python {os.path.join(os.path.dirname(__file__),'main.py')}")
