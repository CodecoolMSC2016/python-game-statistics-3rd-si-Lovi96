import sys
from reports import *


def main(file_name, title):
    with open("export.txt", "w") as text_file:
        print("Most played game: " + str(get_most_played(file_name)), file=text_file)
        print("All sales: " + str(sum_sold(file_name)), file=text_file)
        print("Average of all sales: " + str(get_selling_avg(file_name)), file=text_file)
        print("Longest title: " + str(count_longest_title(file_name)), file=text_file)
        print("Average of all release dates: " + str(get_date_avg(file_name)), file=text_file)
        print("Given games properties: " + str(get_game(file_name, title)), file=text_file)

main(sys.argv[1], sys.argv[2])
