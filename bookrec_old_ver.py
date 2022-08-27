from numpy import dot
from operator import itemgetter

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
    ratings_dictionary = dict(zip(names, num_list))
ratings.close()


def dotprod(x, y):
    """takes two reader's score, and returns a single
    number representing the affinity score between the two readers
    """
    reader_ratings = ratings_dictionary[x]
    compared_reader_ratings = ratings_dictionary[y]
    affinity_score = dot(reader_ratings, compared_reader_ratings)
    return affinity_score


def friends(name):  # takes a reader's name, and returns a list of two readers
    score_list = []
    new_name_list = []
    two_friends = []
    for key in ratings_dictionary:  # for each reader, add the reader's name and score to a list
        new_name_list.append(key)
        score_list.append(dotprod(name, key))
    score_dictionary = dict(zip(new_name_list, score_list))
    del score_dictionary[name]
    maximum_one = max(score_dictionary, key=score_dictionary.get)
    two_friends.append(maximum_one)
    del score_dictionary[maximum_one]
    maximum_two = max(score_dictionary, key=score_dictionary.get)
    two_friends.append(maximum_two)
    two_friends.sort()
    return two_friends


def recommend(name):  # takes a reader's name, and returns a list of books
    books_not_read = []  # a list of the books the reader hasn't read
    a_dictionary = dict(zip(book_information, ratings_dictionary[name]))
    for k, v in a_dictionary.items():  # if the reader hasn't read the book, add it to the list
        if v == 0:
            books_not_read.append(k)
    bookrec = []
    b_dictionary = dict(
        zip(book_information, ratings_dictionary[friends(name)[0]]))
    for i, j in b_dictionary.items():  # for each book the first reader has read, add the book and the score to a dictionary
        if j == 3:
            bookrec.append(i)
    c_dictionary = dict(
        zip(book_information, ratings_dictionary[friends(name)[1]]))
    for l, m in c_dictionary.items():  # if the reader has read the book, add it to the list
        if m == 3:
            if m not in bookrec:
                bookrec.append(l)
        elif m == 5:
            if m not in bookrec:
                bookrec.append(l)
        book_for_reader = []
        for b in books_not_read:  # if the reader hasn't read the book, add it to the list
            if b in bookrec:
                book_for_reader.append(b)
    author_name_list = []
    book_list = []
    author_name_tuple = []
    author_name_title = []
    for n in book_for_reader:
        author_name_list.append(tuple((n[0].split())))
    for o in author_name_list:
        name_book_tuple = []
        name_book_tuple.append(o[-1])
        name_book_tuple.append(' '.join(o[0:-1]))
        author_name_tuple.append(tuple(name_book_tuple))
    for p in book_for_reader:
        title = []
        title.append(p[1])
        book_list.append(tuple(title))
    for q in range(0, len(author_name_tuple)):
        author_name_title.append(author_name_tuple[q] + book_list[q])
    sorted_author_book = sorted(author_name_title, key=itemgetter(0, 1, 2))
    final_recommendations = []
    tuple_names = []
    for r in sorted_author_book:
        t = r[0:-1]
        flipped = tuple(reversed(t))
        tuple_names.append(flipped)
    for s in tuple_names:
        kit = []
        kit.append(' '.join(s[0:]))
        final_recommendations.append(tuple(kit))
    sorted_title = []
    ready_to_print = []
    for t in sorted_author_book:
        title_two = []
        title_two.append(t[-1])
        sorted_title.append(tuple(title_two))
    for u in range(0, len(final_recommendations)):
        ready_to_print.append(final_recommendations[u] + sorted_title[u])
    return ready_to_print


def main():

    while True:  # asks the user for a reader's name, and prints the reader's recommendations
        reader = input("Enter a reader's name: ")
        if reader not in names:
            print(f"No such reader {reader}")
        else:
            friend_list = friends(reader)
            print(
                f"Recommendations for {reader} from {friend_list[0]} and {friend_list[1]}:")
            rec_books = recommend(reader)
            for book in rec_books:
                print(f"\t{book[0]}, {book[1]}")


if __name__ == '__main__':
    main()
