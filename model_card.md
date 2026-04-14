# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

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
    - I checked whether the top-ranked songs actually matched the spirit of each profile — for example, whether the Indie Pop Fan got upbeat indie songs and whether the Pop Fan got high-energy tracks — and whether the score breakdown in the "Why" column explained the ranking in a way that made intuitive sense.
- What surprised you  
    - The Folk Listener's top recommendation ("Golden Hour Letters") surprised me: despite the user wanting very high energy (0.90), the only folk song in the catalog has energy 0.46, so the genre match forced a low-energy song to the top — showing that the genre weight can override continuous feature alignment entirely.
- Any simple tests or comparisons you ran  
    - I compared the Folk Listener and Pop Fan side-by-side since both have moods not in the catalog; this confirmed that the missing mood label costs exactly 0.30 points per song regardless of how well everything else matches, and the Pop Fan still scored higher purely because more pop songs existed with matching energy levels.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
