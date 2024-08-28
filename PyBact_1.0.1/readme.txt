*************************************************************************************
PyBact, Version 1.0, October 2008.
The software is available at http://pybact.sf.net/

Chanin Nantasenamat 1,2,*, Likit Preeyanon 1,2, Chartchalerm Isarankura-Na-Ayudhya 2 and Virapong Prachayasittikul 2
1 Center of Data Mining and Biomedical Informatics,
2 Department of Clinical Microbiology and Applied Technology,
Faculty of Medical Technology
Mahidol University
*E-mail: mtcnt@mahidol.ac.th
*************************************************************************************

PyBact is a program that is designed to generate simulated data set for bacterial identification. The algorithm generates simulated data which derives its information from frequency tables of diagnostic microbiology textbook. The algorithm is flexible as it can mimic the dynamic nature of naturally occuring bacterias by randomly generating positive/negative biochemical test results in a probabilistic manner which accurately reflects the unique biochemical profile of each species. 

The software is distributed under the terms of the Open Software License 3.0 (OSL 3.0). For more information, please refer to http://www.opensource.org/licenses/osl-3.0.php

The program was written in Python and compiled with py2exe into an executable file that is Windows compatible. It may be compiled to work with other operating system using the provided source code. The source code may be modified under the condition that the header information containing author information is left intact at the top of the code.

This release is comprised of the following files:
bz2.pyd
library.zip
MSVCR71.dll
pybact.exe           <----- The PyBact executable 
pybact.py             <----- The source code of PyBact written in Python
python25.dll
readme.txt
unicodedata.pyd
vibrio.txt              <----- An input file for Vibrio species
w9xpopen.exe

Usage:
Under command prompt, use the following command

        pybact [input file] [output file] [number of isolates]

Therefore, to create a data matrix for Vibrio species using 100 isolates per species, type in the following command

        pybact vibrio.txt vibrio-output.txt 100

The output file is tab delimited and can readily be used as data set for machine learning analysis. The program is flexible in which the number of biochemical tests it can handle are automatically determined from the input file. In addition, the number of isolates can be adjusted to produce small or large data sets as desired.