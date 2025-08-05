def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2<=len(s)<=6): #check if length min 2 and max 6
        return False
    
    if not s.isalnum(): # check no punctuations
        return False
    
    if not s[:2].isalpha(): # check first 2 chars are alpha only not nums
        return False
    
    for i in range(len(s)):
        if s[i].isdecimal():             #check for num start in the plate
            if not s[i:].isdecimal():    #check all the chars after a digit are nums only i.e nums are not in between
                return False
            
            if int(s[i]) == 0:          #check starting digit is not '0' 
                return False
            
            break                     '''Here we used 'break' because this line of code will be reached
                                        Only when both conditions in for loop are Fasle. When both are Fasle we 
                                        we found a vlaid plate. In case if we dont use break even in case of a valid 
                                        plate the code goes for next iteration in that iteration the digit might not be zero so it will
                                         evaluates to True which mean invalid Plate. We are only concerened if a plate has digits in between
                                          that starting digit should not be zero. So we should not go for next iteration incase of valid plate. ''' 

    return True
    
main()