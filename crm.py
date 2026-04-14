import json

def load_contacts():
    with open("data/contacts.json", "r") as f:
        return json.load(f)

def segment_contacts(contacts):
    segments = {"founders": [], "marketers": [], "freelancers": []}

    for c in contacts:
        persona = c.get("persona")

        if persona not in segments:
            print(f"⚠️ Skipping unknown persona: {persona}")
            continue
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
HUBSPOT_BASE_URL = "https://api.hubapi.com"

def create_contact(email, persona):
    # clearly structured payload
    payload = {
        "properties": {
            "email": email,
            "persona": persona
        }
    }
