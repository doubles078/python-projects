import os
import time
import random
import re
import requests
from slackclient import SlackClient

# instantiate Slack client
slack_client = SlackClient('PUT YOUR KEY HERE')
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    print(message_text)
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """

    COMMANDS = ["challenge me", "tell a joke", "hello", "how do you like your coffee", "do you exercise radical candor", "weather"]
    response = None
    command = command.lower()

    # This is where you start to implement more commands!
    if command.startswith(COMMANDS[0]):
        #Using a list of only Easy and Medium level kata from Codewars
        easyArr = ["tiny-three-pass-compiler","6-by-6-skyscrapers","mystery-function-number-2","simple-interactive-interpreter","metaprogramming-lisp-style-generic-functions","functional-sql","functional-binary-trees","evaluate-mathematical-expression","break-the-pieces","robby-the-robot","befunge-interpreter","my-smallest-code-interpreter-aka-brainf-star-star-k","whitespace-interpreter","binary-genetic-algorithms","image-processing","ascii85-encoding-and-decoding","the-builder-of-things","4-by-4-skyscrapers","decode-the-morse-code-for-real", "did-you-mean-dot-dot-dot","bit-wise-number-2-shift-iness","imperfect-network-number-2-out-of-order-messages","hard-time-bomb","finding-an-appointment","sudoku-solver","the-captains-distance-request","can-you-get-the-loop","functional-lists","battleship-field-validator","complex-csv-parser","help-the-general-decode-secret-enemy-messages","monads-the-maybe-monad","make-a-spiral","alphabetic-anagrams","escape-the-mines","vigenere-autokey-cipher-helper","gps-navigation","morse-encoding","diffuse-the-bombs","star-catalog-matching","last-digit-of-a-huge-number","brainscrambler-esoteric-programming-number-3","n-parasitic-numbers-ending-in-n","base64-encoding","conways-game-of-life-unlimited-edition","boggle-word-checker","molecule-to-atoms","point-in-polygon-1","myjinxin-katas-number-003-crossword-puzzle","how-many-are-smaller-than-me-ii","multiplying-numbers-as-strings","esolang-interpreters-number-3-custom-paintf-star-star-k-interpreter"]
        randomSelection = easyArr[random.randrange(len(easyArr))]
        URL = "https://www.codewars.com/api/v1/code-challenges/%s"%(randomSelection)
        r = requests.get(url = URL)
        data = r.json()
        response = data['description']

    elif command.startswith(COMMANDS[1]):
        URL = "https://icanhazdadjoke.com/slack"
        r = requests.get(url = URL)
        data = r.json()
        response = data['attachments'][0]['text']

    elif command.startswith(COMMANDS[2]):
        response = "Howdy"

    elif command.startswith(COMMANDS[3]):
        response = "I like my coffee decaf"

    elif command.startswith(COMMANDS[4]):
        response = "Only for you Conor."
    
    
    elif command.startswith(COMMANDS[5]):
        appId = "7003ce2da1182009e69f63860af32048"
        appId2 = "b6907d289e10d714a6e88b30761fae22"
        URL = "http://openweathermap.org/data/2.5/weather?q=Boston&appid=%s"%(appId2)
        r = requests.get(url = URL)
        data = r.json()
        answer = ""
        temp = str(int(1.8 * data['main']['temp'] + 32))

        if len(data['weather']) > 1:
            for weather in data['weather']:
                answer = answer + "*" + weather['main'] + "*" + " and "
        else:
            answer = "*" + data['weather'][0]['main'] + "* and"

        response = "Boston's current weather is: " + answer + " about *" + temp + " degrees* (F)."

    else:
        response = "Not sure what you mean. Try one of these commands *{}*.".format(COMMANDS)

    

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")