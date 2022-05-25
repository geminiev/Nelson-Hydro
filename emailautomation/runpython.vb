' Macro to open Python script with VBA

Sub RunPython()

Dim objShell As Object
Dim PythonExe, PythonScript As String

    Set objShell = VBA.CreateObject("Wscript.Shell")

    PythonExe = """C:\Users\ESankar\Anaconda3\python.exe"""
    PythonScript = "C:\Users\ESankar\gmail_to_outlook.py"

    objShell.Run PythonExe & PythonScript

End Sub
