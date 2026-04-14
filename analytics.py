import random

def generate_metrics():
    return {
        "founders": {
            "open_rate": round(random.uniform(0.15, 0.35), 2),
            "click_rate": round(random.uniform(0.03, 0.12), 2)
        },
        "marketers": {
            "open_rate": round(random.uniform(0.25, 0.45), 2),
            "click_rate": round(random.uniform(0.08, 0.2), 2)
        },
        "freelancers": {
            "open_rate": round(random.uniform(0.18, 0.38), 2),
            "click_rate": round(random.uniform(0.05, 0.15), 2)
        }
    }

def analyze_performance(metrics):
    best = max(metrics, key=lambda x: metrics[x]["click_rate"])

    summary = f"""
📊 PERFORMANCE SUMMARY

Best performing segment: {best}

Insights:
- Engagement varies by persona targeting
- Content personalization improves click-through rates
- Recommend increasing tailored examples for {best}

Next step:
- Generate more targeted content for underperforming segments
"""

    return summary
