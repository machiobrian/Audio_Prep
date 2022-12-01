
# LJAhNEy++D83aj0clU0fN67MJnAnyWhEKW+dC4efSBaHD5VkaZKKXA==

import pvporcupine as por 
access_key = "LJAhNEy++D83aj0clU0fN67MJnAnyWhEKW+dC4efSBaHD5VkaZKKXA=="
handle = por.create(
    access_key=access_key,
    keyword_paths=['Porcupine/hey-sunday_en_raspberry-pi_v2_1_0.ppn']
    )
def get_next_audio_frame():
    pass

while True:
    keyword_index = handle.process(get_next_audio_frame())

    # if key
