class shiftSolver:

    def solve(self, c, s):
        print("Input ciphertext:\n",c)
        shifts = int(s)

        dic = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g',
               8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n',
               15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u',
               22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

        shift = []

        length = int(len(dic))

        for x in c:
            for n in x:
                if n == ' ':
                    shift.append(' ')
                for y in range(1, length+1):
                    if n == str(dic[y]):
                        print(y, dic[y])
                        if y+shifts == 26:
                            y=shifts
                        elif y+shifts >=26:
                            restartShift = y+shifts-26
                            y=restartShift
                        else:
                            y+=shifts
                        shift.append(dic[y])

        postShift = ''.join(shift)
        print(postShift)

    def main(self):
        crypt = []
        userInput = str(input("Please enter the cipher: ")).lower()
        shiftInput = str(input("How many shifts do you want to implement: "))

        crypt.append(userInput)

        self.solve(crypt, shiftInput)

if __name__ == "__main__":
    caesar = shiftSolver()
    caesar.main()