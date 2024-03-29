# remove punctuation from a sentence

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = ' Hello!!!, he said ---and went.'

no_punt = " "

for char in my_str:
    if char not in punctuation:
        no_punt += char
print(no_punt)