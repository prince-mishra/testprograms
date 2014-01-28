import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

class MiniatureDachshund:
    def maxMikan(self, mikan, weight):
        maxweight = 5000
        mikan = sorted(mikan)
        count = 0
        for item in mikan:
            weight+=item
            if weight<=maxweight:
                count +=1
            else:
                break
        return count

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
	obj = MiniatureDachshund()
	startTime = time.clock()
	answer = obj.maxMikan(p0, p1)
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
p0 = (100,100,100,100,100)
p1 = 4750
p2 = 2
all_right = (disabled or KawigiEdit_RunTest(0, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = (100,100,100,100,50)
p1 = 4750
p2 = 3
all_right = (disabled or KawigiEdit_RunTest(1, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = (120,90,130,100,110,80)
p1 = 3000
p2 = 6
all_right = (disabled or KawigiEdit_RunTest(2, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = (50,)
p1 = 5000
p2 = 0
all_right = (disabled or KawigiEdit_RunTest(3, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = (200,50,200,50,200,50,200,50)
p1 = 4800
p2 = 4
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
# Dachshund is a popular dog breed. In this problem, a miniature dachshund is defined as a dachshund whose weight is not more than 5,000 grams.
# 
# 
# Lun the miniature dachshund loves mikan (satsuma oranges). She has just bought some mikan. You are given a tuple (integer) mikan. It gives the weight of all mikan she bought. For each valid i, mikan[i] is the weight of the i-th mikan in grams.
# 
# 
# You are also given an integer weight. Currently, Lun weighs weight grams. When she eats i-th mikan, her weight increases by mikan[i] grams. If she eats multiple mikan, her weight increases by their total weight. She cannot eat just a part of a mikan. In other words, if she chooses to eat a mikan, she eats it completely.
# 
# 
# She wants to remain being a miniature dachshund. That is, she wants her weight not to exceed 5,000 grams. Under this condition, calculate and return the maximum number of mikan Lun can eat.
# 
# DEFINITION
# Class:MiniatureDachshund
# Method:maxMikan
# Parameters:tuple (integer), integer
# Returns:integer
# Method signature:def maxMikan(self, mikan, weight):
# 
# 
# CONSTRAINTS
# -mikan will contain between 1 and 50 elements, inclusive.
# -Each element of mikan will be between 50 and 200, inclusive.
# -weight will be between 3,000 and 5,000, inclusive.
# 
# 
# EXAMPLES
# 
# 0)
# {100, 100, 100, 100, 100}
# 4750
# 
# Returns: 2
# 
# Here, Lun weighs 4,750 grams and has bought 5 mikan, each of which weighs 100 grams. When she eats 2 of these, her weight will be 4,950 grams. She should not eat more.
# 
# 1)
# {100, 100, 100, 100, 50}
# 4750
# 
# Returns: 3
# 
# This time, one of the mikan is smaller. She can eat it with 2 of the 100-gram mikan. Note that her weight is allowed to be exactly 5,000 grams.
# 
# 2)
# {120, 90, 130, 100, 110, 80}
# 3000
# 
# Returns: 6
# 
# When she is light enough, she can eat all of the mikan she has bought.
# 
# 3)
# {50}
# 5000
# 
# Returns: 0
# 
# When her weight is already 5,000 grams, she should not eat anything.
# 
# 4)
# {200, 50, 200, 50, 200, 50, 200, 50}
# 4800
# 
# Returns: 4
# 
# 
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pf 2.3.0!