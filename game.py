answer = 11
count = 0
while 1:
    k = input("입력해주세요: ")
    if k.isdecimal():
        k = int(k)
        count += 1
        if k > answer:
            print("down")
        elif k < answer:
            print("up")
        else:
            print("정답")
            print(count + 1)
            break
        

    else:
        print("숫자를 입력해주세요.")

