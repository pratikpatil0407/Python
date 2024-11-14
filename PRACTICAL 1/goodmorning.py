import time

p=input("Enter your name:")

current_time=time.strftime("%H:%M:%S") #strft=string format time converts a `datetime' object into a string based on a specified format representing the date and time.
print(current_time)

H=int(time.strftime("%H"))
print(H)

if(H>=5 and H<=12):
    print("Good Morning ",p,"\nHave a Nice Day")
elif(H>=12 and H<=16):
    print("Good Afternoon ",p,"\nHave a Nice Day")
else:
    print("Good Evening ",p,"\n Hope you had great Day")