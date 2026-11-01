# services/resources_engine.py

RESOURCES = {

    "AI/ML Engineer": [
        {
            "title": "Python Programming",
            "platform": "Python.org",
            "type": "Programming",
            "url": "https://www.python.org/about/gettingstarted/"
        },
        {
            "title": "Machine Learning",
            "platform": "Google for Developers",
            "type": "Machine Learning",
            "url": "https://developers.google.com/machine-learning"
        },
        {
            "title": "TensorFlow Tutorials",
            "platform": "TensorFlow",
            "type": "Deep Learning",
            "url": "https://www.tensorflow.org/tutorials"
        },
        {
            "title": "Git Documentation",
            "platform": "Git",
            "type": "Tools",
            "url": "https://git-scm.com/doc"
        }
    ],

    "Data Scientist": [
        {
            "title": "Python for Data Science",
            "platform": "Kaggle",
            "type": "Data Science",
            "url": "https://www.kaggle.com/learn/python"
        },
        {
            "title": "Pandas Documentation",
            "platform": "Pandas",
            "type": "Data Analysis",
            "url": "https://pandas.pydata.org/docs/"
        },
        {
            "title": "Machine Learning",
            "platform": "Google for Developers",
            "type": "Machine Learning",
            "url": "https://developers.google.com/machine-learning"
        },
        {
            "title": "SQL Tutorial",
            "platform": "W3Schools",
            "type": "Database",
            "url": "https://www.w3schools.com/sql/"
        }
    ],

    "Data Analyst": [
        {
            "title": "Excel Training",
            "platform": "Microsoft",
            "type": "Data Analysis",
            "url": "https://support.microsoft.com/excel"
        },
        {
            "title": "SQL Tutorial",
            "platform": "W3Schools",
            "type": "Database",
            "url": "https://www.w3schools.com/sql/"
        },
        {
            "title": "Power BI Learning",
            "platform": "Microsoft",
            "type": "Visualization",
            "url": "https://learn.microsoft.com/power-bi/"
        },
        {
            "title": "Python for Data Analysis",
            "platform": "Kaggle",
            "type": "Programming",
            "url": "https://www.kaggle.com/learn/python"
        }
    ],

    "Web Developer": [
        {
            "title": "HTML Tutorial",
            "platform": "MDN Web Docs",
            "type": "Frontend",
            "url": "https://developer.mozilla.org/en-US/docs/Web/HTML"
        },
        {
            "title": "CSS Tutorial",
            "platform": "MDN Web Docs",
            "type": "Frontend",
            "url": "https://developer.mozilla.org/en-US/docs/Web/CSS"
        },
        {
            "title": "JavaScript Guide",
            "platform": "MDN Web Docs",
            "type": "JavaScript",
            "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript"
        },
        {
            "title": "Flask Documentation",
            "platform": "Flask",
            "type": "Backend",
            "url": "https://flask.palletsprojects.com/"
        }
    ],

    "Software Developer": [
        {
            "title": "Python Programming",
            "platform": "Python.org",
            "type": "Programming",
            "url": "https://www.python.org/about/gettingstarted/"
        },
        {
            "title": "Object Oriented Programming",
            "platform": "GeeksforGeeks",
            "type": "Programming",
            "url": "https://www.geeksforgeeks.org/oops-concepts/"
        },
        {
            "title": "Git Documentation",
            "platform": "Git",
            "type": "Tools",
            "url": "https://git-scm.com/doc"
        },
        {
            "title": "SQL Tutorial",
            "platform": "W3Schools",
            "type": "Database",
            "url": "https://www.w3schools.com/sql/"
        }
    ],

    "Cybersecurity Analyst": [
        {
            "title": "Cybersecurity Fundamentals",
            "platform": "Cisco",
            "type": "Cybersecurity",
            "url": "https://www.cisco.com/c/en/us/products/security/what-is-cybersecurity.html"
        },
        {
            "title": "OWASP Web Security",
            "platform": "OWASP",
            "type": "Web Security",
            "url": "https://owasp.org/www-project-top-ten/"
        },
        {
            "title": "Networking Fundamentals",
            "platform": "Cisco",
            "type": "Networking",
            "url": "https://www.cisco.com/c/en/us/solutions/small-business/resource-center/networking/networking-basics.html"
        },
        {
            "title": "Linux Documentation",
            "platform": "Linux",
            "type": "Operating System",
            "url": "https://www.linux.org/"
        }
    ],

    "Cloud Engineer": [
        {
            "title": "AWS Training",
            "platform": "AWS",
            "type": "Cloud",
            "url": "https://aws.amazon.com/training/"
        },
        {
            "title": "Microsoft Azure Learning",
            "platform": "Microsoft",
            "type": "Cloud",
            "url": "https://learn.microsoft.com/azure/"
        },
        {
            "title": "Docker Documentation",
            "platform": "Docker",
            "type": "DevOps",
            "url": "https://docs.docker.com/"
        },
        {
            "title": "Linux Documentation",
            "platform": "Linux",
            "type": "Operating System",
            "url": "https://www.linux.org/"
        }
    ]
}


PROJECTS = {

    "AI/ML Engineer": [
        "House Price Prediction System",
        "Student Performance Prediction",
        "Movie Recommendation System",
        "AI Career Recommendation System"
    ],

    "Data Scientist": [
        "Customer Churn Prediction",
        "Sales Forecasting System",
        "COVID-19 Data Analysis",
        "Student Performance Analysis"
    ],

    "Data Analyst": [
        "Sales Dashboard",
        "Student Result Analysis",
        "Customer Data Analysis",
        "Business Intelligence Dashboard"
    ],

    "Web Developer": [
        "E-Commerce Website",
        "Online Learning Platform",
        "Portfolio Website",
        "College Management System"
    ],

    "Software Developer": [
        "Library Management System",
        "Student Management System",
        "Expense Tracker",
        "Task Management Application"
    ],

    "Cybersecurity Analyst": [
        "Password Strength Analyzer",
        "Network Security Scanner",
        "Phishing Detection System",
        "SQL Injection Simulator"
    ],

    "Cloud Engineer": [
        "Cloud File Storage System",
        "Cloud-Based Web Application",
        "Dockerized Web Application",
        "Cloud Monitoring Dashboard"
    ]
}


def get_resources(career):
    """
    Return learning resources for the selected career.
    """

    return RESOURCES.get(career, RESOURCES["AI/ML Engineer"])


def get_projects(career):
    """
    Return project recommendations for the selected career.
    """

    return PROJECTS.get(career, PROJECTS["AI/ML Engineer"])