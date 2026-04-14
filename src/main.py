"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from tabulate import tabulate
from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Taste profile: upbeat indie pop fan who likes moderate energy and some acoustic warmth
    user_prefs = {
        "genre": "indie pop",
        "mood": "happy",
        "energy": 0.75,
        "tempo_bpm": 120,
        "likes_acoustic": False,
        "acousticness": 0.30,
    }

    # Taste profile: laid-back acoustic folk listener who prefers calm, high-energy songs
    # Edge-case profile: calm mood but high energy preference
    user_prefs_2 = {
        "genre": "folk",
        "mood": "calm",
        "energy": 0.90,
        "tempo_bpm": 85,
        "likes_acoustic": True,
        "acousticness": 0.80,
    }

    # Taste profile: high-energy pop fan who wants danceable, upbeat tracks
    user_prefs_3 = {
        "genre": "pop",
        "mood": "energetic",
        "energy": 0.90,
        "tempo_bpm": 140,
        "likes_acoustic": False,
        "acousticness": 0.10,
    }

    for label, prefs in [
        ("Indie Pop Fan", user_prefs),
        ("Folk Listener", user_prefs_2),
        ("Pop Fan", user_prefs_3),
    ]:
        recommendations = recommend_songs(prefs, songs, k=5)

        rows = []
        for rank, (song, score, reasons) in enumerate(recommendations, start=1):
            reasons_str = "\n".join(f"  - {r}" for r in reasons)
            rows.append([rank, song["title"], song["artist"], f"{score:.2f}", reasons_str])

        headers = ["#", "Title", "Artist", "Score", "Why"]
        table = tabulate(rows, headers=headers, tablefmt="grid")

        title_line = f"  Top Recommendations for: {label}"
        width = max(len(title_line), len(table.splitlines()[0]))
        print(f"\n{'=' * width}")
        print(title_line)
        print(f"{'=' * width}")
        print(table)

if __name__ == "__main__":
    main()
