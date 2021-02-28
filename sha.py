# first_list=[1,2,3,4]
# second_list=first_list.copy()
# print(first_list)
# print(second_list)

# second_list[1]=1000
# print(first_list)
# print(second_list)  #Here you can see that item for second_list only changed not for first_list because both the list has diffrent diffrent location 

# first_list=[[1,2,3,4],[5,6,7,8]] # defination of shallow list will change when we will use nested list
# second_list=first_list.copy()
# print(first_list)
# print(second_list)
# first_list[0][1]=1000
# print(first_list)     #here you can see that value is changed for both the list because it is refreaing to same object inside the nested list
# print(second_list)

first_list=[[1,2,3,4],[5,6,7,8]]
second_list=first_list.copy()
first_list.append([9,10,11,12])
print(first_list)               # here you can see it is appended only on first_list not in second_list because they are refaring to different memory location
print(second_list)