import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Cinema AI - Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ============================================================
# SESSION STATE MANAGEMENT
# ============================================================

if "recommendations_generated" not in st.session_state:
    st.session_state.recommendations_generated = False

def generate_recommendations():
    st.session_state.recommendations_generated = True

def reset_recommendations():
    st.session_state.recommendations_generated = False

# ============================================================
# CUSTOM UI CSS (CINEMA DARK / HIGH-CONTRAST MODERN THEME)
# ============================================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #090d16 0%, #111827 50%, #080c14 100%);
    color: #f8fafc;
    font-family: 'Inter', system-ui, sans-serif;
}

/* Container Padding */
.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* Navigation / Top Header Bar */
.nav-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 24px;
    background: rgba(15, 23, 42, 0.7);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    margin-bottom: 2rem;
}

.logo-text {
    font-size: 22px;
    font-weight: 800;
    letter-spacing: -0.5px;
    background: linear-gradient(90deg, #38bdf8, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.nav-badges {
    display: flex;
    gap: 12px;
}

.nav-badge {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    color: #cbd5e1;
}

/* Main Hero Titles */
.hero-title {
    font-size: 46px !important;
    font-weight: 900 !important;
    text-align: center;
    letter-spacing: -1px;
    color: #ffffff !important;
    margin-bottom: 8px;
}

.hero-subtitle {
    text-align: center;
    font-size: 18px;
    color: #94a3b8 !important;
    margin-bottom: 2rem;
}

/* Sidebar / Preferences Card Styling */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(17, 24, 39, 0.8) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
}

/* Selectbox Headers */
div[data-testid="stWidgetLabel"] p {
    color: #38bdf8 !important;
    font-size: 13px !important;
    font-weight: 800 !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
}

/* Selectboxes Inputs */
div[data-baseweb="select"] > div {
    background-color: #0f172a !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
}

div[data-baseweb="select"] span {
    color: #f8fafc !important;
    font-weight: 600 !important;
}

/* Green Action Button (State 1) */
.green-button div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #16a34a 0%, #15803d 100%) !important;
    color: #ffffff !important;
    width: 100% !important;
    height: 52px !important;
    border-radius: 12px !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    border: none !important;
    box-shadow: 0 4px 20px rgba(22, 163, 74, 0.4) !important;
    transition: all 0.2s ease !important;
}

.green-button div[data-testid="stButton"] > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(22, 163, 74, 0.6) !important;
}

/* Red Action Button (State 2 - Reset/Generated) */
.red-button div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%) !important;
    color: #ffffff !important;
    width: 100% !important;
    height: 52px !important;
    border-radius: 12px !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    border: none !important;
    box-shadow: 0 4px 20px rgba(220, 38, 38, 0.4) !important;
    transition: all 0.2s ease !important;
}

.red-button div[data-testid="stButton"] > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(220, 38, 38, 0.6) !important;
}

/* Best Match Spotlight Card */
.best-match-card {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.9) 100%);
    border: 2px solid #f59e0b;
    border-radius: 20px;
    padding: 24px;
    position: relative;
    box-shadow: 0 10px 30px rgba(245, 158, 11, 0.2);
    margin-bottom: 20px;
}

.best-badge {
    position: absolute;
    top: 16px;
    right: 16px;
    background: #f59e0b;
    color: #0f172a;
    font-weight: 900;
    font-size: 12px;
    padding: 6px 14px;
    border-radius: 20px;
    text-transform: uppercase;
}

.match-score {
    font-size: 28px;
    font-weight: 900;
    color: #10b981;
}

/* Regular Card Styling */
.movie-card {
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 12px;
}

.movie-title {
    font-size: 20px;
    font-weight: 800;
    color: #f8fafc;
}

