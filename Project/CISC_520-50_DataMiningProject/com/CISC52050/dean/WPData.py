'''
@author: Dean D'souza
'''
import csv

csvfile = open('C:/Users/demon/OneDrive/Documents/GitHub/CISC_520-50_FA2016/Project/data/FinalData.csv','r')

nfile = open('C:/Users/demon/OneDrive/Documents/GitHub/CISC_520-50_FA2016/Project/data/AllAuthors.txt','w')
dfile = open('C:/Users/demon/OneDrive/Documents/GitHub/CISC_520-50_FA2016/Project/data/AllText.txt','w')


reader = csv.DictReader(csvfile, dialect='excel', fieldnames=['sentiment', 'ID', 'Date', 'Query', 'author', 'content'])
for row in reader:
    print(row)
    nfile.write(row['author']+"\n")
    dfile.write(row['content']+" ")

nfile.close()
dfile.close()
csvfile.close()