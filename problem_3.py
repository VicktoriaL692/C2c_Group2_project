import unittest #self.assert functions

def even_or_not(n): #need function to check if number is even or odd
    return n % 2 == 0 #number over 2 tells if even or odd

class Even_four(unittest.TestCase): 

    def test_even(self):# define number and test has to be lowercase
        self.assertTrue(even_or_not(4)) #True or false + the variable 4

if __name__ == '__main__': #This plays the command
    unittest.main()