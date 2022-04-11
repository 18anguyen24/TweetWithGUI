import urllib.request

from videoGIF import *


def tweetIMG(import_values, import_api, locate):
    input_url = import_values['-INPUT-']
    input_url = input_url.split('?', 1)
    input_url = input_url[0]
    input_url = input_url.split('/')
    if "photo" in input_url:
        input_url = input_url[len(input_url) - 3]
    else:
        input_url = input_url[-1]

    # accessing the properties of the tweet using its ID on the Twitter API
    id_ = [input_url]
    stat = import_api.lookup_statuses(id_, tweet_mode='extended')
    i = 0
    location = ""
    for status in stat:
        # extended entities allows for multiple indices per media link
        # print(status.extended_entities['media'][i])
        while i != len(status.extended_entities['media']):
            if status.extended_entities['media'][i]['type'] != 'photo':
                videoGif(status, i, input_url, locate)
            else:
                url = status.extended_entities['media'][i]['media_url']
                # manipulating string to add format
                file_type = url[-3:]
                url = url[:-4]
                final_url = url + "?format=" + file_type + "&name=4096x4096"

                # save onto computer locally
                location = locate + "\\" + input_url + "_" + str(i) + ".png"
                urllib.request.urlretrieve(final_url, location)
            i += 1
