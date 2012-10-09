#!/usr/bin/env python

# 0) profile A
# 1) arg1 = from_dir
# 2) arg2 = to_dir
# 3) cp or mv
# 4) postfix
# 5) year-digits = 1-4
# 6) month-digits = 5-6

import sys
import os
import re

woman = {}
woman['to_dir'] = '/media/4b65836d-6b9a-47e9-b452-363f2e722f93/Koti'
woman['from_dir'] = '/media/Nokia N9/DCIM/'
woman['postfix'] = "_n"

man = {}
man['to_dir'] = '/media/4b65836d-6b9a-47e9-b452-363f2e722f93/Koti'
man['from_dir'] = '/media/Nokia N9/DCIM'
man['postfix'] = '_m'

profile_ptr = {}

profiles = {'woman': woman, 'man': man}

# from_dir
# from_file (fullpath)
# from_files (jpg and mp4 files without path)
#
# to_dir
# to_file (fullpath)

if (len(sys.argv) != 2):
    print "Specify one profile."
    print "Possible profiles are:"
    print profiles.keys();
    sys.exit(0);

profile = sys.argv[1];

if (not profiles.has_key(profile)):
    print "This profile does not exist."
    sys.exit(0);

profile_ptr = profiles[profile];

from_files = []
from_files = os.listdir(profile_ptr['from_dir']);

for file in from_files:
    # report the yyyymm
    print file

    m = re.match("((\d{6})\d{2}_\d{3}).(\w{3})", file);

    if (m):
        if (m.group(3) == "jpg"):
            to_dir = os.path.join(profiles[profile]['to_dir'], "MyPictures", m.group(2));
        elif (m.group(3) == "mp4"):
            to_dir = os.path.join(profiles[profile]['to_dir'], "MyVideos", m.group(2));
        else:
            print "File type", m.group(3), " not recognized.."
            sys.exit(0);

        to_file = os.path.join(to_dir, m.group(1) + profiles[profile]['postfix'] + "." + m.group(3));
        from_dir = profiles[profile]['from_dir']
        from_file = os.path.join(profiles[profile]['from_dir'], file)
        
        if (not os.path.exists(to_dir)):
            print "making directory", to_dir, "..."
            os.mkdir(to_dir, 0755) 
            
    # if the to_file does not exist..
        if (not os.path.isfile(to_file)):
            print from_file, to_file
    

class Operate(object):
    def __init__(self, name):
        pass
    
    def sync():
        pass
        
        
#for in in all the files in the DCIM (/media/Nokia_N9/DCIM)
#  do
#    identify the year-month of the file (how?)
#    identify the filetype (mp4 or jpg)
#
#    check if the destination is available (/media/4444/Koti/201106)
#
#    if not available
#      mkdir the destination
#    else
#      cp/mv the files to the destination

# here is the test
