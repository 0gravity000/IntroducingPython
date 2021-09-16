from datetime import date
import multiprocessing

def now(seconds):
  from datetime import datetime
  from time import sleep
  sleep(seconds)
  print('wait', seconds, 'seconds, time is', datetime.utcnow())

if __name__ == '__main__':
  import random
  for n in range(3):
    #seconds = random.random()
    seconds = random.randint(1, 5)
    proc = multiprocessing.Process(target=now, args=(seconds,))
    proc.start()
