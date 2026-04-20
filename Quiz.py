
########## TOOLS ###########

import time
import random
import json
import os

################# UX & UTILITIES ####################
def pause(seconds=1):
    time.sleep(seconds)

def typewriter(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

############## INPUT & VALIDATION ########################
def ask_credentials(prompt, mode):
    while True:
        typewriter(prompt)
        answer = input().strip()

        if mode == "letters" and answer.replace(" ", "").isalpha():
            return answer

        elif mode == "numbers" and answer.isdigit():
            return int(answer)

        typewriter("Invalid answer, please try again.")

def choose_option(prompt, options):
    options = list(options)
    while True:
        typewriter(f"\n{prompt}")
        for option in options:
            print("-", option)

        choice = input("Your choice: ").strip().lower()

        for option in options:
            if choice == option.lower():
                return option

        print("Invalid choice. Try again.")

################### SCORING W/ LEADERBOARD ##########################

def save_score(name, topic, score, total, filename):
    os.makedirs("data", exist_ok=True)
    scores = load_scores(filename)

    new_entry = {
        "name": name,
        "topic": topic,
        "score": score,
        "total": total,
    }

    scores.append(new_entry)
    with open(filename, "w") as f:
        json.dump(scores, f, indent=4)

    typewriter ("Your score has been successfully saved!")

def load_scores(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def show_leaderboard(topic):
    all_scores = []

    for filename in os.listdir("data"):
        if filename.endswith(".json"):
            filepath = f"data/{filename}"
            scores = load_scores (filepath)
            all_scores.extend(scores)

    topic_scores = [entry for entry in all_scores if entry["topic"] == topic]
    topic_scores.sort(key=lambda x: x["score"], reverse=True)

    print (f"\n--- Leaderboard for: {topic} ---")

    if not topic_scores:
        typewriter("No scores saved for this topic yet.")
        return

    for i, entry in enumerate(topic_scores, start=1):
        print(f"{i}. {entry['name']} - {entry['score']}/{entry['total']}")


#################### QUIZ LOGIC ########################################

def ask_question(question, right_answer):
    typewriter(question)
    answer = input().strip().lower()

    ### lowers letters into lowercase no matter what the input is #####
    if answer in [ans.lower() for ans in right_answer]:
        typewriter("That's correct!\n")
        return 1
    else:
        typewriter(f"Unfortunately, that's wrong! The right answer is: {right_answer[0]}\n")
        return 0

def run_quiz():
    chosen_topic = choose_option("Available topics:", quiz.keys())
    chosen_sub = choose_option(
        f"Subtopics under {chosen_topic}",
        quiz[chosen_topic]
    )

    score = 0

    all_questions = sub_topics[chosen_sub][:]
    random.shuffle(all_questions)

    for questions, answers in all_questions:
        score += ask_question(questions, answers)

    total = len(sub_topics[chosen_sub])
    print(f"Final Score: {score}/{total}")
    pause(3)

    if score == total:
        print(f"Wow! You got a {score} out of {total}! A perfect score!")
    elif score >= total * 0.6:
        print(f"You got... a {score} out of {total}! Nice one!")
    else:
        print(f"You got a {score} out of {total}! Not bad, but it could be better.")
    pause(2)
    typewriter("\nWould you like to save your score? (yes/no) ")
    save_choice = input().strip().lower()

    if save_choice in ["yes", "y", "yeah", "yup", "sure", "fine"]:
        save_score(username, chosen_sub, score, total, filename)

    show_leaderboard(chosen_sub)

######################## DICTIONARIES #################################

quiz = {
    "Science": ["Biology", "Geography"],
    "Social Sciences": ["Geopolitics"]
}

sub_topics = {
    "Biology": [
        ("What is the powerhouse of the cell? ", ["mitochondria"]),
        ("What substance is main component of a plant's cell wall? ", ["cellulose"]),
        ("What's the main thing that plants use to initiate photosynthesis? ", ["sunlight"]),
        ("what is the name of the specific metabolic process by which cells break down glucose in the absence of oxygen to produce energy? ", ["fermentation"]),
        ("Which protein in red blood cells is responsible for carrying oxygen? ", ["hemoglobin"]),
    ],
    "Geography": [
        ("What is the largest desert in the world? ", ["antarctica"]),
        ("Which continent is said to have land in all four hemispheres? ", ["africa"]),
        ("What is the deepest point in the world's oceans? ", ["challenger deep"]),
        ("Which imaginary line divides the Earth into the Northern and Southern Hemispheres?", ["equator"]),
        ("Which specific type of rock is formed from the cooling and solidification of magma?", ["igneous"]),
    ],
    "Geopolitics": [
        ("What do you call the official power of a country to reject a proposal or bill?", ["veto"]),
        ("What is the term for a country that is completely surrounded by the territory of other countries?", ["landlocked"]),
        ("What term describes a state that has total authority over its own territory?", ["sovereignty"]),
        ("Which term refers to the soft power or influence a nation exerts through culture and values?", ["hegemony"]),
        ("Which international organization was established in 1945 to maintain global peace?", ["united nations", "UN"]),
    ]
}

################### MAIN PROGRAM ###################

typewriter("Let's answer a quiz!")
pause(3)
print("-" * 30)

username = ask_credentials("First off, what is your name? ", "letters")
username = username.title()
filename = f"data/scores_{username.lower()}.json"
typewriter(f"Nice name, {username}!")
pause(2)
print()
age = ask_credentials(f"Okay, {username}, how old are you? ", "numbers")
if age >= 9:
    typewriter('You are just old enough to answer the quiz! Congratulations!')
    pause(2)
else:
    typewriter('You are too young to answer the quiz, unfortunately..')
    exit()
print()

typewriter(f"Anyways, it seems that you are {age} years old. That's a pretty good age if I do say so myself.")
pause(2)
print()
typewriter("Let us start, shall we?")
pause(2)

while True:
    run_quiz()
    pause(2)
    typewriter("\nWould you like to play again? (yes/no) ")
    again = input().strip().lower()
    if again not in ["yes", "y"]:
        typewriter(f"Thanks for playing, {username}! See you next time.")
        break


