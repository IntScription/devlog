import re
from pathlib import Path
from datetime import datetime

def parse_date_from_filename(filename):
    """Extract date from filename like '2025-07-17'"""
    match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
    if match:
        return datetime.strptime(match.group(1), '%Y-%m-%d')
    return None

def get_log_sequence():
    """Get all logs sorted by date"""
    logs_dir = Path('logs')
    logs = []
    
    for log_dir in logs_dir.iterdir():
        if log_dir.is_dir():
            date = parse_date_from_filename(log_dir.name)
            if date:
                logs.append((date, log_dir.name))
    
    return sorted(logs)

def fix_navigation_in_file(file_path, prev_log=None, next_log=None):
    """Fix navigation in a single log file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old HTML navigation (more thorough)
    content = re.sub(r'<div class="nav-links">.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="nav-links">\s*---\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="nav-links">\s*', '', content, flags=re.DOTALL)
    
    # Remove old Markdown navigation lines
    content = re.sub(r'^\[← Previous\].*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\[Next →\].*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\[← Previous\].*\|.*\[Next →\].*$', '', content, flags=re.MULTILINE)
    
    # Remove trailing --- before navigation
    content = re.sub(r'\n---\s*$', '', content)
    
    # Build new navigation
    nav_parts = []
    if prev_log:
        nav_parts.append(f'[← Previous]({{{{site.baseurl}}}}/logs/{prev_log}/)')
    if next_log:
        nav_parts.append(f'[Next →]({{{{site.baseurl}}}}/logs/{next_log}/)')
    
    if nav_parts:
        # Add navigation at the end
        content = content.rstrip() + '\n\n---\n\n' + ' | '.join(nav_parts) + '\n'
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed navigation in {file_path}")

def main():
    """Fix navigation in all log files"""
    logs = get_log_sequence()
    
    for i, (date, log_name) in enumerate(logs):
        file_path = Path('logs') / log_name / 'index.md'
        
        if not file_path.exists():
            continue
        
        # Determine previous and next logs
        prev_log = logs[i-1][1] if i > 0 else None
        next_log = logs[i+1][1] if i < len(logs) - 1 else None
        
        fix_navigation_in_file(file_path, prev_log, next_log)

if __name__ == '__main__':
    main() 