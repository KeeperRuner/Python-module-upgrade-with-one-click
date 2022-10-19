import os,time

allPackage=os.popen('pip list')

allPackage=allPackage.read()

allPackage=allPackage.split('\n')

allPackage=[pkg.split(' ')[0] for pkg in allPackage]

for pkg in allPackage:
    if pkg!='':
        print(os.popen('pip install -U {}'.format(pkg)).read())
        time.sleep(3)