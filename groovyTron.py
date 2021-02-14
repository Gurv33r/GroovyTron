import tweepy

def decisionTree():
    input_char = input("""Give me a command to do - 
                      If you want to tweet something, enter t. 
                      If you want to reply to something, enter r. 
                      If you want to spam something with text and/or media, enter s.
                      If you want to delete something, enter d. 
                      If you'd like to quit, hit CTRL+Z (or any other exit key depending on your OS)
                      Enter here: """)
    if input_char == 't':
        confirm('t')
    elif input_char == 'n':
        decisionTree()
    elif (input_char == 'r') | (input_char == 's') | (input_char == 'd'):
        print("This command is currently not supported")
        restartTree()
    else:
        print("Invalid command!")
        restartTree()


def confirm(s):
    if s == 't':
        confirm = input("""You have chosen to tweet something. 
                            If you still want to do so, enter y.
                            If you want to go back and do something else, enter n
                            If you want to stop here, hit your exit shortkey (CTRL+Z for Windows)
                            Enter here: """)
        if confirm == 'y':
            tweet2Twitter()


def tweet2Twitter():
    """Tweets String input from user to Twitter under account that the user is current logged into"""
    s = input("Enter your tweet here (emojis and media not supported yet): ")
    print("You want to tweet:\n" + s)
    final_check = input("""If you still want to tweet this, enter y.
                        If you want to tweet something else, type r.
                        If you want to do something else, enter q. 
                        If you want to quit entirely, Enter CTRL+Z (or any other exit key depending on your OS). 
                        Enter here: """)
    if final_check == 'y':
        api.update_status(status=s)
        print("Successfully tweeted!")
    elif final_check == 'r':
        tweet2Twitter()
    else:
        restartTree()


def restartTree():
    """Restarts decision tree, asks for confirmation fist"""
    restart = input('Either quit here or type any letter to go back: ')
    if restart:
        decisionTree()


def read_key_file(file):
    """Takes a file and returns a list of keys need for twitter authentication"""
    # format = token_label: *actual tokens and keys*
    key_file = open(file, 'r')
    keys = key_file.readlines()
    key_file.close()
    # all lines are in in the list "keys", organize them such that keys is a list of the actual tokens and keys
    # make sure to get rid of newline chars
    token_list = []
    for line in keys:
        line_parts = line.split(' ')
        token_list.append(line_parts[1].strip('\n'))
    return token_list


# main
summoner = input('This is GroovyTron 10000 speaking, Who is this? I am ')
print("Hello " + summoner + ", you have effectively summoned GroovyTron 10000. I hope you know what you're getting into.")
keys_and_tokens = input("What's the security token file (template = filename.format)? ")
tokens = read_key_file(keys_and_tokens)
# tokens should now hold all the necessary info, just assign the elements of keys to variables
consumer_key = tokens[0]
consumer_secret = tokens[1]
bearer_token = tokens[2]
access_token = tokens[3]
access_token_secret = tokens[4]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
decisionTree()
