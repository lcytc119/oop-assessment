# Write you Customer Class here
# class Customer:
    # Write you Customer Class here
# from classes.person import Person
import csv
class Customer:
    customers={}
    
    @staticmethod
    def get_customer_by_id():
        intp = input("please input a id: ")
        return Customer.customers[int(intp)]
    
    @staticmethod
    def create_customer():
        lastid = len(Customer.customers)
        intp = input("first name:")
        fn = intp
        intp = input("last name:")
        ln = intp
        intp = input("type:")
        ty = intp
        res = [lastid+1, ty, fn, ln, ""]
        Customer(res)
        return {
            "id": lastid + 1,
            "first_name": fn,
            "last_name": ln,
            "account_type": ty,
        }
        
    @property
    def return_a_video(self):
        pass
    @return_a_video.setter
    def return_a_video(self, name):
        self.current_video_rentals.remove(name)

    @property
    def rent_a_video(self):
        pass
    @rent_a_video.setter
    def rent_a_video(self, value):
        print(self.current_video_rentals)
        if len(self.current_video_rentals) >= 3:
            return
        print("3")
        if value[1] == "R" and  (not self.type.endswith("x")):
            return 
        print("r")
        if self.type.startswith("s"):
            print(len(self.current_video_rentals))
            if len(self.current_video_rentals) >= 1:
                return 
        print("s")
        self.current_video_rentals.append(value[0])
        
    def get_customer_rented_videos(self):
        return f"{self.first_name} has the following rentals:\n{self.current_video_rentals}"

    def __init__(self, data):
        self.id = len(Customer.customers) + 1
        self.nid = data[0]
        self.type = data[1]
        self.first_name = data[2]
        self.lastN = data[3]
        tmp = data[4].split("/")
        if tmp == [""]:
            self.current_video_rentals = []
        else:
            self.current_video_rentals = tmp
        Customer.customers[int(self.id)] = self
        
    # def __repr__(self):
    #     return f"id: {self.id} | account type: {self.account_type} | {super().__repr__()} | rental(s): {self.current_video_rentals}"

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