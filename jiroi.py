 # _*_ coding: utf-8 _*_
import random

def recur(x,y,arr,varr):
    end = 0
    #count = 주변에 지뢰가 얼마나 있는가?
    count = 0
    #지뢰 밟았을때(mine). result=[리스트,사용자에 보이는 리스트,결과] 반환정보: 0:지뢰를 밟음: 실패 1:빈 칸을 열음 2:이미 연 칸을 열음
    if arr[x][y]== "m":
        print "You trapped Mine!"
        result = [0,0,0]
        return result
    #이미 연칸을 또 열었을때
    elif arr[x][y] == "f":
        print "Hey!"
        result = [arr,varr,2]
        return result
    #빈칸을 열 때
    else:
        #주변에 지뢰가 얼마나 있는지 카운트를 올린다. 비효율적인 코드같음 정리해야할듯
        if (x >= 1 and y >= 1) and (x <= (n-2) and y <= (n-2)):
            if arr[x + 1][y] == "m":
                count += 1
            if arr[x][y + 1] == "m":
                count += 1
            if arr[x - 1][y] == "m":
                count += 1
            if arr[x][y - 1] == "m":
                count += 1
        if x == n-1 or y == n-1:
            if x != 0:
                if arr[x - 1][y] == "m":
                    count += 1
            if y != 0:
                if arr[x][y - 1] == "m":
                    count += 1
            if y != n-1:
                if arr[x][y + 1] == "m":
                    count += 1
            if x != n-1:
                if arr[x + 1][y] == "m":
                    count += 1
        if x == 0 or y == 0:
            if x != n-1:
                if arr[x + 1][y] == "m":
                    count += 1
            if y != n-1:
                if arr[x][y + 1] == "m":
                    count += 1
            if y != 0:
                if arr[x][y - 1] == "m":
                    count += 1
            if x != 0:
                if arr[x - 1][y] == "m":
                    count += 1

        #temp는 resursive돌리기 전의 arr정보 저장.
        temp = arr[x][y]
        #varr는 사용자에 보이는 지뢰찾기 배열값:: count값 저장
        varr[x][y] = str(count)
        #arr은 내부에서 돌아가는 지뢰찾기 배열값: 지뢰가 없으면 "F"값 저장.
        arr[x][y] = "f"
        result = [arr,varr,1]

        #내부에서 잘 돌아가는지 확인 이거는 나중에 주석 처리 할것.
        #for i in arr:
        #    print i

        #지뢰 찾기 Recursive. 이것도 위에 코드랑 같이 정리할 필요가 있음
        if (x>=1 and y>=1) and (x<=(n-2) and y<=(n-2)):
            if temp == arr[x-1][y]:
                recur(x-1,y,arr,varr)
            if temp == arr[x][y-1]:
                recur(x,y-1,arr,varr)
            if temp == arr[x+1][y]:
                recur(x+1,y,arr,varr)
            if temp == arr[x][y+1]:
                recur(x,y+1,arr,varr)
        if x==n-1 or y == n-1:
            if x != 0:
               if temp == arr[x - 1][y]:
                   recur(x - 1, y, arr,varr)
            if y != 0:
                if temp == arr[x][y - 1]:
                    recur(x, y - 1, arr,varr)
            if y != n-1:
                if temp == arr[x][y + 1]:
                    recur(x, y + 1, arr,varr)
            if x != n-1:
                if temp == arr[x+1][y]:
                    recur(x+1, y, arr,varr)
        if x==0 or y==0:
            if x != n-1:
                if temp == arr[x + 1][y]:
                     recur(x + 1, y, arr,varr)
            if y != n-1:
                if temp == arr[x][y + 1]:
                  recur(x, y + 1, arr,varr)
            if y != 0:
                if temp == arr[x][y -1]:
                    recur(x, y - 1, arr,varr)
            if x != 0:
                if temp == arr[x - 1][y]:
                    recur(x - 1, y, arr,varr)
        return result

#n은 배열의 크기 정한다.:
n = int(raw_input("Game Size:"))
#지뢰의 빈도 정하기: 지금은 5:3이 있는 배열에서 랜덤 초이스.
mine = [0,0,0,0,0,"m","m","m"]
#지뢰수
minecount=0
#지뢰 랜덤 생성
list = [[random.choice(mine) for i in range(n)] for i in range(n)]
for i in list:
    for j in i:
        if j =="m":
            minecount+=1
print minecount
random.shuffle(list)
#사용자에 보이는 지뢰찾기 배열 생성
vlist = [["#" for i in range(n)]for i in range(n)]

print "this is list \n"
for i in vlist:
    print i
#이미 찾은 빈칸 blank
blank = n**2
result = [1,1,1]
#빈칸이 지뢰보다 많을때 AND result[2]!=0: 지뢰를 밟지 않았을때
while blank>minecount and result[2]>0:
    blank = 0
    #이미 열어본 지뢰찾기 배열 또 선택할때
    if result[2]==2:
        print "This is already opened!"
    y = int(raw_input("enter x"))
    x = int(raw_input("enter y"))

    result = recur(x, y, list,vlist)
    #지뢰 안 밟았을때
    if result[2]>=1:
        print "\n result: \n"
        for i in result[1]:
            for j in i:
                if j == "#":
                    blank+=1
        for i in result[1]:
            print i
    #지뢰 밟았을때
    if result[2]==0:
        print "\n you failed! \n"


if blank == minecount:
    print "You win!"
