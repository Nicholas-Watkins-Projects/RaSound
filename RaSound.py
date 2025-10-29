import random, os, time
import playsound
import SettingHandler as setH
from multiprocessing import Process, Queue
import threading

class SoundClip:

    def __init__(self, sound_location: str, chance: float = .05, time: str = "minute"):
        self.sound_location = sound_location
        self.chance = chance
        self.time = time

        if time == "minute":
            self.chance = self.chance / 60

        if time == "hour":
            self.chance = (self.chance / 60) / 60

def SoundPlay(sound_location):
    playsound.playsound(sound_location)
    print(f"Played Sound at {sound_location}")
    time.sleep(5)
    pass

def SoundHandle(sound):
    while True:
        sound_location = sound.get()
        if sound_location is None:
            break

        thread1 = threading.Thread(target=SoundPlay, args=(sound_location,))
        thread1.start()
        thread1.join() # Play sound over each other, aka make new thread for each sound that comes in, TESTING

def SoundLoop(hour_limit = 2, timeInterval = 0, sound_queue = None):
    seconds = 0
    minutes = 0
    hours = 0
    clips_played = {}

    running = True
    while running:

        time.sleep(timeInterval)
        os.system("cls")
        seconds += 1

        for sound_clip in sound_clips:
            per_chance = random.random()

            if per_chance <= sound_clip.chance:
                soundLoc = sound_clip.sound_location

                if soundLoc not in list(clips_played.keys()):
                    clips_played[sound_clip.sound_location] = 0
    
                clips_played[sound_clip.sound_location] += 1
                sound_queue.put(sound_clip.sound_location)
                    
        if seconds == 60:
            seconds = 0
            minutes += 1

            if minutes == 60:
                minutes = 0
                hours += 1
            
                if hours >= hour_limit:
                    running = False

        total_seconds = (((hours * 60) + minutes) * 60) + seconds
        print(f"Elapsed: {hours}:{minutes}:{seconds} s:{total_seconds} | Clips: {clips_played}") ################################################

    return clips_played
    
if __name__ == '__main__':

    sound_clips = []
    for i in setH.HandleSetting("settings_file.txt"):
        sound_clips.append(SoundClip(i[0], float(i[1]), i[2]))

    sound = Queue()
    sound_handler = Process(target=SoundHandle, args=(sound,))
    sound_handler.start()
    
    SoundLoop(1, 1, sound)
    sound_handler.join()
