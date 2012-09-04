#!/usr/bin/env python
# SPIKE Framework tweaking script.
# Author: sickness
# For bugs or suggestions: sick.n3ss416@gmail.com
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

import sys,os,subprocess,time
from time import *

def spike_tweak():
	spike_path = "/pentest/fuzzers/spike/src/"
	  
	subprocess.Popen("apt-get -y install automake",shell=True).wait()
	print "\n"
	subprocess.Popen("sed -i '/tried to send to a closed socket/{n;s/return 0/exit (1)/}' " + spike_path + "spike.c",shell=True).wait()
	print "\n"
	subprocess.Popen("cd " + spike_path + " && aclocal",shell=True).wait()
	print "\n"
	subprocess.Popen("cd " + spike_path + " && automake && ./configure",shell=True).wait()
	print "\n"
	subprocess.Popen("cd " + spike_path + " && automake && ./configure",shell=True).wait()
	print "\n"
	subprocess.Popen("cd " + spike_path + " && ./configure",shell=True).wait()
	print "\n"
	subprocess.Popen("sed -i 's/CFLAGS = -Wall -funsigned-char -c -fPIC -ggdb/CFLAGS = -Wall -funsigned-char -c -fPIC -ggdb -fno-stack-protector/g' " + spike_path + "Makefile",shell=True).wait()
	print "\n"
	subprocess.Popen("cd " + spike_path + " && make",shell=True).wait()
	print "\n"


print "\n"
print "Tweaking SPIKE for sickfuzz, please wait!"
print "Warning this might take a few minutes!\n"
sleep(2)
spike_tweak()
print "\n"
print "Everything is setup correctly, sickfuzz is ready!\n"
sys.exit()
