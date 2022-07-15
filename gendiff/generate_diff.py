import argparse
import json


gendiff = argparse.ArgumentParser(prog='gendiff', description='Compares two configuration files\
     and shows a difference.')
gendiff.add_argument('first_file')
gendiff.add_argument('second_file')
gendiff.add_argument('-f', '--format', help='set format of output')
args = gendiff.parse_args()


def generate_diff(file_path1, file_path2):
     file1 = json.load(open(file_path1))
     file2 = json.load(open(file_path2))
     result = '{' + '\n'
     for i in file1.keys() & file2.keys():
          if file1[i] == file2[i]:
               result = result + '   ' + i + ': ' + str(file1[i]) + '\n'
          else:
               result = result + ' + ' + i + ': ' + str(file2[i]) + '\n'
               result = result + ' - ' + i + ': ' + str(file1[i]) + '\n'
     for i in file1.keys() - file2.keys():
          result = result + ' - ' + i + ': ' + str(file1[i]) + '\n'
     for i in file2.keys() - file1.keys():
          result = result + ' + ' + i + ': ' + str(file2[i]) + '\n'
     result = result + '}'
     return result
