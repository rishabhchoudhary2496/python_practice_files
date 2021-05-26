#tuples are immutable type like string can not add new items and delete from it
movie_releasing = ('into the wild','Your name',"Silent Voice","Weathring With You")
#tuples are ordered 

first_release = movie_releasing[0]
print(first_release)

# (s1,s2,s3) = movie_releasing
# print(s1,s2,s3)
a ='foo'
b='bar'
a,b =b,a
print(a,b)
a='f'
