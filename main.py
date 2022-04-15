import tweepy
import PySimpleGUIQt as sg

#import from other files here.
from imgDwn import *
from find_location import *

#environment variables
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_S_KEY = os.getenv("API_S_KEY")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_S_TOKEN = os.getenv("ACCESS_S_TOKEN")

auth = tweepy.OAuthHandler(API_KEY, API_S_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_S_TOKEN)
api = tweepy.API(auth)


#start code
#GUI and layout for program.
sg.theme('Light Blue 1')
layout = [
        [sg.Text('Please enter your Twitter link here:')],
        [sg.Input(key='-INPUT-', do_not_clear=False, size=(40, 5))],
        [sg.Text(size=(40, 1), key='-OUTPUT-')],
        [sg.Image(size=(300, 300), key='IMG')],
        [sg.FolderBrowse(key="-IN-", change_submits=True, size=(6, .5))],
        [sg.Button('Download', bind_return_key=True, size=(40, 3))]
    ]
window = sg.Window('Window Title', layout)

#accepts input for as long as possible until user exits.
tracker = 0


while True:
    event, values = window.Read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    #check if user changes directory
    if event == "-IN-":
        filename = values["-IN-"]
        location_file = open('input_location.txt', "w")
        location_file.write(filename)
        location_file.close()

    #function call from another file that downloads the image
    tweetIMG(values, api, findLocation())

    tracker += 1
    window['-OUTPUT-'].update('Downloaded. You have downloaded ' + str(tracker) + " photos.")

window.close()
