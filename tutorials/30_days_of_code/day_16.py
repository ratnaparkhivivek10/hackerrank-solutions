#!/bin/python3

import sys


S = input().strip()

try:
    print(int(S))
except ValueError as e:
    print('Bad String')
