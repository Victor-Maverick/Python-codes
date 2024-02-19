class Gun:

    def __init__(self, no_of_bullets: int, is_magazine_empty: bool):
        self.is__magazine_empty = is_magazine_empty
        self.__no_of_bullets = no_of_bullets

    def reload(self):

        if not self.__no_of_bullets >= 0 or not self.__no_of_bullets < 5:
            self.__no_of_bullets = self.__no_of_bullets
        else:
            self.__no_of_bullets += 1

    def check_empty(self):
        if self.__no_of_bullets == 0:
            self.is__magazine_empty = True
        else:
            self.is__magazine_empty = False
        return self.is__magazine_empty

    def check_magazine(self):
        return self.__no_of_bullets

    def shoot(self):
        if self.__no_of_bullets > 0:
            self.__no_of_bullets -= 1
        else:
            print('empty')

    def replace_magazine(self):
        self.__no_of_bullets = 5
