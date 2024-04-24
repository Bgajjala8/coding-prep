# Write a  method  to  replace all  spaces in  a  string  w i t h '%20'. You  may assume  that  the  string 
# has  sufficient  space  at  the  end  to  hold  the  additional  characters,  and  that  you  are  given  the "true" 
# length  of  the  string.  (Note:  If  implementing  in  Java,  please  use  a  character  array  so  that  you  can  
# perform  this  operation  in  place.) 

# ASCII for space is 32
# join -> join takes '' and joins string 

def replace(s):
    l =[1,2,3,4]
    
    len_s = len(s)
    for i in range(len_s):
        char_s = s[i]
        while ord(s[i]) == 32 and i <  len_s:
            i = i + 1
            char_s = '%20'
             
        l.append(char_s)
        
    return ''.join(l)

        
        
test = "bharath gajjala"

print(replace(test))
    
        
            
                
        
