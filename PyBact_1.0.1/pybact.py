#############################################################################################################
# PyBact, Version 1.0, October 2008.                                                                        #
# The software can be downloaded from http://pybact.sf.net/                                                 #
# It is available under the terms of the Open Software License 3.0 (OSL 3.0).                               #
# Any derivatives of this work must retain this header information at the top of the code.                  #
#                                                                                                           #
# Chanin Nantasenamat, Likit Preeyanon, Chartchalerm Isarankura-Na-Ayudhya and Virapong Prachayasittikul*   #
# Department of Clinical Microbiology                                                                       #
# Faculty of Medical Technology                                                                             #
# Mahidol University                                                                                        #
# *E-mail: mtvpr@mahidol.ac.th                                                                              #
#############################################################################################################

import random
import os
import sys
import tqdm
from tqdm import tqdm

# Generate function
def generate(datafile,target, strains):
    
    f = open(datafile, 'r').readlines() #read data from a file
    
    data = []
    for i in f:
        column = i.split('\t')  #split data
        data.append(column)     #append each new row in data[]

    ignored = []
    row = len(data)
    
    for i in range(1,len(column)):
        check_zero = 0
        for j in range(1,row):
            check_zero += int(data[j][i])
        if check_zero == 0:
            ignored.append(i)
            
    f[0] = f[0].replace('\n','')
    title = f[0].split('\t')

    newdata = []

    for v in tqdm(range(1,row), desc="Processing Organisms"):        #number of organisms
        organism_name = [data[v][0]]*strains    #create list of name
        org = []
        org.append(organism_name)
        for j in range(1,len(column)):          #number of biochemical tests
            if j not in ignored:
                biochem = ['0']*strains         #set biochem negative for every strain first
                pos_percent = max(0, min(100, int(data[v][j])))  #get the percentage of positive result
                random_times = int((pos_percent * strains) / 100)
                if random_times == 0 :
                    org.append(biochem)
                else:
                    # Mutate `biochem` so that its sum is equal to `random_times`
                    for i in range(random_times):
                        r = random.randrange(strains)
                        while biochem[r] == '1':
                            r = random.randrange(strains)       #random again if found the positive one
                        if biochem[r] == '0': biochem[r] = '1'  #change negative result to positive
                    org.append(biochem)                         #append biochemical test to org[]
        newdata.append(org)                                     #add complete orgranism to newdata[]

    newfile = open(target,'w')      #open file to write the output
    for n in range(1,len(title)):   #write the column title
        if n not in ignored: newfile.write(title[n]+'\t')
    newfile.write(title[0]+'\n')    #move name to the last
    
    for k in tqdm(range(len(newdata)), desc="Writing Data"):   #write data
        for i in range(strains):
            for j in range(1, len(newdata[k])):  # Use len(newdata[k]) instead of len(org)
                newfile.write(newdata[k][j][i] + '\t')
            newfile.write(newdata[k][0][i])
            newfile.write('\n')
    newfile.close()
    return 0
            
        
if __name__=='__main__':

    if len(sys.argv) > 1:
        datafile = sys.argv[1]
        target   = sys.argv[2]
        strains   = int(sys.argv[3])
        
        targetfile = generate(datafile,target,strains)
    else : print("The format for running PyBact is:\n   pybact [input text file] [output text file] [number of strain]\n   e.g. pybact input.txt output.txt 100")