"""class parent Media
ABC play pause stop for methods ;
instance method get duration in minute
atrebute duration int__>seconds
child class movie

abc method pause play stop override

class child music
method music->second int skip to it
lyrics-> add string to music as lyrics


method movie director ,genre,get_info
    """
from abc import ABC ,abstractmethod
class Media(ABC):
    def __init__(self,duration):
        """duration in second"""
        pass
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
        pass
    def validate_duration(self):
        pass


class Music(Media):
    def __init__(self,duration,lyrics):
        super().__init__()
    def skip(self):
        pass
    def lyrics(self):
        pass
    def play(self):
        pass
    def pause(self):
        pass
    def stop(self):
        pass



class Movie(Media):
    def __init__(self,duraion,director,genre):
        super().__init__()
    def get_info(self):
        pass
    def play(self):
        pass
    def pause(self):
        pass
    def stop(self):
        pass