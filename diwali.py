import streamlit as st
from gtts import gTTS
from io import BytesIO
 
# Define the absolute path to the video
video_path = r"C:\Users\VCSDEV0274\Downloads\8240564-hd_1920_1080_25fps.mp4"   # Replace with your MP4 file name
 
# Define the Streamlit app
def main():
    st.title("Happy Diwali Ecubix Family")
   
    # Display a welcome video
    try:
        st.video(video_path)  # Use the absolute path for the MP4 file
    except Exception as e:
        st.error(f"Error loading video: {str(e)}")
 
    # Input for the user's name
    name = st.text_input("Enter your name")
   
    # Default message in Gujarati
    default_gujarati_text = (
        "સુખ અને સમૃદ્ધિ તમારા આંગણામાં ચમકે… "
        "દીવા શાંતિના ચારેય દિશાઓમાં ઝળકે… "
        "ખુશીઓ તમારા ઘર આંગણે આવીને ઉજવણી કરે… "
        "દિવાળીના તહેવારની તમને હાર્દિક શુભકામનાઓ!!"
    )  # Gujarati message for Diwali wishes
   
    # Combine the name and message
    if name:
        gujarati_text = f"{name}, {default_gujarati_text}"
    else:
        gujarati_text = default_gujarati_text  # Use default if no name is provided
 
    # Variable to store generated audio
    audio_bytes = None
   
    if st.button("Generate Speech"):
        # Convert text to speech and load it into a BytesIO object
        mp3_fp = BytesIO()
        tts = gTTS(text=gujarati_text, lang='gu')
        tts.write_to_fp(mp3_fp)
       
        # Reset file pointer to the beginning
        mp3_fp.seek(0)
       
        # Store the audio bytes for playback
        audio_bytes = mp3_fp.read()  # Read the content of BytesIO as raw bytes
       
        st.success("Speech generated successfully!")
 
        # Automatically play the audio after it is generated
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
 
# Run the Streamlit app
if __name__ == "__main__":
    main()