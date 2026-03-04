Questions=[
    {
     "Which of the following creates a tuple?",
    "options":["a) t=(1,2,3)", "b) t=[1,2,3]", "c) t={1,2,3}", "d) t={}"],
     "Your answer (a/b/c/d)": "a"
    },
    {
    "Question 2": "Which language is used for web apps?",
    "options":["a) Python", "b) Java", "c) C++", "d) HTML"],
    "Your answer (a/b/c/d)": "a"
    },
    {
    "Question 3 ": "Which keyword is used for loop?",
    "options":["a) loop", "b) for", "c) while", "d) repeat"],
    "Your answer (a/b/c/d)": "b"
    }
]
score = 0

for i in Questions:
    print(i["Your answer (a/b/c/d)"])
    for opt in i["options"]:
        print(opt)

    user = input("Your answer (a/b/c/d): ")

    if user == i["Your answer (a/b/c/d)"]:
        print("Correct ✅\n")
        score += 1
    else:
        print("Wrong ❌\n")

print("Your Final Score:", score)
print("Great job! keep Practicing")
     
    
