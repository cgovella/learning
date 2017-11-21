import win32com.client as com
filepath = r"D:\PythonCode\Chapter2\CSVexamples\toolhire.xlsx"
fileopen = 1   # found by trial and error!
app = com.Dispatch("Excel.Application")
app.Visible = True
fd = app.FileDialog(fileopen)
fd.InitialFileName = filepath
fd.Title = "Open the toolhire spreadsheet"
if fd.Show() == -1:
   fd.Execute()
 