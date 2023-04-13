import unittest


def palindrome(pal):
     principio=0
     final=len(pal)-1
     while principio  != final:
        if pal[principio] == pal[final]:
            principio +=1 
            final -=1
            return True 
        else: return False
        

class TestPalindrome(unittest.TestCase):

    def test_palindrome_simple(self):
        result = palindrome('neuquen')
        self.assertEqual(result, True)
    def test_palindrome_simple2(self):
        result = palindrome('hola')
        self.assertEqual(result,False)

if __name__ == '__main__':
    unittest.main()


