# Open the manimm.py file
with open('manimm.py', 'r') as file:
    # Read the contents of the file
    content = file.read()
    # Find the index of the word "class"
    index = content.find('class')
    if index != -1:
        # Find the index of the next word after "class"
        next_word_index = content.find(' ', index + len('class') + 1)
        if next_word_index != -1:
            # Extract the word after "class"
            word_after_class = content[index + len('class'): next_word_index].strip()
            word_after_class=word_after_class[:-8]
            print("Word after 'class':", word_after_class)
        else:
            print("No word found after 'class'")
    else:
        print("No 'class' found in the file")