/* Footer Styling */
.footer {
    text-align: center;
    color: #64748b;
    font-size: 14px;
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# DATASET
# ============================================================

movies = [
    # ENGLISH
    {"title": "Interstellar", "genre": "Sci-Fi", "language": "English", "type": "Drama", "rating": "8.7", "year": "2014", "description": "When Earth becomes uninhabitable, a team of ex-NASA pilots undertakes a interstellar mission to find a new home."},
    {"title": "Inception", "genre": "Sci-Fi", "language": "English", "type": "Thriller", "rating": "8.8", "year": "2010", "description": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea."},
    {"title": "The Martian", "genre": "Sci-Fi", "language": "English", "type": "Adventure", "rating": "8.0", "year": "2015", "description": "An astronaut becomes stranded on Mars after his team assumes him dead, and must rely on his ingenuity to survive."},
    {"title": "The Notebook", "genre": "Romance", "language": "English", "type": "Drama", "rating": "7.8", "year": "2004", "description": "An elderly man reads a love story written in his notebook to a fellow nursing home resident."},
    {"title": "Avengers: Endgame", "genre": "Action", "language": "English", "type": "Adventure", "rating": "8.4", "year": "2019", "description": "After devastating events, the remaining Avengers assemble once more in order to reverse Thanos' actions."},
    {"title": "Joker", "genre": "Crime", "language": "English", "type": "Thriller", "rating": "8.4", "year": "2019", "description": "A mentally troubled comedian embarks on a downward spiral that leads to the creation of an iconic villain."},
    {"title": "Titanic", "genre": "Romance", "language": "English", "type": "Drama", "rating": "7.9", "year": "1997", "description": "A seventeen-year-old aristocrat falls in love with a kind-hearted but poor artist aboard the luxurious Titanic."},

    # HINDI
    {"title": "3 Idiots", "genre": "Comedy", "language": "Hindi", "type": "Drama", "rating": "8.4", "year": "2009", "description": "Two friends search for their long-lost companion while recollecting their college days and life lessons."},
    {"title": "Dangal", "genre": "Sports", "language": "Hindi", "type": "Drama", "rating": "8.3", "year": "2016", "description": "Former wrestler Mahavir Singh Phogat trains his daughters Geeta and Babita to become world-class wrestlers."},
    {"title": "PK", "genre": "Comedy", "language": "Hindi", "type": "Drama", "rating": "8.1", "year": "2014", "description": "An alien stranded on Earth loses his communication device and questions human religious beliefs and dogmas."},

    # URDU
    {"title": "The Legend of Maula Jatt", "genre": "Action", "language": "Urdu", "type": "Adventure", "rating": "8.0", "year": "2022", "description": "A fierce prizefighter with a tortured past seeks vengeance against his arch-nemesis in an epic rivalry."},
    {"title": "Cake", "genre": "Drama", "language": "Urdu", "type": "Drama", "rating": "7.6", "year": "2018", "description": "A woman residing in London returns home to Pakistan when her family's matriarch falls ill."},

    # KOREAN
    {"title": "Parasite", "genre": "Crime", "language": "Korean", "type": "Thriller", "rating": "8.5", "year": "2019", "description": "Greed and class discrimination threaten the newly formed symbiotic relationship between two families."},
    {"title": "Train to Busan", "genre": "Action", "language": "Korean", "type": "Thriller", "rating": "7.6", "year": "2016", "description": "While a zombie virus breaks out in South Korea, passengers struggle to survive on a train from Seoul to Busan."},

    # TURKISH
    {"title": "Miracle in Cell No. 7", "genre": "Drama", "language": "Turkish", "type": "Drama", "rating": "8.2", "year": "2019", "description": "A mentally impaired father separated from his daughter must prove his innocence after being accused of murder."},
    {"title": "Ayla: The Daughter of War", "genre": "Drama", "language": "Turkish", "type": "Drama", "rating": "8.3", "year": "2017", "description": "During the Korean War, a Turkish soldier risks his life to save a orphaned Korean child."}
]

# ============================================================
# SIMILARITY LOGIC
# ============================================================

def calculate_similarity(movie, preferences):
    matches = 0
    for key in preferences:
        if movie[key] == preferences[key]:
            matches += 1
    return matches / len(preferences)

def get_recommendations(preferences):
    results = []
    for movie in movies:
        score = calculate_similarity(movie, preferences)
        res = movie.copy()
        res["similarity"] = score
        results.append(res)
    results.sort(key=lambda x: x["similarity"], reverse=True)
    return results[:5]

# ============================================================
# TOP NAVIGATION HEADER
# ============================================================

st.markdown("""
<div class="nav-header">
    <div class="logo-text">🎬 Cinema AI Recommender</div>
    <div class="nav-badges">
        <span class="nav-badge">⚡ Matcher v2.0</span>
        <span class="nav-badge">🤖 Similarity Engine</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# HERO TITLE
# ============================================================

st.markdown('<div class="hero-title">Movie Recommender AI</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Get AI-powered movie recommendations based on your personal preferences and interests.</div>', unsafe_allow_html=True)

# ============================================================
# MAIN LAYOUT (SIDEBAR PREFERENCES + RECOMMENDATION RESULTS)
# ============================================================

left_col, right_col = st.columns([1, 2.2], gap="large")

with left_col:
    with st.container(border=True):
        st.subheader("🎯 Filter Preferences")
        st.write("Customize attributes to compute similarity score:")
        st.write("")

        genre = st.selectbox(
            "🎭 PREFERRED GENRE",
            ["Action", "Comedy", "Crime", "Drama", "Romance", "Sci-Fi", "Sports"]
        )

        language = st.selectbox(
            "🌍 LANGUAGE",
            ["English", "Hindi", "Urdu", "Korean", "Turkish"]
        )

        movie_type = st.selectbox(
            "🎞️ MOVIE TYPE / TONE",
            ["Adventure", "Drama", "Thriller"]
        )

        user_preferences = {
            "genre": genre,
            "language": language,
            "type": movie_type
        }

        st.write("")
        st.divider()

        # Dynamic Button Trigger (Green to Red state transition)
        if st.session_state.recommendations_generated:
            st.markdown('<div class="red-button">', unsafe_allow_html=True)
            if st.button("🔴 Reset Recommendations", on_click=reset_recommendations):
                pass
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="green-button">', unsafe_allow_html=True)
            if st.button("🟢 🔍 Get Recommendations", on_click=generate_recommendations):
                pass
            st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    if not st.session_state.recommendations_generated:
        st.info("👈 Select your preferences on the left and click **'Get Recommendations'** to view matched results.")
        
        # Display Placeholder Card Preview
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: rgba(255,255,255,0.02); border-radius: 16px; border: 1px dashed rgba(255,255,255,0.1);">
            <div style="font-size: 40px; margin-bottom: 10px;">🍿</div>
            <div style="color: #94a3b8; font-weight: 600;">Your calculated recommendations will appear here.</div>
        </div>
        """, unsafe_allow_html=True)

    else:
        recommendations = get_recommendations(user_preferences)
        best_match = recommendations[0]
        best_score = int(best_match["similarity"] * 100)

        # 1. BEST MATCH HIGHLIGHT CARD
        st.markdown(f"""
        <div class="best-match-card">
            <div class="best-badge">🏆 TOP CHOICE</div>
            <div style="color: #94a3b8; font-size: 13px; font-weight: 700;">#{1} MATCH</div>
            <div style="font-size: 32px; font-weight: 900; color: #ffffff; margin: 4px 0;">{best_match['title']}</div>
            <div style="display: flex; gap: 15px; margin-bottom: 12px; font-size: 14px; color: #cbd5e1;">
                <span>⭐ {best_match['rating']}/10</span>
                <span>📅 {best_match['year']}</span>
                <span>🎭 {best_match['genre']}</span>
                <span>🌍 {best_match['language']}</span>
            </div>
            <div style="color: #cbd5e1; font-size: 14px; margin-bottom: 16px; line-height: 1.5;">{best_match['description']}</div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span class="match-score">{best_score}% Match</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.progress(best_match["similarity"])
        st.write("")

        # 2. OTHER MATCHED RECOMMENDATIONS
        st.subheader("✨ Other Top Matched Movies")

        for idx, item in enumerate(recommendations[1:], start=2):
            score_percent = int(item["similarity"] * 100)
            
            with st.container(border=True):
                col_a, col_b = st.columns([3, 1])
                with col_a:
                    st.markdown(f"### #{idx} {item['title']}")
                    st.markdown(f"**Genre:** {item['genre']} • **Lang:** {item['language']} • **Type:** {item['type']}")
                    st.caption(item['description'])
                with col_b:
                    st.markdown(f"### `{score_percent}%` Match")
                    st.progress(item["similarity"])

# ============================================================
# HOW IT WORKS SECTION
# ============================================================

st.write("")
st.divider()

with st.expander("🤖 How does this Recommendation Engine work?"):
    st.subheader("1. Preference Extraction")
    st.write("The system takes user selections for Genre, Language, and Movie Type.")
    
    st.subheader("2. Attribute Comparison")
    st.write("It evaluates every movie entry in the database using simple attribute-matching logic.")
    
    st.subheader("3. Similarity Calculation")
    st.code("Similarity Score = (Matching Preference Attributes) / (Total Selected Preferences)")
    
    st.subheader("4. Ranking & Presentation")
    st.write("Results are dynamically sorted by descending similarity scores and displayed using modern UI elements.")

# ============================================================
# ABOUT SECTION
# ============================================================

st.divider()
st.subheader("💡 About Project 3")
st.write(
    "This application was built as part of the AI Recommendation System project. "
    "It demonstrates fundamental rule-based similarity logic combined with high-contrast, "
    "user-friendly web interface principles in Streamlit."
)

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    🎓 DecodeLabs AI Project 3 • Built by <b>Abeeha Javed</b><br>
    Movie Recommendation System (Similarity Logic Engine)
</div>
""", unsafe_allow_html=True)