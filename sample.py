import os
#os.system('git --version')
a  = os.popen('git diff --name-only').readlines()
print(a)
if('sample.tex\n' in a):
  os.system('pdflatex /home/panja/Documents/GitHub/Latexx/sample.tex')
  os.system('git add sample.pdf sample.tex')
  os.system('git commit -m "Bot Committed"')
  os.system('git push --all')
else:
  print("No Changes, No Push")
#12665c8e2d657a42124b87a1bd01daef99f89868	
