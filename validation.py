from datetime import datetime

def validate_task_title(title):
    # Check length and raise a ValueError if empty
    if len(title) == 0:
        raise ValueError("Title cannot be empty")
    return True
    
def validate_task_description(description):
    # Check length and raise a ValueError if empty
    if len(description) == 0:
        raise ValueError("Description cannot be empty")
    return True    
    
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        # Re-raise a ValueError to satisfy the Semgrep check
        raise ValueError("Invalid date format")
