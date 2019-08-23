from datetime import datetime
import csv
import os
class FileIO:
    def createCSVFile(self, jsonData):
        dirName= os.path.dirname(__file__)
        fileName= "./files/"+datetime.now().strftime("%d-%m-%Y-%H-%M-%S")+ ".csv"
        print(type(fileName))
        print(fileName)
        with open(fileName,'w+') as file:
            try:
                fieldNames = ['Item', 'Office', 'Week']
                theWriter= csv.DictWriter(file,fieldnames= fieldNames)
                #write header name
                theWriter.writeheader()
                for item in jsonData:
                    # add row to CSV file
                    theWriter.writerow({'Item': item['item'], 'Office':item['office'], 'Week':item['week']})

            except:
                print("IO error")

        return fileName
