
def __init__(self,color):
    self.color = color

    def get_color(self,color):
        return self.color
    
    def set_color(self,color):
        self.color = color

        Cookiesone = Cookies("blue")
        cookietwo = Cookies("red")

        print('cookie is green', Cookiesone.get_color())
        print('cookie is red', cookietwo.set_color())   