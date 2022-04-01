import random

def san_sinh_mang_ngau_nhien(n):
    mang=[]
    
    for i in range(n):
        so_ngau_nhien = random.randint(0,100)
        mang.append(so_ngau_nhien)
        
    return mang

def sap_xep_noi_bot(mang):
    n = len(mang)
    
    for i in range(n): # i =[0,n-1]
        tiep_tuc = False
        
        for j in range(n-2, i-1, -1): # j = [n-2, i]
            if mang[j] > mang[j+1]:
                mang[j],mang[j+1] = mang[j+1], mang[j]
                tiep_tuc = True
                
        print(i + 1, '-', mang)
        
        if tiep_tuc == False:
            break
def main():
    mang = san_sinh_mang_ngau_nhien(10)
    #n=int(input("Nhap so phan tu trong mang: \n"))
    #mang=[]
    #for i in range(n):
        #mang.append(int(input()))
    print("Mang ban dau la:\n", mang)
    sap_xep_noi_bot(mang)
    print("Mang sau khi sap xep la:\n",mang)

if __name__ == '__main__':
    main()
                
        