person = "210818-3XXXXXX"
year = person[0:2]
month = person[3]
day = person[4:6]
gender = person[7]
print("20" + year + "년 " + month + "월 " + day + "일")
if gender == "3":
    print("남자입니다")
else:
    print("여자입니다")
