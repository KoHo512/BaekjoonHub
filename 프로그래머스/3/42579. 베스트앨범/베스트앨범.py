def solution(genres, plays):
    playlist = {}
    genre_plays = {}
    
    for genre in set(genres):
        playlist[genre] = {}
        
    for i in range(len(plays)):
        playlist[genres[i]][i] = plays[i]
        genre_plays[genres[i]] = genre_plays.get(genres[i], 0) + plays[i]
        
    answer = []
    for genre, _ in sorted(genre_plays.items(), key=lambda x: -x[1]):
        sorted_song = sorted(playlist[genre].items(), key=lambda x: -x[1])
        answer.extend([song for song, _ in sorted_song[:2]])
        
    return answer