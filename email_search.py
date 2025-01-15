import string
import random 
# number of emails generated based user input
# create a email 
# construct string for address
def email_constructor(length):
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

# concatinate domain label1, Tld 
    # concatintate address and domain name
    # append email address to email list 
    # return email list 

# create a list# emails need to be inserted into a collection list, dectionary etc
# user needs to be able to insert a specific email into the list
# email to be placed into list @ position specified by the user
# application to search for specified email within randomized email list
# application to output time took to find specified email and position email was found

   