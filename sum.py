import sys

A = 5
B = 4
iRet = ""

class sum:

    def sum_calculation(self):
        print ("\n*********************************************************************************************")
        print ("\n*  Test is based on after sum of two value, The result should be less then or equal to 10.  *")
        print ("\n*********************************************************************************************")
        
        c = A + B

        if c <= 10:
            iRet = 'PASS'
            print ("\n\nTEST PASS..!")

        else:
            iRet = 'FAIL'
            print ("\n\nTEST FAIL..!")

        return iRet

    def main(self):
        self.sum_calculation()

if __name__ == "__main__":
    obj = sum()
    obj.main()