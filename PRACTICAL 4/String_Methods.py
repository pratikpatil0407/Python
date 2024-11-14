p="! !!Pratik!!!"
print(p)
print(len(p))

print(p.upper()) #converts p string into upper case
print(p.lower()) #converts p string into lower case

print(p.split(" ")) #converts string into list with whitespace seperating it
print(p.strip("!")) #here strip will remove ! characters which is before or after in a string
print(p.rstrip("!")) #here rstrip will remove trailing characters in string here it is ! but it will not remove trailing characters written before string

print(p.replace("Pratik","Patil")) #replaced Pratik with Patil
print(p.count("!")) #here it will count how many times ! has come in our string

print(p.endswith("!")) #here it will check whether our string ends with ! as given in parameter and it will give boolean output 
print(p.startswith("P")) #here it will check whether our string starts with P as given in parameter and it will give boolean output

string="python Programming"
print(string.capitalize()) #only converts first character into upper case and other characters into lower case
print(string.swapcase()) #changes lowercase characters to uppercase characters

str1="I am studying in T.Y CSE"
print(str1.center(40,".")) #Here our string will print after 40 blank spaces as mentioned

print(str1.find("in")) #Here it will find where is "in" in string and returns index number 
print(str1.find("and")) #Here "and" is not available in string so it will return index -1 
# print(str1.index("and")) #Here it will give us exception(error) ValueError: substring not found

str2 = "Pratik0407"
print(str2.isalnum()) #Returns true if the entire string only consists of A-Z, a-z, 0-9.
print(str2.isalpha()) #Returns true if the entire string only consists of A-Z, a-z.

str3="PRATIK"
print("Given string ",str3," is in uppercase is ",str3.isupper()) #Gives output true if our string is in uppercase
print("Given string ",str3," is in lowercase is ",str3.islower()) #Gives output true if our string is in lowercase

who="world health organization"
WHO=who.title() #converts each first character of string in capital letters
print(WHO)
print(WHO.istitle()) #returns true if each first character is in capital letters