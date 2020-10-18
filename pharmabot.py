import random
import webbrowser
from googlesearch import search
def greet_and_introduce():
    responses = ["Hi buddy! I am pharmabot.I can help you in knowing details about any medicine.May I know your name?","Wonderful.It is so nice to be in touch with you.I am a pharmabot.May I know your name?"]
    print(random.choice(responses))
def welcome(name):
    messages = ["Nice to meet you","Lets have some good time together"]
    print("{0} {1}".format(random.choice(messages),name))
def show_menu():
    print("1.Continue with other medicine")
    print("2.End this chat.")
    print("--------------")
    choice=int(input())
    if 1<=choice<=2:
        return choice
    else:
        return 0
def details_medicine():
    query=input("Enter name of the medicine: ")
    query=query+ "medicine"
    for j in search(query,tld="co.in",num=1,stop=1,pause=1):
        webbrowser.open(j)
def pharmabot():
    greet_and_introduce()
    name=input("Your name: ")
    welcome(name)
    option = show_menu()
    while option != 2:
        if option == 1:
            details_medicine()
        else:
            print("Enter choice between 1 and 2.")
        option = show_menu()
pharmabot()


