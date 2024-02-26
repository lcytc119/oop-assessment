# Write your Store Class here
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

from classes.customer import Customer
from classes.video import Video

from classes.customer_types import Customer_pf, Customer_sf, Customer_sx

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
    
    def load_data(self, fname):
        # filePath = __file__
        with open("./data/"+fname+".csv", mode="r", newline="") as cvsFile:
            reader = csv.reader(cvsFile, delimiter = ",")
            res = []
            for row in reader:
                if row[0] == "id":
                    continue
                res.append(row)
            setattr(self, fname, res)
        if fname == "customers":
            for data in self.customers:
                c = Customer(data)
        if fname == "inventory":
            for data in self.inventory:
                print("video: ", data)
                inv = Video(data)
                
    def run_the_store(self):
        # parse adifhad
        return "Thank you, please come again!"
        
    def customer_type_maker(self, data):
        ndata = list(data.values())
        ndata = [ndata[0],ndata[3],ndata[1],ndata[2],""]
        ty = data["account_type"]
        match ty:
            case "pf":
                return Customer_pf(ndata)
            case "sx":
                return Customer_sx(ndata)
            case "sf":
                return Customer_sf(ndata)