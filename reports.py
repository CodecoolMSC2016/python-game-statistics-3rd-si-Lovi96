import csv


def count_games(file_name):
    '''Counts the number of games in the given file.'''
    csv_file = open(file_name, 'r')
    csv_rows = []
    number = 0
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        csv_rows.append(row)
    for row in csv_rows:
        number += 1
    csv_file.close()
    return number


def decide(file_name, year):
    '''Returns true if there is a game with the given release year'''
    year = str(year)
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        if row[2] in year:
            csv_file.close()
            return True
    csv_file.close()
    return False


def get_latest(file_name):
    '''Gets the latest games name'''
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file, delimiter='\t')
    latest_year = 0
    for row in csv_reader:
        if latest_year < int(row[2]):
            latest_year = int(row[2])
    csv_file.close()
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        if str(latest_year) in row[2]:
            game_name = row[0]
            csv_file.close()
            return game_name


def count_by_genre(file_name, genre):
    '''Counts the occurencies of the given genre'''
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file, delimiter='\t')
    counter = 0
    for row in csv_reader:
        if row[3] in genre:
            counter += 1
    csv_file.close()
    return counter


def get_line_number_by_title(file_name, title):
    '''Gets the line number of given title'''
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file, delimiter='\t')
    counter = 1
    for row in csv_reader:
        if row[0] != title:
            counter += 1
        else:
            csv_file.close()
            return counter


def when_was_top_sold_fps(file_name):
    '''Gets the top sold fps year of release'''
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file, delimiter='\t')
    fps_name = ""
    fps_year = 0
    fps_sold = 0
    for row in csv_reader:
        if row[3] == "First-person shooter":
            if float(row[1]) > fps_sold:
                fps_sold = float(row[1])
                fps_year = int(row[2])
    csv_file.close()
    return fps_year


def get_genres(file_name):
    '''Gets all the genres from the given file and returns them as a list.
    Currently sorted() bugs out and returns the items in the wrong alphabetical order.'''
    csv_file = open(file_name, 'r')
    csv_reader = csv.reader(csv_file, delimiter='\t')
    list_of_genres = []
    for row in csv_reader:
        if row[3] not in list_of_genres:
            list_of_genres.append(row[3])
    csv_file.close()
    # print(sorted(list_of_genres))
    return sorted(list_of_genres)
    # Report functions
