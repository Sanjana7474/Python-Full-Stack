
data={
    'megha':{"status":False,"python":None,"sql":None},
    'sai':{"status":True,"python":96,"sql":85},
    'sree':{"status":True,"python":44,"sql":55},
    'chay':{"status":True,"python":90,"sql":58}
    }
user=input()
if user in data:
    if data[user]["status"]:
        sum=data[user]["python"]+["sql"]
        avg=sum/2
        if avg>80:
            print(f"{user}, pass")
        elif avg<30:
            print(f"{user},fail betterluck next time")
    else:
        print("not write any exam")
else:
    print(f"{user},fail")
