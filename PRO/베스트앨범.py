def solution(genres, plays):
    genre_total = {}   # 장르별 총 재생 수
    genre_songs = {}   # 장르별 노래 리스트
    
    # 데이터
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        
        # 총합
        if g not in genre_total:
            genre_total[g] = 0
        genre_total[g] += p
        
        # 노래 리스트
        if g not in genre_songs:
            genre_songs[g] = []
        genre_songs[g].append((p, i))
    
    # 장르 정렬 (총 재생 수 기준)
    sorted_genres = sorted(
        genre_total.keys(),
        key=lambda x: genre_total[x],
        reverse=True
    )
    
    answer = []
    
    # 각 장르별 top 2
    for g in sorted_genres:
        songs = sorted(
            genre_songs[g],
            key=lambda x: (-x[0], x[1])
        )
        
        for i in range(min(2, len(songs))):
            answer.append(songs[i][1])
    
    return answer