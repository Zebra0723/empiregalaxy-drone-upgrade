import streamlit as st
import pandas as pd

st.set_page_config(page_title="EmpireGalaxy: DJI Neo Upgrade Command", page_icon="🕸")

st.title("🕸 EmpireGalaxy: DJI Neo Upgrade Command")

st.markdown("## Persuade your parents to upgrade from the Mini 3 to the DJI Neo!")

st.markdown("This interactive app compares the costs, features and benefits of repairing the DJI Mini 3 versus buying the DJI Neo Motion Fly More Combo. Use this to make a convincing case!")

# Cost comparison table
cost_data = {
    "Option": ["Repair Mini 3", "Buy DJI Neo Motion Combo", "Build Your Own (Neo + RC Motion 3 + Goggles N3)"],
    "Estimated Cost": ["\u00a3300–\u00a3450", "\u00a3365–\u00a3445", "\u00a3451–\u00a3468"],
    "What you get": [
        "Fixed old drone",
        "New drone + Motion controller + Goggles N3 + 3 batteries + hub",
        "Neo + Motion controller + Goggles N3 separate purchases"
    ]
}

df_cost = pd.DataFrame(cost_data)

with st.expander("\ud83d\udcb0 Compare Costs"):
    st.write("Here's how repairing the Mini 3 stacks up against buying the Neo Combo:")
    st.table(df_cost)

# Feature comparison table
feature_data = {
    "Feature": ["Voice control", "Gesture control", "Motion controller", "FPV goggles", "Propeller guards", "Flight time", "Camera sensor"],
    "Neo Combo": ["Yes", "Yes", "Included", "Included", "Built-in", "~20 min", "1/2.3\" 12 MP"],
    "Mini 3": ["No", "No", "No", "Not supported", "Extra accessory", "~38 min", "1/1.3\" 12 MP"]
}

df_feat = pd.DataFrame(feature_data)

with st.expander("\u2728 Feature Comparison"):
    st.write("See the differences between the Neo Combo and the Mini 3:")
    st.table(df_feat)

# Decision form
st.markdown("## \ud83c\udfc1 Ready to Decide?")
status = st.selectbox("What's your current drone situation?", [
    "Broken Mini 3 (ESC damage)",
    "Partially working Mini 3",
    "No drone"
])
choice = st.radio("Choose your path:", ["Repair the Mini 3", "Buy the Neo Motion Combo"])

if choice == "Buy the Neo Motion Combo":
    st.success("Great choice! You'll get a brand-new drone with immersive FPV goggles, voice control and motion controller. Plus, it's safer with built-in guards and has 3 batteries for extended flights.")
    st.balloons()
else:
    st.warning("Repairing the Mini 3 means spending money on old tech without gaining new features. Make sure you really want to keep the older drone.")

st.markdown("---")
st.markdown("### \ud83c\udf89 Final Persuasion Tips")
st.markdown(
    """
    - **Emphasize value:** The Neo Combo costs about the same as repairing your Mini 3 but comes with new tech and extra batteries.
    - **Highlight safety:** Propeller guards and auto-return features mean fewer accidents and more peace of mind.
    - **Include everyone:** Invite your parents to try the goggles and experience flying firsthand.
    - **Show the future:** Voice commands and motion control are the next generation of drones—why stay in the past?
    """
)
