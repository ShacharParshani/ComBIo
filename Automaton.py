import random
class automaton:
    def _init_(self, p, l, pros1, pros2, pros3, pros4):
        self.p = p
        self.l = l
        self.pro = pro  # probabilities of s
        self.matrix = [[None for j in range(100)] for i in range(100)] # create a 2D array
    def create_matrix(self):
        # Define the options and their probabilities
        options = [1, 2, 3, 4]
        probabilities = [0.1, 0.2, 0.3, 0.4]

        # Generate a random number from the options with specified probabilities
        random_number = random.choices(options, probabilities)[0]
        for i in range(100):
            for j in range(100):
                self.matrix[i][j] = Person()
