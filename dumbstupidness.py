import requests
import os
import time
import sys

f = open('dumbstupidness/true.txt', "w")
f.write("""mod_cache = True
pf_cache = True
""")
f.close()

blockwarn = input(
    f"\n\033[32mWarning: I have been created to, in all technicalities, delete and reinstall fleasion.py and assets.json.\nThis is so I can inject Dumbstupidness into a fresh clean slate.\nI promise, pinky promise (even though I don't have pinkies), that I won't touch your custom presets.\nI know you put a lot of effort in creating those.\nBut if you've edited either fleasion.py or assets.json yourself,\nI implore you to back-up the changes you've made.\n\nI can also, alternatively, not reinstall Fleasion, and just bruteforce the installation.\nIf you've installed Dumbstupidness before, you WILL I repeat WILL see duplicate entries in everything.\n\nType 'install' to update and overwrite fleasion.py and assets.json,\n'skip' to bruteforce the Dumbstupidness install,\nor just press ENTER if you're uncertain. I'll close the program for you.\n\033[0m")
if blockwarn == "install":
    os.remove("fleasion.py")
    response = requests.get('https://raw.githubusercontent.com/CroppingFlea479/Fleasion/main/fleasion.py')
    with open('fleasion.py', 'wb') as f:
        f.write(response.content)
    print("\033[32mThat's Fleasion done,")
    os.remove("assets.json")
    response = requests.get('https://raw.githubusercontent.com/CroppingFlea479/Fleasion/main/assets.json')
    with open('assets.json', 'wb') as f:
        f.write(response.content)
    print("\033[32m...and that's the assets list! Alright, I will now inject my dumbstupid beauty into these newly fetched files.")
elif blockwarn == "skip":
    print("\033[32m...aaalllright, if you're that certain.")
    pass
else:
    print("\033[32mYeah, I get that. I'll see you when you really want to install Dumbstupidness. Buhbye!")
    time.sleep(3)
    sys.exit(0)

with open('fleasion.py','r') as file2:
    phrase='options = input(": ")'

    for (insert_row, line) in enumerate(file2):
        if phrase in line:
            response = requests.get('https://raw.githubusercontent.com/modraws/dumbstupidness/main/dumbstupidness/custompresetlist.txt')
            with open('dumbstupidness/custompresetlist.txt', 'wb') as f:
                f.write(response.content)
            with open('dumbstupidness/custompresetlist.txt', 'r+') as file1, open('fleasion.py', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("\033[32mAdded entries for Dumbstupidness in the main menu.\033[0m\n")

            new_lines = file2_lines[:insert_row] + file1_lines + file2_lines[insert_row:]
    
            with open('fleasion.py', 'w') as file2:
                file2.writelines(new_lines)
time.sleep(0.3)

with open('fleasion.py','r') as file2:
    phrase='case 0:'

    for (insert_row, line) in enumerate(file2):
        if phrase in line:
            response = requests.get('https://raw.githubusercontent.com/modraws/dumbstupidness/main/dumbstupidness/dumbstupidnesspresets.txt')
            with open('dumbstupidness/dumbstupidnesspresets.txt', 'wb') as f:
                f.write(response.content)
            with open('dumbstupidness/dumbstupidnesspresets.txt', 'r') as file1, open('fleasion.py', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("\033[32mPasted Dumbstupidness presets in fleasion.py.\033[0m\n")

            new_lines = file2_lines[:insert_row] + file1_lines + file2_lines[insert_row:]
    
            with open('fleasion.py', 'w') as file2:
                file2.writelines(new_lines)
time.sleep(0.3)

with open('assets.json','r') as file2:
    phrase='"skins": {'

    for (insert_row, line) in enumerate(file2):
        if phrase in line:
            response = requests.get('https://raw.githubusercontent.com/modraws/dumbstupidness/main/dumbstupidness/dumbstupidnessskins.txt')
            with open('dumbstupidness/dumbstupidnessskins.txt', 'wb') as f:
                f.write(response.content)
            with open('dumbstupidness/dumbstupidnessskins.txt', 'r') as file1, open('assets.json', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("\033[32mPasted Dumbstupidness skins under " + phrase + " in assets.json.\033[0m\n")

            new_lines = file2_lines[:insert_row+1] + file1_lines + file2_lines[insert_row+1:]
    
            with open('assets.json', 'w') as file2:
                file2.writelines(new_lines)
time.sleep(0.3)

with open('assets.json','r') as file2:
    phrase='"reticle replacement": {'

    for (insert_row, line) in enumerate(file2):
        if phrase in line:
            response = requests.get('https://raw.githubusercontent.com/modraws/dumbstupidness/main/dumbstupidness/dumbstupidnessreticles.txt')
            with open('dumbstupidness/dumbstupidnessreticles.txt', 'wb') as f:
                f.write(response.content)
            with open('dumbstupidness/dumbstupidnessreticles.txt', 'r') as file1, open('assets.json', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("\033[32mPasted Dumbstupidness reticles under " + phrase + " in assets.json.\033[0m\n")

            new_lines = file2_lines[:insert_row+1] + file1_lines + file2_lines[insert_row+1:]
    
            with open('assets.json', 'w') as file2:
                file2.writelines(new_lines)
time.sleep(0.3)

with open('assets.json','r') as file2:
    phrase='"hit sounds": {'

    for (insert_row, line) in enumerate(file2):
        if phrase in line:
            response = requests.get('https://raw.githubusercontent.com/modraws/dumbstupidness/main/dumbstupidness/dumbstupidnesssounds.txt')
            with open('dumbstupidness/dumbstupidnesssounds.txt', 'wb') as f:
                f.write(response.content)
            with open('dumbstupidness/dumbstupidnesssounds.txt', 'r') as file1, open('assets.json', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("\033[32mPasted Dumbstupidness sounds under " + phrase + " in assets.json.\033[0m\n")

            new_lines = file2_lines[:insert_row] + file1_lines + file2_lines[insert_row:]
    
            with open('assets.json', 'w') as file2:
                file2.writelines(new_lines)
time.sleep(0.3)

checkwarn = input(
    f"\n\033[95mHey, if you want, I can also disable the cache checks.\nI get how annoying they become after a few times of wiping cache, trust me.\nJust let me do my magic.\nType 'disable' to proceed, any other input will stop this program from changing cache checking settings.\n\033[0m")
if checkwarn == "disable":
    with open('fleasion.py','r') as file2:
        phrase='pf_cache = False'

        for (insert_row, line) in enumerate(file2):
            if phrase in line:
                with open('dumbstupidness/true.txt', 'r') as file1, open('fleasion.py', 'r') as file2:
                    file1_lines = file1.readlines()
                    file2_lines = file2.readlines()

                print("Boom!\n")

                new_lines = file2_lines[:insert_row+1] + file1_lines + file2_lines[insert_row+1:]

                with open('fleasion.py', 'w') as file2:
                    file2.writelines(new_lines)
                os.remove('dumbstupidness/true.txt')
else:
    os.remove('dumbstupidness/true.txt')
    pass
