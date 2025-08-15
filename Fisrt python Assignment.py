##Reverse a string without using built-in function
##CODE:
n = "shiva"
reverse_n = n[::-1]
print(reverse_n)
##OUTPUT:
avihs


##Check if a given string is palindrome or not
##CODE:
n = input("enter a string: ")
if n == n[::-1]:
    print("palindrome")
else:
    print("not palindrome")
##OUTPUT:
enter a string:shiva
not palindrome

enter a string:madam
palindrome


##Count no of vowels and consonants in a string
##CODE:
n = input("enter a string: ")
vowels_count = 0
consonants_count = 0
vowels = "aeiouAEIOU"
for i in n:
    if i in vowels:
        vowels_count+=1
    else:
        consonants_count+=1
print("vowels_count: ")
print("consonants_count: ")
##OUTPUT:
enter a string:shiva
vowels_count:2
consonants_count:3


##Remove all spaces from a given string
##CODE:
n = input("enter a string: ")
result = n.replace(" ", "")
print(result)
##OUTPUT:
enter a string:shiva king
shivaking


##Count the frequency of each charector in a given string
##CODE:
n = input("Enter a string: ")
freq = {}
for char in n:
    freq[char] = freq.get(char, 0) + 1
print("Character frequencies:")
for char, count in freq.items():
    print(char, ":", count)
##OUTPUT:
enter a string:shivas
{s:2,h:1,i:1,v:1,a:1}

