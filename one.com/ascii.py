# -*- coding: utf8 -*- 



def ascii(self):
    code = self.lower()
    if '!' in code:
        return self.replace('!','%21')
    elif '#' in code:
         return self.replace('#','%23')
    elif '$' in code:
         return self.replace('$','%24')
    elif '%'in code:
         return self.replace('%','%25')
    elif '&' in code:
         return self.replace('&','%26')
    elif "'" in code:
         return self.replace("'",'%27')
    elif '(' in code:
         return self.replace('(','%28')
    elif ')'in code:
         return self.replace(')','%29')
    elif '*' in code:
         return self.replace('*','%2A')
    elif '+' in code:
         return self.replace('+','%2B')
    elif '@' in code:
         return self.replace('@','%40')
    else:
        return self

