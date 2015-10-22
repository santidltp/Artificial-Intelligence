#! /usr/bin/python3
import itertools
import random
import copy

# NUM_INPUTS        | 1 | 2 | 3 | 4 | 5 |  6 |  7 |  8 |
# NUM_COMPARATORS   | 0 | 1 | 3 | 5 | 9 | 12 | 16 | 19 |

NUM_INPUTS      = 4
NUM_COMPARATORS = 5

def is_sorted(array):
    """
        Returns True if array is sorted, otherwise False
    """
    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            return False

    return True

def generate_evaluation_cases():
    """
        Returns a list of all possible unsorted lists of size NUM_INPUTS
        that contain only 0's and 1's.

        Example:
            NUM_INPUTS = 2, [[1,0]]
            NUM_INPUTS = 3, [[0,1,0],[1,0,0],[1,0,1],[1,1,0]]

        Hint: Think binary numbers
    """
    ### FILL THIS IN ###
    unsorted_lists = []
    lst = [list(i) for i in itertools.product([0, 1], repeat=NUM_INPUTS)]
    for pair in lst:
        for k in range(len(pair)-1):
            if pair[k] > pair[k+1]:
                #unsorted
                unsorted_lists.append(pair)


    # print (unsorted_lists) # for testing purposes
    return unsorted_lists

class SortingNetwork:
    EVALUATION_CASES = generate_evaluation_cases()

    def __init__(self):
        """
            Creates a random sorting network with NUM_COMPARATORS comparators
            to sort an array of size NUM_INPUTS

            Note: For all comparators (x,y), x < y

            Example:
                (0,2) => correct
                (4,0) => incorrect
                (1,1) => incorrect

            Note: Consecutive comparators in list shouldn't be the the same

            Example:
                [(0,1),(0,2),(1,2)] => correct
                [(0,3),(0,3),(0,2)] => incorrect
                [(0,3),(0,2),(0,3)] => correct
        """
        self.comparators = []
        ### FILL THIS IN ###
        random_sorting_network = []
        test=[]
        for x in range(NUM_INPUTS):
            for y in range(NUM_INPUTS):
                if x < y:
                    tup = (x, y)
                    test.append(tup)
        self.comparators = random.sample(test,NUM_COMPARATORS)
        # print (self.comparators)

    def __str__(self):
        return str(self.comparators)

    def apply_on(self, array):
        """
            Uses the sorting network to (try to) sort the array
        """

        ### FILL THIS IN ###
        for comparator in self.comparators:
            # if they the first number is biggger, then swap
            if array[comparator[0]] > array[comparator[1]]:
                array[comparator[0]],array[comparator[1]]=array[comparator[1]],array[comparator[0]]


    def evaluate(self):
        """
            Evaluate sorting network over each case in EVALUATION_CASES.
            Returns the percentage that the sorting network correctly sorts.

            WARNING: Do not modify the evaluation cases
        """

        ### FILL THIS IN ###
        correct = 0

        for i in self.EVALUATION_CASES:
            temp = copy.deepcopy(i)
            self.apply_on(temp)
            if is_sorted(temp):
                correct += 1
        return correct/len(self.EVALUATION_CASES)

if __name__ == "__main__":
    network = SortingNetwork()
    #
    print("SORTING NETWORK : " + str(network))
    print("EVALUATION CASES: " + str(network.EVALUATION_CASES))

    percent_correct = network.evaluate()

    print(str(percent_correct) + "% of possible inputs sorted correctly")
