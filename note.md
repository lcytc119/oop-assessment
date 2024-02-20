


Make a video inventory management application
    0. Welcome page:
            == Welcome to Code Platoon Video! ==
        X1. View store video inventory
        2. View customer rented videos
        3. Add new customer
        4. Rent video
        5. Return video
        6. Exit


    x1.manage customer info:
        x- id
        x- acc type
        x- cus first name
        x- last name
        x- list of video rentals
    
    1.5 customer class
        instance attributes:
        - id
        - acc type (list of acc type object instances):
            """ 
            sx - one rental
            px - three rentals
            sf - max 1 rental out and can't rent "R" rated
            pf - max 3 rentals out and can't rent "R" rated
            """
        - customer (list of customer object instances)
        - videos (list of video object instances)
    
    2. video inventory:
        - video id
        - video title
        - video rating
        - video release year
        - num of copies available in-store
    
    2.5 video class
        instance attributes:
        - video id
        - video title
        - video infor
        - copies available
