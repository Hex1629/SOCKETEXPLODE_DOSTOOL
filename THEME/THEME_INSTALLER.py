import requests,time,platform,os
from colored import fg,attr

#CLI

WHO_MAKE = 'DEV#HEX1629'.split('#') # * YOU NEED REPLACE ONLY DEV TO OTHER AND HEX1629 TO OTHER EXAMPLE LIKE THIS DEVM#NIXWASHERE
VERSION = '0.001' # * YOU NEED REPLACE THIS
NAME_MOD = 'COVID-19.MOD' # * YOU NEED REPLACE THIS TOO
SPEED_INSTALL = int(0.5) # * YOU CAN REPLACE THIS

class CLI():
   def setting_loading():
      print(f'[INSTALLER] COLORED (PACKAGE)')
      time.sleep(0.5)
      print(f'[INSTALLER] REQUESTS (PACKAGE)')
      time.sleep(0.5)
      print(f'  [SETTING] INSTALL MOD.INSTALLER (WRITE FILES)')
      time.sleep(0.5)
      print(f'  [RUNNING] RUNNING MOD.INSTALLER (EXECUTE)')
      if platform.system().lower() == 'windows':
         os.system('cls')
      else:
         os.system('clear')

   def banner():
      global WHO_MAKE,VERSION,NAME_MOD
      print(f'''
{fg(196)}╔╦╗╔═╗╔╦╗ {fg(78)}┬┌┐┌┌─┐┌┬┐┌─┐┬  ┬  ┌─┐┬─┐
{fg(197)}║║║║ ║ ║║ {fg(77)}││││└─┐ │ ├─┤│  │  ├┤ ├┬┘
{fg(198)}╩ ╩╚═╝═╩╝{fg(7)}o{fg(76)}┴┘└┘└─┘ ┴ ┴ ┴┴─┘┴─┘└─┘┴└─

{fg(184)}╔═════════════════════════════════════╗╗
{fg(185)}     MOD NAME - {NAME_MOD}
{fg(186)}         VERSION - {VERSION}
{fg(187)}            MAKE BY {WHO_MAKE[0]}.{WHO_MAKE[1]}
{fg(188)}╚═════════════════════════════════════╝╝{attr(0)}''')

# * YOU NEED REPLACE EXAMPLE THIS https://www.example.com:example.py to YOU FILES OF MOD
URL = ['https://www.example.com#example.py','FOLDER#EXAMPLE_FOLDER'] # ! <--- YOU FILES OF MOD PUT HERE HOW TO PUT LIKE THIS URL#FILES IF YOU WANNA WRITE FOLDER NOT REPLACE FOLDER PLS REPLACE EXAMPLE_FOLDER
path_files = 'OS.JOIN' # * YOU NEED REPLACE THIS FOR SET YOU PATH USE ( OS.JOIN for install in folder SOCKETEXPLODE or YOU MOD NOT THIS IN FOLDER SOCKETEXPLODE YOU NEED PUT FOLDER PATH TOO )

# INSTALL
def INSTALLER():
    global SPEED_INSTALL,path_files,URL
    num = 0
    for url_packet in URL:
     num += 1
     URL_GET = url_packet.split('#')
     if URL_GET[0].upper() == 'FOLDER':
         if path_files.upper() == 'OS.JOIN':
           open_files_leak = os.path.join(os.path.dirname(__file__),URL_GET[1])
         else:
           open_files_leak = URL_GET[1]
         try:
            os.makedirs(open_files_leak)
            print(f'{fg(7)}[{fg(40)}I{fg(41)}N{fg(42)}S{fg(43)}T{fg(44)}A{fg(80)}L{fg(81)}L{fg(7)}] {fg(87)}{URL_GET[0]} {fg(86)}OF {num} {fg(85)}FOLDER={URL_GET[1]} {fg(84)}STATUS_CODE=200:OK{attr(0)}')
         except:
            print(f'{fg(7)}[{fg(196)}F{fg(197)}A{fg(198)}I{fg(198)}L{fg(199)}E{fg(200)}D{fg(7)}] {fg(184)}{URL_GET[0]} {fg(185)}OF {fg(185)}{num} {fg(186)}WRITING FAILED . . .{attr(0)}')
     else:
      try:
        r = requests.get(url=str(URL_GET[0]))
        if path_files.upper() == 'OS.JOIN':
           open_files_leak = os.path.join(os.path.dirname(__file__),URL_GET[1])
        else:
           open_files_leak = URL_GET[1]
        if r.status_code == 200:
           with open(open_files_leak,'wb') as f:
            f.write(r.content)
           print(f'{fg(7)}[{fg(40)}I{fg(41)}N{fg(42)}S{fg(43)}T{fg(44)}A{fg(80)}L{fg(81)}L{fg(7)}] {fg(87)}{URL_GET[0]} {fg(86)}OF {num} {fg(85)}FILES={URL_GET[1]} {fg(84)}STATUS_CODE={r.status_code}:{r.reason}{attr(0)}')
        else:
           print(f'{fg(7)}[{fg(196)}F{fg(197)}A{fg(198)}I{fg(198)}L{fg(199)}E{fg(200)}D{fg(7)}] {fg(184)}{URL_GET[0]} {fg(185)}OF {fg(185)}{num} {fg(186)}STATUS_CODE={r.status_code}:{r.reason}{attr(0)}')
      except:
        print(f'{fg(7)}[{fg(196)}F{fg(197)}A{fg(198)}I{fg(198)}L{fg(199)}E{fg(200)}D{fg(7)}] {fg(184)}{URL_GET[0]} {fg(185)}OF {fg(185)}{num} {fg(186)}INSTALL . . .{attr(0)}')
     time.sleep(SPEED_INSTALL)

# RUNNING FILES
# * YOU NEED REPLACE THIS FOR RUNNING FILES
files_running = 'example.py' # * EXAMPLE I NEED RUN setup.py I REPLACE THIS WITH main.py
type_running = 'python' # * YOU NEED REPLACE THIS FOR RUNNING YOU FILES WITH MODE ( py/python or exec/execute )

def RUNNING():
   global files_running,type_running

   if path_files.upper() == 'OS.JOIN':
      files_running2 = os.path.join(os.path.dirname(__file__),files_running)
   else:
      files_running2 = files_running

   if type_running.upper() == 'PY' or type_running.upper() == 'PYTHON':
      os.system(f'python {files_running2}')
   else:
      exec(files_running2)
# USAGE
CLI.setting_loading()
time.sleep(0.5)
CLI.banner()
time.sleep(0.5)
INSTALLER()
time.sleep(0.5)
RUNNING()
