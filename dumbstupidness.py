with open('fleasion.py','r') as file2:
    phrase='case 0:'
    badphrase='mo_option'

    for (insert_row, line) in enumerate(file2):
        if badphrase in line:
            break
        if phrase in line:
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
            with open('dumbstupidness/dumbstupidnessstartupsounds.txt', 'r') as file1, open('assets.json', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("\033[32mPasted Dumbstupidness startup sounds under " + phrase + " in assets.json. You can replace these from my custom presets!\033[0m\n")

            new_lines = file2_lines[:insert_row] + file1_lines + file2_lines[insert_row:]
    
            with open('assets.json', 'w') as file2:
                file2.writelines(new_lines)

print("\033[95mI have added a handful of links to assets for example, or my own texture game. If you CTRL+click those links, they'll automatically open in your favourite web browser! (at least, on most terminals that should happen.)\033[0m\n")