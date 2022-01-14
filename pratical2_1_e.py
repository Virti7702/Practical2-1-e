'''
Name - Virti Shah
ID - 20CE135
Aim - A python program to concatenate following dictionaries to one.
Github link - https://github.com/Virti7702/Practical2-1-e.git

'''

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print (dic4)