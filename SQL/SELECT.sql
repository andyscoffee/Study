# 모든 레코드 조회하기
SELECT * FROM ANIMAL_INS

# 역순 정렬하기
SELECT NAME, DATETIME FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC
# 아픈 동물 찾기

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE INTAKE_CONDITION = "Sick"

# 어린 동물 찾기
SELECT animal_id, name FROM ANIMAL_INS
where not intake_condition = "Aged"

# 동물의 아이디와 이름
SELECT animal_id, name FROM ANIMAL_INS
order by animal_id

# 여러 기준으로 정렬하기
SELECT animal_id, name, datetime FROM ANIMAL_INS
order by name, datetime desc

# 상위 n개 레코드
SELECT name FROM ANIMAL_INS
where datetime = (select min(datetime) FROM ANIMAL_INS)

# 흉부외과 또는 일반외과 의사 목록 출력하기 (난이도 1)
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD,'%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME ASC

# 3월에 태어난 여성 회원 목록 출력하기 (난이도 2)
SELECT MEMBER_ID, MEMBER_NAME, GENDER, 
    DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d')AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE GENDER='W' AND DATE_OF_BIRTH LIKE '%-03-%' AND TLNO IS NOT NULL
ORDER BY MEMBER_ID ASC

# 강원도에 있는 생산 공장 목록 출력하기 (난이도 1)
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '강원도%'
ORDER BY FACTORY_ID ASC