import time
def pause(seconds=1):
    time.sleep(seconds)

def typewriter(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

typewriter("Let's answer a quiz!")
pause(3)
print("-" * 30)

def ask_credentials(prompt, mode):
    while True:
        typewriter(prompt)
        answer = input().strip()

        if mode == "letters" and answer.replace(" ", "").isalpha():
            return answer

        elif mode == "numbers" and answer.isdigit():
            return int(answer)

        typewriter("Invalid answer, please try again.")

def ask_question(question, right_answer):
    typewriter(question)
    answer = input().strip()
    if answer in right_answer:
        typewriter("That's correct! Moving on-", 0.05)
        print()
        return True
    else:
        typewriter("Unfortunately, that's not correct.", 0.05)
        return False

username = ask_credentials("First off, what is your name? ", "letters")
typewriter(f"Nice name, {username}!")
pause(2)
print()
age = ask_credentials(f"Okay, {username}, how old are you? ", "numbers")
if age >= 9:
    typewriter('You are just old enough to answer the quiz! Congratulations!')
    pause(3)
else:
    typewriter('You are too young to answer the quiz, unfortunately..')
    exit()
print()

typewriter(f"Anyways, it seems that you are {age} years old. That's a pretty good age if I do say so myself.")
pause(4)
print()
typewriter("Let us start, shall we?")
pause(3)

topics = {
    "biology": [
        ("What is the powerhouse of the cell? ", ["mitochondria"]),
        ("What substance is main component of a plant's cell wall? ", ["cellulose"]),
        ("What's the main thing that plants use to initiate photosynthesis? ", ["sunlight"]),
        ("what is the name of the specific metabolic process by which cells break down glucose in the absence of oxygen to produce energy? ", ["fermentation"]),
        ("Which protein in red blood cells is responsible for carrying oxygen? ", ["hemoglobin"]),
    ],
    "geography": [
        ("What is the largest desert in the world? ", ["antarctica"]),
        ("Which continent is said to have land in all four hemispheres? ", ["africa"]),
        ("What is the deepest point in the world's oceans? ", ["challenger deep"]),
        ("Which imaginary line divides the Earth into the Northern and Southern Hemispheres?", ["equator"]),
        ("Which specific type of rock is formed from the cooling and solidification of magma?", ["igneous"]),
    ],
    "geopolitics": [
        ("What do you call the official power of a country to reject a proposal or bill?", ["veto"]),
        ("What is the term for a country that is completely surrounded by the territory of other countries?", ["landlocked"]),
        ("What term describes a state that has total authority over its own territory?", ["sovereignty"]),
        ("Which term refers to the soft power or influence a nation exerts through culture and values?", ["hegemony"]),
        ("Which international organization was established in 1945 to maintain global peace?", ["united nations", "UN"]),
    ]
}

def choose_topic(topics):
    print("-" * 30)
    typewriter("Available topics:")
    for topic in topics:
        print("-", topic)
    print()

    while True:
        print()
        typewriter("Choose a topic:")
        choice = input().lower().strip()
        if choice in topics:
            return choice
        typewriter("Invalid topic, try again.")

selected_topic = choose_topic(topics)
questions = topics[selected_topic]

score = 0

for question, right_answer in questions:
    if ask_question(question, right_answer):
        score += 1
if score == 5:
    print(f"Wow! You got a {score} out of 5! A perfect score!")
elif 3 <= score < 5:
    print(f"You got... a {score} out of 5! Nice one!")
else:
    print(f"You got a {score} out of 5! Not bad, but it could be better.")

