import random
import string
def p(n):
  print(f'Your password is : {n}')
sym='!@#$%^&*<>?+'
while True:
  print('------------------------PASSWORD GENERATION------------------------')
  l=int(input('Enter the length of the password to generate : '))
  print('_______________________________________________________________________')
  print('Choose one of the below options to generate password you decired...')
  print('1.The password should only contains letters.')
  print('2.The password should only contains numbers.')
  print('3.The password should only contains symbols(! @ # $ % ^ & * < > ? +).')
  print('4.The password should contains both letters and numbers.')
  print('5.The password should contains both letters and symbols.')
  print('6.The password should contains both numbers and symbols.')
  print('7.The password should contains all letters,numbers and symbols.')
  print('8.EXIT')
  print('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
  ch=int(input('Enter your choice from the above options : '))
  if ch==1:
      password=''
      s=string.ascii_letters
      for i in range(l):
        password+=random.choice(s)
      p(password)
  elif ch==2:
      password=''
      s=string.digits
      for i in range(l):
        password+=random.choice(s)
      p(password)
  elif ch==3:
      password=''
      s=sym
      for i in range(l):
        password+=random.choice(s)
      p(password)
  elif ch==4:
      password=''
      s=string.ascii_letters+string.digits
      for i in range(l):
        password+=random.choice(s)
      p(password)
  elif ch==5:
      password=''
      s=string.ascii_letters+sym
      for i in range(l):
        password+=random.choice(s)
      p(password)
  elif ch==6:
      password=''
      s=string.digits+sym
      for i in range(l):
        password+=random.choice(s)
      p(password)
  elif ch==7:
      password=''
      s=string.ascii_letters+string.digits+sym
      for i in range(l):
        password+=random.choice(s)
      p(password)
  elif ch==8:
      print('EXITING.......')
      break
  else:
      print('You are entered an invalid input...!\nPlease try again.....')
