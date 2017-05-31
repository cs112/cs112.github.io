##############################################################################
# String CT [5 mins] 
##############################################################################
def ct1(s, t):
    result = ""
    for c in  s:
        if (c.upper() not in  "NO!!!"):
            i = t.find(c)
            if (result != ""): result += ":"
            result += "%d%s%s%s" % (i, c, s[i], t[i])
    return result
print(ct1("net",   "two"))

##############################################################################
# FR [35 mins] 
##############################################################################
import string 

"""
collapseWhitespace(s) 
Without using the s.replace() method, write the function collapseWhitespace(s), 
that takes a string s and returns an equivalent string except that each 
occurrence of whitespace in the string is replaced by a single space. So, for 
example, collapseWhitespace("a\t\t\tb\n\nc") replaces the three tabs with a 
single space, and the two newlines with another single space , returning 
"a b c". A few more test cases are provided below. 
"""
def collapseWhitespace(s):
    return "Zzz" # replace with your answer!

def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert(collapseWhitespace("a\n\n\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") ==
                              "a b c ")
    print("Passed!")

# testCollapseWhitespace() # uncomment this line to test your function! 

"""
bestStudentAverage
Background: for this problem, a "gradebook" is a multiline string where each 
row contains a student's name (one word, all lowercase) followed by one or more 
comma-separated integer grades. A gradebook always contains at least one 
student, and each row always contains at least one grade. Gradebooks can also 
contain blank lines and lines starting with the "#" character, which should be 
ignored. 

With this in mind, write the function bestStudentAndAvg(gradebook), that takes 
a gradebook and finds the student with the best average (ignoring the case 
where there is a tie) and returns a string of that student's name followed by 
a colon (":") followed by his/her average (rounded to the nearest integer). 

Hint: you most likely will want to use both s.split(",") and s.splitlines() in 
your solution.
"""

# Test cases 
gradebook1 = """
# ignore  blank lines and lines starting  with  #'s
Rudina,91,93
Rohan,80,85,90,95,100
Kosbie,1
"""
gradebook2 = """
# ignore  blank lines and lines starting  with  #'s
Kosbie,9
"""
gradebook3 = """
# ignore  blank lines and lines starting  with  #'s
Rohan,80,85,90,95,100
"""
gradebook4 = """
# ignore  blank lines and lines starting  with  #'s

Rudina,91,93

Rohan,80,85,90,95,100

"""
def bestStudentAndAvg(gradebook):
    return "Kosbie:-100"

def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    assert(bestStudentAndAvg(gradebook1) ==  "Rudina:92")
    assert(bestStudentAndAvg(gradebook2) ==  "Kosbie:9")
    assert(bestStudentAndAvg(gradebook3) ==  "Rohan:90")
    assert(bestStudentAndAvg(gradebook4) ==  "Rudina:92")
    assert(bestStudentAndAvg('Kosbie,0') ==  "Kosbie:0")
    assert(bestStudentAndAvg('Rudina,-1\nKosbie,-2') == "Rudina:-1")
    print("Passed. (Add more tests to be more sure!)")

# testBestStudentAndAvg() # uncomment this line to test your function

##############################################################################
# Bonus (More String Practice
# at https://www.cs.cmu.edu/~112/notes/quiz3-practice.html#codeTracing)
##############################################################################
"""
vowelCount(s) 
Write the function vowelCount(s), that takes a string s, and returns the number 
of vowels in s, ignoring case, so "A" and "a" are both vowels. The vowels are 
"a", "e", "i", "o", and "u". So, for example:
   vowelCount("Abc def!!! a? yzyzyz!")
returns 3 (two a's and one e).
"""
def vowelCount(s):
    return 42 # replace with your answer!

def testVowelCount():
    print("Testing vowelCount()...", end="")
    assert(vowelCount("abcdefg") == 2)
    assert(vowelCount("ABCDEFG") == 2)
    assert(vowelCount("") == 0)
    assert(vowelCount("This is a test.  12345.") == 4)
    assert(vowelCount(string.ascii_lowercase) == 5)
    assert(vowelCount(string.ascii_lowercase*100) == 500)
    assert(vowelCount(string.ascii_uppercase) == 5)
    assert(vowelCount(string.punctuation) == 0)
    assert(vowelCount(string.whitespace) == 0)
    print("Passed!")

# testVowelCount() # uncomment this line to test your function

"""
interleave(s1, s2) 
Write the function interleave(s1, s2) that takes two strings, s1 and s2, and 
interleaves their characters starting with the first character in s1. For 
example, interleave('pto', 'yhn') would return the string "python". If one 
string is longer than the other, concatenate the rest of the remaining string 
onto the end of the new string. For example ('a#', 'cD!f2') would return the 
string "ac#D!f2". Assume that both s1 and s2 will always be strings.
"""
def interleave(s1, s2):
    return "Z" # replace with your answer!

def testInterleave():
    print("Testing interleave()...", end="")
    assert(interleave("abcdefg", "abcdefg") == "aabbccddeeffgg")
    assert(interleave("abcde", "abcdefgh") == "aabbccddeefgh")
    assert(interleave("abcdefgh","abcde") == "aabbccddeefgh")
    assert(interleave("Smlksgeneg n a!", "a ie re gsadhm") ==
                      "Sam likes green eggs and ham!")
    assert(interleave("","") == "")
    print("Passed!")

# testInterleave() # uncomment this line to test your function


