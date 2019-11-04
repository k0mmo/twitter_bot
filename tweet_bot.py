import tweepy
from termcolor import colored
import sys


def choice():
    print("would like to make a tweet?\n")
    print("( y,n )\n")
    user_choice = input(">>> ")
    if user_choice == 'y':
        print(" ")
        tweet()
    elif user_choice == 'n':
        sys.exit()
    else:
        print("invalid selection\n")
        choice()


def tweet():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

    # Create API object
    api = tweepy.API(auth)

    # Create a tweet
    print("Please enter your tweet:\n")
    mess = input(">>> ")
    api.update_status(mess)
    # terminal display output
    print(" ")
    buff = colored("========================================", "green")
    print(buff)
    print("you have tweeted:\n")
    print(mess + "\n")
    print(buff)




while True:
    choice()
