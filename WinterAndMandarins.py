import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

class WinterAndMandarins:
    def getNumber(self, bags, K):
        lbags = sorted(bags) #10, 20, 30
        gdiff = lbags[-1]-lbags[0]
        for i in range(0, len(lbags)-1):
            if i+K == len(bags)+1:
                break
            diff = lbags[i + K -1] - lbags[i]
            if diff < gdiff:
                gdiff = diff
        return gdiff

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pf 2.3.0
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, hasAnswer, p2):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("{"))
	for i in range(len(p0)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str(p0[i]))
	
	sys.stdout.write(str("}") + str(",") + str(p1))
	print(str("]"))
	obj = WinterAndMandarins()
	startTime = time.clock()
	answer = obj.getNumber(p0, p1)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		print(str("Desired answer:"))
		print(str("\t") + str(p2))
	
	print(str("Your answer:"))
	print(str("\t") + str(answer))
	if (hasAnswer):
		res = answer == p2
	
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
p0 = (10,20,30)
p1 = 2
p2 = 10
all_right = (disabled or KawigiEdit_RunTest(0, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = (4,7,4)
p1 = 3
p2 = 3
all_right = (disabled or KawigiEdit_RunTest(1, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = (4,1,2,3)
p1 = 3
p2 = 2
all_right = (disabled or KawigiEdit_RunTest(2, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = (5,4,6,1,9,4,2,7,5,6)
p1 = 4
p2 = 1
all_right = (disabled or KawigiEdit_RunTest(3, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = (47,1000000000,1,74)
p1 = 2
p2 = 27
all_right = (disabled or KawigiEdit_RunTest(4, p0, p1, True, p2) ) and all_right
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
# It's winter time!
# Time to eat a lot of mandarins with your friends.
# 
# 
# 
# 
# You have several bags with mandarins.
# You are given an tuple (integer) bags.
# For each i, the i-th element of bags represents the number of mandarins in the i-th bag.
# You are also given an integer K.
# You want to choose exactly K bags and distribute them among you and your friends.
# To be as fair as possible, you want to minimize the difference between the chosen bag with most mandarins and the
# chosen bag with fewest mandarins.
# Return the smallest difference that can be achieved.
# 
# 
# DEFINITION
# Class:WinterAndMandarins
# Method:getNumber
# Parameters:tuple (integer), integer
# Returns:integer
# Method signature:def getNumber(self, bags, K):
# 
# 
# CONSTRAINTS
# -bags will contain between 2 and 50 elements, inclusive.
# -Each element of bags will be between 1 and 1,000,000,000, inclusive.
# -K will be between 2 and N, inclusive, where N is the number of elements in bags.
# 
# 
# EXAMPLES
# 
# 0)
# {10, 20, 30}
# 2
# 
# Returns: 10
# 
# There are three ways to choose two bags in this case: {10, 20}, {20, 30}, and {10, 30}.
# Both in the first case and in the second case the difference between the largest and the smallest number of mandarins is 10.
# In the third case the difference is 20.
# Thus, the smallest possible difference is 10.
# 
# 1)
# {4, 7, 4}
# 3
# 
# Returns: 3
# 
# 
# 
# 2)
# {4, 1, 2, 3}
# 3
# 
# Returns: 2
# 
# 
# 
# 3)
# {5, 4, 6, 1, 9, 4, 2, 7, 5, 6}
# 4
# 
# Returns: 1
# 
# 
# 
# 4)
# {47, 1000000000, 1, 74}
# 2
# 
# Returns: 27
# 
# 
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pf 2.3.0!
