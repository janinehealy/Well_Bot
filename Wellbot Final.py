#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def gen_lines(filepath):
    # Line generator: Open the file and yield each line
    with open(filepath) as f:
        for line in f:
            yield line
        else:
            print("That's all the information I have. Please mind.org.uk to find out more or if you feel like you need help, please contact your GP.")


def choose_argument():
    # Asks the user to choose an argument and return the right line generator
    res = input("What can I teach you about today? \n[a] Facts about mental health \n[b] Types of mental illnesses \n ")
    if res.lower() == "a":
        return gen_lines("facts.txt")
    elif res.lower() == "b":
        return get_type()
    elif res.lower() == "x":
        print("For more information, visit mind.org.uk or if you feel like you need help, please contact your GP. ")
        # Exits out of the programme as the user has indicated they no longer wish to continue
        return False
    else:
        print("I'm sorry, I don't know what you want me to do.")
        return False


def asking_loop(line_generator):
    # Looping the lines asking the user at each step
    # Get the first line from the generator
    print(next(line_generator))
    # Loop until the user enters N
    while True:
        want_more = input("Do you want to know more? \n[y] Yes \n[n] No \n >>  ")
        if want_more.lower() == "y":
            # When using next(), an error will be thrown if you get to the end of the lines, so it must be tested for: 
            line  = next(line_generator, False)
            if line:
                print(line)
                continue
            else:
                break
        elif want_more.lower() == "n":
            print("If you feel like you need help, please contact your GP or visit mind.org.uk for more information. ")
            break
        else:
            print("I'm sorry, I don't know what you want me to do.")
            continue

def get_type():
    res = input("I can tell you about the five most common mental health issues. Choose one! \n Depression \n Anxiety \n PTSD \n Phobias \n OCD \n ")

    types = ['depression', 'anxiety', 'ptsd', 'phobias', 'ocd']
    if res.lower() in types:
        return gen_lines(res.lower() + '.txt')
    else:
        print("I'm sorry, I don't know what you want me to do. Please try again. ")
        return get_type()
        
def main():
    # Main function
    print("Hi there, my name is Well Bot. ")
    print("My job is to tell people general facts about mental health and different types of mental illnesses. ")
    more = 'Y'
    while more.lower() == 'y' :
        line_generator = choose_argument()
        # Only run the loop if the line_generator has a valid value
        if (line_generator) :
             asking_loop(line_generator)
        more = input("I can tell you about something else if you like. \n Would you like to learn more? Enter Y or N! ")
    print("Thanks for talking to me. Please visit mind.org.uk to find out more or if you feel like you need help, please contact your GP.")


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




