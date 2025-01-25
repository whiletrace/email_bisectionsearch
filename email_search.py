import string
import random 
from binary_search import bisection_iter
from timer import Timer

# get user input
label = int(input("How long would you like the label of the email to be? You can choose between 1 and 63 characters. "))
domain = int(input("how long would you like the domain to be? You can chooose between 1 and 245 characters. "))
num_of_emails = int(input('How many emails would you like to generate? '))
user_defined_email = input( 'Now please define your own email and we will put it in a random index position and find it usint bisectional search and show you an analysis of how long in seconds it took to find the email, print your email, and give you the position of your email within the list generated. ')
# create random email address 
class Email:
   
   # constructor for address and domain 
   def label1(self,label):
      addr = ''
      char = string.ascii_letters + string.digits
      for n in range(0, label):
         addr = addr + char[random.randrange(0, len(char))]
       
      return addr
   # tob leve domain 
   def tld(self):
      tlds = [
       'academy', 'agency', 'ai', 'am', 'app', 'art', 'asia', 'audio', 'au', 'bar',
       'beer', 'bio', 'biz', 'blog', 'br', 'business', 'ca', 'cafe', 'cc', 'center',
       'chat', 'city', 'click', 'cloud', 'cn', 'co', 'com', 'company', 'cool', 'date',
       'de', 'design', 'dev', 'digital', 'edu', 'email', 'energy', 'es', 'eu', 'events',
       'expert', 'fan', 'film', 'finance', 'fit', 'fm', 'food', 'foundation', 'fr', 'games',
       'gg', 'global', 'golf', 'gov', 'group', 'guru', 'health', 'help', 'host', 'hotel',
       'house', 'in', 'info', 'io', 'it', 'jp', 'kr', 'life', 'link', 'live',
       'media', 'me', 'mil', 'mx', 'name', 'net', 'news', 'nl', 'nu', 'online',
       'org', 'photos', 'plus', 'pro', 'ru', 'shop', 'site', 'solutions', 'space', 'store',
       'tech', 'to', 'tv', 'uk', 'us', 'website', 'world', 'ws', 'zone'
      ]
      domain = tlds[random.randrange(0,len(tlds))]
      return domain

    # concatintate address, domain name, top level domain   
   def email(self, label, domain):
      email = f'{self.label1(label)}@{self.label1(domain)}.{self.tld()}'
      # return random email string
      return email

# create list of emails based upon user input
def random_email_list(length):
   email = Email()
   email_list = []
   for i in range(length):
      rand_email = email.email(label, domain)
      email_list.append(rand_email)
   # return email list 
   return email_list

# inserts user defined email string to list of 
def insert_email(user_defined):
   email_list = random_email_list(num_of_emails)
   # inserts user defined email at random index within email list
   email_list.insert(random.randrange(0, len(email_list)), user_defined)
   #returns email list that includes user defined email
   return email_list

# allows time alalysis 
def analyze_func(func_name, n, arr):
    t = Timer()
    t.start()
    func_name(n,arr)
    print(func_name(n, arr))
    t.stop(func_name)

#separator
print("-"*40)
# define email list
l = insert_email(user_defined_email)
#sirt kust before search
l.sort()
# execute search
analyze_func(bisection_iter, user_defined_email, l)
#seperator
print("-"*40)
