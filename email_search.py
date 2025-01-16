import string
import random 
# number of emails generated based user input
# create a email 
# construct string for address
'''
def label1(length):
   addr = ''
   char = string.ascii_letters + string.digits
   for n in range( length):
      addr = addr + char[random.randrange(0, len(char))]
       
   return addr

 # print(email_constructor(8))

 # construct string for domain 
def tld():
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
'''
class Email:
   def label1(self,label):
      addr = ''
      char = string.ascii_letters + string.digits
      for n in range(0, label):
         addr = addr + char[random.randrange(0, len(char))]
       
      return addr

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

   def email(self,domain, label):
      email = f'{self.label1(label)}@{self.label1(domain)}.{self.tld()}'

      return email

print(Email().email(4,5))

'''

# concatintate address and domain name
email =f'{label1(4)}@{label1(2)}.{tld()}'

# create random email list generator
def random_int_list(length):
    random_list = []
    for i in range(length):
        random_list.append(email)
    return random_list

print(email)
# concatinate domain label1, Tld 
    
    # append email address to email list 
    # return email list 

# create a list# emails need to be inserted into a collection list, dectionary etc
# user needs to be able to insert a specific email into the list
# email to be placed into list @ position specified by the user
# application to search for specified email within randomized email list
# application to output time took to find specified email and position email was found

'''
