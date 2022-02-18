# 최댓값 구하기
SELECT max(DATETIME) FROM ANIMAL_INS

# 최솟값 구하기
SELECT min(datetime) FROM ANIMAL_INS

# 동물 수 구하기
SELECT count(*) FROM ANIMAL_INS

# 중복 제거하기
SELECT count(distinct name) FROM ANIMAL_INS
