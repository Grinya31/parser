import xlsxwriter
from parser_new import category_tov

workbook = xlsxwriter.Workbook('Parser01.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': 1})


row=0
col=0
c=1

for key,values in category_tov.items():
    worksheet.write_string(row,col, key,bold)
    for key_a,value_a in values.items():
        c+=1
        worksheet.write_string(row+c,col,key_a,bold)
        row+=1    
        worksheet.write(row+c,col,"Название")
        worksheet.write(row+c,col+1,"Ссылка")
        worksheet.write(row+c,col+2,"Цена")
        for i in value_a:
            row+=1
            worksheet.write_string(row+c,col,i[0])
            worksheet.write_string(row+c,col+1,i[1])
            worksheet.write_string(row+c,col+2,i[2])
            
workbook.close()






