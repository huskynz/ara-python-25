class Jar:
    """ JAR """
    def __init__(self, cookie_count = 0, calories_count = 0):
        self.all_cookies = []
        self.cookie_count = cookie_count
        self.calories_count = calories_count

the_Jar = Jar()
print(the_Jar.cookie_count)
print(the_Jar.calories_count)