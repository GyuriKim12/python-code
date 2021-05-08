#1
def generateDictionary(n):
    dic={}
    for i in range(n):
        word=input("프로그래밍 언어 이름: ")
        desc=input('프로그래밍 언어 설명: ')
        dic[word]=desc
        
    return dic

def translateDictionary(dic):
    new_dic={}
    for word in dic:
        print('=영어사전 생성=')
        print("discription:", dic[word])
        new_word=input('Input the name of the language in English: ')
        new_desc=input('Input the description of the language in English: ')
        new_dic[new_word]=new_desc

    return new_dic


n=int(input('Input number of keys: '))
dic1=generateDictionary(n)
dic2=translateDictionary(dic1)
print('=결과 사전 출력=')
print(dic1)
print(dic2)

#2
def generateDictionary(n):
    dic={}
    for i in range(n):
        word=input("프로그래밍 언어 이름: ")
        desc=input('프로그래밍 언어 설명: ')
        dic[word]=desc
        
    return dic

def translateDictionary(dic):
    new_dic={}
    for word in dic:
        print('=영어사전 생성=')
        print("discription:", dic[word])
        new_word=input('Input the name of the language in English: ')
        new_desc=input('Input the description of the language in English: ')
        new_dic[new_word]=new_desc
  
    return new_dic

def searchDictionary(*dicts):
    while True:
        Dic=[]
        a=input('Enter a word for serch: ')
        for dic in dicts:
            for word in dic:
                if a in dic[word]:
                    Dic.append(word)
        if Dic!=[]:
             print("Search result: ",Dic)
        else:
            print("No match!! Break!")
            break

n=int(input('Input number of keys: '))
dic1=generateDictionary(n)
dic2=translateDictionary(dic1)
searchDictionary(dic1,dic2)