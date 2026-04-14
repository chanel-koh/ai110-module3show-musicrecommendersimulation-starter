# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**BopFinder 1.0**  

---

## 2. Intended Use  

- What kind of recommendations it generates:
    - A list of 5 top recommendations a specific user profile is likely to enjoy.
- What assumptions does it make about the user:  
    - It assumes that the user only has one favorite genre and that their mood preference stays the same.
- Is this for real users or classroom exploration:  
    - Classroom exploration

---

## 3. How the Model Works  

- What features of each song are used (genre, energy, mood, etc.)  
    - Genre, mood, energy closeness, acousticness, tempo closeness
- What user preferences are considered  
    - Preferred genre, preferred mood, target energy level, acoustic preference
- How does the model turn those into a score  
    - Uses a weighted sum where every feature contributes a value within [0, 1]
    - Each song is compared to one user profile
    - Points are given for yes/no matches of categorial attributes (genre match, mood match), while closeness points are given for numeric features(energy, tempo)
    - For example, if genre is weighted at 0.35 and the genre of the song matches, 1*0.35 would be added to the sum
- What changes did you make from the starter logic
    - A weighted sum calculation to factor in importance of a feature, closeness scores for continuous features 

---

## 4. Data  
- How many songs are in the catalog: 
    - 18 songs
- What genres or moods are represented: 
    - 15 genres (pop, lofi, rock, folk, jazz, indie pop, hip hop, r&b, house, metal, country, reggae, ambient, synthwave, classical) 
    - 14 moods (happy, chill, intense, focused, relaxed, moody, nostalgic, confident, romantic, euphoric, rebellious, wistful, uplifted, serene)
- Did you add or remove data: 
    - No songs were added or removed from the original dataset
- Are there parts of musical taste missing in the dataset: 
    - Common mood descriptors like "energetic" and "calm" are absent, and the catalog has no songs for several genre combos a user might prefer (for example, EDM, K-pop)

---

## 5. Strengths  

Where does your system seem to work well.  

- User types for which it gives reasonable results: 
    - Users whose preferred genre and mood exist in the catalog (for example, the Indie Pop Fan) get the most coherent recommendations since the two heaviest features both contribute fully
- Any patterns you think your scoring captures correctly: 
    - The weighted sum correctly prioritizes categorical alignment first, then rewards songs that are close in energy and tempo. Therefore, a genre-and-mood match that is also near the target energy reliably floats to the top
- Cases where the recommendations matched your intuition: 
    - The Indie Pop Fan's top results were all upbeat indie or pop tracks with moderate energy, exactly what the profile describes

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

- Features it does not consider  
    - valence, danceability, and the likes_acoustic boolean are collected but never used in scoring. Artist diversity or listening history are also not considered.
- Genres or moods that are underrepresented  
    - Pop and lofi dominate the dataset, while moods like "calm" and "energetic" dont't exist in the dataset, zeroing out 0.30 of the score for users who have these moods as their preference.
- Cases where the system overfits to one preference  
    - Gengre and mood together account for 0.65 of the total score, so a genre+mood match will almost always outrank a song that fits perfectly on every continuous feature but misses those two labels.
- Ways the scoring might unintentionally favor some users  
    - Users whose preferences match the catalog's exact label vocabulary get full credit on the two heaviest features, while users with genres or moods not in the dataset are permanently penalized with no fallback or warning.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

- Which user profiles you tested:
    - **Indie Pop Fan**: upbeat indie pop listener who prefers moderate energy (0.75), 120 BPM tempo, a "happy" mood, and slight acoustic warmth (acousticness 0.30).
    - **Folk Listener** (edge case): laid-back acoustic folk listener who paradoxically wants very high energy (0.90) despite a "calm" mood preference and slow tempo (85 BPM), with strong acoustic preference (acousticness 0.80).
    - **Pop Fan**: high-energy pop fan seeking fast, danceable tracks (0.90 energy, 140 BPM, "energetic" mood) with minimal acousticness (0.10).

- What you looked for in the recommendations  
    - I checked whether the top ranked songs actually matched the spirit of each profile. For example, whether the Indie Pop Fan got upbeat indie songs and whether the Pop Fan got high-energy tracks. Additionally, I checked whether the score points breakdown in the output explained the ranking in a way that made intuitive sense.

- What surprised you  
    - The Folk Listener's top recommendation ("Golden Hour Letters") surprised me: despite the user wanting very high energy (0.90), the only folk song in the catalog has energy 0.46, so the genre match forced a low energy song to the top, showing that the genre weight can override continuous feature alignment entirely.

- Any simple tests or comparisons you ran  
    - I compared the Folk Listener and Pop Fan side-by-side since both have moods not in the catalog; this confirmed that the missing mood label costs exactly 0.30 points per song regardless of how well everything else matches, and the Pop Fan still scored higher purely because more pop songs existed with matching energy levels.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

- Additional features or preferences, like including valence and danceability to make song scoring even more tailored to a user, especially if more songs are added to the database.
- Fuzzy matching so a user doesn't have to guess if their mood or genre is in the database.
- Improving diversity among the top results, like incorporating songs with different artists.

---

## 9. Personal Reflection  

A few sentences about your experience.  

- What you learned about recommender systems: 
    - Even a simple weighted sum can produce surprisingly sensible results, but the weight distribution can get easily tricked by a contradiction in a user profile (like calm mood but high energy preference).
- Something unexpected or interesting you discovered: 
    - A single genre match can completely override continuous feature alignment, meaning a user can consistently get low-energy songs when they explicitly asked for high energy.
- How this changed the way you think about music recommendation apps: 
    - I now notice that real apps likely use a scoring function on the backend as well, and are collecting information when I user their app in terms of usual song mood and what/when I skip.   
- Biggest learning moment: 
- How AI tools helped me and when I needed to double-check:
    - AI tools helped me implement the functions in recommender.py, adding data to the .csv, and build sample profiles. I needed to double check if what the functions were doing with scoring matched with what I designed in the README. I also needed to check if the user profiles had attributes that matched the README
- What I would try next:
    - I would like to try adding fuzzy matching because it seems very important for users to actually use the recommender. 
