class Roman:
    def __init__(self, num):
        self.num = num

    def convert(self):
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        result = ""
        n = self.num
        for v, s in values:
            while n >= v:
                result += s
                n -= v
        return result

n = int(input())
r = Roman(n)
print(r.convert())
