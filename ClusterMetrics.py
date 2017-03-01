"""
This class offers a few simple measures to assess the quality of clustering
models when we know the correct cluster assignments (supervised clustering).
For explanations of Rand index, Purity, and F Measure, see:
http://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-clustering-1.html

Author: Abe Khaleghi
Email : amkhaleghi@gmail.com
"""

class ClusterMetrics():

    def __init__(self, assignments, truth):
        self.assignments = assignments
        self.truth = truth

    # Checks for valid input
    def __valid_input(self):

        # Inputs must be lists
        if(not(isinstance(assignments, list)) or not(isinstance(assignments, list))):
            print "Error: Input type must be list.",
            return False

        # Lists of cluster assignments and correct classes must be the same
        if (len(self.assignments) != len(self.truth)):
            print "Error: Lists of assignments and ground truths must be same length.",
            return False

        # The lists must contain only ints
        if (not(all(isinstance(item, int) for item in assignments)) or
                not(all(isinstance(item, int) for item in truth))):
            print "Error: Input items must be of type int.",
            return False

        else:
            return True

    # The Rand index is essentially the number of corrrectly classified
    # instances divided by the total number of instances. An "instance"
    # is a comparison of two data points. If they are in the same cluster
    # in the same cluster and same class, or in different clusters and
    # different classes, then the instance is correctly classified.
    def rand_index(self):

        if(self.__valid_input()):

            n = len(self.truth)

            true_pos = self.confusion_matrix()[0]
            true_neg = self.confusion_matrix()[1]

            return float((true_pos + true_neg))/((n * (n - 1))/2)

    # Purity is a measure of how well the model correctly assigns
    # items by taking the number of correct assignments divided by n.
    def purity(self):

        if(self.__valid_input()):
            table = self.assignment_table()

            items_in_majority_class = 0

            for x in range(len(set(self.assignments))):
                items_in_majority_class += max(table[x])

            return 1.0/len(self.truth) * items_in_majority_class

    # The F measure can be used to penalize false negatives more
    # strongly than false positives by selecting beta > 1, thus giving
    # more weight to recall.
    def f_measure(self, beta):

        if(self.__valid_input()):

            true_pos = float(self.confusion_matrix()[0])
            false_pos = float(self.confusion_matrix()[2])
            false_neg = float(self.confusion_matrix()[3])

            if (true_pos == 0):

                return 0.0

            else:
                precision = true_pos/(true_pos + false_pos)
                recall = true_pos/(true_pos + false_neg)

                f = ((beta**2 + 1) * precision * recall)/(beta**2 * precision + recall)

                return f

    # Calculates true positives, true negatives, false positives and
    # false negatives.
    def confusion_matrix(self):
        true_pos = 0
        true_neg = 0
        false_pos = 0
        false_neg = 0
        n = len(self.truth)

        for x in range(n):
            for y in range(n):
                if ((x <= y) and (x != y)):
                    if (self.assignments[x] == self.assignments[y]):
                        if (self.truth[x] == self.truth[y]):
                            true_pos += 1
                        else:
                            false_neg += 1
                    elif (self.assignments[x] != self.assignments[y]):
                        if (self.truth[x] != self.truth[y]):
                            true_neg += 1
                        else:
                            false_pos += 1

        return true_pos, true_neg, false_pos, false_neg

    # Creates a table of cluster assignments, based on class.
    def assignment_table(self):
        assignment_clusters = len(set(self.assignments))
        truth_clusters = len(set(self.truth))
        table = [[0 for x in range(truth_clusters)] for y in range(assignment_clusters)]

        for x in range(len(self.truth)):
            table[self.assignments[x]][self.truth[x]] += 1

        return table

if __name__ == "__main__":

    # A perfect clustering assignment
    #assignments = [0,0,1,1,2]
    #truth = [2,2,0,0,1]

    # A bad clustering; model assigns all to same cluster but all in different clusters
    #assignments = [0,0,0,0,0]
    #truth = [0,1,2,3,4]

    assignments = [0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2]
    truth = [0,0,0,0,0,1,0,1,1,1,1,2,0,0,2,2,2]

    metrics = ClusterMetrics(assignments, truth)

    print "Rand Index: ",
    print metrics.rand_index()
    print "Purity: ",
    print metrics.purity()
    print "F measure (beta = 1): ",
    print metrics.f_measure(1)

