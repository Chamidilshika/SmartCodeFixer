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
    lines = code.split("\n")
    fixed_lines = []
    
    for line in lines:
        fixed_line = line
        
        # 1. Fix print statements without parentheses while preserving spaces/indentation
        if "print " in fixed_line:
            indent = len(fixed_line) - len(fixed_line.lstrip())
            content = fixed_line.strip().split("print ", 1)[1]
            fixed_line = " " * indent + f"print({content})"
            
        # 2. Fix '=' instead of '==' in conditionals
        if ("if " in fixed_line or "elif " in fixed_line) and "=" in fixed_line and "==" not in fixed_line:
            fixed_line = fixed_line.replace("=", "==")
            
        # 3. Fix missing colons ':' at the end of structures
        stripped = fixed_line.strip()
        keywords = ["def ", "if ", "elif ", "else", "for ", "while "]
        if any(stripped.startswith(kw) for kw in keywords):
            if not stripped.endswith(":"):
                fixed_line = fixed_line + ":"
                
        fixed_lines.append(fixed_line)
        
    return "\n".join(fixed_lines)