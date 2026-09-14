from datetime import datetime

def validate_task_title(title):
    # Returns True if title is not empty, False otherwise
    return bool(title.strip())
    
def validate_task_description(description):
    # Returns True if description is not empty, False otherwise
    return bool(description.strip())    
    
def validate_due_date(due_date):
    # Validates if due_date is in YYYY-MM-DD format
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
