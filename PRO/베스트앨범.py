def solution(genres, plays):
    from collections import defaultdict
    
    # 장르별 총 재생 수
    genre_total = defaultdict(int)
    
    # 장르별 노래 리스트 (재생 수, 고유번호)
    genre_songs = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] += p
        genre_songs[g].append((p, i))
    
    # 장르를 총 재생 수 기준으로 정렬
    sorted_genres = sorted(genre_total, key=lambda x: genre_total[x], reverse=True)
    
    answer = []
    
    # 각 장르별 상위 2개 선택
    for g in sorted_genres:
        # 재생 수 내림차순 고유번호 오름차순
        songs = sorted(genre_songs[g], key=lambda x: (-x[0], x[1]))
        
        # 최대 2개 선택
        answer.extend([idx for _, idx in songs[:2]])
    
    return answer