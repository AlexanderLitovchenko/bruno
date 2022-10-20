class StringVar():
    string = 'empty string'

    def set(self):
        self.string = input('Change the string: ')

    def get(self):
        return self.string

a = StringVar

