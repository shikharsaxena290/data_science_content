# l=[1,345,45,"shikhar",True,5+7j,345.56]
# print(type(l))--------->list

# indexing
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[5])
# print(l[6])
# print(l[3][0:3])

# slicing
# print(l[0:5])
# print(l[-1::-1])
# print(l[::2])


# l=[1,2,3]
# l1=[4,5,6]
# print(l+l1)------->concatenation [addition]
# print(l*4)--------->concatenation[multiplication]

# print(len(l))--------->len()

# l.append(4)------------->append()
# print(l)
# l.append(l1)----------->appending list in list nested list
# print(l)

# print(l[3][1])------------->subindexing

# l.extend("shikhar")--------->extend() "extend list by appending elements from iterable"
# print(l)  o/p [1, 2, 3, 's', 'h', 'i', 'k', 'h', 'a', 'r']
# l.extend([4,5,6])
# print(l)

# l.insert(1,"shikhar")
# print(l)
# l.insert(3,300)
# print(l)

# l.pop()--------------------->pop()
# print(l)
# l.pop(1)
# print(l)

# l.remove(2)------------------>remove()
# print(l)
# l1=[1,2,3,[4,5,6],7,8]----------> to remove nested element in list for ex 5
# l1[3].remove(5)
# print(l1)

# l1.reverse()------------------------>reverse()
# print(l1)

# l2=[3,5,7,4,9,8,2,1,6]
# l2.sort()-------------------->sort()
# print(l2)
# print(l2.index(8))---------------->index()
# print(l2.count(4))----------------->count()

# l2[5]=4
# print(l2)#item assignment is possible in list unlike str---->list are mutable

# tuples  :- tuples and list are almost same both have same indexing , slicing concept but the point of differnce is that tuples are immutable , we can't change their values
# t=(2,3,4,5,"shikhar")
# print(type(t)) ----> <class 'tuple'>
# print(len(t))--------->len()
# print(t[0])---------->indexing
# print(t[0:5])--------->slicing

# tuple inbuilt function 
# two types of inbuilt function are there in tuples
# 1.count
# 2.index
# print(t.count(3))
# print(t.index(4))


# sets
s1={2,3,4,5,6,7,8,9}
print(type(s1))
