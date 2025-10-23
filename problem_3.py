import unittest #self.assert functions

def even_or_not(n): #need function to check if number is even or odd
    return n % 2 == 1 #number over 2 tells if even or odd

class Even_four(unittest.TestCase): 

    def Test_even(self):   # define number
        self.assertTrue(even_or_not(4)) #True or false + our variable, 4

#if __name__ == '__problem.3__'
#    unittest()
#DNF