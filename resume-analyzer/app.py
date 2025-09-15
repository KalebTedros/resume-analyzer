import streamlit as st
from sentence_transformers import SentenceTransformer, util
import re

# Set the page title
st.set_page_config(page_title="Resume Matcher AI", layout="wide")
st.title("🔍 AI-Powered Resume & Job Description Matcher")

# Load a lightweight AI model for text similarity
@st.cache_resource(show_spinner="Loading AI model...") # Cache so it loads only once
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2') # Small but powerful model
model = load_model()

# Load the resume text
with open('resume.txt', 'r') as file:
    resume_text = file.read()

st.subheader("Your Resume Text")
st.text_area("", resume_text, height=150)

# Get the job description from the user
job_desc = st.text_area("Paste the Job Description Here:", height=200)

if st.button("Analyze Match") and job_desc:
    with st.spinner('Analyzing...'):

        # Step 1: Create embeddings (numerical representations) of the texts
        resume_embedding = model.encode(resume_text, convert_to_tensor=True)
        job_embedding = model.encode(job_desc, convert_to_tensor=True)

        # Step 2: Calculate cosine similarity (the "match score")
        similarity_score = util.pytorch_cos_sim(resume_embedding, job_embedding).item()
        match_percentage = round(similarity_score * 100, 1)

        # Step 3: Display the result
        st.subheader("Results")
        st.metric(label="**Overall Match Score**", value=f"{match_percentage}%")

        # Step 4: (Optional) Basic Keyword Extraction
        st.write("### 🔑 Keyword Insights")
        # Simple way to find words in JD that are NOT in the resume
        jd_words = set(re.findall(r'\w+', job_desc.lower()))
        resume_words = set(re.findall(r'\w+', resume_text.lower()))
        missing_keywords = jd_words - resume_words

        # Filter for likely important keywords (longer words)
        important_missing = [word for word in missing_keywords if len(word) > 5 and not word.isnumeric()]
        
        if important_missing:
            st.warning("**Potential Missing Keywords:** " + ", ".join(important_missing[:10]))
        else:
            st.success("Good keyword coverage!")

elif st.button("Analyze Match"):
    st.warning("Please paste a job description first.")