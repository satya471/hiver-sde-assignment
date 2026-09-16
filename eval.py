import app

GOLDEN_SET = [
    {"tweet": "My package was supposed to be here on Monday but it hasn't arrived.", "true_intent": "Order_Delay", "true_action": "auto-handle"},
    {"tweet": "Someone locked me out of my account, I need to reset my password ASAP!!", "true_intent": "Account_Issue", "true_action": "escalate"},
    {"tweet": "The shoes I ordered arrived with a completely broken sole.", "true_intent": "Product_Return", "true_action": "auto-handle"},
    {"tweet": "Do you guys ship internationally to India?", "true_intent": "General_Query", "true_action": "auto-handle"}
]

def run_trivial_baseline(tweet):
    return {"intent": "General_Query", "action": "auto-handle"}

def run_keyword_baseline(tweet):
    text = tweet.lower()
    if "late" in text or "arrive" in text or "package" in text:
        return {"intent": "Order_Delay", "action": "auto-handle"}
    if "lock" in text or "password" in text or "account" in text:
        return {"intent": "Account_Issue", "action": "escalate"}
    if "broken" in text or "return" in text or "defective" in text:
        return {"intent": "Product_Return", "action": "auto-handle"}
    return {"intent": "General_Query", "action": "auto-handle"}

def evaluate_all():
    models = {
        "Trivial Baseline": run_trivial_baseline,
        "Keyword Baseline": run_keyword_baseline,
        "Our AI Agent Pipeline": lambda t: app.run_agent(t)
    }

    print("=== Running Evaluation Harness ===")
    for model_name, model_fn in models.items():
        correct_intents = 0
        correct_actions = 0
        total = len(GOLDEN_SET)

        for item in GOLDEN_SET:
            pred = model_fn(item["tweet"])
            if pred["intent"] == item["true_intent"]:
                correct_intents += 1
            if pred["action"] == item["true_action"]:
                correct_actions += 1

        intent_acc = (correct_intents / total) * 100
        action_acc = (correct_actions / total) * 100

        print(f"\n[{model_name}]")
        print(f" -> Intent Accuracy: {intent_acc:.1f}%")
        print(f" -> Action/Escalation Accuracy: {action_acc:.1f}%")

if __name__ == "__main__":
    evaluate_all()
