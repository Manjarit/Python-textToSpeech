'''
#print(dir(gtts))
#print(tts)
'''
import gtts

from gtts import gTTS
tts=gTTS("happy coding")

tts.save('my.mp3')
