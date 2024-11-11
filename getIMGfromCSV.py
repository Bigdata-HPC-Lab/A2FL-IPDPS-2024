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
        # use csv and output image
        outFile = tmpFileName.replace("/csv/", "/img/")
        print("fileName is ", fileName)
        print("outfileName is ", outFile)
        
        data = pd.read_csv(fileName)  # csv file name

        # Extract the columns
        start = data['Start(s)']
        offset = data['Offset']

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.scatter(start, offset)  # Create a scatter plot
        plt.xlabel('Start (s)', fontname='Times New Roman')  # Using Times New Roman font
        plt.ylabel('Offset', fontname='Times New Roman')     # Using Times New Roman font
        # plt.title('Start vs Offset Plot', fontname='Times New Roman')  # Using Times New Roman font 
        plt.savefig(outFile, format='jpg', dpi=300)  # Adjust 'dpi' for the image resolution

