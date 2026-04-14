import json

HUBSPOT_BASE_URL = "https://api.hubapi.com"


# -------------------------
# Load contacts
# -------------------------
def load_contacts():
    with open("data/contacts.json", "r") as f:
        return json.load(f)


# -------------------------
# Segment contacts safely
# -------------------------
def segment_contacts(contacts):
    segments = {
        "founders": [],
        "marketers": [],
        "freelancers": []
    }

    for c in contacts:
        persona = c.get("persona")

        if persona not in segments:
            print(f"⚠️ Skipping invalid persona: {persona}")
            continue

        segments[persona].append(c)

    return segments


# -------------------------
# Send newsletter (safe access)
# -------------------------
def send_newsletter(contacts, newsletter_content):
    logs = []

    for c in contacts:
        email = c.get("email")

        if not email:
            print("⚠️ Skipping contact with missing email")
            continue

        print(f"\n📧 Sending to: {email}")
        print(f"Content: {newsletter_content}")

        logs.append({
            "email": email,
            "status": "sent"
        })

    return logs


# -------------------------
# Campaign logging
# -------------------------
def log_campaign(topic):
    print(f"\n✅ Campaign logged for topic: {topic}")


# -------------------------
# OPTIONAL: HubSpot-style function (mock-safe)
# -------------------------
def create_contact(email, persona):
    payload = {
        "properties": {
            "email": email,
            "persona": persona
        }
    }

    print("Mock HubSpot payload:", payload)
    return payload
