#!/usr/bin/env python

import Bot
import signal
import subprocess
import sys
import time

bot1 = subprocess.Popen("python Bot.py -p 43400 -r 1", shell=True)
bot2 = subprocess.Popen("python Bot.py -p 43401 -r 1", shell=True)
bot3 = subprocess.Popen("python Bot.py -p 43402 -r 1", shell=True)
bot4 = subprocess.Popen("python Bot.py -p 43403 -r 1", shell=True)
bot5 = subprocess.Popen("python Bot.py -p 43404 -r 1", shell=True)
bot6 = subprocess.Popen("python Bot.py -p 43405 -r 1", shell=True)
bot7 = subprocess.Popen("python Bot.py -p 43406 -r 1", shell=True)

def shutdown(signum, frame):
   print '\nInicializando bots de simulacion...\n'

   bot1.terminate()
   bot2.terminate()
   bot3.terminate()
   bot4.terminate()
   bot5.terminate()
   bot6.terminate()
   bot7.terminate()

   print 'Apagando bots de simulacion\n'
   sys.exit(0)

if __name__ == '__main__':
   signal.signal(signal.SIGINT, shutdown)

   print '\nUsar Ctrl+C para detener la simulacion\n'

   # keep the main thread running, can be stopped with ctrl+c
   while True:
      time.sleep(60)
