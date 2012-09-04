(RA)spberry (PI) (D)ropbox
==========================
rapid v0.2

villain@evilthings.org

about
=======
rapid is something i worked on in order to help with a pentest. it's designed to be a 'drop box' of sorts which phones home via ssh, something you can connect to a network and launch a pentest, scan or pivot from. it's built to run on a raspberry pi with the debian7/wheezy beta that is currently out. haven't tested with raspbian or anything else, so not sure how it'll work out. the idea was the keep it as lightweight as possible. i didn't see the value of adding too many tools like john or hydra because of the lack (comparitively) of processing power on the raspberrypi.

sshtun
======
i've included an ssh script which is installed to /usr/local/bin. a few vars need to be set, and then add the script to the rc.local file once its configured. upon reboot, the script will try to connect to an SSH host of your choice over several ports

tools
=====
all of the tools you will find in backtrack. since i spend quite a bit of time in backtrack, i figured i would try and stick with the same tools. installed as part of the package are;
- nmap
- john the ripper
- metasploit (quite slow)
- dsniff
- netcat
- proxychains
- openvpn
- exploitdb archive
- sqlmap
- w3af
- set
- weevely
- skipfish
- a bunch more

most of the tools are installed to /pentest except for metasploit which is installed to /opt/metasploit. an update script is also located in /usr/local/bin for the tools which are installed via github or svn. the tools installed via apt-get are either in /usr/bin or /usr/sbin

TODO
====
- add wireless support when the need arises
