#!/usr/bin/env python
# Sickfuzz is a Web server fuzzer made for BackTrack
# Author: sickness
# For any bugs/suggestions contact: sick.n3ss416@gmail.com
#
# (C)opyright 2011 - sickness & g0tmi1k                                                        #
#---License------------------------------------------------------------------------------------#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#---License------------------------------------------------------------------------------------#

import sys,subprocess,time,os,signal,socket,getopt,urllib2
from time import sleep,localtime,strftime

#-------------------------------------------------------------------------------

spike = "/pentest/fuzzers/spike/src/"
fpath = "/pentest/fuzzers/sickfuzz/"
script = ""
ip = ""
port = ""
iface = ""
log = ""

#-------------------------------------------------------------------------------

def help_screen():
	print "                    __             ___                           "
	print "         __        /\ \          /'___\                          "
	print "     ____/\_\    ___\ \ \/'\     /\ \__/  __  __  ____    ____    "
	print "   /',__\/\ \  /'___\ \ , <     \ \ ,__\/\ \/\ \/\_ ,`\ /\_ ,`\  "
	print "  /\__, `\ \ \/\ \__/\ \ \\`\    \ \ \_/\ \ \_\ \/_/  /_\/_/  /_ "
	print "  \/\____/\ \_\ \____\\ \_\ \_\   \ \_\  \ \____/ /\____\ /\____\ "
	print "   \/___/  \/_/\/____/ \/_/\/_/    \/_/   \/___/  \/____/ \/____/\n\n"
	print "  Welcome to sickfuzz Version: 1.0"
	print "  Codename: 'Have you g0tmi1k!?'"
	print "  Author: sickness"
	print "  Bug reports or suggestions at: sick.n3ss416@gmail.com\n"
	print "  Usage example:"
	print "  ./sickfuzz.py --script all --ip 192.168.1.64 --port 80 --iface wlan0 --log /root/"+"\n"
	print "	-h/--help  - prints this help menu."
	print "	-s/--script <[all]/[number]>    use --script-show to view available scripts"
	print "	-t/--ip <target ip>"
	print "	-p/--port <target port>"
	print "	-i/--iface <network interface>"
	print "	-l/--log <path where .pcap log files will be saved> (Other then 'pcap_logs' directory.)\n"
	sys.exit()

def script_show():
	print "  [1/6] Fuzzing: GET  /AAAAAA."
	print "  [2/6] Fuzzing: POST /AAAAAA."
	print "  [3/6] Fuzzing: HEAD /AAAAAA."
	print "  [4/6] Fuzzing: GET  Headers."
	print "  [5/6] Fuzzing: POST Headers."
	print "  [6/6] Fuzzing: HEAD Headers."
	sys.exit()

if len(sys.argv) == 1:
	help_screen()
elif sys.argv[1] == ("--script-show" or "-s-show"):
	script_show()
elif sys.argv[1] == ("-?" or "-h" or "--help"):
	help_screen()

	
def openport():
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		s.connect((ip,int(port)))
		s.shutdown(2)
		return True
	except:
		return False
	

def spike_fuzz( x ):
	if x == 0: print "  [1/6] Fuzzing: GET /AAAAAA."
	elif x == 1: print " [>] [2/6] Fuzzing: POST /AAAAA."
	elif x == 2: print " [>] [3/6] Fuzzing: HEAD /AAAAA."
	elif x == 3: print " [>] [4/6] Fuzzing: GET Headers."
	elif x == 4: print " [>] [5/6] Fuzzing: POST Headers."
	elif x == 5: print " [>] [6/6] Fuzzing: HEAD Headers."
	
	try:
		subprocess.Popen("export LD_LIBRARY_PATH=. && cd "+spike+"&&"+fuzzer+" "+ip+" "+port+" " + fpath + scripts[x]+ " " + skipv + " > " + fpath + "spike_log.txt",shell=True).wait()
	except (RuntimeError,KeyboardInterrupt):
		clean_up()
		subprocess.Popen("killall tshark",shell=True)

	if openport() == True:
		try:
			print "\n [>] Finished, moving to next script ..."
			print " [>] Press CTRL+C again to stop fuzzing!\n"
		except KeyboardInterrupt:
			clean_up()
			subprocess.Popen("killall tshark",shell=True)
			sys.exit()
	elif openport() == False:
		print "\n"
		print " [>] We have a crash!"
		clean_up()
		subprocess.Popen("killall tshark",shell=True)
		sys.exit()
		
