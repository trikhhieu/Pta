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

#     def __init__(self,name,age,weight,type,color,sex):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.type = type
#         self.color = color
#         self.sex = sex 
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

# class people:
#     def __init__(self,chauluc,ten,tuoi,mauda,cannang,chieucao):
#         self.chauluc = chauluc
#         self.ten = ten
#         self.tuoi = tuoi
#         self.mauda = mauda
#         self.cannang = cannang
#         self.chieucao = chieucao 

    
# person1 = people("chau phi","Ben","18","da den","75kg","175")
# print(person1.chauluc)
# print(person1.ten)
# print(person1.tuoi)
# print(person1.mauda)
# print(person1.cannang)
# print(person1.chieucao)

# class PhuongTien: # dong goi
#     def __init__(self, loai_xe, hang_xe, mau_sac, so_cho_ngoi, so_banh_xe, gia_tien):
#         self.loai_xe = loai_xe
#         self.hang_xe = hang_xe
#         self.mau_sac = mau_sac
#         self.so_cho_ngoi = so_cho_ngoi
#         self.so_banh_xe = so_banh_xe
#         self.gia_tien = gia_tien
#     def Thongtin(self):
#         print("loai xe: ",self.loai_xe)
#         print("hang xe: ",self.hang_xe)
#         print("mau xe: ",self.mau_sac)
#         print("so cho ngoi: ",self.so_cho_ngoi)
#         print("so banh xe: ",self.so_banh_xe)
#         print("gia tien: ", self.gia_tien)


# vehicle1 = PhuongTien("Xe_hoi", "Ford", "red", 7, 4, 50000000)
# print("Loại xe:", vehicle1.loai_xe)
# print("Hãng xe:", vehicle1.hang_xe)
# print("Màu sắc xe:", vehicle1.mau_sac)
# print("Số chỗ ngồi xe:", vehicle1.so_cho_ngoi)
# print("Số bánh xe:", vehicle1.so_banh_xe)
# print("Giá tiền của xe:", vehicle1.gia_tien)
# ThuCung:
#     def __init__(self,Ten,Giong,Mausac,Tuoi,Cannang):
#         self.Ten = Ten
#         self.Giong = Giong
#         self.Mausac = Mausac
#         self.Tuoi = Tuoi
#         self.Cannang = Cannang
#     def Thongtin(self):
#         print("Ten: ",self.Ten)
#         print("Giong: ",self.Giong)
#         print("Mau sac: ", self.Mausac)
#         print("Tuoi: ",self.Tuoi)
#         print("Can nang",self.Cannang)
# cho1 = ThuCung("lucy","chihuahua","mau nau",5,"13kg")
# cho1.Thongtin()
# print(" ")
# meo1= ThuCung("my","meo rung","trang nau","3","5kg")
# meo1.Thongtin()
# class 
# Lớp cha
# class Xe:
#     def __init__(self, hang, mau_sac, gia_tien):
#         self.hang = hang
#         self.mau_sac = mau_sac
#         self.gia_tien = gia_tien

#     def khoi_dong(self):
#         print(f"Xe {self.hang} đang khởi động")

# # Lớp con XeDap kế thừa từ lớp Xe
# class XeDap(Xe):
#     def dap_bang_hai_chan(self):
#         print(f"Xe {self.hang} đang được đạp về phía trước")

# # Lớp con XeHoi kế thừa từ lớp Xe
# class XeHoi(Xe):
#     def chay_bang_bon_banh(self):
#         print(f"Xe {self.hang} đang chạy về phía trước bằng động cơ")

# # Sử dụng các lớp
# xe_dap = XeDap("Giant", "Xanh", 2000)
# xe_dap.khoi_dong()
# xe_dap.dap_bang_hai_chan()

# xe_hoi = XeHoi("Toyota", "Đỏ", 500000)
# xe_hoi.khoi_dong()
# xe_hoi.chay_bang_bon_banh()


class Xe:
    def __init__(self,Hang,Mausac,Giatien):
        self.Hang = Hang
        self.Mausac = Mausac
        self.Giatien = Giatien

    def Khoidong(self):
        print(f"xe {self.Hang} dang khoi dong")

class xedap(Xe):
    def chay_bang_bon_banh(self):
        print(f"xe {self.Hang} dang duoc dap ve phia truoc")

class xeoto(Xe):
    def chay_bang_dong_co(self):
        print(f"xe {self.Hang} dang duoc chay bang dong co ve phia truoc")

xe1 = xedap("patin","xam","1tr")
xe1.Khoidong()
xe1.chay_bang_bon_banh()

xe2 = xeoto("ford","nau","2ty")
xe2.Khoidong()
xe2.chay_bang_dong_co()




    