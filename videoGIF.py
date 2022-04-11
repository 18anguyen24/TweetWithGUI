from imgDwn import *

from os import path
this_script_dir = path.dirname(path.realpath(__file__))
ffmpeg_path = this_script_dir + '\\ffmpeg.exe'

from moviepy.editor import *

import time

def videoGif(status, i, input_url, locate):
    if status.extended_entities['media'][i]['video_info']['variants'][0]['content_type'] == 'application/x-mpegURL':
        #url = status.extended_entities['media'][i]['video_info']['variants'][1]['url']
        #new
        max_value = max(status.extended_entities['media'][i]['video_info']['variants'],
                        key=lambda item: item['bitrate'] if item['content_type'] == 'video/mp4' else 0)
        index = status.extended_entities['media'][i]['video_info']['variants'].index(max_value)
        url = status.extended_entities['media'][i]['video_info']['variants'][index]['url']
        print(max_value)
    else:
        max_value = max(status.extended_entities['media'][i]['video_info']['variants'],
                    key=lambda item: item['bitrate'] if item['content_type'] == 'video/mp4' else 0)
        index = status.extended_entities['media'][i]['video_info']['variants'].index(max_value)
        url = status.extended_entities['media'][i]['video_info']['variants'][index]['url']
        #print(max_value)

    # manipulating string to add format
    url = url.split('?', 1)
    url = url[0]

    # save onto computer locally
    location = locate + '\\' + input_url + "_" + str(i) + ".mp4"
    urllib.request.urlretrieve(url, location)
    print(status.extended_entities['media'][i]['video_info'])

    # checks if it's a gif, and then converts .mp4 to gif
    if status.extended_entities['media'][i]['type'] == 'animated_gif':
        gif_location = locate + '\\' + input_url + "_" + str(
            i) + ".gif"
        clip = (VideoFileClip(location))
        clip.write_gif(gif_location)
        time.sleep(1)
        os.remove(location)
