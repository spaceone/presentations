import os

os.setuid(0)
os.system("cd /var/buildsystem/mypackage && make &> /dev/null")
