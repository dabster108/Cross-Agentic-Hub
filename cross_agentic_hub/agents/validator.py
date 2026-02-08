class ValidatorAgent:
    """Validates / fixes code (placeholder for now)"""
    def validate(self, code):
        if len(code) > 0:
            return {"status": "success", "message": "Code generated correctly."}
        else:
            return {"status": "error", "message": "Code is empty."}
