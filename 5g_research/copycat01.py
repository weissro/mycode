#!/usr/bin/env python3

import shutil
import os
#script will start from the mycode directory
os.chdir("/home/student/mycode/")
# copies the file from that file to a new name
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
# backs up 5g_research in a new directory /home/student/mycode/5g_research_backup
shutil.copytree("5g_research/", "5g_research_backup/")

