class Account:

    def __init__(self, name, followers, description, country):
        self.name = name
        self.followers = followers
        self.dis = description
        self.country = country

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.dis, self.country)

    def __getitem__(self, item):
        return self.followers
