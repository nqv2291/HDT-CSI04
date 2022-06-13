list1 = range(1,1000000000)

def findMe(ds,target):
    for i,v in enumerate(ds):
        if v == target:
            return i
        
print(findMe(list1,9736249))