#!/usr/bin/env python
# coding: utf-8

# In[1]:


from parser import parse

import unittest 

class Test(unittest.TestCase):

    def testforFactorial(self):
        self.assertEqual(parse([['5', '+', '1' ,'!'], '*', '4']),['*', ['+', ['5', [], []], ['!', ['1', [], []], []]], ['4', [], []]])

    
    def testsmallerExpression(self):
        self.assertEqual(parse(['1', '-', ['7', '!']]),['-', ['1', [], []], ['!', ['7', [], []], []]])
        
    def testjustREgularExpression(self):
        self.assertEqual(parse(['6', '!']),['!', ['6', [], []], []])
        
    
    def test4(self):
        self.assertEqual(parse(['4' , '*', ['2', '+' , '3 ']]),['*', ['4', [], []], ['+', ['2', [], []], ['3 ', [], []]]])

    
    def test5(self):
        self.assertEqual(parse(['4' , '/' ,['7', '+' ,'2']]),['/', ['4', [], []], ['+', ['7', [], []], ['2', [], []]]])
    
if __name__ == '__main__' : # Defines a command-line entry point; runs the unittest test-runner .main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)        


# In[ ]:





# In[ ]:




