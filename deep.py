import copy
# first_list=[1,2,3,4]
# second_list=copy.deepcopy(first_list)
# print(first_list)
# print(second_list)

# second_list[1]=1000
# print(first_list)
# print(second_list) # here you can see value is chaged for second_list only and it works same as shallow copy when we have non nested list
first_list=[[1,2,3,4],[5,6,7,8]]
second_list=copy.deepcopy(first_list)
print(first_list)
print(second_list)

second_list[0][1]=100
print(first_list)
print(second_list) #here you can see value is changed for second_list only not like shallow copy where value will be changed in both the list it because object will have diffrent location 

