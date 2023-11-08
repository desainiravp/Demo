import sys

A = 7
B = 8
iRet = ""


class multiply:

    def multiply_calculation(self):
        print ("\n**************************************************************************************************")
        print ("\n*  Test is based on after multiply of two value, The result should be less then or equal to 25.  *")
        print ("\n**************************************************************************************************")

        c = A * B

        if c <= 25:
            iRet = 'PASS'
            print("\n\nTEST PASS..!")

        else:
            iRet = 'FAIL'
            print("\n\nTEST FAIL..!")

        return iRet

    def main(self):
        self.multiply_calculation()


if __name__ == "__main__":
    obj = multiply()
    obj.main()
