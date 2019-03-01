
password = "a123456"
x=3
while x > 0 :
    x = x - 1
    passw = input("請輸入密碼")
    if passw == password :
        print("登入成功")
        break
    else:
        print("登入失敗")
        if x >0 :
            print("登入失敗剩下", x, "次機會")

