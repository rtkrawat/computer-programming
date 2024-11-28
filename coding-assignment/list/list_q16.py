# Given an array arr containing equal number of positive and negative elements, arrange the array such that every positive element is followed by a negative element.
def arranged(self,arr):
        p=[]
        n=[]
        for i in arr:
            if i<0:
                n.append(i)
            else:
                p.append(i)
        p.sort()
        n.sort()
        o=n[::-1]
        l=[]
        j=0
        for i,k in zip(p,o):
            l.append(i)
            l.append(k)
            j+=1
        if len(p)>len(o):
            l.append(p[j])
        elif len(o)>len(p):
            l.append(o[j])
            
        return l
        
