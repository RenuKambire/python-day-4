# print the numbers upto 1 to 100
i=1
while i<=100 :
    print(i)
    i+=1

# print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1    

# print the multiplication table of a number n.
n = int(input("enter the number ="))
i =1
while i<=10: 
    print(i*n)
    i+=1

#print the elements  of the following list using a loop
nums =[1,4,9,16,25,36,49,64,81,100]

idx =0
while idx < len(nums):
    print(nums[idx])
    idx +=1

#search for a number x in this tuple using loop.
a =(1,4,9,16,25,36,49,64,81,100)
x = 36
i =0
while i < len(a):
    if(a[i]==x):
       print("found the no. =",i)
    i+=1  


