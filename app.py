import streamlit as st

# Streamlit App Configuration
st.set_page_config(
    page_title="Valentine's Day Special",
    page_icon="💖",
    layout="centered",
)

# Title and Header
st.title("💝 Happy Valentine's Day 💝")
st.header("Thank you for making college life better!")

# Spotify Playlist Section
st.subheader("🎶 Here's a special playlist I made for you 🎶")
spotify_embed_code = """
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7qhoem5Ra30xTuAIdpPVnR?utm_source=generator&theme=0" 
width="100%" height="152" frameBorder="0" allowfullscreen="" 
allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
"""
st.markdown(spotify_embed_code, unsafe_allow_html=True)

# Image Section
st.subheader("✨ A couple of our favorite memories ✨")
col1, col2 = st.columns(2)

with col1:
    st.image("image1.jpg", caption="A special moment")  # Replace with your image path
with col2:
    st.image("image2.jpg", caption="Another special memory")  # Replace with your image path

# Cute Message Section
st.subheader("💬 A Cute Message for You 💬")
st.write(
    """
    You’ve made my college life brighter and better in ways I could never imagine.  
    Every laugh, every memory, and every moment with you has been the best part of my journey.  
    Here’s to us, and to many more memories to come. 💖  
    """
)

# Footer
st.markdown(
    "<p style='text-align: center;'>Made for my pookie <3</p>",
    unsafe_allow_html=True,
)
