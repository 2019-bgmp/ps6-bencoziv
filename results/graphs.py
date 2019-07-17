#!/usr/bin/env python3
import glob
import matplotlib.pyplot as plt
for filename in glob.glob('*.txt'):
    with open (filename,'r') as fh:
        x=[]
        y=[]
        for line in fh:
            if line[0].isdigit():
                a=int(line.split('\t')[0])
                b=int(line.split('\t')[1])
                x.append(a)
                y.append(b)
            else:
                continue
    y = y
    x = x
    plt.scatter(x, y)
    plt.ylabel('Count')
    plt.xlabel('Bin ')
    plt.title('Bin Vs Count'+str(filename));
    plt.show()
