from utils.helpers import call_mistral

class ValidatorAgent:
    def validate(self, code):
        prompt = f"Check if this code is correct and provide fixes if needed:\n{code}"
        validation = call_mistral(prompt)
        return validation
