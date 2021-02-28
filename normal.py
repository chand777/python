# data should be collection because collection has mutable property 
first_list=[[1,2,3,4],[5,6,7,8]]
second_list=first_list

print(first_list)
print(second_list)

second_list[0][1]=1000  
print(first_list)   # you can see here value for both the list changed because there are refering to the same memory location 
print(second_list)