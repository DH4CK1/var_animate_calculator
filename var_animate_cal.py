#!/bin/python2.7
import var_animate

animvar = var_animate.animvar()
animinput = var_animate.animinput()
banner = var_animate.banner('Calculator','Desta','1.0')

print(banner)
no1 = int(animinput.ask('Nomer1'))
opt = animinput.ask('Operator[+/-*]')
no2 = int(animinput.ask('Nomer2'))

if opt == "+":
   hasil = no1+no2
   print(animvar.true('Hasil: {}').format(hasil))
elif opt == '-':
   hasil = no1-no2
   print(animvar.true('Hasil: {}').format(hasil))
elif opt == '*':
   hasil = no1*no2
   print(animvar.true('Hasil: {}').format(hasil))
elif opt == '/':
   hasil = no1/no2
   print(animvar.true('Hasil: {}').format(hasil))
else:
   print(animvar.false('Sepertinya operator salah'))
