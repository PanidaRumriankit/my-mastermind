
class Mastermind:
    def __init__(self):
        self.__color = 0
        self.__pos = 0
        self.__ans = ''

    def setup(self, color, pos):
        import random
        if not isinstance(color, int):
            raise TypeError('color must be an integer')
        if not isinstance(pos, int):
            raise TypeError('position must be an integer')
        if color < 1 or color > 8:
            raise ValueError('color must not less than 1 or greater than 8')
        if pos < 1 or pos > 10:
            raise ValueError('position must not less than 1 or greater than 10')
        self.__color = color
        self.__pos = pos
        for i in range(pos):
            self.__ans += str(random.randint(1, color))
        # print(self.__ans)

    def get_color(self):
        return self.__color

    def get_position(self):
        return self.__pos

    def play(self):
        w = self.guess()
        if not len(w) == self.get_position():
            raise ValueError('Your guess must not be an empty string')
        for s in w:
            if not 1 <= int(s) <= self.get_color():
                raise ValueError(f'There are only {self.get_color()} colors')
        print(self.check(w))
        print()
        return w

    def all_play(self):
        print(f"Playing Mastermind with {self.get_color()} colors and {self.get_position()} positions")
        w = self.play()
        count = 1
        i = 0
        while self.__ans != w:
            w = self.play()
            count += 1
            if count % 10 == 0 and int(count/10) <= self.get_position():
                print(self.get_hint(i))
                i += 1
        print(f"You solve it after {count} rounds")

    def guess(self):
        word = input("What is your guess?: ")
        print("Your guess is", word)
        return word

    def check(self, word):
        chec = ""
        ins = []
        dup = []
        for s in self.__ans:
            dup.append(s)
        for i, s in enumerate(self.__ans):
            if word[i] == s:
                chec += '*'
                ins.append(i)
                dup.remove(word[i])
                # print(dup)
                # dup += word[i]
                # print('*:', word[i])
        for i, s in enumerate(self.__ans):
            if word[i] in dup and i not in ins:
                chec += 'o'
                dup.remove(word[i])
                # print('o:', word[i])
        return chec

    def get_hint(self, ind):
        return f"Hint: {self.__ans[ind]}???"


m = Mastermind()
m.setup(6, 4)
m.all_play()

