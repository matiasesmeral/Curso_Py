
#importar modulo csv, definir una funcion que lea el css, convertirlo en dictionario y mostrarlo.

import csv
from email import header

def readCsv():
    with open("./archivosPy/data.csv","r") as readcsv:
        reader = csv.reader(readcsv,delimiter=',');
        header = next(reader)
        data = [];

        for row in reader:
            indexation = zip(header,row);
            datadictionary = {key:value for (key,value) in indexation};
            #col = list(filter(lambda x: x["country"]=='Colombia',datadictionary))
            data.append(datadictionary);
            
        return data;        


if __name__ == "__main__":

    lis = readCsv()
    
    au = list(filter(lambda item: item['Country']=='Colombia',lis))
    print(au)
    
   # print(lis)
