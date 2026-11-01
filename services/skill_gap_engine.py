CAREER_SKILLS = {

    "AI/ML Engineer": [
        "Python",
        "NumPy",
        "Pandas",
        "Mathematics",
        "Statistics",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "SQL",
        "Git"
    ],

    "Data Scientist": [
        "Python",
        "NumPy",
        "Pandas",
        "Statistics",
        "Mathematics",
        "SQL",
        "Machine Learning",
        "Data Visualization",
        "Git"
    ],

    "Data Analyst": [
        "SQL",
        "Excel",
        "Python",
        "Statistics",
        "Data Visualization",
        "Power BI",
        "Tableau"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "Git",
        "Responsive Design",
        "React",
        "REST API",
        "SQL"
    ],

    "Software Developer": [
        "Programming",
        "Python",
        "Java",
        "Data Structures",
        "Algorithms",
        "SQL",
        "Git",
        "Object Oriented Programming"
    ],

    "Cybersecurity Analyst": [
        "Networking",
        "Linux",
        "Cybersecurity",
        "Python",
        "Ethical Hacking",
        "Cryptography",
        "Operating Systems",
        "Security Tools"
    ],

    "Cloud Engineer": [
        "Linux",
        "Networking",
        "AWS",
        "Azure",
        "Docker",
        "DevOps",
        "Git",
        "Python"
    ]
}


def normalize(text):
    return text.lower().strip()


def calculate_skill_gap(user, career):

    current_skills_text = normalize(
        user.skills or ""
    )

    required_skills = CAREER_SKILLS.get(
        career,
        []
    )

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if normalize(skill) in current_skills_text:

            matched_skills.append(skill)

        else:

            missing_skills.append(skill)

    total_skills = len(required_skills)

    if total_skills > 0:

        match_percentage = round(
            (len(matched_skills) / total_skills) * 100
        )

    else:

        match_percentage = 0

    return {
        "career": career,
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": match_percentage
    }