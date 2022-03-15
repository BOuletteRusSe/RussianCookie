Dim Response

Response = MsgBox("This programm can destroy your computer, continue ?",4,"Warning")

If Response = vbYes Then
	CreateObject("WScript.Shell").Run "RussianCookie.exe" 
End If