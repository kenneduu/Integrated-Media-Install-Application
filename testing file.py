from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from tokenize import String
from pytube import YouTube

class IMIA (App):
     def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.add_widget(Image(source = "logo.png"))
        self.message = Label(text="Welcome to IMIA")
        self.window.add_widget(self.message)

        self.user = TextInput(multiline=False)
        self.window.add_widget(self.user)

        self.button = Button(text = "Install")
        self.button.bind(on_press=download)

        self.window.add_widget(self.button)

        return self.window
        
def download(instance):
    Youtube_link = video_Link.get()

    download_Folder = download_Path.get()

    getVideo = YouTube(Youtube_link)

    videoStream = getVideo.streams.first()

    videoStream.download(download_Folder)

   

    

if __name__ == "__main__":
    IMIA().run()        


