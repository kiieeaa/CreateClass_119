
class persegipanjang:
    def __init__(self,panjang ,lebar):
          self.panjang = panjang
          self.lebar = lebar

    def hitung_keliling(self):
        return 2 *(self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
     return f"persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"


if __name__=="__main__":
     try:
          panjang = float (input ("masukin panjangnya berapa??"))
          lebar = float (input ("masukin lebar berapaa??"))

          if panjang <= 0 or lebar <= 0:
               raise ValueError("panjang dan lebar harus lebih besar dari nol.")
          

          p = persegipanjang(panjang , lebar)
          print(p)
          print("keliling: ",p.hitung_keliling())
          print("luas:" , p.hitung_luas())

     except Exception as e:
          print(f"terdapat kesalahan saat membuat objek: {e}")

