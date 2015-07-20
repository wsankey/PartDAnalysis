'''
The prupose of this program is to read
and write the large XLSX files in my directory
into CSVs.
'''
import os
import csv
import xlrd

path =  "E:\Part D Public Data"
files = os.listdir(path)
files_xlsx = [f for f in files if f[-4:] == 'xlsx']
print files_xlsx
counter = 0
for x in range(0,1):
    counter+=1
    wb = xlrd.open_workbook(path + '\\' + files_xlsx[x])
    sh = wb.sheet_by_index(0)
    your_csv_file = open(path + "partd_csv" + str(counter) +".csv", "wb")
    wr = csv.writer(your_csv_file)

    print "Beginning to write now..."
    for rownum in xrange(sh.nrows):
          wr.writerow(sh.row_values(rownum))

    your_csv_file.close()
    print "Saved the " + str(counter) + " one!"
    
print "Successfully saved all XLSX as CSV!"
