# Decompile by Xyzon Dev
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2022-01-03 13:36:30.746764
import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
ok,cp,id,loop = [],[],[],0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_key = {"january": "January", "february": "February", "march": "March", "april": "April", "may": "May", "june": "June", "july": "July", "august": "August", "september": "September", "october": "October", "november": "November", "december": "December"}
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
        
def yayanxd():
    os.system('clear')
    print (' %s*%s %stools ini menggunakan login cookies facebook.%s\n %s*%s %sapakah kamu sudah tau cara mendapatkan cookies facebook?%s\n %s*%s %sketik%s %sopen%s %suntuk mendapatkan cookies%s'%(O,N,P,N,O,N,P,N,O,N,P,N,O,N,P,N))
    cookie = input("\n %s[%s?%s] Cookies : %s"% (N,K,N,P))
    if cookie in['OPEN','Open','open']:
      jalan("\n  %s* %s %sanda akan di arahkan ke YouTube%s"%(O,H,P,O));time.sleep(3);os.system('xdg-open https://youtu.be/DF7bUCn0GFY');yayanxd()
    try:
        head={'Host':'business.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type' : 'text/html; charset=utf-8','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cookie': cookie}
        asww=requests.get("https://business.facebook.com/creatorstudio/home", headers=head)
        reqq=re.search('{"accessToken":"(EAA\w+)', asww.text)
        tokn=reqq.group(1)
        open('.cokie.txt', 'a').write(cookie)
        open('.token.txt', 'a').write(tokn)
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(tokn)).json()['name']
        print('\n\n %s*%s %sselamat datang%s %s%s%s'%(O,N,P,N,K,nama,N));time.sleep(1)
        print(' %s*%s %smohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...%s'%(O,N,P,N));time.sleep(1)
        input(' %s*%s %sTekan enter%s '%(O,N,P,N))
        os.system('xdg-open https://www.facebook.com/bintangt.zy.92')
        moch_yayan()
    except AttributeError:
        print('\n %s[%s×%s] cookies invalid'%(N,M,N));time.sleep(1);yayanxd()
    except UnboundLocalError:
        print('\n %s[%s×%s] cookies invalid'%(N,M,N));time.sleep(1);yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] tidak ada koneksi\n'%(N,M,N))
def xyzondev():
    try:
        kontol = open('.token.txt', 'r').read()
    except IOError:
        print('\n %s[%s×%s] cookie invalid'%(N,M,N));time.sleep(2);os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt');yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
    except KeyError:
        print('\n %s[%s×%s] cookie invalid'%(N,M,N));time.sleep(2);os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt');yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] tidak ada koneksi\n'%(N,M,N))
    IP = requests.get("https://api.ipify.org").text
    _mmk_ = open('.cokie.txt').read()
    kueh  = {"cookie":_mmk_}
    
    print("[%s•%s] %sServer sedang maintenance%s"%(O,N,K,N))
    print("[%s•%s] %stunggu lah beberapa saat lagi%s"%(O,N,K,N))
    print("[%s•%s] %skarana admin sedang memperbaiki sistem yang rusak%s"%(O,N,K,N))
    print("[%s•%s] %sTerimakasih. sudah memakai script/tools ini.%s"%(O,N,K,N))
    print("[%s•%s] %sBy Xyzon Dev%s"%(O,N,K,N))
    
    loping= 1
if __name__ == '__main__':
    os.system('git pull')
    xyzondev()
# Mau Ngapain Cuk?
