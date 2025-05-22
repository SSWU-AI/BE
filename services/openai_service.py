import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_openai(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "운동 코치 역할을 해줘."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500,
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"OpenAI API 호출 오류: {e}"
