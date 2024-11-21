import random
import os
import sys

#link to my repo
dir = '/storage/emulated/0/MHDM_git'
Healthcheck_libs = os.path.join(dir, 'Health_Check')
sys.path.append(Healthcheck_libs)

from logger_class import ScriptLogger


rand_test = random.random()
print(rand_test)