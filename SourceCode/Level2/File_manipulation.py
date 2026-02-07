import string
def file_manipulation():

    # Step1: Read the file(Raw data)
    filename = r"C:\Users\Welcome\Desktop\Python_Intern_Task\file.txt"
    with open(filename,'r') as f:
        text = f.read()
    
    # step2: Split words 
    text = text.lower()
    # Remove puntuation 
    text = text.translate(str.maketrans('','', string.punctuation))
    words = text.split()

    # Step3: Count the words how many times occurance in file
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Step4: Display Results in alphabetical order
    print("\n Word Counts in Alphabetic Order: \n")
    for word in sorted(word_count):
        print(word,word_count[word])
    
file_manipulation()

