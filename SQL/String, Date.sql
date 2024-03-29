# 루시와 엘라 찾기
SELECT DISTINCT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty")
ORDER BY ANIMAL_ID

# 이름에 el이 들어가는 동물 찾기
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE ("%EL%")
AND ANIMAL_TYPE = "DOG"
ORDER BY NAME

# 중성화 여부 파악하기
SELECT ANIMAL_ID, NAME, 
IF (SEX_UPON_INTAKE LIKE "%INT%", "X", "O") AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

# 오랜 기간 보호한 동물(2)
SELECT A.ANIMAL_ID, A.NAME 
FROM ANIMAL_INS A JOIN ANIMAL_OUTS B
USING (ANIMAL_ID)
ORDER BY B.DATETIME - A.DATETIME DESC LIMIT 2

# DATETIME에서 DATE로 형 변환
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME,"%Y-%m-%d") AS "날짜"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

# 취소되지 않은 진료 예약 조회하기 (난이도 4)
SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, D.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM APPOINTMENT A
JOIN PATIENT P
    ON A.PT_NO = P.PT_NO
JOIN DOCTOR D 
    ON A.MDDR_ID = D.DR_ID 
WHERE A.APNT_YMD LIKE '2022-04-13%'
    AND D.MCDP_CD = 'CS'
    AND A.APNT_CNCL_YN = 'N'
ORDER BY A.APNT_YMD ASC