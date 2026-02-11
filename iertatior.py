l=[1,2,3,4,5]
item=iter(l)
print(next(item))
print(next(item))
print(next(item))
print(next(item))


'''
#Custom Itreation
class count:
    def __init__(self,start,end):
        pass  #placholder
    def __iter__():
        pass #placeholder
    def __next__():
        pass #plachodler

'''

class count:
    def __init__(self,start,end):
        self.current=start
        self.end=end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current<=self.end:
            value=self.current
            self.current+=1
            return value
        else:
            raise StopIteration
        
c=count(1,5)

for num in c:
    print(num)