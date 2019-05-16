from decimal import Decimal
import csv

def restorezeros(s):
    d, c = s.split('.')
    if len(c) == 0:
        return d + ".00"
    elif len(c) == 1:
        return d + "." + c + "0"
    else:
        return s
        

def collectcv(desc='0.06'):
    desc = Decimal(desc)
    FILENAME = "c:/Users/Heitor/Desktop/code/imagecaption/tab2.csv"

    cods = {}

    with open(FILENAME) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            cv = Decimal(row[8].replace(",", ".")) * 3 * (Decimal('1') - desc)
            strippedr = str(cv).rstrip('0')
            finalv = restorezeros(strippedr).replace(".", ",")
            cods[row[0]] = finalv
    return cods
