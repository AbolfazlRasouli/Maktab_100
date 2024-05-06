from abc import ABC, abstractmethod
import time
import datetime


class Media(ABC):
    def __init__(self, duration):
        """duration in second"""
        self.duration = self.validate_duration(duration)

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def get_duration_in_minute(self):
        """div by 60"""
        return self.duration / 60

    @staticmethod
    def validate_duration(duration):
        """check the duration to be digit"""
        duration = str(duration)
        if duration.isdigit():
            return int(duration)
        else:
            raise ValueError("please enter seconds in number!")


class Music(Media):
    def __init__(self, duration, lyrics: str):
        super().__init__(duration)
        self.lyrics = lyrics
        self.timestarted = None
        self.timepaused = None
        self.paused = False

    def lyrics(self):
        return self.lyrics

    def play(self):
        self.timestarted = datetime.datetime.now()
        self.paused = False
        return 'music is playing!'

    def pause(self):
        if self.timestarted is None:
            raise ValueError("music not started")
        if self.paused:
            raise ValueError("music is already paused")
        print('Pausing music')
        self.timepaused = datetime.datetime.now()
        self.paused = True

    def stop(self):
        self.timestarted = None
        self.timepaused = None
        self.paused = False
        return "music stopped"

    def get(self):
        if self.timestarted is None:
            raise ValueError("Timer not started")
        if self.paused:
            return self.timepaused - self.timestarted
        else:
            return datetime.datetime.now() - self.timestarted


    def skip(self, selected_second, backorforth: str):
        timepassed = self.get()
        timepassed=timepassed.seconds
        selected_second = int(selected_second)
        if backorforth == 'b':
            self.timestarted = timepassed - selected_second

            if self.timestarted < 0:
                self.timestarted = None
            return f'skipped backward to {self.timestarted}'

        elif backorforth == 'f':
            self.timestarted = timepassed + selected_second
            if self.timestarted > self.duration:
                self.timestarted = None
            return f'skipped forward to{self.timestarted}'

        else:
            return "u can only choose b for back, and f for forth"


class Movie(Media):
    def __init__(self,name:str, duration, director, genre):
        super().__init__(duration)
        self.director=director
        self.genre=genre
        self.name=name

    def get_info(self):
        return f"{self.name.capitalize()},directed by {self.director}, gerne:{self.genre}"

    def play(self):
        self.timestarted = datetime.datetime.now()
        self.paused = False
        return 'movie is playing!'

    def pause(self):
        if self.timestarted is None:
            raise ValueError("movie not started")
        if self.paused:
            raise ValueError("movie is already paused")
        print('Pausing music')
        self.timepaused = datetime.datetime.now()
        self.paused = True

    def stop(self):
        self.timestarted = None
        self.timepaused = None
        self.paused = False
        return "movie stopped"

    def get(self):
        if self.timestarted is None:
            raise ValueError("Movie not started")
        if self.paused:
            return self.timepaused - self.timestarted
        else:
            return datetime.datetime.now() - self.timestarted

    def skip(self, selected_second, backorforth: str):
            timepassed = self.get()
            timepassed = timepassed.seconds
            selected_second = int(selected_second)
            if backorforth == 'b':
                self.timestarted = timepassed - selected_second

                if self.timestarted < 0:
                    self.timestarted = None
                return f'skipped backward to {self.timestarted}'

            elif backorforth == 'f':
                self.timestarted = timepassed + selected_second
                if self.timestarted > self.duration:
                    self.timestarted = None
                return f'skipped forward to{self.timestarted}'




movie1 = Movie('lucy',38000, "mamad",'sci-fic')

while True:
    comand = int(input('movie:1-play,2-pause,3-skip,4-stop?'))
    if comand == 1:
        print(movie1.play())
    elif comand == 2:
        movie1.pause()
        print(movie1.get())
    elif comand == 3:
        selected_second = input('how much seconds?')
        backandforth = input('enter b for backwards,f for forwards')
        print(movie1.skip(selected_second, backandforth))

    elif comand == 4:
        print(movie1.stop())
        break

print(movie1.get_info())
music1 = Music(150, "hello")

while True:
    comand = int(input('1-play,2-pause,3-skip,4-stop?'))
    if comand == 1:
        print(music1.play())
    elif comand == 2:
        music1.pause()
        print(music1.get())
    elif comand == 3:
        selected_second = input('how much seconds?')
        backandforth = input('enter b for backwards,f for forwards')
        print(music1.skip(selected_second, backandforth))

    elif comand == 4:
        print(music1.stop())
        break

print(music1.get_duration_in_minute())
