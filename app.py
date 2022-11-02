import os.path


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


FILE_NAME = "bestsellers.txt"
TITLE_INDEX = 0
AUTHOR_INDEX = 1
PUBLISHER_INDEX = 2
DATE_INDEX = 3
CATEGORY_INDEX = 4
MONTH_INDEX = 5
DAY_INDEX = 6
YEAR_INDEX = 7
book_lists = []


def show_filter_books(book_lists):
    for book in book_lists:
        print('{0}, by {1} ({2})'.format(
            book[TITLE_INDEX], book[AUTHOR_INDEX], book[DATE_INDEX]))


def build_book_lists():
    file_content = open(FILE_NAME, "r")
    book_lists = []

    for line in file_content:
        book = line.split("\t")
        book = [x.strip(' ') for x in book]
        m_d_y = book[DATE_INDEX].split("/")
        book.extend(m_d_y)
        # [title, author, publisher, date, category, month, date, year]
        book_lists.append(book)
    return book_lists


def get_book_between_year(lists, start, end):
    filtered_book_lists = []
    for book in lists:
        if (int(book[YEAR_INDEX]) >= start and int(book[YEAR_INDEX]) <= end):
            filtered_book_lists.append(book)
    return filtered_book_lists


def get_book_by_month_year(lists, month=0, year=0):
    filtered_book_lists = []
    for book in lists:
        if (int(book[MONTH_INDEX]) == month and int(book[YEAR_INDEX]) == year):
            filtered_book_lists.append(book)
    return filtered_book_lists


def get_book_by_author_name(lists, name):
    filtered_book_lists = []
    for book in lists:
        if (name in book[AUTHOR_INDEX].lower()):
            filtered_book_lists.append(book)

    return filtered_book_lists


def get_book_by_title(lists, title):
    filtered_book_lists = []
    for book in lists:
        if (title in book[TITLE_INDEX].lower()):
            filtered_book_lists.append(book)

    return filtered_book_lists


def main():
    if os.path.isfile(FILE_NAME):
        book_lists = build_book_lists()
        alive = True
        message = """
      What would you like to do?
      1: Look up year range
      2: Look up month/year
      3: Search for author
      4: Search for title
      Q: Quit

      """
        while (alive):
            print(message)
            command = input()
            if command == "1":
                start_year = int(input("Enter beginning year: "))
                end_year = int(input("Enter ending year: "))
                filtered_book_lists = get_book_between_year(
                    book_lists, start_year, end_year)

                if len(filtered_book_lists) > 0:
                    print(
                        'All titles between {0} and {1}:\n'.format(start_year, end_year))
                    show_filter_books(filtered_book_lists)
                else:
                    print(
                        'No books found between {0} and {1}'.format(start_year, end_year))
            elif command == "2":
                month = int(input("Enter month (as a number, 1-12): "))
                if (month > 12 or month < 1):
                    print("Month should be 1-12")
                    continue
                year = int(input("Enter year: "))

                filtered_book_lists = get_book_by_month_year(
                    book_lists, month, year)

                if len(filtered_book_lists) > 0:
                    print('All titles in month {0} of {1}:\n'.format(
                        month, year))
                    show_filter_books(filtered_book_lists)
                else:
                    print('No books found in month {0} of {1}'.format(
                        month, year))
            elif command == "3":
                author_name = input(
                    "Enter an author's name (or part of a name): ")
                filtered_book_lists = get_book_by_author_name(
                    book_lists, author_name)

                if len(filtered_book_lists) > 0:
                    print('All books by author name:\n')
                    show_filter_books(filtered_book_lists)
                else:
                    print('No books found for {0}'.format(author_name))
            elif command == "4":
                book_title = input("Enter a title (or part of a title): ")
                filtered_book_lists = get_book_by_title(
                    book_lists, book_title)

                if len(filtered_book_lists) > 0:
                    print('All books by book title:\n')
                    show_filter_books(filtered_book_lists)
                else:
                    print('No books found for {0}'.format(book_title))
            elif (command == "q" or command == "Q"):
                print("Process end, Thank you")
                alive = False

    else:
        print("bestsellers.txt file not exist in the directory")


if __name__ == "__main__":
    print(bcolors.OKCYAN +
          "Warning: No active frommets remain. Continue?" + bcolors.OKCYAN)

    main()
