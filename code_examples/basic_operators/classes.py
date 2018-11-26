import math


class Empty:
    pass


class Point:
    display_name = ""

    # it's not safe to use mutable types like list or dict as class attributes
    # (shared across the all class instances)
    coordinates = []

    # private attributes
    __private_name = "just a name"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates.append((x, y))

    def distance(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    @classmethod
    def help(cls):
        print("This is a class method example")

    def __str__(self):
        return "Point[{point.display_name}]({point.x:.2f}, {point.y:.2f})".format(point=self)


class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, point):
        return math.sqrt((self.x - point.x) ** 2 +
                         (self.y - point.y) ** 2 +
                         (self.z - point.z) ** 2)

    def __str__(self):
        return "Point[{point.display_name}]({point.x:.2f}, {point.y:.2f}, {point.z:.2f})".format(point=self)


p1, p2 = Point(2.0, 3.0), Point(1.0, 1.0)
p1.display_name = "p1"
p2.display_name = "p2"
print("Distance between %s and %s is %.2f" % (p1, p2, p1.distance(p2)))
# print(p1.__private_name)

print("P1 coordinates: %s" % p1.coordinates)
print("P2 coordinates: %s" % p2.coordinates)

print(Point3D(1.0, 2.0, 3.0))


class Base1:
    def base_1(self):
        print("Base 1 method")


class Base2:
    def base_2(self):
        print("Base 2 method")


class ExtendedBase(Base1, Base2):
    pass


obj = ExtendedBase()
obj.base_1()
obj.base_2()

empty_obj = Empty()
print("Does empty object have 'name' attribute? %s" % hasattr(empty_obj, "name"))
print("empty_obj.name: '%s'" % getattr(empty_obj, "name", ""))

setattr(empty_obj, 'name', 'EMPTY')
print("Does empty object have 'name' attribute? %s" % hasattr(empty_obj, "name"))
print("empty_obj.name: '%s'" % getattr(empty_obj, "name", ""))

delattr(empty_obj, "name")
print("Does empty object have 'name' attribute? %s" % hasattr(empty_obj, "name"))
print("empty_obj.name: '%s'" % getattr(empty_obj, "name", ""))
