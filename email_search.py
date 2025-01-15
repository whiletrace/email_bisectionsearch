import string
import random 

# email generator
def email_constructor(length):
   # value of random character within assi letters
   label1 = ''
   for x in range(length):
      label1 +=  string.ascii_letters[random.randrange(0, len(string.ascii_letters))]
   return label1

print(email_constructor(8))


    # email format has two parts the address and domain name
    # construct string for address 
    # construct string for domain 
     # domain label1
     # domain label2
     # TLD
   
    # concatinate domain label1, domain label2, Tld 
    # concatintate address and domain name
    # append email address to email list 
    # return email list 
   
   
    # construct a string

    # characters in string constructed to follow specific pattern
    # pattern to follow format of email
    # characters in string pattern to be random 
    
    # string to be appended to list
 

    

   

# get user input 
# create a list
# create a email 
# email should follow a certain format
# number of emails generated based user input
# emails need to be inserted into a collection list, dectionary etc
# user needs to be able to insert a specific email into the list
# email to be placed into list @ position specified by the user
# application to search for specified email within randomized email list
# application to output time took to find specified email and position email was found