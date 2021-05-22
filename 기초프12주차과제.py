#1
def getAverage(vect):
    avg=0
    for elem in vect:
        assert type(elem) is int, 'Cannot calculate invalid arguments'
        try:
            avg+=int(elem)
        except:
            raise AssertionError
    assert len(vect)!=0,'Average result is nan'        
    try:
        avg/=len(vect)
    except:
        raise AssertionEroor
    return avg
try:
    lst=[100, 20, 43, 57, 12, 66, 77,'aaa']
    print("input:{}".format(lst))
    avg=getAverage(lst)
    print("Average result is",int(avg))
except AssertionError as errorMsg:
    print(errorMsg)

#2
def getAverage(vect):
    avg=0
    for elem in vect:
        assert type(elem) is int, 'Cannot calculate invalid arguments'
        try:
            avg+=int(elem)
        except:
            raise AssertionError
    assert len(vect)!=0,'Average result is nan'        
    try:
        avg/=len(vect)
    except:
        raise AssertionEroor
    return avg
try:
    lst=[100, 20, 43, 57, 12, 66, 77]
    print("input:{}".format(lst))
    avg=getAverage(lst)
    print("Average result is",int(avg))
except AssertionError as errorMsg:
    print(errorMsg)

#3
def getAverage(vect):
    avg=0
    for elem in vect:
        assert type(elem) is int, 'Cannot calculate invalid arguments'
        try:
            avg+=int(elem)
        except:
            raise AssertionError
    assert len(vect)!=0,'Average result is nan'        
    try:
        avg/=len(vect)
    except:
        raise AssertionEroor
    return avg
try:
    lst=[]
    print("input:{}".format(lst))
    avg=getAverage(lst)
    print("Average result is",int(avg))
except AssertionError as errorMsg:
    print(errorMsg)