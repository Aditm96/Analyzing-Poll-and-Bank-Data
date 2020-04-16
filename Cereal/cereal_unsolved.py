import os
import csv

cereal_csv = os.path.join("..","Cereal", "Resources", "cereal.csv")
with open(cereal_csv, 'r') as file:
   csv_reader=csv.reader(file)
   next(csv_reader, None)
   for row in csv_reader:
        fiberCount = row[8]
        cereal = row[0]
        if float(fiberCount) >= 5:
            print(f'{cereal} has a fiber count of {fiberCount}.')
             
    
    
    
    