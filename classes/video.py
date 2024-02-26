# Write your video Class here
import csv
class Video():
    videos = {}
    
    @staticmethod
    def get_a_video_by_title():
        title = input("title: ")
        return Video.videos[title]

    @property
    def return_a_video(self):
        pass
    @return_a_video.setter
    def return_a_video(self, value):
        self.copies_available = value
    @property
    def rent_a_video(self):
        pass
    @rent_a_video.setter
    def rent_a_video(self, value):
        self.copies_available = value
        
        
    def __init__(self, data):
        self.id = data[0]
        self.title = data[1]
        self.rating = data[2]
        self.year = data[3]
        self.copies_available = int(data[4])
        Video.videos[self.title]=self