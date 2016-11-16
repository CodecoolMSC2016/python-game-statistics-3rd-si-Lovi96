import csv
import math


def get_most_played(file_name):
    '''Gets the most played games name'''
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file, delimiter='\t')
    played = 0
    game = ""
    for row in csv_reader:
        if float(row[1]) > float(played):
            played = row[1]
            game = row[0]
    csv_file.close()
    return game


def sum_sold(file_name):
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file, delimiter='\t')
    number1 = 0.0
    for row in csv_reader:
        number1 = number1 + float(row[1])
    csv_file.close()
    return number1


def get_selling_avg(file_name):
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file, delimiter='\t')
    number1 = 0.0
    rownum = 0.0
    for row in csv_reader:
        number1 = float(number1) + float(row[1])
        rownum += 1
    number1 = float(number1) / float(rownum)
    csv_file.close()
    return float(number1)


def count_longest_title(file_name):
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file, delimiter='\t')
    title_length = 0
    for row in csv_reader:
        if len(row[0]) > title_length:
            title_length = len(row[0])
    csv_file.close()
    return title_length


def get_date_avg(file_name):
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file, delimiter='\t')
    years = 0
    counter = 0
    for row in csv_reader:
        years = years + int(row[2])
        counter += 1
    years = years / counter
    csv_file.close()
    return math.ceil(years)


def get_game(file_name, title):
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file, delimiter='\t')
    whole_row = []
    for row in csv_reader:
        if row[0] == title:
            whole_row.append(row[0])
            whole_row.append(float(row[1]))
            whole_row.append(int(row[2]))
            whole_row.append(row[3])
            whole_row.append(row[4])
    return whole_row
