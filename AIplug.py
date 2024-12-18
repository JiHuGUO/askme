import google.generativeai as genai
import re
import os 
my_key = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=my_key)

model = genai.GenerativeModel("gemini-1.5-flash")
sample_pdf = genai.upload_file('input/1-s2.0-S1364815222002444-main.pdf')
response = model.generate_content(["Now, imagine you are a professor leading graduate students through reading this article. You need to pose a multiple-choice question with four options at critical points, based on each paragraph, every question start with **Q**, for example **Q1**:. In the end, show all the answers, starting with **Answers:**", sample_pdf])


paragraphs = response.text

questions = re.findall(r'\*\*Q(.*?)\*\*Q',paragraphs,re.DOTALL)

answer = re.findall(r'\*\*Answers:\*\*.*',paragraphs,re.DOTALL)

print(response.text)
print(questions)
print(answer)