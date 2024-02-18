
#          hello i am tall tales
# pip install pyttsx3

import pyttsx3 as ptx


def Tell(text):
    speaker = ptx.init()
    test = 1
    for i in range(2):
        if test == 1:
            answer = "-"
            speaker.say("         " + answer)
            speaker.runAndWait()
            test = 0
        else:
            speaker.say("         " + text)
            speaker.runAndWait()
            

"""
# this is just for the testing purpose only 
while True:
    answer1 = input("Enter speech: ")
    if (answer1 == "=" or answer1 == ""):break
    Tell(answer1)
"""

  











