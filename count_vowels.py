# program to count the number of vowels in a string

vowels = 'aeiou'

my_string = " Hello My name is Gautam Kumar kushwaha. I am the student of computer sceince and Engineering. And I am doing too much laziness. I have to work very hard at least 10 hours of coding everyday to complete DSA, Operating system, System Design and Architecture, Networking and Security, Web and App Development, Clouds and Devops. Lets do 10 hours of coding, Gautam you can do it.. Lets do it Gautam, 10 hours of coding. Lets do it.. You can do it... And you have to do it.. Lets make it.. As you complete the 10 hours of coding, you will be able to called as a programmer, and You will land a exciting job, in the multinational company, along with your starup ideas and business forms. You can still keep on working on these forms, and keep people to work on these ideas."

my_string = my_string.casefold()

count = {}.fromkeys(vowels, 0)


# count the vowels

for char in my_string:
    if char in count:
        count[char] += 1
        
        
print(count)