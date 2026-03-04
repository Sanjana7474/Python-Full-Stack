'''with open('sample.txt','r') as file:
    content=file.read()
    print(content)'''


'''with open('sample.txt','a') as file:
    file.write('\nPython File operations')'''

'''with open('sample.txt','w') as file:
    file.write('Override')'''


'''import csv

with open('sample.csv','r') as file:
    data=csv.reader(file)
    for row in data:
        #print(row)
        print(row[1])'''


'''import csv

with open('sample.csv','a',newline='\n') as file:
    data=csv.writer(file)
    data.writerow(['5','stalin'])
    data.writerow(['6','poojitha'])'''
'''import csv

with open('products.csv','w',newline='') as file:
    data=csv.writer(file)
    data.writerow(['Product_Ids','Product','Price'])
    data.writerow(['1','laptop','52000'])
    data.writerow(['2','charger','2000'])
    data.writerow(['3','Mouse','500'])
    data.writerow(['4','Tab','32000'])
    data.writerow(['5','iphone','152000'])'''


'''import csv

with open('products.csv','r') as file:
    data=csv.reader(file)
    for i in data:
        print(i)'''


import json
'''with open('demo.json', "w") as file:
    data=[
        {'id':'1','name':'Pooja'},
        {'id':'2','name':'Keerthi'},
        {'id':'3','name':'Teju'},
        ]
    json.dump(data,file,indent=4)
    print("data saved successfully!")'''

with open('demo.json',"r") as file:
        data=json.load(file)
         #for i in data:
         #print(i)'''

data.append({'id':'4','name':'stalin'})
#print(data)
with open('demo.json',"w") as file:
    json.dump(data,file,indent=4)

    
    





    
