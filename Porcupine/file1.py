import pvporcupine as por 
import os

access_key = os.environ.get('ACCESS_KEY')


# create an instance of Porcupine that detects the included 
# built-in wakewords - computer and bumblebee
porcupine = por.create(
    access_key=access_key,
    keywords=['computer', 'bumblebee']
)

# pass in frames of audio to the .process function

def get_next_audio_frame():
    pass

while True:
    audio_frame = get_next_audio_frame()
    keyword_index = porcupine.process(audio_frame)

    if(keyword_index==0):
        # detect computer
        print("Hey, Computer")
    elif keyword_index==1:
        #detect bumble bee
        print("Hey, bumblebee") 