from datetime import datetime

def validate_task_title(title):
    # Explicitly check for length if it's empty or whitespace only
    if title is None or len(title.strip()) == 0:
        return False
    return True
    
def validate_task_description(description):
    # Explicitly check for length if it's empty or whitespace only
    if description is None or len(description.strip()) == 0:
        return False
    return True    
    
def validate_due_date(due_date):
    # First, verify if it's an empty string using len
    if due_date is None or len(due_date.strip()) == 0:
        return False
        
    # Check for the correct format and catch format issues
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
