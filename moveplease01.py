#!/usr/bin/env python3

import shutil
import os

# start directory
os.chdir('/home/student/mycode')
# moves raynor from /home/student/mycode to /home/student/mycode/ceph_storage
shutil.move('raynor.obj', 'ceph_storage')
xname = input('What is the new name for kerrigan.obj? ')

#moves Kerrigan to the same location but with a new name, whatever you specify
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
print("Raynor says 'Oh Yeah!!!!'")

