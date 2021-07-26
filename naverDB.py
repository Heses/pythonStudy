# 파이썬에서 디비에 데이터 입력 -> 데이터 입력 멈추면 전체 조회

import sqlite3

con, cur=None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

row =None

con = sqlite3.connect("C:/sqlite3/naverDB") #데이터베이스 연결

cur = con.cursor() #커서 생성

while (True):
    data1 = input("사용자ID==> ")
    if data1 == "" :
        break;
    data2 = input("사용자이름==> ")
    data3 = input("이메일==> ")
    data4 = input("출생연도==> ")

    sql="INSERT INTO userdb VALUES('"+data1+"','"+data2+"','"+data3+"',"+data4+")" #문자열을 ''로 묶음, 정수는 ""로만
    cur.execute(sql)

con.commit()


cur.execute("SELECT * FROM userdb")
print("사용자ID     사용자이름     이메일         출생연도")
print("-------------------------------------")

while (True):
    row = cur.fetchone() #조회한 데이터를 한 행씩 접근한 후 출력하는 함수???
    if row == None:
        break;
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%s  %15s  %20s  %d" %(data1,data2,data3,data4))


#cur.execute("CREATE TABLE userdb (id char(4), userName char(15), email char(20), birthYear int)")

#cur.execute("INSERT INTO userdb VALUES('yejin','sieben','yoru@naver.com','1997')")
#cur.execute("INSERT INTO userdb VALUES('dori','kim','mangu@naver.com','1997')")


con.close()
