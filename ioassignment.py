#!/usr/bin/env python3

import csv
import json 
import yaml


def make_json(file_name_csv):
    file_name_json = 'input.json'
    data = dict() 

    with open(file_name_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    with open(file_name_json, 'w') as jsonfile:
        json.dump(rows, jsonfile)

def make_yaml(file_name_csv):
    with open(file_name_csv, 'r') as csvfile:
        next(csvfile)
        freader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        yaml_file = open('input.yaml', 'w')
        for i, row in enumerate(freader):
            csv_content = ' '.join(row)
            csv_content = csv_content.split(',')
            yaml_file.write('person:\n')
            yaml_file.write('   fname: %s\n' % csv_content[0])
            yaml_file.write('   lname: %s\n' % csv_content[1])
            yaml_file.write('   month: %s\n' % csv_content[2])
            yaml_file.write('   year: %s\n' % csv_content[3])
            yaml_file.write('   fcolor: %s\n' % csv_content[4])
            yaml_file.write('   fmovie: %s\n' % csv_content[5])
        yaml_file.close()
        
if __name__ == '__main__':
    file_name_csv = 'input.csv'
    #make_json(file_name_csv)
    make_yaml(file_name_csv)
