import os,time

data = input('YOU SYSTEM SUPPORT PIP (Y OR N)?').upper()
if data == 'YES' or data == 'Y':
    os.system('''pip install pybase64
pip install requests
pip install cryptography
pip install colored
pip install colorama
pip install discord-webhook''')
else:
    os.system('''python -m pip install pybase64
python -m pip install requests
python -m pip install cryptography
python -m pip install colored
python -m pip install colorama
python -m pip install discord-webhook''')
print('DONE INSTALL')
os.system(f"python {os.path.join(os.path.dirname(__file__),'main.py')}")
os.remove(__file__)