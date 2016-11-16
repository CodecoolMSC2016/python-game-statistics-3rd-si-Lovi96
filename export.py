import sys
from reports import *


def main(file_name, year, title):
    with open("export.txt", "w") as text_file:
        print("Amount of games: " + str(count_games(file_name)), file=text_file)
        print("Game from given year: " + str(decide(file_name, year)), file=text_file)
        print("Latest game in file: " + str(get_latest(file_name)), file=text_file)
        print("Number of title: " + str(get_line_number_by_title(file_name, title)), file=text_file)
        print("Top sold fps year: " + str(when_was_top_sold_fps(file_name)), file=text_file)
        print("List of genres: " + str(get_genres(file_name)), file=text_file)

main(sys.argv[1], sys.argv[2], sys.argv[3])
