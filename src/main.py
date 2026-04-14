"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

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

    width = 52

    for label, prefs in [
        ("Indie Pop Fan", user_prefs),
        ("Folk Listener", user_prefs_2),
        ("Pop Fan", user_prefs_3),
    ]:
        recommendations = recommend_songs(prefs, songs, k=5)

        print(f"\n{'Top Recommendations for: ' + label:^{width}}")
        print("=" * width)

        for rank, (song, score, reasons) in enumerate(recommendations, start=1):
            print(f"\n  #{rank}  {song['title']}")
            print(f"       Artist : {song['artist']}")
            print(f"       Score  : {score:.2f}")
            print(f"       Why    :")
            for reason in reasons:
                print(f"                - {reason}")

        print("\n" + "=" * width)


if __name__ == "__main__":
    main()
