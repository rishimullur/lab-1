import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(page_title="My Personal Website", page_icon=":guardsman:", layout="wide")
    
    # Add profile picture
    st.image("profile_picture.jpg", width=200)
    
    # Add about section
    st.header("About")
    st.write("Hi, I'm [Your Name]. I'm a [Your Profession] with a passion for [Your Interests].")
    
    # Add education section
    st.header("Education")
    st.write("- [Degree], [Major], [University], [Graduation Year]")
    
    # Add work experience section
    st.header("Work Experience")
    st.write("- [Job Title], [Company], [Start Date] - [End Date (if applicable)]")
    st.write("  - [Brief description of your role and responsibilities]")
    
    # Add hobbies and interests section
    st.header("Hobbies and Interests")
    st.write("- [Hobby/Interest 1]")
    st.write("- [Hobby/Interest 2]")
    st.write("- [Hobby/Interest 3]")
    
    # Add interesting projects section
    st.header("Interesting Projects")
    st.write("- [Project 1 Name]")
    st.write("  - [Brief description of the project]")
    st.write("- [Project 2 Name]")
    st.write("  - [Brief description of the project]")

if __name__ == "__main__":
    main()

