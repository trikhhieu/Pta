# class Cat:
#     # name = ""
#     # age = ""
#     # weight = ""
#     # type = ""
#     # color = ""
#     # sex = ""


# pet1 = Cat()
# Cat.name = "an"
# Cat.age = "3"

    # def __init__(self,name,age,weight,type,color,sex):
    #     self.name = name
    #     self.age = age
    #     self.weight = weight
    #     self.type = type
    #     self.color = color
    #     self.sex = sex 
# pet1 = Cat()
# print(pet1.name == "an")


# class vatnuoi:
#     def __init__(self,giong,mausac,tuoi,cannang):
#         self.giong = giong
#         self.mausac = mausac
#         self.tuoi = tuoi
#         self.cannang = cannang
# pet1 = vatnuoi("husky","xam trang","5","15kg")
# print(pet1.giong)
# print(pet1.tuoi)
# print(pet1.mausac)
# print(pet1.cannang)

class people:
    def __init__(self,chauluc,ten,tuoi,mauda,cannang,chieucao):
        self.chauluc = chauluc
        self.ten = ten
        self.tuoi = tuoi
        self.mauda = mauda
        self.cannang = cannang
        self.chieucao = chieucao 
person1 = people("chau phi","Ben","18","da den","75kg","175")
print(person1.chauluc)
print(person1.ten)
print(person1.tuoi)
print(person1.mauda)
print(person1.cannang)
print(person1.chieucao)
