import pdb 
import sys 
import time
import datetime
import pandas
import numpy
import math
import pandas as pd
import os
import re
import datetime


if __name__ == '__main__':
        fileName = str(sys.argv[1])
        tmpFileName = fileName
        # use darsha log (txt) and output csv for all file offsets (only write in this case)
        outFile = tmpFileName.replace("/txt/", "/csv/")
        print("fileName is ", fileName)
        print("outfileName is ", outFile)
        
        # flag to start parsing
        posixFlag = 0
        # count to start
        cnt = 0


        # Module (0)    Rank (1)  Wt/Rd (2)  Segment (3)    Offset (4)   Length (5)   Start(s) (6)     End(s) (7)
        with open(outFile, 'w', encoding='utf-8') as outfile:
                outfile.write("Module    Rank  Wt/Rd  Segment          Offset       Length    Start(s)      End(s)\n")
                with open(fileName, 'r', encoding='utf-8') as infile:
                        for line in infile:
                                if "X_POSIX" in line and "write" in line:
                                        outfile.write(line)

