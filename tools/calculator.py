class CalculatorTool:

    def calculate(self, expression: str) -> str:
        try:
            # Safe eval - only math operations allowed
            allowed = set("0123456789+-*/(). ")
            if not all(c in allowed for c in expression):
                return "Invalid Expression"
            result = eval(expression)  # noqa: S307
            return str(result)
        except Exception:
            return "Invalid Expression"