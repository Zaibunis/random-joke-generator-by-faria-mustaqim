import streamlit as st
import requests

# Function to fetch a random joke
def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        response = requests.get("http://127.0.0.1:8000/pakistani_jokes")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch joke. Please try again later."
    except:
        return "Why did the programmer quit his job? \nBecause he didn't get array!"

# Main Streamlit App
def main():
    st.title("🤣 Pakistani Joke Generator!")
    st.write("Click the button below to generate a random joke:")

    if st.button("Tell me a joke?"):
        joke = get_random_joke()
        st.success(joke)

    # Adding a divider
    st.divider()

    # Custom HTML & CSS Styling Below Joke Generator
    st.markdown(
        """
        <style>
            .footer {
                text-align: center;
                margin-top: 50px;
                padding: 10px;
                font-size: 18px;
                font-weight: bold;
                color: white;
            }
            .footer a {
                color: #007bff;
                text-decoration: none;
                font-weight: bold;
            }
            .footer a:hover {
                text-decoration: underline;
            }
            .custom-container {
                text-align: center;
                background-color: #f9f9f9;
                padding: 15px;
                border-radius: 10px;
                margin-top: 20px;
                box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
            }
        </style>

        <div class='footer'>
            <p>Built with ❤️ by <a href="https://github.com/Zaibunis" target="_blank">Faria Khan</a> using Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Run the app
if __name__ == "__main__":
    main()
