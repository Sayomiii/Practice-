
import json

# Open the JSON file and convert its contents to a Python dictionary.
with open("feedback.json", "r", encoding="utf-8") as file:
    feedback = json.load(file)

# Access individual fields.
feedback_id = feedback["feedback_id"]
text = feedback["text"]
source = feedback["source"]
include_summary = feedback["include_summary"]

# Display the values.
print("Feedback ID:", feedback_id)
print("Text:", text)
print("Source:", source)
print("Include summary:", include_summary)
