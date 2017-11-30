# 空元组
foo = ()
# 元组 只有一个元素的元组
zoo = ('python','elephent','snake')
print('Number of animals in the zoo is',len(zoo))


new_zoo = 'monkey','camel',zoo
print('Numbers of animals in the zoo is',len(new_zoo))

print('All the animals in the zoo is',new_zoo)

print('Animals brought from old zoo are',new_zoo[2])
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals int the new zoo is',len(new_zoo)-1+len(new_zoo[2]))
