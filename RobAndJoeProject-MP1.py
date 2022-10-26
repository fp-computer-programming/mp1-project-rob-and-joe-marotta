# author: RED and JM 10/24/22

# set the variables
v1 = input("adj: ")
v2 = input("noun: ")
v3 = input("place: ")
v4 = input("town: ")
v5 = input("state: ")
v6 = input("verb: ")
v7 = input("person: ") 
v8 = input("noun: ")
v9 = input("name of a Prep student")
v10 = input("noun: ")
v11 = input("name: ")
v12 = input("African country: ")
v13 = input("name of sport: ")
v14 = input("number: ")
v15 = input("place: ")
v16 = input("subject: ")
v17 = input("noun: ")
v18 = input("verb: ")
v19 = input("name of book: ")
v20 = input("verb with ing: ")
v21 = input("name of prep teacher: ")
v22 = input("noun: ")
v23 = input("past tense verb: ")
v24 = input("noun: ")
v25 = input("flavor: ")
v26 = input("adj: ")
v27 = input("name of prep teacher: ")
v28 = input("room: ")
v29 = input("noun: ")
v30 = input("verb: ")
v31 = input("adverb: ")
v32 = input("color: ")
v33 = input("clothing item: ")
v34 = input("subject: ")
v35 = input("object: ")
v36 = input("floor of prep: ")
v37 = input("past tense verb: ")
v38 = input("adj: ")
v39 = input("name of prep administrator: ")
v40 = input("emotion: ")
v41 = input("restaurant: ")
v42 = input("food: ")
v43 = input("drink: ")
v44 = input("food: ")
v45 = input("drink: ")
v46 = input("adj: ")
v47 = input("group of people: ")
v48 = input("personality trait: ")
v49 = input("verb: ")
v50 = input("adj: ")

# Nouns: v2, v8, v10, v17, v22, v24, v29
nouns = [v2, v8, v10, v17, v22, v24, v29] # Put all the noun varibales in a list
for var in nouns: # iterate through the list
    nouns.remove(var) # remove the current noun so it doesn't count itself as a duplicate
    for i in range(0,len(nouns)): # search through each noun in the list
        if var == nouns[i]: # if they are the same
            print(f'You have a duplicate noun: {var}') # prints if you have the same noun and it prints the noun that you is duplicate
            exit() # Stop the code

# Verb: v6, v18, v20, v23, v30, v37, v49
verbs = [v6, v18, v20, v23, v30, v37, v49] # See above
for var in verbs:
    verbs.remove(var)
    for i in range(0,len(verbs)):
        if var == verbs[i]:
            print(f'You have a duplicate verb: {var}')
            exit()

# Subjects: v34, v16
subjects = [v34, v16]
for var in subjects:
    subjects.remove(var)
    for i in range(0,len(subjects)):
        if var == subjects[i]:
            print(f'You have a duplicate subject: {var}')
            exit()

# Place: v3, v15
places = [v3, v15]
for var in places:
    places.remove(var)
    for i in range(0,len(places)):
        if var == places[i]:
            print(f'You have a duplicate place: {var}')
            exit()

# Adjective: v1, v26, v31, v38, v46, v50
adjectives = [v1, v26, v31, v38, v46, v50]
for var in adjectives:
    adjectives.remove(var)
    for i in range(0,len(adjectives)):
        if var == adjectives[i]:
            print(f'You have a duplicate adjective: {var}')
            exit()

# Teacher: v21, v27
teachers = [v21, v27]
for var in teachers:
    teachers.remove(var)
    for i in range(0,len(teachers)):
        if var == teachers[i]:
            print(f'You have a duplicate teacher: {var}')
            exit()

# food: v42, v44
foods = [v42, v44]
for var in foods:
    foods.remove(var)
    for i in range(0,len(foods)):
        if var == foods[i]:
            print(f'You have a duplicate food: {var}')
            exit()
    
# drink: v43, v45
drinks = [v43, v45]
for var in drinks:
    drinks.remove(var)
    for i in range(0,len(drinks)):
        if var == drinks[i]:
            print(f'You have a duplicate drinks: {var}')
            exit()

print("The Story of Mr. Coffey") # Print the title
print('---------------------')

# The story: (used ''' for multiline print)
print(f'''There once was a man, a very {v1} {v2}. He worked at {v3} for many years. 
He was from {v4} and attended {v5}
University for his studies. He loved to {v6} and spent much 
of his time with {v7}. At Fairfield Prep, Mr. Coffey 
taught a class about {v8} and his favorite 
student was {v9}. In his class, Mr. 
Coffey taught students Jesuit ideals and history, and encouraged 
everyone to be a man for {v10}. Mr. Coffey’s 
favorite Jesuit was St. {v11} of {v12}.
Aside from teaching, Mr. Coffey was also the coach of our 
{v13} team, where he led his team to win 
{v14} state championships. 
After working at Fairfield Prep for two years, 
Mr. Coffey went to {v15}
to finish his Jesuit studies of {v16}.
There, he hopes to become ordained into the Society of {v17}.
One day, while Mr. Coffey was {v18} in the Jesuit Residence, 
he found a book called {v19}.  
While he was {v20} with this book, 
he realized his arch nemesis {v21} 
was hiding behind the {v22}. 
Mr. Coffey {v23} behind the {v24} 
in order to hide. While Mr. Coffey watched his nemesis, 
he took a sip of his {v25} flavored coffee, 
which tasted very {v26}. 
Then, Mr. Coffey watched as {v27} 
went into the {v28} 
and stole Mr. Coffey’s expensive {v29}. 
Seeing this, Mr. Coffey decided to {v30} 
after his nemesis. He {v31} grabbed his {v32}
colored {v33} and ran out of the door. 
He realized that the book he was reading was really about {v34}. 
With Mr. Coffey’s knowledge of this subject, he realized what he had to do. 
Using the {v35} he picked up from the ground of {v36}, 
he {v37} it at his nemesis. Mr. Coffey’s nemesis fell down, 
making a {v38} noise. When Mr. Coffee had his nemesis cornered, 
he realized that the person he was chasing was actually {v39}.
When Mr. Coffey realized this, 
he was extremely {v40}.
After seeing that it was not his nemesis, 
he invited them to {v41} for some lunch. 
He ordered {v42} and {v43} and his companion ordered {v44} and {v45}. 
Just like the Jesuits taught him, Mr. Coffey forgave his enemy for his crime. 
At the end of the day, Mr. Coffey is a {v46} 
Jesuit who should be a role model for {v47}. 
From Mr. Coffey, we can all learn to be {v48}, 
and to never {v49} our enemy! Hope you have a {v50} day!
''')
# Joe did nothing ad I did everything