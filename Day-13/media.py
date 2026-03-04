print("Media Gallery:")
'''Media={
    1:"beach.png",
    2:"mountain.jpg",
    3:"party.jpg",
    4:"selfie.png",
    5:"birthday.png",
    6:"dance.mp4",
    7:"movie.mp4",
    8:"song.mp4"
}'''
Media=["beach.png","mountain.jpg","party.jpg","selfie.png","dance.mp4","movie.mp4"]

for i in Media:
    print(i)
select=set(input("select photos to share: ").split(','))

print("Sharing The following media:")
photos=[]
videos=[]
for i in Media:
    if i.endswith('.mp4'):
        videos.append(i)
    else:
        photos.append(i)
for i in photos:
    print(i)
for i in videos:
    print(i)
for i in select:
    if i in Media:
        print(f'{i}-sent')
    else:
        print(f'{i}-file not found')
        
