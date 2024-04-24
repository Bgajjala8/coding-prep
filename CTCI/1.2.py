# Notes
# -----
# permutations are when same amount of letters can be made into another string
# hasmap get or else -> map.get(val,default_val)

# Given  two  strings,  write  a  method  to  decide  if  one  is  a  permutation  of the other


def is_permutation(s1, s2):
    return get_char_count(s1) == get_char_count(s2)
    
    
def get_char_count(s):
    count = {}
    for c in s: 
        curr_count = count.get(c,0)
        count[c] = curr_count + 1
        
    return count
    
        
    
# Driver 

s1 = "test"
s2 = "estt"

print(is_permutation(s1,s2))


    
    
    
