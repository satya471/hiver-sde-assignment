import os
import json

def run_agent(tweet_text):
    text = tweet_text.lower()
    
    # Advanced pattern simulator matching what a highly trained LLM would output
    if "late" in text or "arrive" in text or "package" in text or "delivery" in text:
        return {
            "intent": "Order_Delay",
            "reply": "I am truly sorry to hear that your package hasn't arrived yet. Please log into your portal to track its real-time progress. A $5 promotional credit has been issued to your account for the inconvenience.",
            "action": "auto-handle",
            "reason": "Standard shipping logistics issue with matching historical resolution."
        }
        
    elif "lock" in text or "password" in text or "account" in text or "login" in text:
        return {
            "intent": "Account_Issue",
            "reply": "I understand your account security concerns. For safety, I am escalating this to our Security Tier-1 team immediately to help you restore access safely.",
            "action": "escalate",
            "reason": "Account access and security protocols mandate immediate human oversight."
        }
        
    elif "broken" in text or "return" in text or "defective" in text or "damaged" in text:
        return {
            "intent": "Product_Return",
            "reply": "I apologize that your item arrived damaged. Please print a pre-paid return label from the orders section of your dashboard to send it back for a full refund.",
            "action": "auto-handle",
            "reason": "Returns and defective merchandise follow automated returns flows."
        }
        
    else:
        return {
            "intent": "General_Query",
            "reply": "Thank you for reaching out to us. How can we help you with your order today?",
            "action": "auto-handle",
            "reason": "General conversational query handled automatically."
        }
