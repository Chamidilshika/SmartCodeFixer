# -------- SUMMARIZE --------
def summarize_code(code):
    if "def" in code:
        return "This code defines a function."
    elif "if" in code:
        return "This code contains a conditional statement."
    elif "for" in code:
        return "This code contains a loop."
    else:
        return "This is a code snippet."


# -------- BUG DETECTION --------
def detect_bug(code):
    issues = []

    if "=" in code and "==" not in code:
        issues.append("Possible use of '=' instead of '=='")

    if "if" in code and ":" not in code:
        issues.append("Missing ':' in control statement")

    if "print " in code:
        issues.append("Use print() with parentheses")

    if len(issues) == 0:
        return "No obvious bugs found"
    
    return issues


# -------- CODE FIX --------
def fix_code(code):
    fixed = code

    if "if" in fixed and "=" in fixed and "==" not in fixed:
        fixed = fixed.replace("=", "==")

    if "print " in fixed:
        content = fixed.split("print ")[1]
        fixed = f"print({content})"

    if "if" in fixed and ":" not in fixed:
        fixed += ":"

    return fixed