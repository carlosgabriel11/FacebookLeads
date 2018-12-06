import win32com.client
xl=win32com.client.Dispatch("Excel.Application")
xl.Visible=True
xl.Workbooks.Open(Filename=".\\MasterCompleta.xls",ReadOnly=1)
xl.Application.Run("UnirPlanilhas")
