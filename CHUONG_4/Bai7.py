from math import sqrt, pow
def DoDai (Xa,Xb,Ya,Yb):
    return sqrt(pow((Xb-Xa),2) + pow((Yb-Ya),2))
Xa = int(input("Nhap Xa:"))
Ya = int(input("Nhap Ya:"))
Xb = int(input("Nhap Xb:"))
Yb = int(input("Nhap Yb:"))
print("Độ Dài AB là: ",DoDai(Xa,Xb,Ya,Yb))