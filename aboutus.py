import streamlit as st
 


about_us = """

        <section class="about">
        <h1>About Us</h1>
        <p style="font-weight: bold">GeeksforGeeks is a leading platform...</p>
        <div class="about-info">
            <div class="about-img">
                <img src=
"https://assets.skyfilabs.com/images/blog/disease-prediction-using-machine-learning.webp">
            </div>
            <div>
     <p>GeeksforGeeks is a leading platform that provides computer science resources
                  and coding challenges for programmers and technology enthusiasts,
                  along with interview and exam preparations for upcoming aspirants.
                  With a strong emphasis on enhancing coding skills and knowledge,
                  it has become a trusted destination for over 12 million plus registered
                  users worldwide.</p>
                  </div>
                  </div>
    </section>
   
        """

st.markdown(about_us, unsafe_allow_html=True)

        # Use Local CSS File
def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("about.css")

