import xlrd
import csv


def csv_from_excel(folder, excel_name, csv_name):
    wb = xlrd.open_workbook(folder + excel_name + '.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open(folder + csv_name + '.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

# Declarando Variáveis
folder = 'G:\\GitHub\\diggi-teste\\estudo_de_caso_diggi\\dados\\'
excel_name = 'Base teste_Cientista de Dados_diggi'
csv_name = 'base_teste'

# Executando a função de conversão
csv_from_excel(folder, excel_name, csv_name)