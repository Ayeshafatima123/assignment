import streamlit as st
import math

class ScientificCalculator:
    def __init__(self):
        self.value = 0

    def calculate(self, expression):
        try:
            # Replace special operators
            expression = expression.replace("^", "**")
            self.value = eval(expression)
        except Exception:
            self.value = "Error"

    def sqrt(self, number):
        return math.sqrt(number)

    def log(self, number):
        return math.log10(number)

    def get_result(self):
        return self.value

def main():
    st.title("🔬 Scientific Calculator")

    expr = st.text_input("Enter expression (e.g. 2^3, 4+5*6):")
    calc = ScientificCalculator()

    if st.button("Calculate"):
        calc.calculate(expr)
        st.success(f"Result: {calc.get_result()}")

    st.write("---")
    st.subheader("Quick Functions")
    number = st.number_input("Enter number for sqrt/log:", value=1.0)

    if st.button("√ Square Root"):
        st.info(f"√{number} = {calc.sqrt(number)}")

    if st.button("log₁₀"):
        st.info(f"log₁₀({number}) = {calc.log(number)}")

if __name__ == "__main__":
    main()
