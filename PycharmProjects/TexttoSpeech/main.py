import pyttsx3
text = input("please enter text: ")
engine = pyttsx3.init()
engine.say(text)
engine.save_to_file( text , 'test.mp3')
engine.runAndWait()
