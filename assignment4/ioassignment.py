#!/usr/bin/env python3

import csv
import json 
import yaml
import tablib

def csv_to_json(csv_file):
    json_file = 'input.json'
    data = dict() 

    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    with open(json_file, 'w') as jsonfile:
        json.dump(rows, jsonfile)

def csv_to_yaml(csv_file):
    with open(csv_file, 'r') as csvfile:
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

def data():
    d = tablib.Dataset()
    d.append_col(['theo', 'simon', 'roger', 'jasper'])
    d.append_col(['student', 'statistician', 'analyst', 'baker'])
    d.headers = ['fname', 'occupation']
    return d

def make_csv(data):
    with open('output.csv', 'w') as newcsv:
        newcsv.write(data.csv)

def make_json(data):
    with open('output.json', 'w') as newjson:
        newjson.write(data.json)

def make_yaml(data):
    with open('output.yaml', 'w') as newyaml:
        newyaml.write(data.yaml)

if __name__ == '__main__':
    csv_file = 'input.csv'
    csv_to_json(csv_file)
    csv_to_yaml(csv_file)
    data = data()
    make_csv(data)
    make_json(data)
    make_yaml(data)
