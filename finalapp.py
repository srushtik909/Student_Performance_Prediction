import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Function to simulate final score prediction
def predict_final_score(inputs):
    return np.clip(np.random.randint(50, 100), 0, 100)  # Simulated model prediction

# Streamlit UI
st.set_page_config(layout="wide", page_title="Student Performance Dashboard", page_icon="🎓")
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 Student Performance Prediction Dashboard")

# Create layout with two columns
col1, col2 = st.columns([1, 2])

with col1:
    st.header("📌 Enter Student Data")
    study_time = st.number_input("Study Time (hours)", min_value=0, max_value=100, value=40)
    num_absences = st.number_input("Number of Absences", min_value=0, max_value=50, value=4)
    past_scores = st.number_input("Past Scores (%)", min_value=0, max_value=100, value=88)
    online_courses = st.number_input("Online Courses Completed", min_value=0, max_value=20, value=3)
    assignment_completion = st.number_input("Assignment Completion Rate (%)", min_value=0, max_value=100, value=66)
    social_media_hours = st.number_input("Time Spent on Social Media (hours/week)", min_value=0, max_value=100, value=14)
    
    predict_button = st.button("Predict Final Score")

with col2:
    if predict_button:
        predicted_score = predict_final_score({
            "study_time": study_time,
            "num_absences": num_absences,
            "past_scores": past_scores,
            "online_courses": online_courses,
            "assignment_completion": assignment_completion,
            "social_media_hours": social_media_hours
        })
        
        # Gauge Chart with Proper Indicator
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=predicted_score,
            title={"text": "Predicted Final Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "blue"},
                "steps": [
                    {"range": [0, 50], "color": "red"},
                    {"range": [50, 75], "color": "yellow"},
                    {"range": [75, 100], "color": "green"}
                ],
                "threshold": {
                    "line": {"color": "white", "width": 4},
                    "thickness": 0.75,
                    "value": predicted_score
                }
            }
        ))

        st.plotly_chart(fig)

        # Pie Chart
        labels = ["Study Time", "Number of Absences", "Past Scores", "Online Courses Completed", 
                  "Assignment Completion Rate", "Time Spent on Social Media"]
        values = [study_time, num_absences, past_scores, online_courses, assignment_completion, social_media_hours]
        pie_chart = px.pie(names=labels, values=values, title="Student Data Distribution")
        
        st.plotly_chart(pie_chart)
        
        # Line Chart (Past Scores vs Predicted Final Score)
        line_chart = px.line(x=["Past Scores", "Predicted Final Score"], 
                             y=[past_scores, predicted_score], 
                             title="Past Scores vs Predicted Final Score",
                             markers=True)
        st.plotly_chart(line_chart)
        
        # Bar Chart
        bar_labels = ["Study Time", "Time Spent on Social Media", "Assignment Completion Rate", "Online Courses", "Number of Absences"]
        bar_values = [study_time, social_media_hours, assignment_completion, online_courses, num_absences]
        bar_chart = px.bar(x=bar_labels, y=bar_values, title="Student Data Comparison", color=bar_values, color_continuous_scale="Viridis")
        st.plotly_chart(bar_chart) 
        
        st.success("✅ Dashboard is ready! 🚀")
