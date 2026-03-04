data=[
    ["Which of the following creates a tuple?","t=(1,2,3)","t=[1,2,3]","t={1,2,3}"," t={}","t=(1,2,3)"],
    ["Which language is used for web apps?","Python","Java","Html","C","Html"]]
score=0
for i in data:
    print(f"Question: {i[0]}")
    print(f"a) {i[1]}")
    print(f"b) {i[2]}")
    print(f"c) {i[3]}")
    print(f"d) {i[4]}")
    ans=input("Your answer (a/b/c/d):")
    if ans==i[5]:
        print("Correct ✅")
        score+=1
    else:
        print(f"Wrong ❌ The correct answer is'{i[5]}'")
print(f" Your Final score: {score}/len(data)")
    
