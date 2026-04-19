def evaluate(project_summary):

    score = 0

    if "api" in project_summary.lower():
        score += 2

    if "automation" in project_summary.lower():
        score += 2

    if "ai" in project_summary.lower():
        score += 3

    if "dashboard" in project_summary.lower():
        score += 2

    if "subscription" in project_summary.lower():
        score += 1

    return {
        "score": score,
        "verdict": "High SaaS potential" if score > 6 else "Moderate potential"
    }