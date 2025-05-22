import json
import os
from datetime import datetime

# JSON file to store reports
GP_REPORT_FILE = "gp_reports.json"

# Load existing reports

def load_gp_reports():
    if not os.path.exists(GP_REPORT_FILE):
        return []
    try:
        with open(GP_REPORT_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# Save reports to disk

def save_gp_report(summary, content, source="voice"):
    report = {
        "summary": summary,
        "content": content,
        "timestamp": datetime.utcnow().isoformat(),
        "source": source
    }
    reports = load_gp_reports()
    reports.append(report)
    with open(GP_REPORT_FILE, 'w') as f:
        json.dump(reports, f, indent=2)
    return "✅ Your GP report has been saved."

# Retrieve the latest report

def get_latest_gp_report():
    reports = load_gp_reports()
    if not reports:
        return "📭 No GP reports found."
    latest = reports[-1]
    return (f"📋 Latest GP Report Summary: {latest['summary']}\n"
            f"📝 Content: {latest['content']}\n📅 Timestamp: {latest['timestamp']}")

# List all reports

def list_all_gp_reports():
    reports = load_gp_reports()
    if not reports:
        return "📭 No GP reports saved yet."
    return "📂 Stored GP Reports:\n" + "\n".join([f"- {r['summary']} ({r['timestamp'][:10]})" for r in reports])

# Handler for GP report intent

def handle_gp_report(intent, user_input, memory):
    memory = memory or {}

    if intent == "read_gp_report":
        return get_latest_gp_report()

    if intent == "summarize_gp_findings":
        return list_all_gp_reports()

    if intent == "check_gp_email":
        # This is a mockup. Real implementation would connect to email API.
        summary = "Blood Test Results from Dr. Smith"
        content = "All levels normal. No action required."
        return save_gp_report(summary, content, source="email")

    # Add voice-captured report
    if intent.startswith("gp_report") or "add" in user_input.lower():
        memory['expecting_report_summary'] = True
        return "📝 Please tell me the summary of your GP report."

    if memory.get("expecting_report_summary"):
        memory['report_summary'] = user_input
        memory['expecting_report_summary'] = False
        memory['expecting_report_content'] = True
        return "📄 Got it. Now please tell me the full content of the report."

    if memory.get("expecting_report_content"):
        summary = memory.pop("report_summary")
        content = user_input
        memory['expecting_report_content'] = False
        return save_gp_report(summary, content, source="voice")

    return "❓ I didn't understand your GP report request."
