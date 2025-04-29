# Title: Mad Libs 
# Author: Ryan Murray
#Purpose: Generates a story using verbs, adjectives, and nouns provided by the user
#Usage: Develop skills in creating reusable Python functions
#Notes: Design a Mad Libs-style game that prompts the user to enter specific types of words
#The story should be brief, but include a clear storyline or plot
 
#Subgoals: 
#If the user enters a name, capitalize the first letter
#Replace 'a' with 'an' when the following word starts with a vowel
 
 
''' 
 
 
 
from time import sleep 
 
def madlibs(): 
    print("Let's begin the Mad Libs! Please enter the following words:") 
    print("------------------------------------------------") 
    touchAdj = input("A word that describes how something feels: ")
    bodyPart = input("A part of the body: ") 
    speed= input("Fast or Slow: ") 
    animal = input("An animal: ") 
    nameofanimal = input("Name of animal: ") 
    describeanimal = input("Describe the animal's appearance (without using color): ") 
    colorofanimal = input("What color is the animal?: ")
    word = input("Any word: ")
    action = input("What action is the animal doing?: ") 
    describeaction = input("Describe how the animal is preforming the action: ") 
 
 
    print("\n------------------------------------------------") 
    print("Words collected. Generating your story...") 
 
    sleep(5) 
    print("\n\nYou feel a " + touchAdj + " sensation on your face. You wake up and slowly blink your eyes" + speed + ", struggling to focus.")
 
    sleep(2) 
    print("Still lying down, you lift your head.") 

    sleep(2)
    print("You glance down at your " + bodyPart + " and spot a " + animal + " named " +nameofanimal+ " happily licking your " + bodyPart+ ".")
 
    sleep(2)
    print("The " +animal+ " is " +colorofanimal+ " and " +describeanimal+ ".")

    sleep(2)
    print("Feeling curious, you reach out to pet it.")
    
    sleep(2)
    print("After a few moments " +nameofanimal+ " suddenly speaks and says " +word+ ".")

    sleep(2)
    print("Before you know it, the " + animal + " starts " + action + ".")

    sleep(2)
    print("The " +animal+ " moves in a  " +describeaction+ " way while " +action+ ".") 

    sleep(2)
    print("That’s the last time you encounter " +nameofanimal+ " because you drift back into a peaceful sleep.")

    sleep(2) 
    print("\nThe end.\n\n") 
 
madlibs() 
 
  
 

