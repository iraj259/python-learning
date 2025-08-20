l=[1,2,3,4,5]
l2=[1,2,3,4,5]

# print(l[0])
# print(l[1:3])
# print(l[::-1])

# l3=[1,2,3,[4,5]]
# print(l3[3][0])

# l4=[[1,2],[3,4],[5,6],[7,8]]
# print(l4[3][1])

# l[0]=100
# print(l)

# adding items
# append for one item and extend for multiple items
# l.append('iraj')
# l.extend([200,'hello',300])
# l.insert(2,'world')
# print(l)

# delete
# del l2
# del l2[0]
# l2.remove(4)
# l2.pop()
# l2.clear()
# print(l2)

# print(len(l))
# print(max(l))
# print(min(l))
# print(sorted(l))
# print(sorted(l,reverse=True))

# l5='hello how are you'
# l6=l5.split()
# print(l6)
# L=[]
# for i in l6:
#     L.append(i.capitalize())
# print(L)
# print(' '.join(L))

# email="abc@gmail.com"
# print(email[:email.find('@')])

# duplicate = [1,1,2,2,3,3,4,4]
# duplicate2=[1,2,3,1]
# unique=[]
# for i in duplicate:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# tuples

# create
t=()
t2=(1,2,3,4,)
t3=(1,'hello','world',2,3,4)
t4=(1,2,3,(3,4))
t5=(1,)
print(type(t5))