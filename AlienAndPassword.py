import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

class AlienAndPassword:
    def getNumber(self, S):
        count = 1
        for i in range(1, len(S)):
            if S[i] != S[i-1]:
                count +=1
        return count

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pf 2.3.0
import sys
import time
def KawigiEdit_RunTest(testNum, p0, hasAnswer, p1):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("\"") + str(p0) + str("\""))
	print(str("]"))
	obj = AlienAndPassword()
	startTime = time.clock()
	answer = obj.getNumber(p0)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		print(str("Desired answer:"))
		print(str("\t") + str(p1))
	
	print(str("Your answer:"))
	print(str("\t") + str(answer))
	if (hasAnswer):
		res = answer == p1
	
	if (not res):
		print(str("DOESN'T MATCH!!!!"))
	elif ((endTime - startTime) >= 2):
		print(str("FAIL the timeout"))
		res = False
	elif (hasAnswer):
		print(str("Match :-)"))
	else:
		print(str("OK, but is it right?"))
	
	print(str(""))
	return res

all_right = True
tests_disabled = False


# ----- test 0 -----
disabled = False
p0 = "A"
p1 = 1
all_right = (disabled or KawigiEdit_RunTest(0, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = "ABA"
p1 = 3
all_right = (disabled or KawigiEdit_RunTest(1, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = "AABACCCCABAA"
p1 = 7
all_right = (disabled or KawigiEdit_RunTest(2, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = "AGAAGAHHHHFTQLLAPUURQQRRRUFJJSBSZVJZZZ"
p1 = 26
all_right = (disabled or KawigiEdit_RunTest(3, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
p1 = 1
all_right = (disabled or KawigiEdit_RunTest(4, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

if (all_right):
	if (tests_disabled):
		print(str("You're a stud (but some test cases were disabled)!"))
	else:
		print(str("You're a stud (at least on given cases)!"))
	
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# 
# Alien Fred wants to destroy the Earth, but he forgot the password that activates the planet destroyer.
# 
# 
# 
# 
# You are given a string S.
# Fred remembers that the correct password can be obtained from S by erasing exactly one character.
# 
# 
# 
# 
# Return the number of different passwords Fred needs to try.
# 
# 
# DEFINITION
# Class:AlienAndPassword
# Method:getNumber
# Parameters:string
# Returns:integer
# Method signature:def getNumber(self, S):
# 
# 
# CONSTRAINTS
# -S will contain between 1 and 50 characters, inclusive.
# -Each character in S will be an uppercase English letter ('A'-'Z').
# 
# 
# EXAMPLES
# 
# 0)
# "A"
# 
# Returns: 1
# 
# In this case, the only password Fred needs to try is an empty string.
# 
# 1)
# "ABA"
# 
# Returns: 3
# 
# The following three passwords are possible in this case: "BA", "AA", "AB".
# 
# 2)
# "AABACCCCABAA"
# 
# Returns: 7
# 
# 
# 
# 3)
# "AGAAGAHHHHFTQLLAPUURQQRRRUFJJSBSZVJZZZ"
# 
# Returns: 26
# 
# 
# 
# 4)
# "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
# 
# Returns: 1
# 
# Regardless of which character we erase, we will always obtain the same string. Thus there is only one possible password: the string that consists of 49 'Z's.
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pf 2.3.0!
