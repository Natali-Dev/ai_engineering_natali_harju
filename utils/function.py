from dotenv import load_dotenv
from google import genai
import os


# a) Connect python to gemini, very important that you place the api key in .env and gitignore it
def get_gemini(prompt: str) -> str:
    """Gets API-key, and generates_content. Send '" "' to check connection.
    \nTo get correct path: 
    import sys
    sys.path.append("jump back")\n

    #### Args:
        prompt (str): message for gemini

    #### Returns:
        str: response from gemini
    """
    if prompt == " ":
        prompt = "Checking connection"
    load_dotenv()
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    if not response.text:
        print("response.text is None! Try restart kernel")
    else:
        return response.text

