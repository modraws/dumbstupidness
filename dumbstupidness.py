import requests
import os
import time
import sys

updatewarn = input(
    f"\n\033[95mHey, just so you know, you can update me now!\nMakes it easy for when I've got new versions of this file you're executing.\nJust to be clear, I've already been grabbing the newest versions of my entries in assets.json and fleasion.py.\nBut sometimes changes will be made to ME too, and you can update me then!\nKeep an eye out on the dumbstupidness-updates channel for when Mo or Neo updates me!\n\nType 'install' to update me. I'll close after this, so make sure to run me again!\nAny other input will continue to the next step, which is installing Dumbstupidness proper.\n\033[0m")
if updatewarn == "install":
    os.remove("dumbstupidness.py")
    response = requests.get('https://github.com/modraws/dumbstupidness/raw/refs/heads/main/dumbstupidness.py')
    with open('dumbstupidness.py', 'wb') as f:
        f.write(response.content)
    print("\033[95mAlright, Dumbstupidness is updated! Make sure to skip this prompt next time you launch me.\033[0m")
    time.sleep(3)
    sys.exit(0)
else:
    pass

blockwarn = input(
    f"\n\033[32mHey, so, I have this cool little thing where I can reinstall fleasion.py and assets.json.\nThat way, I can make sure everything goes perfectly right when applying Dumbstupidness to Fleasion.\nIt DOES mean that if you've edited those files yourself, those changes will be removed.\nMake backups in that case. I don't want your own progress to be gone.\n\nI can also, alternatively, not reinstall Fleasion, and just bruteforce the installation.\nIf you've installed Dumbstupidness before, you WILL I repeat WILL see duplicate entries in everything.\n\nType 'install' to update and overwrite fleasion.py and assets.json,\n'skip' to bruteforce the Dumbstupidness install,\nor just press ENTER if you're uncertain. I'll close the program for you.\n\033[0m")
if blockwarn == "install":
    os.remove("fleasion.py")
    response = requests.get('https://raw.githubusercontent.com/CroppingFlea479/Fleasion/main/fleasion.py')
    with open('fleasion.py', 'wb') as f:
        f.write(response.content)
    print("\033[32mThat's Fleasion done,\n\033[0m")
    os.remove("assets.json")
    response = requests.get('https://raw.githubusercontent.com/CroppingFlea479/Fleasion/main/assets.json')
    with open('assets.json', 'wb') as f:
        f.write(response.content)
    print("\033[32m...and that's the assets list! Alright, I will now inject my dumbstupid beauty into these newly fetched files.\n")
    time.sleep(3)
elif blockwarn == "skip":
    print("\033[32m...aaalllright, if you're that certain.\033[0m")
    pass
else:
    print("\033[32mYeah, I get that. I'll see you when you really want to install Dumbstupidness. Buhbye!\033[0m")
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
    phrase='match int(options):'

    for (insert_row, line) in enumerate(file2):
        if phrase in line:
            response = requests.get('https://raw.githubusercontent.com/modraws/dumbstupidness/main/dumbstupidness/dumbstupidnesspresets.txt')
            with open('dumbstupidness/dumbstupidnesspresets.txt', 'wb') as f:
                f.write(response.content)
            with open('dumbstupidness/dumbstupidnesspresets.txt', 'r') as file1, open('fleasion.py', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("\033[32mPasted Dumbstupidness presets in fleasion.py.\033[0m\n")

            new_lines = file2_lines[:insert_row+1] + file1_lines + file2_lines[insert_row+1:]
    
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
print("\033[95mAlright, all should be good! Now run Fleasion.py, and hopefully the changes should've been made.")
os.system('pause')
print("\033[0m")"
