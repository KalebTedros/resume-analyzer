Resume & Job Matcher
A simple web app that uses AI to see how well your resume matches a job description. It gives you a match score and shows you keywords you might be missing.

How to Try It (Takes 2 Minutes):

- Click the green "Code" button at the top of this page.
- Click the "Codespaces" tab.
- Click "Create codespace on main".
- Wait for the codespace to start. In the terminal that opens, copy and paste this command:
  ----- python -m streamlit run app.py --server.port 8501 -----
- A preview window will open. That's the app! Paste a job description and click "Analyze Match".

What It Does
- Paste a Job Description: Copy the text from any job posting you're interested in.
- Get a Match Score: The app uses an AI model to understand the meaning of the text and gives you a compatibility score.
- Find Missing Keywords: It shows you important words from the job that aren't in your resume, so you know what to add.
What This Project Shows
- I built this to learn and demonstrate:
    Python & AI: Using the transformers library to add powerful language AI to an app.
    Web Development: Creating an interactive tool with Streamlit.
    Cloud Development: Building a project entirely in the cloud with GitHub Codespaces, with no setup needed.
    Problem-Solving: Creating a tool that is actually useful for me in my job search.

File Guide
app.py - The main application code.
requirements.txt - The list of Python packages the app needs.
resume.txt - Put your own resume text here.
.devcontainer/ - Configuration to make Codespaces work automatically.
