#!/bin/bash

echo " "
echo "[x] updating rapid"
echo " "

echo "[x] starting update process"
echo -n "[x] running apt-get update/upgrade.. "
/usr/bin/apt-get -y update > /dev/null 2>&1
/usr/bin/apt-get -y upgrade > /dev/null 2>&1
echo "done"

echo -n "[x] updating metasploit.. "
cd /opt/metasploit/msf3
git pull origin master  > /dev/null 2>&1
echo "done"

echo -n "[x] updating sqlmap.. "
cd /pentest/sqlmap
git pull  > /dev/null 2>&1
echo "done"

echo -n "[x] updating w3af.. "
cd /pentest/w3af
svn update > /dev/null 2>&1
echo "done"

echo -n "[x] updating sqlninja.. "
cd /pentest/sqlninja
svn update > /dev/null 2>&1
echo "done"

echo -n "[x] updating SET.. "
cd /pentest/set
svn update > /dev/null 2>&1
echo "done"

echo -n "[x] updating waf-research.. "
cd /pentest/waf-research
git pull > /dev/null 2>&1
echo "done"

echo -n "[x] updating weevely.. "
cd /pentest/weevely
git pull > /dev/null 2>&1
echo "done"

echo -n "[x] updating wpscan.. "
cd /pentest/wpscan
git pull > /dev/null 2>&1
echo "done"

echo -n "[x] updating exploitdb archive.. "
cd /pentest/exploitdb
wget http://www.exploit-db.com/archive.tar.bz2  > /dev/null 2>&1
tar jxf archive.tar.bz2 > /dev/null 2>&1
rm -rf archive.tar.bz2 > /dev/null 2>&1
echo "done"

echo -n "[x] updating nikto.. "
/usr/bin/nikto -update > /dev/null 2>&1
echo "done"
echo " "
echo "[x] update complete"
echo " "
