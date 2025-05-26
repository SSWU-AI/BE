import openai
import os
from datetime import date

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_age_group(birth_date):
    #나이대 계산
    if not birth_date:
        return "알 수 없음"
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    if age < 20:
        return "10대"
    elif 20 <= age < 30:
        return "20대"
    elif 30 <= age < 40:
        return "30대"
    elif 40 <= age < 60:
        return "중장년"
    else:
        return "노인"

def ask_openai_with_profile(user, goal: str) -> str:
    try:
        profile = user.profile
        nickname = profile.nickname or user.username
        gender = profile.get_gender_display() if profile.gender else "미입력"
        age_group = get_age_group(profile.birth_date)
        height = f"{profile.height}cm" if profile.height else "미입력"
        weight = f"{profile.weight}kg" if profile.weight else "미입력"
        experience_level = profile.get_experience_level_display() if profile.experience_level else "미입력"
        experience_desc = {
            "초보": "운동 경험 없음",
            "중급": "어느 정도 운동 경험 있음",
            "고급": "운동 경험 풍부함",
            "미입력": "운동 경험 정보 없음"
        }.get(experience_level, "운동 경험 정보 없음")
        preferred_exercise = profile.preferred_exercise if profile.preferred_exercise else "특별히 선호하는 운동 없음"

        prompt = (
            f"사용자 닉네임: {nickname}\n"
            f"성별: {gender}\n"
            f"나이대: {age_group}\n"
            f"키: {height}\n"
            f"몸무게: {weight}\n"
            f"운동 경험 수준: {experience_level} ({experience_desc})\n"
            f"선호 운동: {preferred_exercise}\n"
            f"운동 목표: {goal}\n\n"
            f"이 정보를 바탕으로 사용자에게 적합한 맞춤형 운동 계획을 제안해주세요."
        )

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
