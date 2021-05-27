class HashMap(object):
    
    def __init__(self):
        self.container={}

    def insert(self,key,value):
        if key not in self.container:
            self.container[key]=value
        else:
            if self.container[key]==value:
                pass
            else:
                print('The key',key,'is already in the hashMap!')
        
    def delete(self,key):
        try:
            if key in self.container:
                del self.container[key]
            else:
                raise ValueError
        except ValueError:
              print('Cannot remove the key',key+'!','it is not in the hashMap!')

    def get(self,key):
        try:
            return self.container[key]
        except:
            return None

    def contain(self,key):
        return key in self.container

    def scoreSort(self):
        values=[]
        for key in self.container:
            values.append(self.container[key])
        values.sort()
        return values

    def __str__(self):
        result1=''
        result=''
        for key in self.container:
            result+=result+"'"+key+"'"+':'+str(self.container[key])+','
            result1+=result
            result=''
        return "{"+result1[:-1]+"}"

hashMap=HashMap()
hashMap.insert("a",1)
hashMap.insert("a",100)
try:
    hashMap.delete("c")
except ValueError as msg:
    print(msg)
hashMap.insert("b",100)
hashMap.insert("c",50)
hashMap.insert("d",20)
hashMap.insert("f",70)
print(hashMap.scoreSort())
print(hashMap)