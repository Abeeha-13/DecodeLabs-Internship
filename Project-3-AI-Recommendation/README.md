\# 🎬 AI Movie Recommendation System



An AI-powered, user-friendly Movie Recommendation Web Application built with \*\*Python\*\* and \*\*Streamlit\*\*. It recommends personalized movies based on user preferences using rule-based similarity logic and displays results in a dark cinema UI.



\---



\## 🎯 Features



\* \*\*Interactive Preferences Selection:\*\* Select preferred Genre, Language, and Movie Type.

\* \*\*Similarity Logic Engine:\*\* Calculates similarity percentages based on attribute matching.

\* \*\*Dynamic Button State:\*\* Interactive button colors (Green for generation, Red for reset).

\* \*\*Modern Cinema UI:\*\* Features spotlight hero cards, similarity percentage progress bars, and high contrast visible elements.

\* \*\*Responsive Layout:\*\* Sidebar controls paired with rich recommendation display cards.



\---



\## ⚙️ How the Algorithm Works



1\. \*\*User Input:\*\* User selects `Genre`, `Language`, and `Type`.

2\. \*\*Matching Engine:\*\* The app loops through the database comparing movie metadata against inputs.

3\. \*\*Similarity Formula:\*\*

&#x20;  $$\\text{Similarity Score} = \\frac{\\text{Matching Attributes}}{\\text{Total Selected Attributes}}$$

4\. \*\*Ranking:\*\* Displays top 5 matches sorted by descending score.



\---



\## 🚀 How to Run Locally



1\. \*\*Clone the repository:\*\*

&#x20;  ```bash

&#x20;  git clone \[https://github.com/your-username/movie-recommendation-ai.git](https://github.com/your-username/movie-recommendation-ai.git)

&#x20;  cd movie-recommendation-ai

