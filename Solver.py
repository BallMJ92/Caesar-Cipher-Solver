class caesarSolver:

    def solve(self, c, s):
        shifts = int(s)
        
        """Dictionary to hold all letters in the alphabet along with their specific index within the alphabet
        This allows easy access of index values and allows the program to simply apply the shifts through addition"""
        dic = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g',
               8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n',
               15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u',
               22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
        
        #List to hold Ciphertext/Plaintext after user specified shift
        shift = []
        
        #Length of dictionary which contains the 26 characters of the alphabet
        length = int(len(dic))
        
        #for Ciphertext/Plaintext in list
        for x in c:
            #for letter in Ciphertext/Plaintext
            for n in x:
                #adding space if it appears in Ciphertext/Plaintext
                if n == ' ':
                    shift.append(' ')
                for y in range(1, length+1):
                    #if character is listed in dictionary
                    if n == str(dic[y]):
                        #if y+shifts equal 26 then y=shifts because a shift of 26 will not change letter
                        if y+shifts == 26:
                            y=shifts
                            #if y+shifts greater than 26 then we continue to 26 and jump back to shift 1 and continue from there
                        elif y+shifts >=26:
                            restartShift = y+shifts-26
                            y=restartShift
                        else:
                            y+=shifts
                        #appending specific value in dictionary with shift y applied to shift list
                        shift.append(dic[y])

        postShift = ''.join(shift)
        print("Plaintext/Ciphertext after %d shifts: %s" % (shifts, postShift))

    def main(self):
        crypt = []
        userInput = str(input("Please enter the Plaintext/Ciphertext: ")).lower()
        shiftInput = int(input("How many shifts do you want to implement: "))
        
        #A shift greater than 26 is no different to a shift below 26 because there are only 26 letters in the alphabet
        if shiftInput > 26:
            shiftInput = int(input("Please enter a shift between 1 and 25: "))
        #A shift of 26 is the same as a shift of 0 because there are only 26 letters in the alphabet
        elif shiftInput == 26:
            print("Shifts by 26 will revert Ciphertext to it's original state")
        else:
            pass

        crypt.append(userInput)
        self.solve(crypt, shiftInput)

if __name__ == "__main__":
    caesar = caesarSolver()
    caesar.main()
    
    
