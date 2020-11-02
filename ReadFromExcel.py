import xlrd
import mysql.connector

class ExcelToMySQl:

    def saveToDB(self,dbRecord):
        #print(dbRecord)
        cnx = mysql.connector.connect(user='root', password='Python@2020',
                                      host='127.0.0.1',
                                      database='pythonbatch3')
        dbVals=""
        for i in dbRecord:
            dbVals+="'"+str(i)+"',"
        queryString="insert into Excel values ("+dbVals
        inputStr=queryString[:-1]+")"
        print(inputStr)
        insertcursor=cnx.cursor()
        insertcursor.execute(inputStr)
        cnx.commit()


    def read_values_from_excel(self):
         filePath="C:\\Users\\navee\\OneDrive\\Desktop\\tasks.xls"
         wb = xlrd.open_workbook(filePath)
         sheet = wb.sheet_by_index(0)
         x=sheet.cell_value(0, 0)
         print(sheet.nrows)
         for i in range(1,sheet.nrows):
           self.saveToDB(sheet.row_values(i))

obj=ExcelToMySQl()
obj.read_values_from_excel()