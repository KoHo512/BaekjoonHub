def solution(genres, plays):
    playlist = {}
    genre_plays = {}
        
    for i, genre in enumerate(genres):
        playlist.setdefault(genre, {})[i] = plays[i]
        genre_plays[genre] = genre_plays.get(genre, 0) + plays[i]
        
    answer = []
    for genre, _ in sorted(genre_plays.items(), key=lambda x: -x[1]):
        sorted_song = sorted(playlist[genre].items(), key=lambda x: (-x[1], x[0]))
        answer.extend([song for song, _ in sorted_song[:2]])
        
    return answer