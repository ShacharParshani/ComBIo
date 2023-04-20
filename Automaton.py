import random
import Person
import time

class Automaton:
    def __init__(self, p, l, pros1, pros2, pros3, pros4, endGen):
        self.p = p
        self.l = l
        self.generation = 0
        self.endGen = endGen
        self.pros1 = pros1  # probabilities of s1
        self.pros2 = pros2  # probabilities of s2
        self.pros3 = pros3  # probabilities of s3
        self.pros4 = pros4  # probabilities of s4
        self.matrix = [[None for j in range(100)] for i in range(100)]  # create a 2D array
        # self.matrix = [[random.random() < 0.5 for x in range(100)] for y in range(100)]
        self.row = -1
        self.col = -1
    def create_matrix(self):
        # Define the options and their probabilities
        options = [1, 2, 3, 4]
        probabilities = [self.pros1, self.pros2, self.pros3, self.pros4]

        # Generate a random number from the options with specified probabilities
        random_num = random.choices(options, probabilities)[0]
        for i in range(100):
            for j in range(100):
                self.matrix[i][j] = Person.Person(random_num)

    def print_array(self):
        for i in range(100):
            for j in range(100):
                if self.matrix[i][j].gen == -1:
                    print("-", end='')
                else:
                    print("*", end='')
            print("\n")
        print("\n")
        print("\n")
        print("========================================")

    def run(self):
        self.create_matrix()
        # random starter
        row = random.randint(0, 99)
        col = random.randint(0, 99)
        self.matrix[row][col].gen = 0
        self.print_array()
        time.sleep(5)  # waits for 1 second

        self.matrix[row][col].prevent = 1
        if row + 1 < 100:
            self.matrix[row + 1][col].gen = 1
            self.matrix[row + 1][col].count_get = 1
        if row - 1 > 0:
            self.matrix[row - 1][col].gen = 1
            self.matrix[row - 1][col].count_get = 1
        if col + 1 < 100:
            self.matrix[row][col + 1].gen = 1
            self.matrix[row][col + 1].count_get = 1
        if col - 1 > 0:
            self.matrix[row][col - 1].gen = 1
            self.matrix[row][col - 1].count_get = 1

        self.print_array()
        time.sleep(5)  # waits for 1 second

        self.generation = 2
        while self.generation <= self.endGen:
            for i in range(100):  # spreading the rumor
                for j in range(100):
                    if self.matrix[i][j].gen == self.generation - 1 and self.matrix[i][j].prevent == 0:
                        # got the rumor in the last generation and not prevented
                        s = self.matrix[i][j].s if self.matrix[i][j].pre_count_get < 2 else self.matrix[i][j].s - 1
                        pro_spread = Person.probability_to_spread(s)
                        outcomes = [0, 1]
                        weights = [1 - pro_spread, pro_spread]
                        is_spread = random.choices(outcomes, weights)[0]
                        if is_spread == 1:
                            self.matrix[i][j].prevent = self.generation
                            if i + 1 < 100:
                                self.matrix[i + 1][j].gen = self.generation
                                self.matrix[i + 1][j].count_get += 1
                            if i - 1 > 0:
                                self.matrix[i - 1][j].gen = self.generation
                                self.matrix[i - 1][j].count_get += 1
                            if j + 1 < 100:
                                self.matrix[i][j + 1].gen = self.generation
                                self.matrix[i][j + 1].count_get += 1
                            if j - 1 > 0:
                                self.matrix[i][j - 1].gen = self.generation
                                self.matrix[i][j - 1].count_get += 1
            for i in range(100):
                for j in range(100):
                    self.matrix[i][j].pre_count_get = self.matrix[i][j].count_get
                    self.matrix[i][j].count_get = 0
                    if (self.generation - self.matrix[i][j].prevent) > self.l:
                        self.matrix[i][j].prevent = 0
            self.generation += 1  # update the generation
            print(self.generation, " ", )
            self.print_array()
            time.sleep(5)
            # waits for 1 second

    def random_starter(self):
        # random starter
        self.row = random.randint(0, 99)
        self.col = random.randint(0, 99)
        self.matrix[self.row][self.col].gen = 0
        # self.print_array()
        self.matrix[self.row][self.col].prevent = 1

    def first_gen(self):
        if self.row + 1 < 100:
            self.matrix[self.row + 1][self.col].gen = 1
            self.matrix[self.row + 1][self.col].count_get = 1
        if self.row - 1 > 0:
            self.matrix[self.row - 1][self.col].gen = 1
            self.matrix[self.row - 1][self.col].count_get = 1
        if self.col + 1 < 100:
            self.matrix[self.row][self.col + 1].gen = 1
            self.matrix[self.row][self.col + 1].count_get = 1
        if self.col - 1 > 0:
            self.matrix[self.row][self.col - 1].gen = 1
            self.matrix[self.row][self.col - 1].count_get = 1

        # self.print_array()
        self.generation = 2

    def gen_running(self):
        for i in range(100):  # spreading the rumor
            for j in range(100):
                if self.matrix[i][j].gen == self.generation - 1 and self.matrix[i][j].prevent == 0:
                    # got the rumor in the last generation and not prevented
                    s = self.matrix[i][j].s if self.matrix[i][j].pre_count_get < 2 else self.matrix[i][
                                                                                            j].s - 1
                    pro_spread = Person.probability_to_spread(s)
                    outcomes = [0, 1]
                    weights = [1 - pro_spread, pro_spread]
                    is_spread = random.choices(outcomes, weights)[0]
                    if is_spread == 1:
                        self.matrix[i][j].prevent = self.generation
                        if i + 1 < 100:
                            self.matrix[i + 1][j].gen = self.generation
                            self.matrix[i + 1][j].count_get += 1
                        if i - 1 > 0:
                            self.matrix[i - 1][j].gen = self.generation
                            self.matrix[i - 1][j].count_get += 1
                        if j + 1 < 100:
                            self.matrix[i][j + 1].gen = self.generation
                            self.matrix[i][j + 1].count_get += 1
                        if j - 1 > 0:
                            self.matrix[i][j - 1].gen = self.generation
                            self.matrix[i][j - 1].count_get += 1
        for i in range(100):
            for j in range(100):
                self.matrix[i][j].pre_count_get = self.matrix[i][j].count_get
                self.matrix[i][j].count_get = 0
                if (self.generation - self.matrix[i][j].prevent) > self.l:
                    self.matrix[i][j].prevent = 0
        self.generation += 1  # update the generation
        print(self.generation, " ", )
        # self.print_array()
        # time.sleep(5)


