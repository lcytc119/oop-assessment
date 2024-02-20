# ENSURE EVERYTHING BELOW IS COMMENTED WHEN YOU SUBMIT YOUR ASSESSMENT AND RUN TESTS
from classes.store import Store
from classes.customer import Customer
import csv
# block_buster = Store("Block Buster")
# block_buster.load_data("inventory")
# block_buster.load_data("customers")
# print(block_buster.run_the_store())

# sample = Customer('Try one', '')
# sample_movie = Store( '', '', ' ', '',"")
# print(sample_movie)
# print(sample.id)

# Customer.all_customers("./data/customers.csv")
# print(Customer.all_customers_lst)
# Store.all_inventory("./data/inventory.csv")
# print(Store.all_inventory_lst)
# customer_name = "Monica Gellar"
# # rental_movie = Customer.get_rental("Monice", "Gellar")
# print(Customer.get_rental())

# Make terminal menu
main_menu_message = """
== Welcome to Code Platoon Video! ==
1. View store video inventory
2. View customer rented videos
3. Add new customer
4. Rent video
5. Return video
6. Exit
"""
# 1. view all video inventory
def display_video_inventory():
    Store.all_inventory("./data/inventory.csv")
    print(Store.all_inventory_lst)
    display_main_menu()

# 2. view a customer's rental if exist
def view_customer_rental():
    get_name = input ("What is the name of the customer you want to check. Please follow first name and last name order.")

    found_customer = Customer.get_customer_by_name(get_name,'./data/customers.csv')

    if found_customer:
        rentals = found_customer.get_rental
        rentals_string = ', '.join(rentals)
        if rentals:
            print(f"Rental movies for {get_name}: {rentals_string}")
        else:
            print(f"{get_name} has no rented movies")
    else:
        print("Customer not found.")

    display_main_menu()
# 3. adding a new customer information:
#   3.1. new id. 2.first_name and last_name. 3.account type
def add_new_customer():
    customers = Customer.all_customers("./data/customers.csv")

    next_id = max([int(element.id) for element in customers]) + 1 if customers else 1
    first_name = input("Enter first name of new customer: ")
    last_name = input("Enter last name of new customer: ")
    account_type = input("Enter account type of this customer(sx, ps, sf or pf): ") 

    new_customer = Customer(id = next_id, account_type=account_type, first_name=first_name, last_name=last_name, current_video_rentals="")
    Customer.add_a_customer(new_customer, "./data/customers.csv")
    display_main_menu()

# 4. rent a video for a customer
def rent_video():
    get_name = input("What is the name of the customer?")
    
    customer = Customer.get_customer_by_name(get_name,"./data/customers.csv")
    if customer:
        account_type =customer.account_type
        max_rental=0
        if account_type == "sx":
            max_rental = 1
        elif account_type == "px":
            max_rental = 3
        elif account_type == "sf":
            max_rental = 1
        elif account_type == "pf":
            max_rental = 3

        if len(customer.get_rental)>=max_rental:
            print("This customer can't rent more movie this time. ")
        else:
            get_movie_title = input("What's the movie customer wants to rent?")
            found_movie = Store.get_video_by_title(get_movie_title, "./data/inventory.csv")

            if found_movie:
                if found_movie.rating == "R" and account_type in ['sf', 'pf']:
                    print("Customer doesn't allow renting 'R' rated movie.")
                else:
                    rentals = customer.get_rental
                    rentals.append(get_movie_title)
                    print(f"Movie {get_movie_title} has been rented for {get_name}")
                    # Sorry this is the hardest part for me to rewrite it on csv which I spent four hours and can't figure it out I have to move on to next
                    # Customer.update_customer_info(get_name, './data/customers.csv')
            else:
                print("Movie not found")
    else:
        print("Customer not found. ")
    display_main_menu()

# 5. return a video for a customer    
def return_video():
    pass


def display_main_menu():
    user_main_menu_input = input(main_menu_message)

    if user_main_menu_input == "1":
        display_video_inventory()
    elif user_main_menu_input == "2":
        view_customer_rental()
    elif user_main_menu_input == "3":
        add_new_customer()
    elif user_main_menu_input == "4":
        rent_video()
    elif user_main_menu_input == "5":
        return_video()
    # Quit
    elif user_main_menu_input == "6":
        exit()

    #Invalid input
    else:
        print("Invalid input, please try again")
        display_main_menu()

display_main_menu()

def test_get_video_by_title():
    path_to_file="./data/inventory.csv"
    title_existing = "Toy Story"
    found_movie = Store.get_video_by_title(title_existing, path_to_file)
    Store.all_inventory(path_to_file)
    all_inventory_lst = Store.all_inventory_lst
    # assert found_movie is not None 
    # print(Store.all_inventory_lst)
    # print(Store.all_inventory_lst.title)
    # print(f"Found movie {title_existing}: {found_movie}")
    print(found_movie.copies_available)
# test_get_video_by_title()
    # found_movie = Store.get_video_by_title("Toy Story", "./data/inventory.csv")
    # if found_movie:
    #     print("Found movie:", found_movie)
    # else:
    #     print("Movie not found.")