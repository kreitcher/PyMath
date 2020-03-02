import sys

def kaprekarCounter(arg, attempt):
    
    try:
        # Checking to see if it is a number
        number = int(arg)
        # converting the string to an array so we can pad 0's
        nArray = list(arg)
        while len(nArray) < 4:
            nArray.append('0')
        # default sort into ascending order
        nArray.sort()
        # the first number
        sortedNumberA = ''.join(nArray)
        # the second number is reverse of the first
        sortedNumberD = sortedNumberA[::-1]
        # the absolute difference
        number = abs(int(sortedNumberA)-int(sortedNumberD))
        # all digits should not be the same
        # TODO: this check could be moved earlier to save some compute
        if(number == 0):
            print('Not a valid number')
            return 0
        #recursive call
        if(number!=6174):
            # tracking the number of attempts to reach 6174
            attempt = kaprekarCounter(str(number),attempt+1)
        else:
            #print(attempt)
            return attempt
        return attempt
    except:
        print('Not a valid number')
        return 0


if __name__ == "__main__":
   attempts = kaprekarCounter(sys.argv[1], 0)
   print(attempts)