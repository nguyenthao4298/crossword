from tkinter import *
import librosa
import numpy as np
import pickle
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from tkinter import messagebox


class Demo(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('CROSSWORD_DEMO')
        self.pack(fill=BOTH, expand=0)
        self.sqsize = 50
        for row in range(10):
            for col in range(10):
                top = row * self.sqsize + 2
                left = col * self.sqsize + 2
                bottom = row * self.sqsize + self.sqsize
                right = col * self.sqsize + self.sqsize
                cas.create_rectangle(left, top, right, bottom, outline='white', fill='black')
        cas.pack()
        self.a = ('English', 'biology', 'music', 'sport', 'history')
        self.q = ('You practise speaking the language of U.S in this subject',
                  'The subject of living organisms',
                  'We learn to sing & play the guitar in this subject',
                  'What do we do in P.E',
                  'We can learn about events of the past and long time ago')

        self.check = ['0', '0', '0', '0', '0']
        self.style = ("ngang", "ngang", "doc", "ngang", "doc")
        self.rowWords = (3, 9, 0, 7, 3)
        self.colWords = (1, 1, 5, 5, 7)
        # questions of hints
        cas.create_text(750, 30, fill="darkblue", font="Times 20 bold", text='CROSSWORDS')
        cas.create_text(530, 70, anchor=W, font="VNI-Dom 18", text='1.' + self.q[0])
        cas.create_text(530, 100, anchor=W, font="VNI-Dom 18", text='2.' + self.q[1])
        cas.create_text(530, 130, anchor=W, font="VNI-Dom 18", text='3.' + self.q[2])
        cas.create_text(530, 160, anchor=W, font="VNI-Dom 18", text='4.' + self.q[3])
        cas.create_text(530, 190, anchor=W, font="VNI-Dom 18", text='5.' + self.q[4])
        cas.create_text(750, 250, fill="darkblue", font="Times 20 bold", text="Correct words: ")
        cas.create_rectangle(850, 270, 900, 230, fill='white')

        # create number and word
        def generateHang(rowPosition, colPosition, lenghtOfWord, wordOrder):
            for col in range(colPosition, lenghtOfWord + colPosition):
                top = rowPosition * self.sqsize + 2
                left = col * self.sqsize + 2
                bottom = rowPosition * self.sqsize + self.sqsize
                right = col * self.sqsize + self.sqsize
                cas.create_rectangle(left, top, right, bottom, fill='white')
            cas.create_text(colPosition * self.sqsize + 10, rowPosition * self.sqsize + 10, text=wordOrder + '.',
                            font=('Times', 10))

        def generateCot(rowPosition, colPosition, lenghtOfWord, wordOrder):
            for row in range(rowPosition, lenghtOfWord + rowPosition):
                top = row * self.sqsize + 2
                left = colPosition * self.sqsize + 2
                bottom = row * self.sqsize + self.sqsize
                right = colPosition * self.sqsize + self.sqsize
                cas.create_rectangle(left, top, right, bottom, fill='white')
            cas.create_text(colPosition * self.sqsize + 10, rowPosition * self.sqsize + 10, text=wordOrder + '.',
                            font=('Times', 10))

        for word in range(0, len(self.a)):
            if self.style[word] == "doc":
                colPo = self.colWords[word]
                rowPo = self.rowWords[word]
                generateCot(rowPo, colPo, len(self.a[word]), str(word + 1))
            if self.style[word] == "ngang":
                colPo = self.colWords[word]
                rowPo = self.rowWords[word]
                generateHang(rowPo, colPo, len(self.a[word]), str(word + 1))

        def get_mfcc(filename):
            data, fs = librosa.load(filename, sr=None)
            mfcc = librosa.feature.mfcc(data, fs, hop_length=128, n_fft=1024)
            return mfcc.T

        choose = ['mot', 'hai', 'ba', 'bon', 'nam']
        filename = ['venv\one.sav', 'venv\\two.sav', 'venv\\three.sav', 'venv\\four.sav', 'venv\\five.sav']
        loaded_model = [pickle.load(open(model, 'rb')) for model in filename]
        button1 = Button(tk, text="RECORD", command=lambda: record_sound('input.wav', 1))
        button1.pack()

        def record_sound(filename, duration=2, fs=44100, play=False):
            print('Recording...')
            sd.play(np.sin(2 * np.pi * 500 * np.arange(fs) / fs), samplerate=fs, blocking=True)
            sd.play(np.zeros(int(fs * 0.2)), samplerate=fs, blocking=True)
            data = sd.rec(frames=duration * fs, samplerate=fs, channels=1, blocking=True)
            if play:
                sd.play(data, samplerate=fs, blocking=True)
            sf.write(filename, data=data, samplerate=fs)
            result = [loaded_model[i].score(get_mfcc('input.wav')) for i in range(len(loaded_model))]
            print(choose[result.index(max(result))])
            box(self, result.index(max(result)))

        def recognize_speech_from_mic(recognizer, microphone):

            # check that recognizer and microphone arguments are appropriate type
            if not isinstance(recognizer, sr.Recognizer):
                raise TypeError("`recognizer` must be `Recognizer` instance")

            if not isinstance(microphone, sr.Microphone):
                raise TypeError("`microphone` must be `Microphone` instance")

            # adjust the recognizer sensitivity to ambient noise and record audio
            # from the microphone
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            # set up the response object
            response = {
                "success": True,
                "error": None,
                "transcription": None
            }

            # try recognizing the speech in the recording
            # if a RequestError or UnknownValueError exception is caught,
            #     update the response object accordingly
            try:
                response["transcription"] = recognizer.recognize_google(audio)
            except sr.RequestError:
                # API was unreachable or unresponsive
                response["success"] = False
                response["error"] = "API unavailable"
            except sr.UnknownValueError:
                # speech was unintelligible
                response["error"] = "Unable to recognize speech"

            return response

        def check_choosed():
            check_count = 0
            for c in range(0, 5):
                if self.check[c] == '1':
                    check_count = check_count + 1
            return check_count

        def box(self, number):
            if self.style[number] == "ngang":
                row = self.rowWords[number]
                top = row * self.sqsize + 2
                left = self.colWords[number] * self.sqsize + 2
                bottom = row * self.sqsize + self.sqsize
                right = (len(self.a[number]) + self.colWords[number]) * self.sqsize

            elif self.style[number] == "doc":
                col = self.colWords[number]
                top = self.rowWords[number] * self.sqsize + 2
                left = col * self.sqsize + 2
                bottom = (len(self.a[number]) + self.rowWords[number]) * self.sqsize
                right = col * self.sqsize + self.sqsize
            boxchoosed = cas.create_rectangle(left, top, right, bottom, outline='red', width=3)
            if check_choosed() == 5:
                messagebox.showerror("Victory!", "You won!")
            if self.check[number] == '0':
                recognizer = sr.Recognizer()
                microphone = sr.Microphone()
                print('Say it')
                guess = recognize_speech_from_mic(recognizer, microphone)
                if guess["transcription"]:
                    print("You said: {}".format(guess["transcription"]))
                if not guess["success"]:
                    print("I didn't catch that. What did you say?\n")
                if guess["error"]:
                    print("ERROR: {}".format(guess["error"]))
                guess_is_correct = (guess["transcription"] == self.a[number])
                if guess_is_correct:
                    unhide(self, number)
                    self.check[number] = '1'
                    check_choosed()
                    cas.create_rectangle(850, 270, 900, 230, fill='white')
                    cas.create_text(875, 250, fill="darkblue", font="Times 20 bold",
                                    text=check_choosed().__str__())
                    cas.delete(boxchoosed)
                else:
                    messagebox.showerror("Error", "The word is incorrect. Try it again.")
                    cas.delete(boxchoosed)
            else:
                messagebox.showerror("Error", "The word is choosed. Try it again.")
                cas.delete(boxchoosed)

        def unhide(self, number):
            wordCount1 = 0
            if self.style[number] == "ngang":
                for col in range(self.colWords[number], len(self.a[number]) + self.colWords[number]):
                    row = self.rowWords[number]
                    top = row * self.sqsize + 2
                    left = col * self.sqsize + 2
                    cas.create_text(left + 25, top + 25, text=self.a[number][wordCount1], font=('Times', 16))
                    wordCount1 = wordCount1 + 1

            if self.style[number] == "doc":
                for row in range(self.rowWords[number], len(self.a[number]) + self.rowWords[number]):
                    col = self.colWords[number]
                    top = row * self.sqsize + 2
                    left = col * self.sqsize + 2
                    cas.create_text(left + 25, top + 25, text=self.a[number][wordCount1], font=('Times', 16))
                    wordCount1 = wordCount1 + 1


if __name__ == '__main__':
    tk = Tk()
    cas = Canvas(tk, width=1000, height=500)
    # tk.geometry("420x250+300+300")
    demo = Demo(tk)
    tk.mainloop()
