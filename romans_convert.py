 
import re

#Define exceptions
class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotIntegerError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass

#Define  mapping
romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))

def toRoman(n):
    """convert integer to Roman numeral"""
    if not (0 < n < 5000):
        raise OutOfRangeError, "number out of range (must be 1..4999)"
    if int(n) != n:
        raise NotIntegerError, "decimals can not be converted"

    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result

#Define pattern to detect valid Roman numerals
romanNumeralPattern = re.compile("""
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """ ,re.VERBOSE)

def fromRoman(s):
    """convert Roman numeral to integer"""
    if not s:
        raise InvalidRomanNumeralError, 'Input can not be blank'
    if not romanNumeralPattern.search(s):
        raise InvalidRomanNumeralError, 'Invalid Roman numeral: %s' % s

    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result


if __name__=="__main__":
  print 'Hi I am Romen your simple chatbot to convert roman numbers from arabic numbers and vice versa'
  while(True):
        st_inp  =  raw_input('Please enter a R_I if you want to  convert to Roman Number from int\n else enter I_R for vice versa and Bye to exit:')
        st_inp = str(st_inp)
        if st_inp == "I_R":
          inp = raw_input('Please enter a number to convert to Roman Representation :')
          try:
            inp = int(inp)
            print 'The Roman representation of this number is :',str(toRoman(inp))
          except:
            print 'Sorry, I only understand arabic numerals and Roman !'
        elif st_inp == "R_I":
          inp = raw_input('Please enter a Roman number to convert to Integer Representation :')
          try:
            inp = str(inp)
            print 'The Roman representation of this number is :',str(fromRoman(inp))
          except:
            print 'Sorry, I only understand arabic and Roman numerals!'
        elif st_inp == "Bye":
            break;    
        else:
            print 'Sorry, you have n\'t chosen valid input only understand I_R and R_I!'