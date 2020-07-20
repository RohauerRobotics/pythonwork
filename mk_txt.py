# ask for text entry and places it into a seperate file
# then reads from that file

# defines a function w/ no function entry
def ask_for_txt():
    # asks for various user inputs
    name = input("What's Your Name: ")
    # converts string input to integer
    age = int(input("How Old Are You: "))
    color = input("What's your color: ")
    # creates a dictionary with all user input
    ret_lib = {"name": name, "age": age, "color" : color}
    # function returns user inputs as a dictionary
    return ret_lib

# runs input function and defines output as a string
fullsend = str(ask_for_txt())

# defines a function with one text entry
def send_txt(txt):
    # opens info.txt file, trunicating its info and allowing python to write in it
    text_file = open("info.txt", "w+")
    # python writes a string into the text file
    text_file.write(txt)
    # closes the text file ***IMPORTANT
    text_file.close()

# operates the function with the user created string
send_txt(fullsend)

# defines a function w/ no variable entry
def read_txt():
    # defines variable as a readable text file
    text_file = open("info.txt", "r")
    # defines a string as the text file's information
    txt_str = text_file.read()
    # returns the text string as a dictionary
    return eval(txt_str)

sent = read_txt()

def special_output(dictionary):
    print("----------------------------")
    print("Your name is:", dictionary["name"])
    birth_year = (2020 - (dictionary["age"]))
    print("You were born in:", birth_year)
    print("Your favorite color is:", dictionary["color"])

special_output(sent)
