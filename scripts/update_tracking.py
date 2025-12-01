import os
import datetime

def count_files(directory):
    if not os.path.exists(directory):
        return 0
    return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

def generate_progress_bar(validated, total, length=20):
    if total == 0:
        percent = 0
    else:
        percent = validated / total
    
    filled = int(length * percent)
    bar = "[" + "=" * filled + "." * (length - filled) + "]"
    return f"{bar} {int(percent * 100)}%"

def update_dashboard():
    domains = ["physics", "biology", "neuroscience", "social_science", "mathematics"]
    base_dir = "."
    data_dir = os.path.join(base_dir, ".agent/data")
    claims_dir = os.path.join(base_dir, "claims/pending")
    
    dashboard_content = "# KDFA Validation Dashboard\n\n"
    dashboard_content += "## Overview\n"
    dashboard_content += f"**Status**: Active\n"
    dashboard_content += f"**Last Updated**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    dashboard_content += "## Progress by Domain\n\n"
    
    total_validated = 0
    total_pending = 0
    
    for domain in domains:
        validated_count = count_files(os.path.join(data_dir, domain))
        # For pending, we might need a better way to categorize by domain if they are all in one folder.
        # For now, let's assume claims are named {domain}_*.md
        pending_count = len([f for f in os.listdir(claims_dir) if f.startswith(domain) and f.endswith(".md")]) if os.path.exists(claims_dir) else 0
        
        total_domain = validated_count + pending_count
        progress_bar = generate_progress_bar(validated_count, total_domain)
        
        dashboard_content += f"### {domain.replace('_', ' ').title()}\n"
        dashboard_content += f"- **Validated**: {validated_count}\n"
        dashboard_content += f"- **Pending**: {pending_count}\n"
        dashboard_content += f"- **Progress**: {progress_bar}\n\n"
        
        total_validated += validated_count
        total_pending += pending_count

    dashboard_content += "## Recent Validations\n"
    # List last 5 validated files
    recent_files = []
    for domain in domains:
        d_path = os.path.join(data_dir, domain)
        if os.path.exists(d_path):
            for f in os.listdir(d_path):
                if os.path.isfile(os.path.join(d_path, f)):
                    recent_files.append((os.path.getmtime(os.path.join(d_path, f)), f, domain))
    
    recent_files.sort(key=lambda x: x[0], reverse=True)
    
    if not recent_files:
        dashboard_content += "*No validated claims yet.*\n\n"
    else:
        for _, fname, domain in recent_files[:5]:
            dashboard_content += f"- [{domain}] {fname}\n"
        dashboard_content += "\n"

    dashboard_content += "## Critical Issues\n"
    dashboard_content += "*None identified.*\n"
    
    with open("VALIDATION_DASHBOARD.md", "w") as f:
        f.write(dashboard_content)
    print("Dashboard updated.")

if __name__ == "__main__":
    update_dashboard()
