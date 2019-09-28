#!/bin/bash

echo ""
echo "================================================================="
echo " 		  Pentest Attack Machine Setup "
echo "	Based on the setup from The Hacker Playbook "
echo "================================================================="
echo ""

# Prepare tools folder
echo "[+] Creating tools folder in /opt"
	mkdir /opt/tools/
echo ""

# Setting up  postgresql
echo "[+] Setting up with postgresql"
	service postgresql start
echo ""

# Adding postgresql services rc.d defaults
echo "[+] Adding postgresql to rc.d defaults"
	update-rc.d -f postgresql defaults
echo ""

#Optional for Metaspolits - Enable Logging
#Very usefull for bulk attack/queries
echo "spool/root/msf_console.log" > /root/.msf4/msfconsole.rc
	echo "[+] Logs will be stored at /root/msf_console.log"

# Discover Scripts - Passive reconnaissance
echo "[+] Installing Discover Scripts (Backtrack-scripts)"
	cd /opt/tools/
	git clone https://github.com/leebaird/discover.git
	cd /opt/tools/discover/
	/opt/tools/discover/setup.sh
echo ""

# SMBexec - Grab hashes out of the Domain Controller and reverse shells
# Step 1: Select option 1
# Step 2: Select option 4
# Step 3: Select option 5
echo "[+] Installing SMBexec"
	cd /opt/tools/
	echo "[-] Remember to select option 1 and locate path /otp/tools/"
	git clone https://github.com/brav0hax/smbexec.git
	cd /opt/tools/smbexec/
	./install.sh
echo "[+] Install missing files libesedb-tools"
	wget http://pkgs.fedoraproject.org/repo/pkgs/libesedb/libesedb-alpha-20120102.tar.gz/198a30c98ca1b3cb46d10a12bef8deaf/libesedb-alpha-20120102.tar.gz
	tar -zxf libesedb-alpha-20120102.tar.gz
	cd libesedb-20120102/
	./configure && make && sudo make install
	rm -f libesedb-alpha-20120102.tar.gz
	echo "Added successfully!!!"
echo ""

# Veil - Create Python based Meterpreter executable
echo "[+] Installing Veil Framework"
	cd /opt/tools/
	git clone https://github.com/veil-evasion/Veil.git Veil
	cd /opt/tools/Veil/setup
	./setup.sh
	echo "Install successfully!!!"
echo ""

# WCE (Windows Credential Editor) - Pulls passwords from memory
echo "[+] Downloading and installing WCE (Windows Credential Editor)"
	mkdir /opt/tools/wce/
	cd /tmp/
	git clone https://github.com/Despereaux222/THPtools.git && cd THPtools/
	unzip -d /opt/tools/wce wce_v1_41beta_universal.zip
	rm -f wce_v1_41beta_universal.zip
echo ""

# Mimikatz - Pulls passwords from memory
echo "[+] Installing Mimikatz"
	mkdir /opt/tools/mimikatz/
cd /tmp/
	wget https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20190813/mimikatz_trunk.zip
	unzip -d /opt/tools/mimikatz/ mimikatz_trunk.zip
	rm -f mimikatz_trunk.zip
echo ""

#Saving Custom Password Lists
echo "[+]Adding Password Lists for cracking hashes"
	cd /opt/tools/ && mkdir password_list && cd ./password_list
#Download full version at: https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm
echo "[+] Downloading crackstation-human-only.txt.gz"
	wget https://crackstation.net/files/crackstation-human-only.txt.gz
	gzip -d crackstation-human-only.txt.gz
echo "[+] Downloading rockyou.txt.bz2"
	wget http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2
	bzip2 -d rockyou.txt.bz2

# PeepingTom - Website snapshots
echo "[+] Installing PeepingTom"
	cd /opt/tools/
	git clone https://bitbucket.org/LaNMaSteR53/peepingtom.git
	cd /opt/tools/peepingtom/
	wget https://gist.githubusercontent.com/nopslider/5984316/raw/423b02c53d225fe8dfb4e2df9a20bc800cc78e2c/gnmap.pl
echo ""

# Download appropriate PhantomJS package
echo "[+] Downloading PhantomJS package"
	wget https://repo1.maven.org/maven2/com/github/klieber/phantomjs/1.9.2/phantomjs-1.9.2-linux-i686.tar.bz2
	tar xvjf phantomjs-1.9.2-linux-i686.tar.bz2
	cp ./phantomjs-1.9.2-linux-i686/bin/phantomjs .
echo ""

# Nmap script - Quicker scanning and smarter identification
echo "[+] Installing Nmap scripts"
	cd /usr/share/nmap/scripts/
	wget https://raw.githubusercontent.com/hdm/scan-tools/master/nse/banner-plus.nse
echo ""

# PowerSploit - Scripts for post exploitation
echo "[+] Installing PowerSploit"
	cd /opt/tools/
	git clone https://github.com/mattifestation/PowerSploit.git
	cd /opt/tools/PowerSploit/
	wget https://raw.githubusercontent.com/obscuresec/random/master/StartListener.py
	wget https://raw.githubusercontent.com/darkoperator/powershell_scripts/master/ps_encoder.py
echo ""

# Responder - Used to gain NTLM challenge/response
echo "[+] Installing Responder"
	cd /opt/tools/
	git clone https://github.com/SpiderLabs/Responder.git
echo ""

# SET (Social Engineering Toolkit) - Pre-installed on Kali Linux
echo "[+] Installing SET (Social Engineering Toolkit)"
	cd /opt/tools/
	git clone https://github.com/trustedsec/social-engineer-toolkit.git SocialEngineeringToolkit
	cd /opt/tools/SocialEngineeringToolkit/
	pip install -r requirements.txt
echo ""

# Bypassuac - Used to bypass UAC in post exploitation
# → https://www.trustedsec.com/downloads/
echo "[+] Installing Bypass UAC"
	cd /tmp/
	wget http://thehackerplaybook.com/Download/bypassuac.zip
	unzip bypassuac.zip
	cp bypassuac/bypassuac.rb /opt/metasploit/apps/pro/msf3/scripts/meterpreter/
	mv bypassuac/uac/ /opt/metasploit/apps/pro/msf3/data/exploits/
	rm -Rf bypassuac
echo ""

# BeEF - cross-site scripting framework at http://beefproject.com/
# BeEF will be used as an cross-site scripting attack framework
echo "[+] Installing BeEF"
apt-get install beef-xss
echo ""

echo "[+] Fuzzing Lists (SecLists)"
	cd /opt
	git clone  https://github.com/danielmiessler/SecLists.git SecLists
echo ""

# PEDA - Python Exploit Development Assistance for GDB at Repository: https://github.com/longld/peda
echo "[+] Installing PEDA"
git clone https://github.com/longld/peda.git /opt/PEDA
echo "source /opt/PEDA/peda.py" >> ~/.gdbinit
echo ""

# The End
echo "[+] All tools installed successfully!"
echo "[+] ~~~ Happy Hacking! ~~~"
echo ""