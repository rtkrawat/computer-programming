#Given the menu of the two restaurants. There may be a chance of fight between them if any one of them have any item in common and you surely don't want that to happen. Each of the menu has 5 items (strings) in them. So, your task is to find out if there is any need to change the menu or let them be happy with their respective menu.
def is_common(self, s, t):
        c=0
        for i in s:
            if i in t:
                c+=1
            else:
                pass
        if c>=1:
            return("CHANGE")
        else:
            return("BEHAPPY")
