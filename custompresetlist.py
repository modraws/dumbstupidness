with open('fleasion.py','r') as file2:
    phrase='options = input(": ")'
    badphrase='custom replacement lists:'

    for (insert_row, line) in enumerate(file2):
        if badphrase in line:
            break
        if phrase in line:
            with open('custompresetlist.txt', 'r') as file1, open('fleasion.py', 'r') as file2:
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()

            print("Added entries for your custom presets!")

            new_lines = file2_lines[:insert_row] + file1_lines + file2_lines[insert_row:]
    
            with open('fleasion.py', 'w') as file2:
                file2.writelines(new_lines)