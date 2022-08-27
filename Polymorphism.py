"""
Exercise 1
Use the Lottery class to the left as the parent class.
Create the PowerBall class as a child class of Lottery. 
Override the shuffle method so that it returns a list of six random integers between 1 and 99.
"""

import random


class Lottery:
    def shuffle(self):
        results = []
        for i in range(5):
            results.append(random.randint(1, 20))
        return results


class PowerBall(Lottery):
    def shuffle(self):
        results = []
        for i in range(6):
            results.append(random.randint(1, 99))
        return results


"""
Exercise 2"""


class Airplane:
    def __init__(self, first_class, business_class, coach):
        self.first_class = first_class
        self.business_class = business_class
        self.coach = coach

    def total(self):
        return self.first_class + self.business_class + self.coach


class Train:
    def __init__(self, car1, car2, car3, car4, car5):
        self.car1 = car1
        self.car2 = car2
        self.car3 = car3
        self.car4 = car4
        self.car5 = car5

    def total(self):
        return self.car1 + self.car2 + self.car3 + self.car4 + self.car5


def passengers(obj):
    print(f'There are {obj.total()} passengers on board.')


"""
Exercise 3"""


class Characters:
    def __init__(self, phrases):
        self.phrases = phrases

    def total_characters(self):
        total = 0
        for phrase in self.phrases:
            total += len(phrase)
        return total

    def __gt__(self, obj):
        return self.total_characters() > obj.total_characters()

    def __lt__(self, obj):
        return self.total_characters() < obj.total_characters()

    def __eq__(self, obj):
        return self.total_characters() == obj.total_characters()


"""
Exercise 4"""


class Median:
    def calculate_median(self, n1, n2, n3=None, n4=None, n5=None):
        if n3 is not None and n4 is not None and n5 is not None:
            numbers = [n1, n2, n3, n4, n5]
        elif n3 is not None and n4 is not None:
            numbers = [n1, n2, n3, n4]
        elif n3 is not None:
            numbers = [n1, n2, n3]
        else:
            numbers = [n1, n2]

        numbers.sort()
        median_index = len(numbers) // 2
        if len(numbers) % 2 == 0:
            median = (numbers[median_index] + numbers[median_index - 1]) / 2
        else:
            median = numbers[median_index]
        return median


"""
Exercise 5"""
source_file = '/home/codio/workspace/code/polymorphism/text_1_exercise5.txt'
answer_file = '/home/codio/workspace/code/polymorphism/answer_exercise5.txt'


class Substitute:
    def __init__(self, source_file, answer_file):
        self.source_file = source_file
        self.answer_file = answer_file
        self.words = None

    def string_to_list(self):
        '''Read text file, turn it into a
        2D list of words for each line'''
        words = []
        with open(self.source_file, 'r') as file_object:
            lines = file_object.read().split('\n')
            for line in lines:
                words.append(line.split())
        self.words = words

    def list_to_string(self):
        '''Convert 2D list back into a 
        string with newline characters'''
        lines = []
        for line in self.words:
            lines.append(' '.join(line))
        string = '\n'.join(lines)
        self.words = string

    def swap_words(self):
        self.string_to_list()
        for line in self.words:
            for i in range(len(line)):
                if (i + 1) % 5 == 0:
                    word = line[i]
                    line[i] = 'HELLO'
        self.list_to_string()


class Stars(Substitute):
    def swap_words(self):
        self.string_to_list()
        for line in self.words:
            for i in range(len(line)):
                if (i + 1) % 3 == 0:
                    word = line[i]
                    line[i] = '*' * len(word)
        self.list_to_string()
        file = open(self.answer_file, 'w')
        file.writelines(self.words)
        file.close()


s = Stars(source_file, answer_file)
s.swap_words()
