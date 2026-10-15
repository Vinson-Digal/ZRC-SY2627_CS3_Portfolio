# Single Inheritance
class SingleParent:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def func1(self):
        print(f"{self.__name}: This function is in the parent class.")


class SingleChild(SingleParent):
    def func2(self):
        print(f"{self.get_name()}: This function is in the child class.")


print("Single Inheritance")
c1 = SingleChild("Child A")
c1.func1()
c1.func2()
c1.set_name("Child A (renamed)")
c1.func2()
c2 = SingleChild("Child B")
c2.func1()


# Multilevel Inheritance
class Grandfather:
    def __init__(self, grandfathername):
        self.__grandfathername = grandfathername

    def get_grandfathername(self):
        return self.__grandfathername

    def set_grandfathername(self, grandfathername):
        self.__grandfathername = grandfathername


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        super().__init__(grandfathername)
        self.__fathername = fathername

    def get_fathername(self):
        return self.__fathername

    def set_fathername(self, fathername):
        self.__fathername = fathername


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        super().__init__(fathername, grandfathername)
        self.__sonname = sonname

    def get_sonname(self):
        return self.__sonname

    def set_sonname(self, sonname):
        self.__sonname = sonname

    def print_name(self):
        print("Family tree:")
        print("  Grandfather:", self.get_grandfathername())
        print("  └─ Father  :", self.get_fathername())
        print("     └─ Son  :", self.get_sonname())


print("\nMultilevel Inheritance")
s1 = Son("Prince", "Manerva", "Mary Grace")
print(s1.get_grandfathername())
s1.print_name()

s1.set_sonname("Arjun")
s1.set_fathername("Ramesh")
print()
s1.print_name()

s2 = Son("Sampaguita", "Isabel", "August")
print()
s2.print_name()


# Hierarchical Inheritance
class HParent:
    def __init__(self, family_name):
        self.__family_name = family_name

    def get_family_name(self):
        return self.__family_name

    def set_family_name(self, family_name):
        self.__family_name = family_name

    def func1(self):
        print(f"This function is in the parent class of the {self.__family_name} family.")


class Child1(HParent):
    def func2(self):
        print(f"This function is in child 1 of the {self.get_family_name()} family.")


class Child2(HParent):
    def func3(self):
        print(f"This function is in child 2 of the {self.get_family_name()} family.")


print("\nHierarchical Inheritance")
object1 = Child1("Santos")
object2 = Child2("Santos")
object1.func1()
object1.func2()
object2.func1()
object2.func3()

object2.set_family_name("Reyes")
object2.func3()
object3 = Child1("Cruz")
object3.func2()

