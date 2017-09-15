#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Sep  2 00:09:06 2017

@author: Juan Antonio Barragán Noguera
@email : jabarragann@unal.edu.co

"""

import argparse


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))