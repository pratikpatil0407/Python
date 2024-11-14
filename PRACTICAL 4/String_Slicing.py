fruit="watermelon"
      #0123456789
print(len(fruit)) #len=gives length of our string

#String Slicing

print(fruit[0:10]) # here it will print characters from 0th index to n-1 i.e 10 elements
print(fruit[:5])  #Slicing from Start python will take 0 by default

print(fruit[5:])   #Slicing till End python will take end as last index n-1
print(fruit[2:8])     #Slicing in between

print(fruit[1:-2])    #Slicing using negative index here python will take -2 as len-2 i.e 10-2=8 i.e It will print from 1st index to 7th index