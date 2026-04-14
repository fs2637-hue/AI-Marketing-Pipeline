import json

def load_contacts():
    with open("data/contacts.json", "r") as f:
        return json.load(f)

def segment_contacts(contacts):
    segments = {"founders": [], "marketers": [], "freelancers": []}

    for c in contacts:
        segments[c["persona"]].append(c)

    return segments

def send_newsletter(contacts, newsletter_content):
    logs = []

    for c in contacts:
        print(f"\n📧 Sending to: {c['email']}")
        print(f"Content: {newsletter_content}")

        logs.append({
            "email": c["email"],
            "status": "sent"
        })

    return logs

def log_campaign(topic):
    print(f"\n✅ Campaign logged for topic: {topic}")
