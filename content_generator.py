import json

def generate_content(topic):
    blog = f"""
# {topic}

AI is rapidly transforming how creative agencies operate. Automation tools now assist with ideation, execution, and distribution of marketing content.

In modern workflows, AI can:
- Generate blog drafts
- Personalize newsletters
- Analyze engagement data

This shift allows teams to focus more on strategy and creativity rather than repetitive tasks.

Overall, AI-driven marketing pipelines improve speed, consistency, and performance optimization.
"""

    newsletters = {
        "founders": f"🚀 Founders: {topic} is reshaping scalable growth. Learn how automation boosts ROI and reduces manual workload.",
        "marketers": f"📊 Marketers: Discover how {topic} improves targeting, segmentation, and campaign performance.",
        "freelancers": f"🎨 Freelancers: Use {topic} tools to automate repetitive work and focus on creative output."
    }

    return {
        "topic": topic,
        "blog": blog,
        "newsletters": newsletters
    }
