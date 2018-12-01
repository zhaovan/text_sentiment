import json
import re

file_d = '../data/drunk.json'
file_s = '../data/sober.json'

drunk = []
sober = []

with open(file_d, 'r') as ifile:
    drunk = json.load(ifile)

with open(file_s, 'r') as ifile:
    sober = json.load(ifile)

