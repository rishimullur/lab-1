import streamlit as st

def main():
    st.title("Welcome to My Personal Website")
    st.write("This is a simple Streamlit app that serves as a personal website.")
    
    st.header("About Me")
    st.write("I'm a passionate individual interested in technology, programming, and data science.")
    
    st.header("Projects")
    st.write("Here are some of the projects I've worked on:")
    st.write("- Project 1: Description of project 1")
    st.write("- Project 2: Description of project 2")
    st.write("- Project 3: Description of project 3")
    
    st.header("Contact Me")
    st.write("Feel free to reach out to me via email at example@email.com")
    
    st.header("Connect with Me")
    st.write("You can also connect with me on LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile/)")
    st.write("Follow me on Twitter: [Your Twitter Profile](https://twitter.com/yourtwitterhandle)")

if __name__ == "__main__":
    main()

