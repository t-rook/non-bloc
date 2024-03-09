import sys
import select
import time
import turtle

time.sleep(3)
t = turtle.Turtle()
t.pu()
t.goto(-100,0)
t.pd()
ang = 2.5


def something(ppenD):
  if ppenD:
    t.pd()
    t.right(2.5)
    posits.append(t.pos())
    t.fd(1)
  else:
    t.pu()
    t.right(2.5)
    t.fd(1)
  if t.pos() in posits[:-1]:
    quit()

  

counter = 0
counter2 = 0
posits = []
while True:
  if t.pos() in posits:
    quit()
  penD = False
  counter +=1
  if counter % 20 == 0:
    penD = True
    counter2 +=1
    if counter2 % 10 != 0:
      counter -=1
  while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
    something(penD)
    print(',')
  else:
    if penD:
      t.pd()
      posits.append(t.pos())
      t.fd(1)
      print('.')
    else:
      t.pu()
      t.fd(1)
      print('.')

  
