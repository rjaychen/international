import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()

key = "running"
print("Speak twat")

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
try:
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
