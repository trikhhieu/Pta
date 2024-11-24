class Hocsinh:
    def __init__(self,hoten,diachi,chieucao,cannang,hocluc):
        self.hoten = hoten
        self.diachi = diachi
        self.chieucao = chieucao
        self.cannang = cannang
        self.hocluc = hocluc
    def thongtin(self):
        print("ho va ten: ",self.hoten)
        print("dia chi: ",self.diachi)
        print("chieu cao: ",self.chieucao)
        print("can nang: ",self.cannang)
        print("hoc luc: ",self.hocluc)
    def diachi_moi(self,diachimoi):
        self.diachi = diachimoi
        print("dia chi moi la: ",self.diachi)
    def chieucao_moi(self,chieucaomoi):
        self.chieucao = chieucaomoi
        if self.chieucao>0:
            print("chieu cao moi la: ",self.chieucao)
        else:
            print("ko hop le")
    def cannang_moi(self,cannangmoi):
        self.cannang = cannangmoi
        if self.cannang >0:
            print("can nang moi la: ",self.cannang)
        else:
            print("ko hop le")
hocsinh1 = Hocsinh("Nguyen van a","1 nguyen hue, quan 1",175,67,"gioi")
hocsinh1.thongtin()
hocsinh1.diachi_moi("hanoi")
hocsinh1.chieucao_moi(180)
hocsinh1.cannang_moi(80)
hocsinh1.thongtin()