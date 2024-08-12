# READ THIS OR I'M COMING TO YOUR HOUSE AND SLIGHTLY UNSCREWING ONE OF THE FEET ON YOUR BEDFRAME

# if you want to add presets to fleasion, replace the badphrase with whatever you set as the _option name. you don't need to edit the phrase.

# however, if you want to add asset codes to assets.json, be mindful of where your presets get placed. it's best to add them to a custom category.
# you will need to change the phrase. if you plan on making a custom category, change the phrase to either
# phrase='"skyboxes": [' or phrase ='"textures": ['
# if you instead want to add assets to an already existing category, change the phrase to the very first hash in that category.
# the additions code always places your txt file ABOVE the phrase you select. remember that.





# for additions to fleasion
with open('fleasion.py','r') as file2:
    phrase='case 0:' # leave this as is, i beg of you
    badphrase='addyourowntitle_option'

    for (insert_row, line) in enumerate(file2):
        if badphrase in line:
            break
        if phrase in line:
            with open('addyourowntitle.txt', 'r') as file1, open('fleasion.py', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("\033[32mPasted your presets at line " + insert_row+1 + " in fleasion.py.\033[0m")

            new_lines = file2_lines[:insert_row] + file1_lines + file2_lines[insert_row:]
    
            with open('fleasion.py', 'w') as file2:
                file2.writelines(new_lines)

# for additions to the assets.json file
with open('assets.json','r') as file2:
    phrase='change this to the full line of the category you want your assets to appear under'
    badphrase="change this to the name of a string in your assets that doesn't appear anywhere else"

    for (insert_row, line) in enumerate(file2):
        if badphrase in line:
            break
        if phrase in line:
            with open('addyourowntitle.txt', 'r') as file1, open('assets.json', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("\033[32mPasted your assets under " + phrase + ", or line " + insert_row+2 + " in assets.json.\033[0m")

            new_lines = file2_lines[:insert_row+1] + file1_lines + file2_lines[insert_row+1:]
    
            with open('assets.json', 'w') as file2:
                file2.writelines(new_lines)

# if you want to make additions to multiple existing categories, please make differing txt files for the entries you want to add,
# and copy and paste the code above to point to those different categories.