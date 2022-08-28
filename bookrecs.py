with open("booklist.txt", "r") as books:
    read_file = books.readlines()
    book_information = []
    for book in read_file:  # adds the book's title and author to a list
        book_information.append(tuple(book.strip().split(',')))
books.close()

with open("ratings.txt", "r") as ratings:
    names = []
    num_list = []
    count = 0
    for line in ratings:  # for each line in the file, add the reader's name and score to a list
        count += 1
        if count % 2 != 0:
            names.append(line.strip().lower())
        else:
            person_ratings = line.split()
            person_rating_list = []
            for i in person_ratings:
                person_rating_list.append(int(i))
            num_list.append(person_rating_list)
    ratings_dictionary = dict(zip(names, (num_list)))
ratings.close()

"""The function prompt the user to enter in a single line a firstname and lastname,
a symbol (>, <, =) and a number. The function returns a list of two values, and one integer value.
"""


def prompt_user():
    user_input = input("Enter a reader's name: ")
    user_input = [int(v) if v.isnumeric() else v for v in input().split()]
    print(user_input)

    # if len(user_input) == 3:
    #     for i in user_input:
    #         input_list.append(i)
    #     return input_list, number_input
    # elif len(user_input) == 4:
    #     for i in user_input:
    #         input_list.append(i)
    #     return input_list[0] + " " + input_list[1], input_list[2], number_input
    # else:
    #     print("Invalid input")
    #     return prompt_user()

    """Function takes a name, a symbol, and a number.
    The function returns a list of books including the book's title
    and author with the ratings by the reader.
    that matches the criteria from the books that reader has read.
    """


def find_books(name, symbol, number):
    books_read = []
    for k, v in ratings_dictionary.items():
        if k == name:
            for i in range(len(v)):
                if symbol == ">":
                    if v[i] > number:
                        books_read.append(book_information[i], v[i])
                elif symbol == "<":
                    if v[i] < number:
                        books_read.append(book_information[i], v[i])
                elif symbol == "=":
                    if v[i] == number:
                        books_read.append(book_information[i], v[i])
    books_read.sort(key=lambda x: x[2])
    return books_read


def main():
    name, symbol, number = prompt_user()
    books_read = find_books(name, symbol, number)
    for book in books_read:
        print(book)


# if __name__ == "__main__":
#     main()

prompt_user()
