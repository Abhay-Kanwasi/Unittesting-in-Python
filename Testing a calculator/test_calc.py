# First how to implement it 

# import unittest
# import calc

# class TestCalc(unittest.TestCase):

#     def test_add(self):
#         # Approch 1

#         # result = calc.addition(10,5)
#         # self.assertEqual(result,15)

#         # Approch 2

#         self.assertEqual(calc.addition(10,5),15)

# if __name__ == "__main__":
#     unittest.main()


###################################################################

# Now let give more conditions

import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.addition(10,5),15)    # When both are positive number.
        self.assertEqual(calc.addition(-10,5),-5)   # When a is negative one.
        self.assertEqual(calc.addition(10,-5),5)    # When b is negative one.
        self.assertEqual(calc.addition(-10,-5),-15) # When both a and b are negative.
    
    def test_subtract(self):
        self.assertEqual(calc.substraction(12,6),6)       # When both are positive.
        self.assertEqual(calc.substraction(-12,6),-18)    # When b is positive.
        self.assertEqual(calc.substraction(12,-6),18)     # When a is positive.
        self.assertEqual(calc.substraction(-12,-6),-6)    # When both are negative.

    def test_multiplication(self):
        self.assertEqual(calc.multiplication(12,6),72)      # When both are positive.
        self.assertEqual(calc.multiplication(-12,6),-72)    # When b is positive.
        self.assertEqual(calc.multiplication(12,-6),-72)    # When a is positive.
        self.assertEqual(calc.multiplication(-12,-6),72)    # When both are negative.
    
    def test_division(self):
        self.assertEqual(calc.division(12,6),2)       # When both are positive.
        self.assertEqual(calc.division(-12,6),-2)     # When b is positive.
        self.assertEqual(calc.division(12,-6),-2)     # When a is positive.
        self.assertEqual(calc.division(-12,-6),2)     # When both are negative.

        # For raising an exception in testing.
        self.assertRaises(ValueError,calc.division,10,0)

        # another method for raising an exception
        with self.assertRaises(ValueError):
            calc.division(10,0)

    
        

if __name__ == "__main__":
    unittest.main()