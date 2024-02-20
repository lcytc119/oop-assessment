# Write you Customer Class here
from classes.person import Person
import csv
class Customer(Person):
    all_customers_lst=[]

    def __init__(self, id=None, account_type=None, first_name=None, last_name=None, current_video_rentals=None) :
        self.id = id
        self.account_type = account_type
        super().__init__(first_name, last_name)
        if current_video_rentals == None:
            self.current_video_rentals = []
        else:
            self.current_video_rentals = current_video_rentals
        
    def __repr__(self):
        return f"id: {self.id} | account type: {self.account_type} | {super().__repr__()} | rental(s): {self.current_video_rentals}"

    @classmethod
    def all_customers(cls, path_to_file):
        # Prototype getting customers.csv
        with open (path_to_file, mode = "r", newline= '') as  csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print(row)
                a_customer = Customer(**row)
                # print(a_customer)
                cls.all_customers_lst.append(a_customer)
        
        return cls.all_customers_lst
    @property
    def get_rental(self):
        if isinstance(self.current_video_rentals, str):
            rental_movies = self.current_video_rentals.split("/")
            return rental_movies
        else:
            return self.current_video_rentals if self.current_video_rentals else []

    @classmethod
    def get_customer_by_name(cls, full_name, path_to_file):
        first_name, last_name = full_name.split(' ')
        customers = cls.all_customers(path_to_file)
        found_customer = None
        for element in customers:
            if element.first_name == first_name and element.last_name == last_name:
                found_customer = element
                break
        return found_customer
    
    @classmethod
    def add_a_customer(cls, customer, path_to_file):
        with open(path_to_file, mode="a", newline = "") as csvfile:
            fieldnames = ["id","account_type","first_name","last_name","current_video_rentals"]
            writer = csv. DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()
            #write new customer information into file
            writer.writerow({
                "id": customer.id,
                "account_type":customer.account_type,
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "current_video_rentals": customer.current_video_rentals
            })
    @classmethod
    def update_customer_info(cls, customer, path_to_file):
        customers = Customer.all_customers_lst

        
        for ele in customers:
            if ele.first_name == first_name and ele.last_name == last_name:
                ele.current_video_rentals = '/'.join(customer.current_video_rentals)
        
        with open(path_to_file, mode="w", newline="") as csvfile:
            fieldname= ['id', 'account_type',"first_name","last_name","current_video_rentals"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldname)

            writer.writeheader()
            writer.writerows(customers)