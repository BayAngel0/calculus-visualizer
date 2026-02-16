import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Calculus Visualizer", layout="centered")

st.title("📈 Interactive Calculus Visualizer")
st.markdown("Visualize a function along with its first and second derivatives.")

st.markdown("### Enter a function of x")
st.markdown("Examples:")
st.code("x**3 - 4*x**2 + np.sin(x)")
st.code("np.exp(-x/3) + np.log(x+6)")
st.code("np.sin(x) * x**2")

function_input = st.text_input("f(x) =", "x**3")

st.markdown("### Select X Range")

col1, col2 = st.columns(2)
with col1:
    x_min = st.number_input("Minimum X", value=-10.0)
with col2:
    x_max = st.number_input("Maximum X", value=10.0)

if st.button("Plot Function"):

    try:
        x = np.linspace(x_min, x_max, 2000)

        # Evaluate function safely
        allowed_names = {
            "x": x,
            "np": np
        }

        y = eval(function_input, {"__builtins__": {}}, allowed_names)

        # Numerical derivatives
        h = 1e-5
        allowed_names_h1 = {"x": x + h, "np": np}
        allowed_names_h2 = {"x": x - h, "np": np}

        y_plus = eval(function_input, {"__builtins__": {}}, allowed_names_h1)
        y_minus = eval(function_input, {"__builtins__": {}}, allowed_names_h2)

        y_prime = (y_plus - y_minus) / (2 * h)
        y_double_prime = (y_plus - 2*y + y_minus) / (h**2)

        # Plotting
        fig, ax = plt.subplots()
        ax.plot(x, y, label="f(x)")
        ax.plot(x, y_prime, label="f'(x)")
        ax.plot(x, y_double_prime, label="f''(x)")
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)

    except Exception as e:
        st.error("Invalid function. Please check your syntax.")