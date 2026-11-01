from services.gemini_service import ask_gemini

answer = ask_gemini("Reply with only the word HELLO.")

print("\nGemini Response:")
print(answer)