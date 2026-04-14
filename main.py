import os
os.makedirs("outputs", exist_ok=True)
import json

print("AI Marketing Pipeline started")

from content_generator import generate_content
from crm import load_contacts, segment_contacts, send_newsletter, log_campaign
from analytics import generate_metrics, analyze_performance


def run_pipeline(topic):

    print("\n🚀 Starting AI Marketing Pipeline...\n")

    os.makedirs("outputs", exist_ok=True)

    content = generate_content(topic)

    with open("outputs/content.json", "w") as f:
        json.dump(content, f, indent=2)

    print("✅ Content generated")

    contacts = load_contacts()
    segments = segment_contacts(contacts)

    logs = {}

    # 👇 THIS LINE MUST BE ALIGNED EXACTLY LIKE THIS
    for persona, users in segments.items():
        newsletter = content["newsletters"].get(persona)

        if not newsletter:
            continue

        logs[persona] = send_newsletter(users, newsletter)
