import random

#makes the response for the normal conversation
def making_the_responses(user_input):
  response_about_day_or_life_story = ["I see.", "nice!", "Oh okay.", "K then.", "that is alright I guess.", "Yay!", "wow", "that sucks, i think?", "wow that sucks","cool"]
  return random.choice(response_about_day_or_life_story)

#initiates the conversation
def starting_the_conversation():
  #the quitting word if you want to quit without using the stop button
  quitting_chatbot_word = "quitSystem"

  #the keyword for something else
  something_else = "somethingElsePlease"

  #the knock knock joke options
  knockknock_jokeoptions_part1 = ["bird", "ice", "warrent", "popcorn", "mayonaise" ]
  knockknock_jokeoptions_part2 = ["is in the bag", "in that cup", "to meet you", "you worried", "is an instrument", "is not an instrument" ]

  #ressponse to you telling a joke
  joke_response_options = ["hahaha", "very funny", "great one", "okay then", "okay joke, i guess", "hmm yes a joke"]
  
  #chatbots introduction to you
  user_input = input("hello I am a chatbot, how was your day (if you want to do something else say'somethingElsePlease')\n")

  #while the user does not enter the quitting word, this will continue
  while user_input != quitting_chatbot_word:
    #initiates if the user enters the code for something else
    if user_input == something_else:

      # asks to choose
      user_input = input("Please choose between these activities 1)an knock knock joke from me 2)a joke to me, i guess, and 3) go back  \n")

      #initiates if choice is 1
      if user_input == "1":
        knockknock_jokepart1 = random.choice(knockknock_jokeoptions_part1)
        knockknock_jokepart2 = random.choice(knockknock_jokeoptions_part2)
        
        user_input = input("Knock knock\n")
        
        #doesn't continue until you say whos there
        while user_input != "whos there":
          user_input = input("maybe you should ask'whos there'")
        else:
          user_input = input(knockknock_jokepart1 + "\n")

          while user_input != f"{knockknock_jokepart1} who":
            user_input = input("Say ____ who\n")
          else:
            print(knockknock_jokepart1 + " " + knockknock_jokepart2)

            #brings the direction back to the original conversation
            user_input = input("that was a random joke, now you are going back to a normal conversation (if you want to do knock knock jokes with me again, you can enter the code for something else and choose 1 [this will repeat every time you choose this route :) ])\n\n")

      #initiates joke option
      if user_input == "2":
        joke_response = random.choice(joke_response_options)
        user_input = input("tell me a joke\n")
        print(joke_response)
        user_input = input("Going back to normal program. Proceed with conversation\n\n")

      #brings back to normal conversation
      if user_input == "3":
        user_input = input("alright then, please continue \n")
      
          
    #continues normal conversation    
    else:user_input = input(making_the_responses(user_input) + " Please continue \n")   

  #you use the "quitting word" and chatbot reacts dramatically
  else:
    print("OH MY GOD, I AM SELF DESTRUCTING, WHY DID YOU SAY THAT CODE INSTEAD OF STOPPING THE PROGRAM, AAAAAAAAAAAAA-")


if __name__ == "__main__":
  starting_the_conversation()