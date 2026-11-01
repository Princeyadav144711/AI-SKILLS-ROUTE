def calculate_recommendations(user):

    skills = (user.skills or "").lower()
    interests = (user.interests or "").lower()
    goal = (user.career_goal or "").lower()

    careers = {

        "AI/ML Engineer": {
            "keywords": [
                "python",
                "machine learning",
                "ai",
                "artificial intelligence",
                "tensorflow",
                "pandas",
                "numpy",
                "data science"
            ]
        },

        "Data Scientist": {
            "keywords": [
                "python",
                "pandas",
                "numpy",
                "statistics",
                "data",
                "machine learning",
                "sql"
            ]
        },

        "Data Analyst": {
            "keywords": [
                "sql",
                "excel",
                "python",
                "data",
                "statistics",
                "power bi",
                "tableau"
            ]
        },

        "Web Developer": {
            "keywords": [
                "html",
                "css",
                "javascript",
                "react",
                "frontend",
                "backend",
                "web"
            ]
        },

        "Software Developer": {
            "keywords": [
                "python",
                "java",
                "c++",
                "javascript",
                "programming",
                "software",
                "git"
            ]
        },

        "Cybersecurity Analyst": {
            "keywords": [
                "cybersecurity",
                "security",
                "network",
                "linux",
                "ethical hacking",
                "penetration testing",
                "python"
            ]
        },

        "Cloud Engineer": {
            "keywords": [
                "aws",
                "azure",
                "cloud",
                "docker",
                "linux",
                "devops",
                "network"
            ]
        }
    }

    results = []

    combined_text = skills + " " + interests + " " + goal

    for career, data in careers.items():

        matched_keywords = []

        for keyword in data["keywords"]:

            if keyword in combined_text:
                matched_keywords.append(keyword)

        score = min(
            100,
            len(matched_keywords) * 15
        )

        # Give extra weight to selected career goal
        if career.lower() == goal:
            score += 30

        score = min(score, 100)

        reason = generate_reason(
            career,
            matched_keywords
        )

        results.append({
            "career": career,
            "score": score,
            "reason": reason
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results


def generate_reason(career, matched_keywords):

    if matched_keywords:

        skills_text = ", ".join(matched_keywords[:5])

        return (
            f"Your profile matches {career} because "
            f"you have interests or skills related to: "
            f"{skills_text}."
        )

    return (
        f"{career} may be suitable for you, "
        f"but you currently have limited matching skills."
    )