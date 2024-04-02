import streamlit as st
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_title="Jessica Smith - Data Scientist",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="auto",
)

# Define custom CSS styles
custom_css = """
<style>
    .profile-img img {
        width: 100%;
        border-radius: 10%;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: #808080;
        text-align: left;
        padding: 10px;
    }
    a:link, a:visited {
        color: #BFBFBF;
        background-color: transparent;
        text-decoration: none;
    }
    a:hover, a:active {
        color: #0283C3;
        background-color: transparent;
        text-decoration: underline;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Load profile picture
profile_pic = Path("profile_picture.jpg")

# Create three columns
col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

# Profile picture
with col1:
    if profile_pic.exists():
        st.image(profile_pic, use_column_width=True)
    else:
        st.image("https://via.placeholder.com/150", use_column_width=True)

# About section
with col2:
    st.markdown(
        """
        ## Jessica Smith (She/Her)
        - Data Scientist at [Company Name](https://www.example.com/)
        - Passionate about leveraging data to drive business decisions
        """
    )

# Blank space
with col3:
    st.write("")

# Education and Work Experience
st.header("Education")
st.write("- M.S. in Data Science, [University Name], [Graduation Year]")
st.write("- B.S. in Statistics, [University Name], [Graduation Year]")

st.header("Work Experience")
st.write("- Data Scientist, [Company Name], [Start Date] - Present")
st.write("  - Developed and deployed machine learning models for predictive analytics")
st.write("  - Conducted data analysis and created data visualizations to communicate insights")
st.write("- Data Analyst, [Company Name], [Start Date] - [End Date]")
st.write("  - Performed statistical analysis and data mining on large datasets")
st.write("  - Collaborated with cross-functional teams to identify data-driven solutions")

# Hobbies and Interests
st.header("Hobbies and Interests")
st.write("- Traveling and exploring new cultures")
st.write("- Playing chess and board games")
st.write("- Reading non-fiction books")

# Interesting Projects
st.header("Interesting Projects")
st.write("- [Project 1 Name](https://www.example.com/project1)")
st.write("  - A brief description of the project and its key features.")
st.write("- [Project 2 Name](https://www.example.com/project2)")
st.write("  - A brief description of the project and its key features.")

# Footer
st.markdown(
    """
    <div class="footer">
        <p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
        with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/yourname" target="_blank"> by YourName</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)

