#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib.pyplot as plt


def main():
    x_axis = []
    splitted_line = []
    values = []

    if len(sys.argv) < 2:
        print("Too few arguments\nCall instruction:\n./wykres.py name_of_file")
        exit(-1)

    for i in range(1,len(sys.argv)):
        x_axis = []
        values = []
        fl = open(sys.argv[i]+'.csv', 'r')
        fl.readline()
        
        for line in fl:
            splitted_line = line.split(',')
            splitted_line.pop(0)
            x_axis.append(int(splitted_line.pop(0)))
            values.append(np.average([float(i) for i in splitted_line]))

        plt.axis([0, x_axis[-1], np.min(values), 1.0])
        plt.plot(x_axis,values, label=sys.argv[i])
        plt.legend(loc="lower right")

    plt.xlabel("Rozegranych gier")
    plt.ylabel("Odsetek wygranych gier")
    plt.savefig('wykres.pdf')
    plt.close()
    print("Done")

if __name__ == '__main__':
    main()