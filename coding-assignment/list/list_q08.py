# Given an array of car numbers car[], an array of penalties fine[], and an integer value date. The task is to find the total fine which will be collected on the given date. The fine is collected from odd-numbered cars on even dates and vice versa.
def totalFine(self, date, car, fine):
        k=[]
        if date%2==0:
            for i,j in zip(car,fine):
                if i%2!=0:
                    k.append(j)
                else:
                    pass
        else:
            for i,j in zip(car,fine):
                if i%2==0:
                    k.append(j)
        return sum(k)
