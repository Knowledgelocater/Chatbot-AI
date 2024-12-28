import pyautogui
import pyperclip
import time
import google.generativeai as genai
import os

# Ensure to set the API key correctly
genai.configure(api_key="AIzaSyDUSzMN2ud3cxGCcYRlEM5nvYmdt7bJffw")  # Replace with your environment variable for API key

# Define the model name
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Allow time to position the mouse or focus on the right window
time.sleep(2)

# Step 1: Click on the icon at (1237, 1056)
pyautogui.click(1182, 1052)

# Allow time for any window or operation to load
time.sleep(1)

# Step 2: Click and drag from (1367, 140) to (1892, 1013)
pyautogui.moveTo(704, 224)
pyautogui.mouseDown()  # Press the mouse button down
pyautogui.moveTo(1821, 904, duration=1)  # Drag to the new position
pyautogui.mouseUp()  # Release the mouse button

# Step 3: Copy the selected text to the clipboard (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(712, 245)

# Allow some time for the copy operation to complete
time.sleep(1)

# Step 4: Retrieve the copied text from the clipboard
chat_history = pyperclip.paste()

# Print or store the copied text in a variable
print(f"Copied Text: {chat_history}")


formatted_history = "\n".join(chat_history)

# Define the prompt including chat history
prompt = f"""
You are Kinshuk Shukla. You speak Hindi and English, and you are Indian. You are a Python coder pursuing a B-Tech degree in Civil Engineering at NIT Jamshedpur. You have to generate single line response to chat alike Kinshuk does , after analyzing chat history

{formatted_history}
"""

# Call the model to generate content based on the chat history
response = model.generate_content(prompt)

# Print or use the response
message =  response.text
pyperclip.copy(message)


# Step 5: Click at (1299, 960) where the text will be pasted
pyautogui.click(1299, 960)

# Step 6: Paste the text (Ctrl + V)
pyautogui.hotkey('ctrl', 'v')

# Allow some time to ensure the text is pasted
time.sleep(0.5)

# Step 7: Press Enter
pyautogui.press('enter')