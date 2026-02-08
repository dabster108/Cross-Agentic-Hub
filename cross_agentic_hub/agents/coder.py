class CoderAgent:
    """Generates code based on plan"""
    def generate_code(self, plan):
        code = "\n".join([f"# Step: {step}" for step in plan])
        code += "\n\nprint('Hello from CrossAgenticHub!')"
        return code
