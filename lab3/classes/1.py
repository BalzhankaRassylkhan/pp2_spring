class string:
    def get_str(self):
        self.string = input()
    def print_string(self):
        print(self.string.upper())


x=string()
x.get_str()
x.print_string