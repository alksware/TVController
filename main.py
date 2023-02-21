import datetime
import time as tm
import random

class Controller():
    def __init__(self, tv_mode, voice_volume=0, channels=['FOX'], avaible_channel='FOX'):
        timeXXX = datetime.datetime.now()
        time = datetime.datetime.ctime(timeXXX)
        print("Controller has been started:", time)
        self.tv_mode = tv_mode
        self.voice_volume = voice_volume
        self.channels = channels
        self.avaible_channel = avaible_channel

    def change_voice_volume(self):
        while True:
            voice_volume_IN = input("Press '+' for high voice volume, Press '-' for incrase voice volume, for quit 'q'")
            if (voice_volume_IN == '+'):
                self.voice_volume += 1
                print("Avaible volume:", self.voice_volume)
            elif (voice_volume_IN == '-'):
                self.voice_volume -= 1
                print("Avaible volume:", self.voice_volume)
            else:
                print("Voice volume updated:", self.voice_volume)
                break

    def close_tv_mode(self):
        print("TV closing...")
        tm.sleep(1)
        print("TV closed")
        self.tv_mode = "turn off"

    def open_tv_mode(self):
        print("TV opening...")
        tm.sleep(1.5)
        print("TV opened")
        self.tv_mode = "turn on"

    def open_random_channel(self):
        create_random_channel = random.randint(0, len(self.channels) - 1)
        self.avaible_channel = self.channels[create_random_channel]
        print("Avaible channel:", self.avaible_channel)

    def append_new_channel(self, channel):
        print("Channel added to list")
        self.channels.append(channel)

    def __str__(self):
        return
        "TV MODE:{}\n TV VOLUME:{}\n CHANNELS LIST:{}\n AVAIBLE CHANNEL:{}".format(self.tv_mode, self.voice_volume,
                                                                                   self.channels, self.avaible_channel)

    def show_avaible_channel_number(self):
        return len(self.channels)

controller = Controller()
print("""---Progresses---
    1.Turn on TV
    2.Turn off TV
    3.TV information
    4.Learn channel number
    5.Add channel
    6.Change TV volume
""")

while True:
        progress = input("Press a progress:")
        if (progress == "1"):
            controller.open_tv_mode()
        elif (progress == "2"):
            controller.close_tv_mode()
        elif (progress == "3"):
            print(controller)
        elif (progress == "4"):
            controller.show_avaible_channel_number()
        elif (progress == "5"):
            new_channel = input("Channel name for add:")
            controller.append_new_channel(new_channel)
        else:
            break



            



