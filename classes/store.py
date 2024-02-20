# Write your Store Class here
"""
2. video inventory:
        x- video id
        x- video title
        x- video rating
        x- video release year
        x- num of copies available in-store
        x- create list of inventory from csv
"""
import csv


class Store:
    all_inventory_lst=[]
    def __init__(self, id=None, title=None, rating=None, release_year=None, copies_available=0):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available

    def __repr__(self):
        return f"id:{self.id} | title: {self.title} | release year: {self.release_year} | copies_available: {self.copies_available}"
    
# sample=("1", "among us", "2024", "75")
# print(sample)

#Prototype getting all inventory from csv
    @classmethod
    def all_inventory(cls, path_to_file):
        with open (path_to_file, mode = 'r', newline='') as  csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                a_movie = Store(**row)
                # print(a_movie)
                cls.all_inventory_lst.append(a_movie)
        
        return cls.all_inventory_lst
    @classmethod
    def get_video_by_title(cls, title, path_to_file):
        cls.all_inventory(path_to_file)
        inventory_info = cls.all_inventory_lst
        
        for ele in inventory_info:
            if ele.title == title:
                return ele
                
        return None