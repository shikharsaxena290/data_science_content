# a=1+1
# print(a*9)
# a=10
# b=12
# print(a+b)
# print(type(a))-------> int

# c=2.09
# print(type(c))-------->float

# c=2.999900393933
# print(type(c))--------->float

# st="shikhar"
# print(type(st))--------->string

# e=True
# print(type(e))---------->boolean

# print(True*False)
# print(True*True)
# print(False*False)
# print(False*True)

# print(True/False)
# print(True/True)
# print(False/False)
# print(False/True)

# d=2j+3
# print(type(d))--------->complex
# inbuilt function related to complex
# print(d.imag)------->imag function gives imaginary number of complex varibale d
# print(d.real)------->real function gives real number of complex variable

# s="pwskills"

# indexing
# print(s[0]) 
# print(s[1]) 
# print(s[2]) 
# print(s[3]) 
# print(s[4]) 
# print(s[5]) 
# print(s[6]) 
# print(s[7])                                     

# reverse indexing
# print(s[-1]) 
# print(s[-2]) 
# print(s[-3]) 
# print(s[-4]) 
# print(s[-5]) 
# print(s[-6]) 
# print(s[-7]) 
# print(s[-8])  

#slicing
# print(s[0:2])   
# print(s[0:7:2]) 
# print(s[::-1])
# print(s[-1:-6:-2])
# print(s[-8:-1:2])
# print(s[7::-1])

# s="this is my string!"
# print(len(s))------->len()
# print(s.find("s"))--->find()
# print(s.count("t"))----->count()
# print(s.upper())-------->upper()
# print(s.lower())--------->lower()
# print(s.title())--------->title()
# print(s.capitalize())----->capitalize()

# concatenation
# s="this is my string!"
# print(s+" "+"welcome to python")----->addition
# s="shikhar"
# print(s*3)------------->multiplication

# str="shikhar"
# s[0]="p"
# print(s)# error :- 'str' object does not support item assignment----> str are immutable

# print(str.replace('s','a'))#-------> temporary changes , if we print str again it will show original data

#sets
# my_set={}
# print(type(my_set))

# my_set={1.0 , "hello",(1,2,3)}
# print(type(my_set))
# my_set.add(2.0)
# my_set.add(3.0)
# my_set.add(4.0)
# print(my_set)
# print(my_set[1:4])
# my_set.remove(1.0)
# print(my_set)

#dictionaries
# d={}
# print(type(d))
# d1={'apple':'fruite','bangan':'vegetable','hindi':'language'}
# print(d1)
# print(d1['apple'])
# print(d1['bangan'])
# print(d1['hindi'])

# d2={'name':'shikhar','email':'shikharsaxena092@gmail.com','name':'shikhar saxena'}
# print(d2['name'])
d3={'name':'shikhar','age':20,'email':'ss@gmail.com','fav_no':2345,21:22,'float':2.0,'complex':5j+3,'items':['a','b','c','d']}
# print(d3)
print(d3['name'])
print(d3.get('age'))
print(d3.keys())
print(d3.values())
# d3['name']='shikhar saxena'
# print(d3)
d3.update({'name':'shiki'})
print(d3)