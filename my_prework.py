#Question 1

def hello_name(user_name):
    print("hello_"+user_name+"!") 
    
user_name = input('Enter USERNAME: ') 
hello_name(user_name)



#Question 2

def first_odds():
 for x in range(1, 100, 2):
    print(x)



#Question 3

def max_num_in_list(a_list):
    max = a_list[ 0 ]  
    for a in a_list:  
        if a > max:  
            max = a  
    return max  
print(max_num_in_list([19, 15, 17, 20])) 



#Question 4

def is_leap_year(a_year):
    leap = False
    if a_year%4 == 0:
      if(a_year%100 != 0 or a_year%400 == 0):
         leap = True
    return leap



#Question 5

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
     
x = [5, 7, 8, 9, 10]
print(is_consecutive(x))