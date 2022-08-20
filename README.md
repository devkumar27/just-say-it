# just-say-it
This is a speech-to-text convertor which takes speech as an input and returns whatever we said with the correct grammar.
## Installation
- Set up a viirtual python environment.
- Open Terminal and paste the command `pip install speechrecogniton`. You can check whether the installed module is working or not pasting `python -m speech_recognition` in the terminal.
- For SpeechRecognition to function with a `Microphone`, install Pyaudio also. `pip install pyaudio`
- Now, open Terminal and paste the command `pip install language-tool-python`.
### Library References
You can check out the usage of these libraries by cliking on the following links. 
- [PyPI SpeechRecognition](https://pypi.org/project/SpeechRecognition/). 
- [PyPI language-tool-python](https://pypi.org/project/language-tool-python/)
- [PyPI PyAudio](https://pypi.org/project/pyaudio/)
> Note: There are many engines in the `SpeechRecognition` library, but we have used _Google Speech Recognition_.

## Requirements
To use all of the functionality of the library, you should have:
**Python** 3.0 or higher. Link to download -[Python](https://www.python.org/downloads/).

## Troubleshooting 
### The recognizer tries to recognize speech even when I'm not speaking, or after I'm done speaking.
You can try increasing the `recognizer_instance.energy_threshold` property. This is basically how sensitive the recognizer is to when recognition should start. Higher values mean that it will be less sensitive, which is useful if you are in a loud room.  
Also, you can check on your microphone volume settings. If it is too sensitive, the microphone may be picking up a lot of ambient noise. If it is too insensitive, the microphone may be rejecting speech as just noise.  
## Demo Implementation
> Will be added soon
