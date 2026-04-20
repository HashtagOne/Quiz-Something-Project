dict = {
    "Balls": ["Basketball", "Football", "Tennis Ball"],
    "Balls 2": ["8-Ball", "Baseball", "Golf Ball"]
}

def ball_picker(prompt, options):
    options = list(options)
    while True:
        print(f"\n{prompt}")
        for option in options:
            print ("-", option)

        choice = input("Enter your choice: ").strip().lower()

        for option in options:
            if choice == option.lower():
                return option

chosen_ball = ball_picker("Available balls:", dict.keys())
