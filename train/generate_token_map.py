import os, sys, numpy as np
import cPickle as p

sys.path.append("../nn/")
from InitParam import *
from ConstructNet import *
import gl
0
sys.path.append("../nn/")
from InitParam import *
from ConstructNet import *
import gl

np.random.seed(100)

tokenMap = dict()
tokenNum = 0

filedir = '../../subtree/'
flog = file('log.txt', 'w')
fileNum = 1
for onefile in os.listdir(filedir):
 fin = open( filedir + onefile)
 print "read file "+filedir + onefile
 while True:
   line = fin.readline().strip('\n\r')
   if not line:
       break
   fin.readline()
   for token in line.split(' '):
       if not tokenMap.has_key(token):
           tokenMap[token] = tokenNum
           tokenNum += 1
 fileNum += 1
 if fileNum%1000 == 0:
   #print fileNum
   fout= file('tokenMap.txt', 'w')
   flog.write(str(fileNum)+'\n')
   flog.flush()
   p.dump(tokenMap, fout)
   fout.close()
 fin.close()

fout = file('tokenMap.txt', 'wb')
import cPickle as p
p.dump(tokenMap, fout)
fout.close()