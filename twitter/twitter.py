from models import *
from database import init_db, db_session
from datetime import datetime

class Twitter:
    """
    The menu to print once a user has logged in
    """

    def __init__(self):
        self.logged_in = False
        self.handle = None
        self.current_user = None
    def print_menu(self):
        print("\nPlease select a menu option:")
        print("1. View Feed")
        print("2. View My Tweets")
        print("3. Search by Tag")
        print("4. Search by User")
        print("5. Tweet")
        print("6. Follow")
        print("7. Unfollow")
        print("0. Logout")
    
    """
    Prints the provided list of tweets.
    """
    def print_tweets(self, tweets):
        for tweet in tweets:
            print("==============================")
            print(tweet)
        print("==============================")

    """
    Should be run at the end of the program
    """
    def end(self):
        print("Thanks for visiting!")
        db_session.remove()
    
    """
    Registers a new user. The user
    is guaranteed to be logged in after this function.
    """
    def register_user(self):
            while (registered == False):
                init_pass = None
                registered = False
                handle = input("What will your twitter handle be? ")
                init_pass = input("Enter a password: ")
                check_pass = input("Re-enter the password: ")
                existing_user = db_session.query(User.username).filter(User.username == handle).first()
                if (existing_user):
                    print("This handle is taken.")
                if (init_pass != check_pass):
                    print("The passwords don't match.")
                if (not(existing_user) & (init_pass == check_pass)):
                    registered = True
                    final_pass = init_pass
                if (registered == True):
                    print("Welcome: " + handle)
                    new_user = User(handle, final_pass)
                    db_session.add(new_user)
                    db_session.commit()
                   
    """
    Logs the user in. The user
    is guaranteed to be logged in after this function.
    """
    def login(self):
        username_check,password_check = None
        while (self.logged_in == False):
            username_check = input("Username: ")
            password_check = input("Password: ")
            user = db_session.query(User).filter((User.username == username_check) & (User.password == password_check)).first()
            if(user):
                self.logged_in = True
            else:
                print("Invalid username or password")

        

    
    def logout(self):
        self.logged_in = False
    """
    Allows the user to login,  
    register, or exit.
    """
    def startup(self):
        user_input = input("Welcome to ATCS Twitter" + "\n" + "Please select a menu option" + "\n" + 
                            "1. Login" + "\n" + "2. Register" + "\n" + "0. Exit")
        if user_input == 1:
            self.login()
        elif user_input == 2:
            self.register_user()
        elif user_input == 0:
            self.end()
        

    def follow(self):
        other_user = input("Who would you like to follow?" + "\n")
        following_user = False
        for following in self.current_user.followings:
            if following.username == other_user:
                print("You already follow" + other_user)
                following_user = True
        if following_user == False:
            user = db_session.query(User).filter(User.username == other_user).first()
            self.current_user.following.append(user)

    def unfollow(self):
        pass

    def tweet(self):
        pass
    
    def view_my_tweets(self):
        pass
    
    """
    Prints the 5 most recent tweets of the 
    people the user follows
    """
    def view_feed(self):
        pass

    def search_by_user(self):
        pass

    def search_by_tag(self):
        pass

    """
    Allows the user to select from the 
    ATCS Twitter Menu
    """
    def run(self):
        init_db()
        if(self.logged_in == True):
            print("Welcome to ATCS Twitter!")
            self.startup()

            self.print_menu()
            option = int(input(""))

            if option == 1:
                self.view_feed()
            elif option == 2:
                self.view_my_tweets()
            elif option == 3:
                self.search_by_tag()
            elif option == 4:
                self.search_by_user()
            elif option == 5:
                self.tweet()
            elif option == 6:
                self.follow()
            elif option == 7:
                self.unfollow()
            else:
                self.logout()
            
            self.end()
