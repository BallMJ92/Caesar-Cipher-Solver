class shiftSolver:

    def solve(self, c, s):
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
                        if y+shifts == 26:
                            y=shifts
                        elif y+shifts >=26:
                            restartShift = y+shifts-26
                            y=restartShift
                        else:
                            y+=shifts
                        shift.append(dic[y])

        postShift = ''.join(shift)
        print("Plaintext/Ciphertext after %d shifts: %s" % (shifts, postShift))

    def main(self):
        crypt = []
        data = str(input("Please enter the Plaintext/Ciphertext: ")).lower()
        crypt.append(data)
        encryptDecrypt = str(input("Do you wish to encrypt or decrypt (e/d): "))

        if encryptDecrypt == "e":
            # A shift greater than 26 is no different to a shift below 26 because there are only 26 letters in the alphabet
            shiftInput = int(input("Please enter a shift between 1 and 25: "))
            self.solve(crypt, shiftInput)
        elif encryptDecrypt == "d":
            print("Decrypting all possible combinations...")
            for i in range(1, 26):
                shiftInput = int(i)
                self.solve(crypt, shiftInput)

                
if __name__ == "__main__":
    caesar = shiftSolver()
    caesar.main()
    
    
