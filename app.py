import streamlit as st

def main():
   # Set page configuration
   st.set_page_config(
      page_title="Jane Doe - Software Engineer",
      page_icon="👩🏻‍💻",
      layout="wide",
      initial_sidebar_state="auto",
   )
   
   # Create two columns
   col1, col2 = st.columns([0.4, 0.6])
   
   # Profile picture and name
   with col1:
      st.markdown(
          """
          <style>
          .profile-img img {
              width: 100%;
              border-radius: 50%;
          }
          </style>
          <div class="profile-img">
              ![](https://rishim.xyz/IMG_0004.JPG)
          </div>
          """,
          unsafe_allow_html=True,
      )
   
   # About section
   with col2:
      st.markdown(
          """
          ## Jane Doe (She/Her)
          - Software Engineer at [Company Name](https://www.example.com/)
          - Passionate about building innovative solutions
          """
      )
   
   # Education and Work Experience
   st.markdown("## Education")
   st.write("- B.S. in Computer Science, [University Name], [Graduation Year]")
   
   st.markdown("## Work Experience")
   st.write("- Software Engineer, [Company Name], [Start Date] - Present")
   st.write("  - Developed and maintained web applications using React, Node.js, and Python")
   st.write("  - Collaborated with cross-functional teams to deliver high-quality products")
   
   # Hobbies and Interests
   st.markdown("## Hobbies and Interests")
   st.write("- Hiking and outdoor activities")
   st.write("- Photography")
   st.write("- Reading and learning new technologies")
   
   # Interesting Projects
   st.markdown("## Interesting Projects")
   st.write("- [Project 1 Name](https://www.example.com/project1)")
   st.write("  - A brief description of the project and its key features.")
   st.write("- [Project 2 Name](https://www.example.com/project2)")
   st.write("  - A brief description of the project and its key features.")
   
   # Footer
   st.markdown(
      """
      <style>
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
      #page-container {
          position: relative;
          min-height: 10vh;
      }
      footer {
          position: relative;
          left: 0;
          top: 230px;
          bottom: 0;
          width: 100%;
          background-color: transparent;
          color: #808080;
          text-align: left;
      }
      </style>
      <div id="page-container">
          <div class="footer">
              <p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
              with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/yourname" target="_blank"> by YourName</a></p>
          </div>
      </div>
      """,
      unsafe_allow_html=True,
   )

if __name__ == "__main__":
    main()

