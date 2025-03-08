import streamlit as st
import random

def main():
    st.title("Number Guessing Game")
    
    # Sidebar: About the Developer
    st.sidebar.title("About the Developer")
    st.sidebar.write("**Name:** Fahad Khakwani")
    st.sidebar.write("**GitHub:** [GitHub Profile](https://github.com/yourusername)")
    st.sidebar.write("**LinkedIn:** [LinkedIn Profile](https://linkedin.com/in/yourusername)")
    st.sidebar.write("**Contact:** +1234567890")
    st.sidebar.write("**Email:** your.email@example.com")
    st.sidebar.write("**Version:** 1.0.1")
    
    # Ensure scores dictionary exists in session state
    if "scores" not in st.session_state:
        st.session_state.scores = {}
    
    username = st.text_input("Enter your name:", key="username")
    
    if username:
        if username not in st.session_state.scores:
            st.session_state.scores[username] = {
                "target_number": random.randint(1, 100),
                "attempts": 0,
                "game_over": False,
                "total_score": 0,
                "last_score": 0
            }
        
        user_data = st.session_state.scores[username]
        
        st.write("Guess a number between 1 and 50")
        
        guess = st.number_input("Enter your guess:", min_value=1, max_value=50, step=1, key=f"guess_{username}")
        
        if st.button("Submit Guess", key=f"submit_guess_{username}") and not user_data["game_over"]:
            user_data["attempts"] += 1
            
            if guess < user_data["target_number"]:
                st.warning("Too low! Try again.")
            elif guess > user_data["target_number"]:
                st.warning("Too high! Try again.")
            else:
                st.success(f"Congratulations {username}! You guessed the number in {user_data['attempts']} attempts.")
                user_data["game_over"] = True
                score = max(100 - user_data["attempts"] * 5, 0)
                user_data["total_score"] += score
                user_data["last_score"] = score
        
        if user_data["last_score"]:
            st.write(f"You earned {user_data['last_score']} points this round!")
        
        st.write(f"Total Score for {username}: {user_data['total_score']}")
        
        if user_data["game_over"]:
            if st.button("Play Again", key=f"play_again_{username}"):
                st.session_state.scores[username] = {
                    "target_number": random.randint(1, 100),
                    "attempts": 0,
                    "game_over": False,
                    "total_score": user_data["total_score"],
                    "last_score": 0
                }
                st.rerun()
    
    # Sidebar: Leaderboard
    st.sidebar.title("Leaderboard")
    if st.session_state.scores:
        sorted_scores = sorted(st.session_state.scores.items(), key=lambda x: x[1]["total_score"], reverse=True)
        for player, data in sorted_scores:
            st.sidebar.write(f"{player}: {data['total_score']} points")
    else:
        st.sidebar.write("No scores yet.")

if __name__ == "__main__":
    main()
