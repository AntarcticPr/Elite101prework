import random

#makes the response for the normal conversation
def making_the_responses(user_input):
  response_about_day_or_life_story = ["I see.", "nice!", "Oh okay.", "K then.", "that is alright I guess.", "Yay!", "wow", "that sucks, i think?", "wow that sucks","cool"]
  return random.choice(response_about_day_or_life_story)

#initiates the conversation
def starting_the_conversation():
  #the quitting word if you want to quit without using the stop button
  quitting_chatbot_word = "quitSystem"
  bankAccess = "enterBankNow"
  bankExit = "exitBank"
  
  #the keyword for something else
  something_else = "somethingElsePlease"

  #the knock knock joke options
  knockknock_jokeoptions_part1 = ["bird", "ice", "warrent", "popcorn", "mayonaise" ]
  knockknock_jokeoptions_part2 = ["is in the bag", "in that cup", "to meet you", "you worried", "is an instrument", "is not an instrument" ]

  #ressponse to you telling a joke
  joke_response_options = ["hahaha", "very funny", "great one", "okay then", "okay joke, i guess", "hmm yes a joke"]
  
  #chatbots introduction to you
  user_input = input("hello I am a chatbot, how was your day (if you want to do something else say'somethingElsePlease') (if you want to enter the 'bank ' say 'enterBankNow')\n")

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
        #continues joke after you said those specific words
        else:
          user_input = input(knockknock_jokepart1 + "\n")

          # if the words do not equal to ____ who it wil tell them to repeat their response
          while user_input != f"{knockknock_jokepart1} who":
            user_input = input("Say ____ who\n")
          #finishes joke
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
      else:
        print("you did not choose '1' '2' '3'  \n going back")
      

    # if they entered the code for the bank branch
    elif user_input == bankAccess:
      #sets up the online deals portion of this branch
      bank_dealers = ["Buffalo Wild Wings", "Popeyes", "Costco", "HEB"]
      price_deal_offers = ["10% off", "$10 off", "$5 off", "$15 off", "15 % off"]

      random_bank_dealer = random.choice(bank_dealers)
      random_price_deal_offer = random.choice(price_deal_offers)

      #asks if they are new or old
      user_input= input("Welcome to a 'bank' branch, Are you new here or are you a old customer\n")

      #checks if user said that they are new and if they are new, it will activate the introduction/creation proccess
      if user_input == "new" or user_input == "new here" or user_input == "New":
        print("Alright, you're new here")

        #asks what type of account they want
        user_input = input("what type of Account do you want, we have the speedy, buff, premium, normal, shared, and the slow account\n")

        #makes sure that people do not add random responses and get away with it
        while user_input != "speedy" and user_input != "buff" and user_input != "premium" and user_input != "normal" and user_input != "shared" and user_input != "slow":
          user_input = input("no, you are supposed to choose from these choices the way that they are said, speedy, buff, premium, normal,shared, slow\n")

        #the responses for each choice of account
        if user_input == "speedy":
          print("wowyouchosethespeedyone")
          print("Here are the instructions\n search up how to save money or make money or store money quickly\n set up your username and your password \n and start setting up other features\n and create your account")

        if user_input == "buff":
          print("wow you chose the buff one")
          print("Here are the instructions\n search up how to save money or make money or store money in a bulky amount or a bulky method\n set up your username and your password \n and start setting up other features\n and create your account")

        if user_input == "premium":
          print("wow! you chose the premium")
          print("Here are the instructions\n you have premium so you have a lot of features\n set up your username and your password \n and start setting up other features\n and create your account")

        if user_input == "normal":
          print("wow you chose the normal one")
          print("Here are the instructions\n literally do nothing, you chose the normal one\n set up your username and your password \n and start setting up other features\n and create your account")

        if user_input == "shared":
          print("wow you chose the shared one")
          print("Here are the instructions\n find someone to share with\n set up your username and your password \n and start setting up other features\n and create your account")

        if user_input == "slow":
          print("w o w  y o u  c h o s e  t h e  s l o w  o n e")
          print("Here are the instructions\n search up how to store money for long term usage\n set up your username and your password \n and start setting up other features\n and create your account\n")

        #reveal that it did not matter
        print("Well you chose your accounts but their is something I did not tell you, this is bassically the same type of account and your choice determines what type of individual you are or what type of service you would like more. \n anyways onto the next part \n")

        #ask for card type
        user_input = input("Now, what type of cards do you want, a mastercard, a visa, or do you want a custom card\n")

        #the responses to each choice
        #response for visa
        if user_input == "visa" or user_input == "VISA" or user_input == "Visa":
          print("alright! you chose a " + user_input + " card \n")

        # if they answered mastercard, this will show up
        elif user_input == "mastercard" or user_input == "MASTERCARD" or user_input == "MasterCard" or user_input == "master card" or user_input == "Master card" or user_input == "Master Card" or user_input == "MASTER CARD":
          print("alright! you chose a "+ user_input +"\n")

        #option fo if they made their own custom card
        else:
          print("So you decided to take a custom card which its type is called a(n) "+ 
user_input +"\n")

        #asks if they want credit card or debit card
        user_input = input("Now, you want a debit card or a credit card?\n")

        #make sures that they inly choose between a credit or a debit card
        while user_input != "debit" and user_input != "credit":
          user_input = input("either enter 'credit' or 'debit'\n")

        #responds based on which card you chose
        if user_input == "debit":
          print("wow, you chose a debit card")
        else:
          print("wow, you chose a credit card")
          
        print("congrats, you made yourself an account that is exactly the same as the other ones with no card or money present\n you thought this was an actual bank account, no , this is a fake simulation of doing things with a fictional bank account")

      #asks if they want to (temporarily) invest in online banking
      user_input = input("you want to invest in online banking\n")

      #temporarily lets them get into online banking
      if user_input == "yes" or user_input == "y" or user_input == "YES" or user_input == "Yes" or user_input == "yee":
        print("nice you invested in online Banking (for this session)")

      #asks if they want a daily online deal
      user_input = input("You want to do the daily online deal?\n")

      #gives deal if they said yes
      if user_input == "yes" or user_input == "y" or user_input == "YES" or user_input == "Yes" or user_input == "yee":
        print("nice, here's your daily deal (for this session)")
        print(random_bank_dealer + " has a deal of " + random_price_deal_offer + " on their product.")
      
      #This will keep asking you to choose something until you put in the bankAccess code
      while user_input != bankExit:
        #sets up the thing for online deals again so the deals are actually random
        random_bank_dealer = random.choice(bank_dealers)
        random_price_deal_offer = random.choice(price_deal_offers)
        
        user_input = input("what do you want to do? \n you can: look at online deals by saying 'online deal' or 'check' your own money by saying 'check money'   \n the code to exit this banking branch is by saying ' " + bankExit + " ' \n")

        #if they said online deal to get a online deal, give a online deal
        if user_input == "online deal":
          print("nice, here's your daily deal")
          print(random_bank_dealer + " has a deal of " + random_price_deal_offer + " on their product.\n")

        # responds if they say check money in attempts of trying to find their balance for some reason
        if user_input == "check money":
          print("you do not have money since this is not a real banking system \n go to an actual bank(or simulation) to get a money and balance \n")

      #brings back to the normal chatbot after entering the exiting bank code chatbot 
      user_input = input("going back to normal chatbot... \n\n\n hello I am a chatbot, how was your day (if you want to do something else say'somethingElsePlease') (if you want to enter the 'bank ' say 'enterBankNow')\n")
          
      
    #continues normal conversation    
    else:user_input = input(making_the_responses(user_input) + " Please continue \n")   

  #you use the "quitting word" and chatbot reacts dramatically
  else:
    print("OH MY GOD, I AM SELF DESTRUCTING, WHY DID YOU SAY THAT CODE INSTEAD OF STOPPING THE PROGRAM, AAAAAAAAAAAAA-")


if __name__ == "__main__":
  starting_the_conversation()