from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top-k recommended songs for the given user profile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a human-readable explanation of why a song was recommended to the user."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv

    int_fields = {"id"}
    float_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}

    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for field in int_fields:
                row[field] = int(row[field])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)

    print(f"Loaded {len(songs)} songs from {csv_path}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    # Genre match (weight: 0.35)
    if user_prefs.get("genre", "").lower() == song.get("genre", "").lower():
        score += 0.35
        reasons.append("genre match (+0.35)")

    # Mood match (weight: 0.30)
    if user_prefs.get("mood", "").lower() == song.get("mood", "").lower():
        score += 0.30
        reasons.append("mood match (+0.30)")

    # Energy closeness (weight: 0.20): 1 - abs(user_energy - song_energy)
    energy_closeness = 1 - abs(user_prefs.get("energy", 0.0) - song.get("energy", 0.0))
    energy_points = round(0.20 * energy_closeness, 4)
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points:.2f})")

    # Tempo closeness (weight: 0.10): 1 - abs(user_bpm - song_bpm) / 170
    tempo_closeness = max(0.0, 1 - abs(user_prefs.get("tempo_bpm", 0) - song.get("tempo_bpm", 0)) / 170)
    tempo_points = round(0.10 * tempo_closeness, 4)
    score += tempo_points
    reasons.append(f"tempo closeness (+{tempo_points:.2f})")

    # Acousticness (weight: 0.05): 1 - abs(user_acousticness - song_acousticness)
    acoustic_closeness = 1 - abs(user_prefs.get("acousticness", 0.0) - song.get("acousticness", 0.0))
    acoustic_points = round(0.05 * acoustic_closeness, 4)
    score += acoustic_points
    reasons.append(f"acousticness closeness (+{acoustic_points:.2f})")

    return round(score, 4), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, List[str]]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, reasons))

    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]
