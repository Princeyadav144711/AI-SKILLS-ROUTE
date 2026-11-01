
from services.gemini_service import ask_gemini


def generate_career_advice(user):
    """Generate personalized career guidance from a student profile."""

    education = user.education or "Not provided"
    experience = user.experience or "Not provided"
    skills = user.skills or "Not provided"
    interests = user.interests or "Not provided"
    career_goal = user.career_goal or "Not sure"

    prompt = f"""
You are the AI Career Advisor for AI Skills Route,
a student career guidance website.

Analyze the following student profile and provide
practical, personalized career guidance.

STUDENT PROFILE
Education: {education}
Experience: {experience}
Current Skills: {skills}
Interests: {interests}
Career Goal: {career_goal}

Write your answer using these headings:

1. Recommended Career
Choose the most suitable career and explain why.

2. Career Match Explanation
Explain how the student's skills and interests relate
to the recommended career. Do not invent qualifications.

3. Skills to Improve
List the most important missing or weak skills.

4. Learning Plan
Give a practical 3-month learning plan, divided into
Month 1, Month 2, and Month 3.

5. Portfolio Projects
Suggest three projects appropriate for the student's level.

6. Next Action
Give one clear action the student can start today.

Keep the answer encouraging, realistic, and easy to understand.
Do not claim that the recommendation guarantees employment.
Clearly mention when information in the profile is missing.
"""

    return ask_gemini(prompt)