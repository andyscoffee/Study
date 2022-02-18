# 고양이와 개는 몇 마리 있을까
SELECT animal_type, count(*) FROM ANIMAL_INS
group by animal_type order by 1

# 동명 동물 수 찾기
SELECT name, count(*) FROM ANIMAL_INS
group by name having count(name) > 1 
order by name

# 입양 시각 구하기(1)
SELECT hour(datetime) as HOUR, count(hour(datetime)) as COUNT FROM ANIMAL_OUTS
group by HOUR 
having hour >= 9 and hour <20
order by HOUR
