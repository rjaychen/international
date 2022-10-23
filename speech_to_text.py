import speech_recognition as sr
r = sr.Recognizer()
lecture = sr.AudioFile('audio_files_harvard.wav')
#mic = sr.Microphone()

with lecture as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

print(type(r.recognize_google(audio)))


""""
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
try:
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

"""