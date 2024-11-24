class TaiKhoanNganHang:
    def __init__(self, ten_ngan_hang, ten_chu_tai_khoan, so_tai_khoan, so_du=0):

        self.ten_ngan_hang = ten_ngan_hang                
        self.ten_chu_tai_khoan = ten_chu_tai_khoan        
        self.so_tai_khoan = so_tai_khoan                  
        self.so_du = so_du  
    def taikhoan(self):
        print("Ngan hang: ",self.ten_ngan_hang)
        print("tai khoan: ",self.ten_chu_tai_khoan)
        print("so tai khoan: ",self.so_tai_khoan)
        print("so du: ",self.so_du)
    def nap_tien(self,so_tien):
        self.so_du += so_tien
        if so_tien>0:
            print(f"nap thanh cong.So du hien tai la {self.so_du}")
        else:
            print("ko hop le")
             
    def rut_tien(self,so_tien):
        self.so_du -= so_tien
        if self.so_du >so_tien:
            if so_tien>0:
                print(f"rut thanh cong.So du hien tai la{self.so_du}")
            else:
                print("ko hop le")
        else:
            print("so du ko du")
    def so_du_trong_tai_khoan(self):
        print(f"so du hien tai la {self.so_du}")   

taikhoan1 = TaiKhoanNganHang("Minh tri bank","Nguyen Minh Tri","123456789",10000000000)
taikhoan1.taikhoan()
taikhoan1.nap_tien(100000)
taikhoan1.rut_tien(20000)
taikhoan1.so_du_trong_tai_khoan()


     