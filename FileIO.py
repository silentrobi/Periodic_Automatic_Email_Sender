from datetime import datetime
import csv

'''
FileIO class creates CSV file. More methods can be added to this class like 'createPdfFile() 
'''
class FileIO:
    def createCSVFile(self, jsonData, addtag): # this method can be modified to make variable number of fields
        fileName= datetime.now().strftime("%d-%m-%Y-%H-%M-%S")+"-"+addtag+ ".csv"
        filePath= "./files/"+fileName
        print(fileName)
        # Bug(26/08/2019): UnicodeEncodeError: 'charmap' codec can't
        # encode character '\u0131' in position 1: character maps to <undefined>
        #fix(26/08/2019): need to specify encode to utf-8 in open () method
        with open(filePath,'w+', encoding='utf-8-sig') as file:

                print("HI")
                fieldNames = ['Item', 'Office', 'Week']
                theWriter= csv.DictWriter(file,fieldnames= fieldNames)
                #write header name
                theWriter.writeheader()
                for item in jsonData:
                    # add row to CSV file
                    theWriter.writerow({'Item': item['item'], 'Office':item['office'], 'Week':item['week']})
                file.close()

        return fileName


