from collections import Counter


# Notes
# -----
# Counter can be brought in from collections this just returns MAP with char:count(char-in-s)
# for string that are even numbers there should be no odds beacuse it should flip correctly 
# from string that are odd numbers one char should repeat because %2 is not o
# remeber when count to LOWERCASE string. Lowercasing string allows for correct calculation in this case
# String to lower -> s.lower()  String to upper -> s.upper()
# s.replace(' ', '') -> to remove any spaces

# Palindrome  Permutation:  Given  a  string,  write a function  to  check  if it  is a  permutation  of a  palin-
# drome.  A  palindrome  is a  w o r d  or  phrase  that  is  the  same  forwards  and  backwards.  A  permutation 
# is a  rearrangement of letters. The palindrome  does  not  need  to  be  limited  to just  dictionary words. 

def is_palindrome_permutation(s):
    
    prepared_string = (s.lower()).replace(' ','')

    # Detrmine weather s is a even or odd lettered 
    is_even_length = is_even(len(prepared_string))
    
    # Count the chars 
    char_count = Counter(prepared_string) 
    
    # Get odd count
    odd_char_count = sum(1 for c in char_count.values() if not is_even(c))
    
    if (is_even_length and odd_char_count != 0) or odd_char_count > 1:
        return False
    
    return True
    
    
# Helper 
def is_even(num):
   return num % 2 == 0


print(is_palindrome_permutation("Tact Coa")) 
print(is_palindrome_permutation("abcde"))  
            
    
    
    

