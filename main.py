print("AI Marketing Pipeline started")
from content_generator import generate_content
from crm import load_contacts, segment_contacts, send_newsletter, log_campaign
from analytics import generate_metrics, analyze_performance
import json

def run_pipeline(topic):

    print("\n🚀 Starting AI Marketing Pipeline...\n")

    # 1. Generate content
    content = generate_content(topic)

    with open("outputs/content.json", "w") as f:
        json.dump(content, f, indent=2)

    print("✅ Content generated")

    # 2. Load CRM contacts
    contacts = load_contacts()
    segments = segment_contacts(contacts)

    # 3. Send newsletters
    logs = {}

    for persona, users in segments.items():
        newsletter = content["newsletters"][persona]
        logs[persona] = send_newsletter(users, newsletter)

    print("\n✅ Newsletters sent")

    # 4. Simulate analytics
    metrics = generate_metrics()

    with open("outputs/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    # 5. AI-style summary
    summary = analyze_performance(metrics)

    with open("outputs/summary.txt", "w") as f:
        f.write(summary)

    print(summary)

    log_campaign(topic)

if __name__ == "__main__":
    run_pipeline("AI in Creative Automation")
