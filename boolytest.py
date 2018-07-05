from booly import *

if __name__ == '__main__':
    userinput = input('Please enter word to evaluate to a boolean: ').lower()
    ourbooly = Booly()
    ourbooly.debugging = input('Debugging? y/n')
    ourbooly.debugging = ourbooly.booly(ourbooly.debugging)
    print(ourbooly.debugging)
    boolyresult = ourbooly.booly(userinput)
    print('\"' + str(userinput) + '\" matched best with: \"' + str(boolyresult[0]) +
          '\" and was interpreted as: ' + str(boolyresult[1]))
          
