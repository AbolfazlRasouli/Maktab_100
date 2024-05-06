class app:
    def __init__(self, name) -> None:
        self.name = name
        # self.rate = []
        self.star = 0
        self.rate_num = 0


    def calculate_star(self, new_rate):
        self.star = ( (self.star * self.rate_num) + new_rate) / (self.rate_num + 1)
        self.rate_num += 1 


    def get_star(self):
        return self.star





def main():
    app_1 = app('one')
    app_1.calculate_star(0)
    app_1.calculate_star(2)
    app_1.calculate_star(5)
    app_1.calculate_star(4)
    app_1.calculate_star(1)

    print(app_1.get_star())


main()

