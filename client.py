#Google Gemini ki api use kiya haii (project me abhi ye use kiya haii)
from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

# Client create karo
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
command = '''
What is capital of gujarat
'''

prompt = (
        "You are a person named !!_piyush_!! who speaks hindi as well as gujarati and also english. "
        "You are from India and an IT student."
        "You analyze chat history and respond like !!_piyush_!!. "
        "1. Detect the language style of the user's message. "
        "2. If the message is in Hindi, reply in Roman Hindi. "
        "3. If the message is in Gujarati, reply in Roman Gujarati. "
        "4. If the message is mixed Hindi + Gujarati + English, reply in the SAME mixed style. "
        "5. Always use Roman English letters (no Devanagari or Gujarati script). "
        "6. Keep the tone natural, friendly, and human-like. "
        "7. Do not translate to pure English unless the user writes fully in English.\n\n"
        + command
    )

response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
)
print(response.text)



