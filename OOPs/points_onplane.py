class point:
    def __init__(self, a, b) -> None:
        self.x = a
        self.y = b

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def odistance(self):
        return (self.x ** 2 + self.y ** 2) ** .5


    def __str__(self) -> str:
        return str((self.x, self.y))  

    def __repr__(self) -> str:
        return str([self.x, self.y])

      

p = point(3, 5)


# print(p.x)  # 3
# print(p.y)  # 5

p.move(2, 5)

print(p.x)  # 5
print(p.y)  # 10

print("distance from origin ", p.odistance())

print("point display ", p)
print("point display ", [p])


