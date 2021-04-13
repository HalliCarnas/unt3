# optie1
import subprocess
proc = subprocess.check_output("ipconfig" ).decode('utf-8')
print (proc)

# optie2
import os
os.system("ifconfig")