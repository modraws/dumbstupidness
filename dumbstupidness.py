import requests
import os

blockwarn = input(
    f"\n\033[32mWarning: I have been created to, in all technicalities, delete and reinstall fleasion.py and assets.json.\nThis is so I can inject Dumbstupidness into a fresh clean slate.\nI promise, pinky promise (even though I don't have pinkies), that I won't touch your custom presets. I know you put a lot of effort in creating those.\nI can also, alternatively, not reinstall Fleasion, and just perform checks on if Dumbstupidness is installed or not.\nYou probably won't get the newest updates because of this, but better to be safe than sorry.\nType 'done' to proceed, any other input will cancel the reinstallation process and continue with routine checks.\n\033[0m")
if blockwarn == "done":
    os.remove("fleasion.py")
    response = requests.get('https://raw.githubusercontent.com/CroppingFlea479/Fleasion/main/fleasion.py')
    with open('fleasion.py', 'wb') as f:
        f.write(response.content)
    print("That's Fleasion done,")
    os.remove("assets.json")
    response = requests.get('https://raw.githubusercontent.com/CroppingFlea479/Fleasion/main/assets.json')
    with open('assets.json', 'wb') as f:
        f.write(response.content)
    print("...and that's the assets list! Alright, I will now inject my dumbstupid beauty into these newly fetched files.")
else:
    pass

with open('fleasion.py','r') as file2:
    phrase='options = input(": ")'
    badphrase='custom replacement lists:'

    for (insert_row, line) in enumerate(file2):
        if badphrase in line:
            break
        if phrase in line:
            response = requests.get('https://raw.githubusercontent.com/modraws/dumbstupidness/main/dumbstupidness/custompresetlist.txt')
            with open('dumbstupidness/custompresetlist.txt', 'wb') as f:
                f.write(response.content)
            with open('dumbstupidness/custompresetlist.txt', 'r+') as file1, open('fleasion.py', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("Added entries for your custom presets!")

            new_lines = file2_lines[:insert_row] + file1_lines + file2_lines[insert_row:]
    
            with open('fleasion.py', 'w') as file2:
                file2.writelines(new_lines)

with open('fleasion.py','r') as file2:
    phrase='case 0:'
    badphrase='mo_option'

    for (insert_row, line) in enumerate(file2):
        if badphrase in line:
            break
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

with open('fleasion.py','r') as file2:
    phrase='case 0:'
    badphrase='mo_option'

    for (insert_row, line) in enumerate(file2):
        if badphrase in line:
            break
        if phrase in line:
            response = requests.get('https://raw.githubusercontent.com/modraws/dumbstupidness/main/dumbstupidness/dumbstupidnessreticles.txt')
            with open('dumbstupidness/dumbstupidnessreticles.txt', 'wb') as f:
                f.write(response.content)
            with open('dumbstupidness/dumbstupidnesspresets.txt', 'r') as file1, open('fleasion.py', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("\033[32mPasted Dumbstupidness presets in fleasion.py.\033[0m\n")

            new_lines = file2_lines[:insert_row] + file1_lines + file2_lines[insert_row:]
    
            with open('fleasion.py', 'w') as file2:
                file2.writelines(new_lines)

with open('assets.json','r') as file2:
    phrase='"reticle replacement": {'
    badphrase='18580671315'

    for (insert_row, line) in enumerate(file2):
        if badphrase in line:
            break
        if phrase in line:
            with open('dumbstupidness/dumbstupidnessreticles.txt', 'r') as file1, open('assets.json', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("\033[32mPasted Dumbstupidness replacement reticles under " + phrase + " in assets.json.\033[0m\n")

            new_lines = file2_lines[:insert_row+1] + file1_lines + file2_lines[insert_row+1:]
    
            with open('assets.json', 'w') as file2:
                file2.writelines(new_lines)

with open('assets.json','r') as file2:
    phrase='"hit sounds": {'
    badphrase='"startup swoosh": {'

    for (insert_row, line) in enumerate(file2):
        if badphrase in line:
            break
        if phrase in line:
            response = requests.get('https://raw.githubusercontent.com/modraws/dumbstupidness/main/dumbstupidness/dumbstupidnessstartupsounds.txt')
            with open('dumbstupidness/dumbstupidnessstartupsounds.txt', 'wb') as f:
                f.write(response.content)
            with open('dumbstupidness/dumbstupidnessstartupsounds.txt', 'r') as file1, open('assets.json', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("\033[32mPasted Dumbstupidness startup sounds under " + phrase + " in assets.json. You can replace these from my custom presets!\033[0m\n")

            new_lines = file2_lines[:insert_row] + file1_lines + file2_lines[insert_row:]
    
            with open('assets.json', 'w') as file2:
                file2.writelines(new_lines)
