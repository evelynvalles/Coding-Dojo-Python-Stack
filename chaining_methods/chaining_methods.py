class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"First_name: {self.first_name}")
        print(f"Last_name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is_rewards_member: {self.is_rewards_member}")
        print(f"Gold_card_points: {self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member")

        self.is_rewards_member = True
        # print(self.is_rewards_member)
        self.gold_card_points = 200
        # print(self.gold_card_points)
        return self

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("You don't have enough points")
            return False

        self.gold_card_points = self.gold_card_points - amount
        # print(self.gold_card_points)
        return self

evelyn = User("evelyn","valles","ev@gmail.com",21)
freddie = User('freddie','mac','fm@gmail.com',25)
daniel = User('daniel','martinez','dm@yahoo.com',20)
daniel.display_info()

evelyn.display_info().enroll().spend_points(50).display_info()
freddie.enroll().spend_points(80).display_info()