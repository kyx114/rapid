#!/bin/bash

echo " "
echo "[x] installing rapid v0.1"
echo "    villain@evilthings.org"
echo " "

# are we root?
if [[ $EUID -ne 0 ]]; then
   echo "ERROR: script requires root privs" 1>&2
   exit 1
fi

if [ -d /opt ]; then
   echo "[x] /opt directory exists"
else
   mkdir /opt > /dev/null 2>&1
   echo "[x] /opt directory created"
fi

if [ -d /pentest ]; then
   echo "[x] /pentest directory exists"
else
   mkdir /pentest > /dev/null 2>&1
   echo "[x] /pentest directory created"
fi

echo -n "[x] running apt-get update/upgrade.. "
/usr/bin/apt-get -y update > /dev/null 2>&1
/usr/bin/apt-get -y upgrade > /dev/null 2>&1
echo "done"

echo -n "[x] installing baseline packages.. "
/usr/bin/apt-get -y install curl git-core nmap john p0f dsniff netcat nikto python-scapy tcpdump hping3 ettercap-text-only nbtscan ptunnel ngrep proxychains tcpflow httptunnel smbclient udptunnel ipcalc tcpreplay subversion ruby irb ri rubygems libruby ruby-dev libpcap-dev python-pexpect tcptraceroute lsof libssl-dev libidn11-dev libidn11 sslsniff hydra sslstrip openvpn tinyproxy macchanger python-beautifulsoup > /dev/null 2>&1
echo "done"

echo -n "[x] removing unnecessary services.. "
/etc/init.d/ntp stop > /dev/null 2>&1
update-rc.d -f ntp remove > /dev/null 2>&1
update-rc.d -f portmap remove > /dev/null 2>&1
/etc/init.d/tinyproxy stop > /dev/null 2>&1
update-rc.d -f tinyproxy remove > /dev/null 2>&1
apt-get -y autoremove > /dev/null 2>&1
apt-get -y clean > /dev/null 2>&1
apt-get -y autoclean > /dev/null 2>&1
echo "done"

echo -n "[x] installing sshtun to /usr/local/bin.. "
cp src/bin/sshtun.sh /usr/local/bin > /dev/null 2>&1
chmod 755 /usr/local/bin/sshtun.sh > /dev/null 2>&1
echo "done"

echo -n "[x] installing update script to /usr/local/bin.. "
cp src/bin/rapid-update.sh /usr/local/bin > /dev/null 2>&1
chmod 755 /usr/local/bin/rapid-update.sh > /dev/null 2>&1
echo "done"

echo -n "[x] installing random tools to /pentest.. "
cd src/pentest
cp -R * /pentest > /dev/null 2>&1
echo "done"

echo -n "[x] downloading exploitdb archive to /pentest.. "
mkdir /pentest/exploitdb
cd /pentest/exploitdb
wget http://www.exploit-db.com/archive.tar.bz2  > /dev/null 2>&1
tar jxf archive.tar.bz2 > /dev/null 2>&1
rm -rf archive.tar.bz2 > /dev/null 2>&1
touch version
echo "done"

echo -n "[x] installing metasploit framework (can take a while).. "
mkdir /opt/metasploit > /dev/null 2>&1
cd /opt/metasploit
git clone https://github.com/rapid7/metasploit-framework.git msf3 > /dev/null 2>&1
ln -sf /opt/metasploit/msf3/msf* /usr/local/bin/ > /dev/null 2>&1
echo "done"

echo -n "[x] installing sqlmap.. "
cd /pentest
git clone https://github.com/sqlmapproject/sqlmap.git > /dev/null 2>&1
echo "done"

echo -n "[x] installing w3af.. "
cd /pentest
svn co https://w3af.svn.sourceforge.net/svnroot/w3af/trunk w3af > /dev/null 2>&1
echo "done"

echo -n "[x] installing sqlninja.. "
cd /pentest
svn co https://sqlninja.svn.sourceforge.net/svnroot/sqlninja sqlninja > /dev/null 2>&1
echo "done"

echo -n "[x] installing SET.. "
cd /pentest
svn co http://svn.secmaniac.com/social_engineering_toolkit set > /dev/null 2>&1 
echo "done"

echo -n "[x] installing waf-research.. "
cd /pentest
git clone https://github.com/ironbee/waf-research.git > /dev/null 2>&1
echo "done"

echo -n "[x] installing weevely.. "
cd /pentest
git clone https://github.com/epinna/Weevely.git weevely > /dev/null 2>&1
echo "done"

echo -n "[x] building skipfish (can take a while).. "
cd /pentest/skipfish
make > /dev/null 2>&1
echo "done"

echo -n "[x] setting permissions on /pentest.. "
chown -R root.root /pentest
echo "done"

echo -n "[x] changing default RAM allocation.. "
cp /boot/arm224_start.elf /boot/start.elf
echo "done"

echo " "
echo "[x] rapid installation complete"
echo "[x] restart required to activtate new RAM allocation"
echo "[x] don't forget to configure /usr/local/bin/sshtun.sh"
echo "    and add it to rc.local"
echo " "
