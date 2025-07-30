
def __init__(self,color):
    self.color = color

    def get_color(self,color):
        return self.color
    
    def set_color(self,color):
        self.color = color

        cookie_one = Cookies('red')
        Cookie_two = Cookies('blue')

        print('Cookie_one is red' , Cookie_one.get_color())
        print('cookie_two is blue', Cookie_two.set_color())

