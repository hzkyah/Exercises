import unittest

def balance(str):
    p_opn = 0
    p_cls = 0
    fifo = []
    #str = "a(b+(c+d))"
    
    for ch in str:
        if ch == '(':
            fifo.append(ch)
            p_opn += 1
        elif ch == ')':
            if p_cls < p_opn:
                fifo.append(ch)
                p_cls += 1
    
    for i in range(len(fifo)-1, -1, -1):
      if fifo[i] == '(' and p_opn > p_cls:
        del fifo[i]
        p_opn -= 1
    
    result = ''.join(fifo)
    print(result)

    return result
    
    
print("ሰላም ነው?\n")

class TestBalance(unittest.TestCase):
    
    data = [("a(b+c)", "()"), (")()", "()"), ("(((", ""), ("()()","()()")]
    
    def test_balance(self):
      for [testcase, expexted] in self.data:
        actual = balance(testcase)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
