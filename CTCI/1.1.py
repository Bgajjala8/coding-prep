#Arrays and Strings


# NOTES
# -----
# enumerate(x) -> returns tuple of (#, item)
# range(x) -> Not inclusive 
# len(x) -> Returns actual amount of len not index
# ord(c) -> Returns value of the ascii number (when working on these remember lowercase and uppercase have diffrent ord values)
# Hashset -> Instansiated by using set() append by using set.append()


#Implement  an  algorithm  to  determine  if a  string  has  all  unique  characters.  What  if you 
#cannot  use additional  data  structures? 
def is_unique(someString):
    for i, s in enumerate(someString):
        for j in range(i + 1, len(someString)):
            if someString[j] == s:
                return False
    return True;

# This method is still using mem o(1) and only uses array
def is_unique_array(s):
    l = [0] * 128 # 128 is the ascii set 

    for i in s:
        ord_num = ord(i)
        if l[ord_num] == 1: #Already checked 
            return False
        
        l[ord_num] = 1 #Update array in place

    return True

def is_unique_hashset(s):
    seen = set()
    for i in s:
        if i in seen:
            return False

        seen.add(i)
    return True

#Driver
ans = [False, True , True]
test_case = ['test', 'tes', 't']

test_result = []
for i in test_case:
    test_result.append(is_unique(i))

print("test #1 : ",test_result == ans)

test_result = []
for i in test_case:
    test_result.append(is_unique_array(i))

print("test #2 : ",test_result == ans)

test_result = []
for i in test_case:
    test_result.append(is_unique_hashset(i))

print("test #3 : ",test_result == ans)