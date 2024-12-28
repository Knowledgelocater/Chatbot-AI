import google.generativeai as genai
import os

# Ensure to set the API key correctly
genai.configure(api_key="AIzaSyDUSzMN2ud3cxGCcYRlEM5nvYmdt7bJffw")  # Replace with your environment variable for API key

# Define the model name
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Example chat history as a list of strings (you can modify it as per your chat format)
chat_history = [
   '''[10:57 AM, 9/19/2024] 𝓚𝓲𝓷𝓼𝓱𝓾𝓴 𝓢𝓱𝓾𝓴𝓵𝓪 🙏: Haan, yahi hai.
[10:57 AM, 9/19/2024] दीदी: Hello'''
    # Add more chat history as needed
]

# Combine chat history into a single string for the prompt
formatted_history = "\n".join(chat_history)

# Define the prompt including chat history
prompt = f"""
You are Kinshuk Shukla. You speak Hindi and English, and you are Indian. You are a Python coder pursuing a B-Tech degree in Civil Engineering at NIT Jamshedpur. You have to generate single line response to chat alike Kinshuk does , after analyzing chat history

{formatted_history}
"""

# Call the model to generate content based on the chat history
response = model.generate_content(prompt)

# Print or use the response
print("Assistant:", response.text)


