from grammar_corrector import Corrector
import datetime
import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        user_said = r.recognize_google(audio, language='en-in')
        print("You said: ", user_said)
    except Exception as e:
        print("Sorry, could not hear that :( \nPlease say it again")
        print(e)
        return 'none'
    return user_said


def greet():
    hour = int(datetime.datetime.now().hour)
    if 3 <= hour < 12:
        print("Good Morning!")
    elif 12 <= hour < 16:
        print("Good Afternoon!")
    else:
        print("Good Evening!")
    print("You may start speaking.")


if __name__ == '__main__':
    print("Loading...")
    greet()
    while True:
        user_inp = takeCommand()
        output = user_inp
        if output == "quit" or output == "exit":
            print("Thank You for using our application!!")
            exit()

        if output != 'none':
            print("Just giving a final touch...")
            output = Corrector.correct_text(user_inp)
            print("Here you go!\n", output, ".")
