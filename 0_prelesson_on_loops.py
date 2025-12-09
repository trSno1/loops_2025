# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# While loops  
#if looping is available then that means it is an iteration
for x in range(1,11):
    print(x)

print("HAPPY NEW YEAR")
for x in range(1,21):
    if x == 13:
        break
else:
    print(x)

print("HAPPY NEW YEAR")
for x in range(1,21):
    if x == 13:
        continue
else:
    print(x) 
    
    
    
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
        if subject == "History":
            break
        print(subject)




for index in range*(len(subjects)):
    print("Subject " + str(index) + ":" + subject[index])