def clean_up():
	print "\n"
	print " [>] Stopping fuzzing and tshark, please wait!"
	os.kill(tshark.pid,signal.SIGTERM)
	subprocess.Popen("killall tshark",shell=True)
	subprocess.Popen("mv -f "+fpath+"spike_log.txt"+" "+log,shell=True).wait()
	print " [>] Done!\n"
	sys.exit()
	
time_start = time.time()
print "\n [>] Fuzzing starting at "+strftime("%a, %d %b %Y %H:%M:%S", localtime())+" ..."

try:
    opts, args = getopt.getopt(sys.argv[1:], "s:t:p:i:l:h?", ["","script=","ip=","port=","iface=", "log=","help"])
except getopt.GetoptError, err:
	help_screen()
	sys.exit()
for o, a in opts:
	if o in ("-s", "--script"):
		script = a
	if o in ("-t", "--ip"):
		ip = a
	if o in ("-p", "--port"):
		port = a
	if o in ("-i", "--iface"):
		iface = a
	if o in ("-l", "--log"):
		log = a
		
try:
	fuzzer = "./generic_web_server_fuzz2"
	scripts = ["HTTP/web00.spk","HTTP/web01.spk","HTTP/web02.spk","HTTP/web03.spk","HTTP/web04.spk","HTTP/web05.spk"]
	skipv = "0 0"
	
	if script == "" :
		print "Missing \"--script/-s\", check --help for more info.\n"
		sys.exit()
	if ip == "" :
		print "Missing \"--ip/-t\", check --help for more info.\n"
		sys.exit()
	if port == "" :
		print "Missing \"--port/-p\", check --help for more info.\n"
		sys.exit()
	if iface == "" :
		print "Missing \"--iface/-i\", check --help for more info.\n"
		sys.exit()
	if log == "" :
		print "Missing \"--log/-l\", check --help for more info.\n"
		sys.exit()

	print " [>] Starting: sickfuzz v1.0"
	if openport() == True:
		pass
	else:
		print " [>] Could not connect, check if the port is opened!"
		sys.exit()
	print " [>] Launching packet capture, please wait ..."
	print "\n"
	try:
		tshark = subprocess.Popen("tshark -i "+iface+" -d tcp.port=="+port+",http -w "+log+"fuzzing_log.pcap -b filesize:65535 -b files:20 -q",shell=True)
		sleep(4)
		print "\n"
		print " [>] Capturing packets, now starting the fuzzer ...!\n"
		sleep(1)
	except KeyboardInterrupt:
		print " [>] Something went wrong!"
		print " [>] Exiting ..."
		sys.exit()
	
	if script == "all":
		script_numbers = range(0,6)
		for i in script_numbers:
			if openport() == True:
				spike_fuzz( i )

			else:
				clean_up()
				subprocess.Popen("killall tshark",shell=True)
				sys.exit()
	else:
		if script == "1":
			spike_fuzz( 0 )
		elif script == "2":
			spike_fuzz( 1 )
		elif script == "3":
			spike_fuzz( 2 )
		elif script == "4":
			spike_fuzz( 3 )
		elif script == "5":
			spike_fuzz( 4 )
		elif script == "6":
			spike_fuzz( 5 )
		else:
			print " [-] You have picked an invalid script."
			print " [-] Use the -s-show/--script-show flags to see available scripts."
		print "\n"
#-------------------------------------------------------------------------------
except KeyboardInterrupt:
	print "\r"
	print " [>] Fuzzing process ended at: "+strftime("%a, %d %b %Y %H:%M:%S", localtime())
	print " [>] Elapsed time: %.2f minutes" % ((time.time() - time_start)/60)
	print "\r"
	clean_up()
	subprocess.Popen("killall tshark",shell=True)
	sys.exit()
