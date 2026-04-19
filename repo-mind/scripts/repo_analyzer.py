import os

IGNORED = [
    "node_modules",
    ".git",
    "dist",
    "build",
    "__pycache__"
]

def scan_repo(path):
    summary = []

    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in IGNORED]

        for file in files:
            if file.endswith((".py", ".js", ".ts", ".md")):
                summary.append(os.path.join(root, file))

    return summary


def summarize(files):
    report = []

    for f in files:
        report.append({
            "file": f,
            "description": "source file"
        })

    return report