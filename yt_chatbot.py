from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

#load environment variables
load_dotenv()


class YouTubeChatbot:
    #Step1: Fetch YouTube Transcript
    def fetch_youtube_transcript(self, video_id):
        #declare variable to return transcript text 
        transcript_text = ""
        try:
            transcript_list = YouTubeTranscriptApi().fetch(video_id=video_id).to_raw_data()
            print("Transcript fetched successfully.")

            # Convert the transcript to a string format
            transcript_text = " ".join([entry['text'] for entry in transcript_list])

            #write the transcript to a text file
            with open(f"{video_id}_transcript.txt", "w", encoding="utf-8") as file:
                file.write(transcript_text)
            return True   
        except TranscriptsDisabled:
            print("Transcripts are disabled for this video.")
            return False
    

if __name__ == "__main__":
    # Create an instance of the YouTubeChatbot class
    transcript = ""
    chatbot = YouTubeChatbot()  
    fetched = chatbot.fetch_youtube_transcript("Gfr50f6ZBvo") 
    if fetched:
        # Read the transcript from the file
        with open("Gfr50f6ZBvo_transcript.txt", "r", encoding="utf-8") as file:
            transcript = file.read()
    print(transcript)


    

