def solution(genres, plays):
    answer = []
    dic_cnt = dict() # 장르 : 재생 횟수
    dic_sep = dict() # 장르 : (곡 번호, 재생 횟수)
    
    for i in genres:
        dic_cnt[i] = 0
        dic_sep[i] = []
        
    idx = 0
    for genre, play in zip(genres, plays):
        dic_sep[genre].append((idx, play))
        dic_cnt[genre] += play
        idx += 1
        
    sorted_cnt = sorted(dic_cnt.items(), key=lambda x:x[1], reverse=True)


    for genre, _ in sorted_cnt:
        fin = sorted(dic_sep[genre], key=lambda x:x[1], reverse=True)
        answer += [idx for idx, _ in fin][:2]
    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]	
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
