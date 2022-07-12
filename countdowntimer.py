import time
def countdown(t):
  while t:
    mins,secs=divmod(t,60)
    timer='{:o2d}:{:02d}'.format(mins,secs)
    print(timer,end="\r")
    time.sleep(1)
    t-=1
  print("time's up")
t=input("enter the time (in secs):")
countdown(int(t))
