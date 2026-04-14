# 🧠 AI Marketing Content Pipeline (NovaMind)

An end-to-end AI-powered marketing automation system that generates blog content, personalizes newsletters by audience persona, distributes messages through a CRM-style pipeline, and analyzes engagement performance to produce actionable insights.

This project simulates a real-world growth engineering system used by modern startups to automate content creation, distribution, and optimization in a closed feedback loop.

---

# 🚀 Key Features

- 📝 AI-generated blog content from a user-defined topic  
- 📬 Persona-based newsletter generation (Founders, Marketers, Freelancers)  
- 👥 CRM-style contact segmentation system  
- 📤 Simulated newsletter distribution pipeline  
- 📊 Automated performance analytics generation  
- 🔁 Full end-to-end workflow orchestrated via `main.py`  
- 📈 Insight generation for content optimization recommendations  

---

# 🏗️ System Architecture

## Flow Overview

Topic Input  
→ AI Content Generation  
→ CRM Contact Segmentation  
→ Newsletter Distribution  
→ Analytics Engine  
→ Insight Summary  

---

## Modular Breakdown

1. **Content Generation (`content_generator.py`)**  
   Generates:
   - Blog post (400–600 words)
   - 3 persona-specific newsletters

2. **CRM Layer (`crm.py`)**  
   - Loads contacts from a local JSON file  
   - Segments users into personas  
   - Simulates email distribution  

3. **Analytics Layer (`analytics.py`)**  
   - Generates mock engagement metrics  
   - Simulates performance tracking across personas  

4. **Orchestration (`main.py`)**  
   - Runs the full pipeline end-to-end  
   - Saves outputs to `/outputs` directory  

---

# 🔧 Tools, APIs, and Models Used

- **Python 3.10+** – Core programming language  
- **JSON** – Used for mock CRM data storage  
- **GitHub Actions** – CI pipeline for automated testing  
- **Simulated AI Logic** – Content generation and analytics are mock implementations (no external API calls required)  
- **Modular Python Design** – Clean separation of pipeline stages  

---

# 🧪 Assumptions

- CRM data is simulated using `data/contacts.json`  
- Email sending is mocked (no real emails are sent)  
- Analytics metrics are randomly generated for demonstration purposes  
- AI-generated content is simulated rather than using a live LLM API  
- System is designed as a prototype for scalable marketing automation workflows  

---

# ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
