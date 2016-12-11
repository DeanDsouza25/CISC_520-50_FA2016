'''
Created on Nov 29, 2016

@author: demon
'''

nfile = open('C:/Users/demon/OneDrive/Documents/GitHub/CISC_520-50_FA2016/Project/data/AllAuthors.txt','r')
dfile = open('C:/Users/demon/OneDrive/Documents/GitHub/CISC_520-50_FA2016/Project/data/AllText.txt','r')

for author in nfile:
    print author
    
#for line in dfile:
#    print line

nfile.close()
dfile.close()