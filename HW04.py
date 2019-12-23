months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','Spetember', 'October', 'November', 'December']

for month in months:
    if month[0] == 'J':
        print(month)

for i in range(0, 100):
    if i % 2 == 0 and i%5 == 0:
        print(i)

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for words in horton:
    for vowel in vowels:
        if vowel in words:
            print(vowel, sep=' ', end='', flush=True)
