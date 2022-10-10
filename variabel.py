# Variabel adalah tempat menyimpan data

s = 5 
# s adalah varibel
# = adalah assigment
# 5 adalah value

# Memanggil variabel
print(s)
print("nilai sandi =", s)

# penamaan varibel 
# tidak boleh menggunakan spasi/strip
# boleh menggunakan underscore 
nilai_sandi = 8  
nilaisandi = 7  
_nilai_sandi = 6  

print(nilai_sandi)
print(nilaisandi)
print(_nilai_sandi)

# 50sandi = 50 tidak boleh
# sandi50 = 50 boleh
# nilaiS = 100 boleh
sandi50 = 50
nilaiS = 100
print(sandi50)
print("nilai teringgi sandi=", nilaiS)

# penggantian variabel 
b = nilaiS 
print("nilai teringgi sandi=", b)
# maka output-nya akan sama nilaiS awal

# merubah value dengan variabel yang sama
nilaiS = 90
print("nilai teringgi sandi=", nilaiS)
# maka nilaiS berubah dari yang tadinya 100 jadi 90
# tetapi tidak merubah value awal

# bisa juga seperti ini
b = nilaiS
print("nilai teringgi sandi=", b)
# maka output akan sama sesuai value terbaru



