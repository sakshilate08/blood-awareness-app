
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Blood Awareness Community App",
    page_icon="🩸",
    layout="wide"
)

# ==========================================
# 2. FILE CONFIGURATION
# ==========================================

SURVEY_FILE = "community_blood_awareness.csv"

SURVEY_COLUMNS = [
    "Age Group",
    "Blood Group",
    "Hemoglobin Awareness",
    "Blood Donation Awareness",
    "Blood Donation Experience",
    "Hemoglobin Test Experience",
    "Awareness Source"
]


# ==========================================
# 3. SAMPLE DEMONSTRATION DATA
# ==========================================

SAMPLE_DATA = [
    {
        "Age Group": "18-25",
        "Blood Group": "O+",
        "Hemoglobin Awareness": "Yes",
        "Blood Donation Awareness": "Yes",
        "Blood Donation Experience": "Yes",
        "Hemoglobin Test Experience": "Yes",
        "Awareness Source": "Social Media"
    },
    {
        "Age Group": "26-35",
        "Blood Group": "B+",
        "Hemoglobin Awareness": "No",
        "Blood Donation Awareness": "Yes",
        "Blood Donation Experience": "No",
        "Hemoglobin Test Experience": "Yes",
        "Awareness Source": "Hospital"
    },
    {
        "Age Group": "18-25",
        "Blood Group": "A+",
        "Hemoglobin Awareness": "Yes",
        "Blood Donation Awareness": "No",
        "Blood Donation Experience": "No",
        "Hemoglobin Test Experience": "No",
        "Awareness Source": "College"
    },
    {
        "Age Group": "36-45",
        "Blood Group": "AB+",
        "Hemoglobin Awareness": "Yes",
        "Blood Donation Awareness": "Yes",
        "Blood Donation Experience": "Yes",
        "Hemoglobin Test Experience": "Yes",
        "Awareness Source": "Hospital"
    },
    {
        "Age Group": "26-35",
        "Blood Group": "O-",
        "Hemoglobin Awareness": "No",
        "Blood Donation Awareness": "No",
        "Blood Donation Experience": "No",
        "Hemoglobin Test Experience": "No",
        "Awareness Source": "Friends and Family"
    },
    {
        "Age Group": "46-60",
        "Blood Group": "B-",
        "Hemoglobin Awareness": "Yes",
        "Blood Donation Awareness": "Yes",
        "Blood Donation Experience": "Yes",
        "Hemoglobin Test Experience": "Yes",
        "Awareness Source": "Social Media"
    },
    {
        "Age Group": "18-25",
        "Blood Group": "O+",
        "Hemoglobin Awareness": "No",
        "Blood Donation Awareness": "Yes",
        "Blood Donation Experience": "No",
        "Hemoglobin Test Experience": "No",
        "Awareness Source": "College"
    },
    {
        "Age Group": "26-35",
        "Blood Group": "A-",
        "Hemoglobin Awareness": "Yes",
        "Blood Donation Awareness": "No",
        "Blood Donation Experience": "No",
        "Hemoglobin Test Experience": "Yes",
        "Awareness Source": "Hospital"
    },
    {
        "Age Group": "36-45",
        "Blood Group": "AB+",
        "Hemoglobin Awareness": "No",
        "Blood Donation Awareness": "Yes",
        "Blood Donation Experience": "Yes",
        "Hemoglobin Test Experience": "No",
        "Awareness Source": "Social Media"
    },
    {
        "Age Group": "18-25",
        "Blood Group": "B+",
        "Hemoglobin Awareness": "Yes",
        "Blood Donation Awareness": "Yes",
        "Blood Donation Experience": "No",
        "Hemoglobin Test Experience": "Yes",
        "Awareness Source": "College"
    },
    {
        "Age Group": "46-60",
        "Blood Group": "O-",
        "Hemoglobin Awareness": "Yes",
        "Blood Donation Awareness": "No",
        "Blood Donation Experience": "No",
        "Hemoglobin Test Experience": "Yes",
        "Awareness Source": "Hospital"
    },
    {
        "Age Group": "26-35",
        "Blood Group": "A+",
        "Hemoglobin Awareness": "Yes",
        "Blood Donation Awareness": "Yes",
        "Blood Donation Experience": "Yes",
        "Hemoglobin Test Experience": "Yes",
        "Awareness Source": "Friends and Family"
    },
    {
        "Age Group": "18-25",
        "Blood Group": "B-",
        "Hemoglobin Awareness": "No",
        "Blood Donation Awareness": "Yes",
        "Blood Donation Experience": "No",
        "Hemoglobin Test Experience": "No",
        "Awareness Source": "Social Media"
    },
    {
        "Age Group": "36-45",
        "Blood Group": "O+",
        "Hemoglobin Awareness": "Yes",
        "Blood Donation Awareness": "Yes",
        "Blood Donation Experience": "Yes",
        "Hemoglobin Test Experience": "Yes",
        "Awareness Source": "Hospital"
    },
    {
        "Age Group": "26-35",
        "Blood Group": "AB-",
        "Hemoglobin Awareness": "No",
        "Blood Donation Awareness": "No",
        "Blood Donation Experience": "No",
        "Hemoglobin Test Experience": "No",
        "Awareness Source": "College"
    }
]


# ==========================================
# 4. INITIALIZE SURVEY STORAGE
# ==========================================

if "survey_data" not in st.session_state:

    if os.path.exists(SURVEY_FILE):

        try:
            existing_df = pd.read_csv(SURVEY_FILE)

            # Add missing columns if an older CSV exists.
            for column in SURVEY_COLUMNS:
                if column not in existing_df.columns:
                    existing_df[column] = ""

            st.session_state.survey_data = (
                existing_df[SURVEY_COLUMNS].to_dict("records")
            )

        except (OSError, pd.errors.ParserError, UnicodeDecodeError):
            st.session_state.survey_data = SAMPLE_DATA.copy()

    else:
        # These records are fictional and for demonstration only.
        st.session_state.survey_data = SAMPLE_DATA.copy()


# ==========================================
# 5. BLOOD GROUP INFORMATION
# ==========================================

blood_groups = {
    "A+": {
        "description": "A antigen and Rh(D) antigen are present.",
        "donors": "A+, A-, O+, O-",
        "recipients": "A+, AB+"
    },
    "A-": {
        "description": "A antigen is present; Rh(D) antigen is absent.",
        "donors": "A-, O-",
        "recipients": "A-, A+, AB-, AB+"
    },
    "B+": {
        "description": "B antigen and Rh(D) antigen are present.",
        "donors": "B+, B-, O+, O-",
        "recipients": "B+, AB+"
    },
    "B-": {
        "description": "B antigen is present; Rh(D) antigen is absent.",
        "donors": "B-, O-",
        "recipients": "B-, B+, AB-, AB+"
    },
    "AB+": {
        "description": "A, B and Rh(D) antigens are present.",
        "donors": "All eight ABO/Rh groups",
        "recipients": "AB+"
    },
    "AB-": {
        "description": "A and B antigens are present; Rh(D) antigen is absent.",
        "donors": "AB-, A-, B-, O-",
        "recipients": "AB-, AB+"
    },
    "O+": {
        "description": "Neither A nor B antigen is present; Rh(D) antigen is present.",
        "donors": "O+, O-",
        "recipients": "O+, A+, B+, AB+"
    },
    "O-": {
        "description": "A, B and Rh(D) antigens are absent.",
        "donors": "O-",
        "recipients": "All eight ABO/Rh groups"
    }
}


# ==========================================
# 6. HEMOGLOBIN AWARENESS INFORMATION
# ==========================================

hemoglobin_info = {
    "What is Hemoglobin?": (
        "Hemoglobin is a protein found in red blood cells. "
        "It transports oxygen from the lungs to body tissues."
    ),

    "Importance of Hemoglobin": (
        "Hemoglobin helps supply oxygen to the body. "
        "Low levels may affect energy and normal body functions."
    ),

    "Possible Signs of Low Hemoglobin": (
        "Possible signs include tiredness, weakness, dizziness, "
        "pale skin and shortness of breath. Symptoms vary between people."
    ),

    "Possible Causes": (
        "Causes may include iron deficiency, vitamin deficiencies, "
        "blood loss and certain medical conditions."
    ),

    "Iron-Rich Foods": (
        "Examples include lentils, beans, chickpeas, leafy green vegetables "
        "and meat. Iron needs and absorption vary between individuals."
    ),

    "Other Important Nutrients": (
        "Vitamin B12 and folate are also needed for healthy red blood "
        "cell production."
    ),

    "Hemoglobin Testing": (
        "A complete blood count (CBC) includes a hemoglobin measurement. "
        "A healthcare professional can explain the results."
    ),

    "Prevention and Awareness": (
        "Eat a balanced diet, seek medical advice about concerning symptoms, "
        "and follow appropriate recommendations for blood testing."
    )
}


# ==========================================
# 7. QUIZ QUESTIONS
# ==========================================

quiz_questions = [
    {
        "question": "What is the main function of hemoglobin?",
        "options": [
            "Carry oxygen",
            "Digest food",
            "Produce hormones",
            "Control vision"
        ],
        "answer": "Carry oxygen"
    },
    {
        "question": "Which blood group is commonly called the universal red blood cell donor?",
        "options": ["A+", "AB+", "O-", "B-"],
        "answer": "O-"
    },
    {
        "question": "Which blood group is commonly called the universal red blood cell recipient?",
        "options": ["O-", "AB+", "A-", "B+"],
        "answer": "AB+"
    },
    {
        "question": "Which test commonly measures hemoglobin?",
        "options": ["CBC", "ECG", "EEG", "Vision test"],
        "answer": "CBC"
    },
    {
        "question": "Which nutrient is important for hemoglobin production?",
        "options": ["Iron", "Sodium", "Fluoride", "Iodine only"],
        "answer": "Iron"
    },
    {
        "question": "What does Rh-positive generally indicate?",
        "options": [
            "Rh(D) antigen is present",
            "Hemoglobin is high",
            "Iron deficiency is present",
            "Blood has no red cells"
        ],
        "answer": "Rh(D) antigen is present"
    },
    {
        "question": "Which blood cells contain hemoglobin?",
        "options": [
            "Red blood cells",
            "Platelets",
            "White blood cells",
            "Nerve cells"
        ],
        "answer": "Red blood cells"
    },
    {
        "question": "How is a person's ABO blood group determined?",
        "options": [
            "Blood typing test",
            "Height measurement",
            "Eye examination",
            "Blood pressure measurement"
        ],
        "answer": "Blood typing test"
    },
    {
        "question": "Which is an example of an iron-containing food?",
        "options": [
            "Lentils",
            "Sugar",
            "Soft drinks",
            "Table salt"
        ],
        "answer": "Lentils"
    },
    {
        "question": "Why is blood donation awareness important?",
        "options": [
            "To help maintain the availability of donated blood",
            "To remove the need for blood testing",
            "To guarantee that everyone can donate",
            "To replace all medical treatments"
        ],
        "answer": "To help maintain the availability of donated blood"
    },
    {
        "question": "Which blood component helps form clots?",
        "options": [
            "Platelets",
            "Hemoglobin",
            "Red cell antigens",
            "Oxygen"
        ],
        "answer": "Platelets"
    },
    {
        "question": "Can a quiz determine someone's actual blood group?",
        "options": [
            "Yes, by age",
            "Yes, by diet",
            "No, a blood typing test is needed",
            "Yes, by height"
        ],
        "answer": "No, a blood typing test is needed"
    }
]


# ==========================================
# 8. SIDEBAR NAVIGATION
# ==========================================

st.sidebar.title("🩸 Blood Awareness")

page = st.sidebar.radio(
    "Select a Section",
    [
        "Home",
        "Blood Group Information",
        "Hemoglobin Awareness",
        "Community Survey",
        "Awareness Quiz",
        "Survey Analytics"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "This application provides educational information "
    "about blood groups, hemoglobin and blood donation."
)


# ==========================================
# 9. HOME PAGE
# ==========================================

if page == "Home":

    st.title("🩸 Blood Group & Hemoglobin Awareness")
    st.subheader("Community Engagement Project")

    st.write(
        "Welcome to the Blood Awareness Application! "
        "This project helps people learn about blood groups, "
        "hemoglobin, blood donation and community health awareness."
    )

    st.markdown("---")

    df = pd.DataFrame(st.session_state.survey_data)

    total_responses = len(df)

    if not df.empty:
        awareness_rate = (
            df["Hemoglobin Awareness"].eq("Yes").mean() * 100
        )

        donation_rate = (
            df["Blood Donation Awareness"].eq("Yes").mean() * 100
        )
    else:
        awareness_rate = 0
        donation_rate = 0

    col1, col2, col3 = st.columns(3)

    col1.metric("Survey Responses", total_responses)
    col2.metric("Hemoglobin Awareness", f"{awareness_rate:.1f}%")
    col3.metric("Donation Awareness", f"{donation_rate:.1f}%")

    st.markdown("---")

    st.subheader("What can you do in this application?")

    st.write("🩸 Learn about all eight common ABO/Rh blood groups.")
    st.write("❤️ Explore hemoglobin and general health awareness.")
    st.write("📝 Participate in the community survey.")
    st.write("🧠 Test your knowledge with the awareness quiz.")
    st.write("📊 Explore survey charts and download the data.")

    st.info(
        "The initial survey records are fictional demonstration data. "
        "Replace them with genuine, consented survey responses "
        "before reporting community findings."
    )


# ==========================================
# 10. BLOOD GROUP INFORMATION PAGE
# ==========================================

elif page == "Blood Group Information":

    st.title("🩸 Blood Group Information")

    selected_group = st.selectbox(
        "Select your blood group to learn about it:",
        list(blood_groups.keys())
    )

    info = blood_groups[selected_group]

    st.subheader(f"Blood Group: {selected_group}")
    st.write("**Description:**", info["description"])

    st.write(
        "**Compatible red blood cell donors:**",
        info["donors"]
    )

    st.write(
        "**Compatible red blood cell recipients:**",
        info["recipients"]
    )

    st.markdown("---")

    st.subheader("Understanding Blood Groups")

    st.write(
        "**ABO system:** Blood groups are classified as A, B, AB or O "
        "according to the presence or absence of A and B antigens."
    )

    st.write(
        "**Rh system:** The plus (+) or minus (-) sign generally "
        "indicates whether the Rh(D) antigen is present or absent."
    )

    st.write(
        "**Red blood cell compatibility:** ABO/Rh compatibility is "
        "important for transfusion. Other antibodies and clinical "
        "testing must also be considered."
    )

    st.warning(
        "Compatibility information is for education only. "
        "Blood transfusions require professional testing and "
        "clinical supervision."
    )


# ==========================================
# 11. HEMOGLOBIN AWARENESS PAGE
# ==========================================

elif page == "Hemoglobin Awareness":

    st.title("❤️ Hemoglobin Awareness")

    st.write(
        "Learn about hemoglobin, its role in the body, "
        "possible signs of low levels and the importance of testing."
    )

    for topic, information in hemoglobin_info.items():

        with st.expander(topic):
            st.write(information)

    st.markdown("---")

    st.subheader("Healthy Lifestyle Awareness")

    st.write("🥗 Eat a balanced and varied diet.")
    st.write("🥬 Include suitable iron-containing foods.")
    st.write("🩺 Follow medical advice about blood tests.")
    st.write("💊 Do not take iron supplements without appropriate advice.")

    st.warning(
        "Hemoglobin reference ranges depend on factors such as age, "
        "sex, pregnancy, altitude and laboratory standards. "
        "This page is educational and cannot diagnose anemia."
    )


# ==========================================
# 12. COMMUNITY SURVEY PAGE
# ==========================================

elif page == "Community Survey":

    st.title("📝 Community Blood Awareness Survey")

    st.write(
        "Please answer the following questions to help understand "
        "community awareness about blood groups and hemoglobin."
    )

    st.info(
        "Do not enter your name, phone number, exact address, "
        "or other unnecessary personal information. "
        "Participation is voluntary."
    )

    with st.form("community_survey_form"):

        age_group = st.selectbox(
            "1. Select your age group",
            ["18-25", "26-35", "36-45", "46-60", "Above 60"]
        )

        blood_group = st.selectbox(
            "2. Do you know your blood group?",
            [
                "Unknown",
                "A+", "A-", "B+", "B-",
                "AB+", "AB-", "O+", "O-"
            ]
        )

        hemoglobin_awareness = st.radio(
            "3. Are you aware of hemoglobin?",
            ["Yes", "No"]
        )

        donation_awareness = st.radio(
            "4. Are you aware of blood donation?",
            ["Yes", "No"]
        )

        donation_experience = st.radio(
            "5. Have you ever donated blood?",
            ["Yes", "No", "Prefer not to say"]
        )

        test_experience = st.radio(
            "6. Have you ever had a hemoglobin test?",
            ["Yes", "No", "Prefer not to say"]
        )

        awareness_source = st.selectbox(
            "7. Where did you learn about blood health?",
            [
                "Social Media",
                "College",
                "Hospital",
                "Friends and Family",
                "Newspaper",
                "Awareness Campaign",
                "Other"
            ]
        )

        consent = st.checkbox(
            "I voluntarily agree to submit these survey answers."
        )

        submitted = st.form_submit_button("Submit Survey")

    if submitted:

        if not consent:
            st.error(
                "Please confirm that you voluntarily agree "
                "to submit your survey answers."
            )

        else:

            new_response = {
                "Age Group": age_group,
                "Blood Group": blood_group,
                "Hemoglobin Awareness": hemoglobin_awareness,
                "Blood Donation Awareness": donation_awareness,
                "Blood Donation Experience": donation_experience,
                "Hemoglobin Test Experience": test_experience,
                "Awareness Source": awareness_source
            }

            st.session_state.survey_data.append(new_response)

            try:
                updated_df = pd.DataFrame(
                    st.session_state.survey_data,
                    columns=SURVEY_COLUMNS
                )

                updated_df.to_csv(
                    SURVEY_FILE,
                    index=False,
                    encoding="utf-8"
                )

                st.success("Your survey response has been saved!")

                st.write(
                    "Total responses:",
                    len(st.session_state.survey_data)
                )

            except OSError as error:
                st.error(
                    "The response is in the current session, but "
                    f"the CSV file could not be saved: {error}"
                )


# ==========================================
# 13. AWARENESS QUIZ PAGE
# ==========================================

elif page == "Awareness Quiz":

    st.title("🧠 Blood Health Awareness Quiz")

    st.write(
        "Answer all 12 questions and submit the quiz "
        "to see your score."
    )

    with st.form("blood_quiz_form"):

        user_answers = []

        for index, question in enumerate(quiz_questions):

            st.markdown(
                f"**Question {index + 1}: {question['question']}**"
            )

            answer = st.radio(
                "Choose your answer:",
                question["options"],
                key=f"quiz_answer_{index}"
            )

            user_answers.append(answer)

        quiz_submitted = st.form_submit_button("Submit Quiz")

    if quiz_submitted:

        score = sum(
            user_answers[index] == question["answer"]
            for index, question in enumerate(quiz_questions)
        )

        st.session_state.quiz_score = score
        st.session_state.quiz_answers = user_answers

    if "quiz_score" in st.session_state:

        score = st.session_state.quiz_score
        total_questions = len(quiz_questions)

        st.markdown("---")
        st.subheader("Your Quiz Result")

        st.metric(
            "Your Score",
            f"{score} / {total_questions}"
        )

        st.progress(score / total_questions)

        percentage = (score / total_questions) * 100

        st.write(f"Percentage: {percentage:.1f}%")

        if score >= 10:
            st.success(
                "Excellent! You have a strong understanding "
                "of blood awareness."
            )

        elif score >= 6:
            st.info(
                "Good effort! Review the awareness information "
                "and try again."
            )

        else:
            st.warning(
                "Keep learning! Read the blood group and "
                "hemoglobin sections before trying again."
            )

        with st.expander("Review Your Answers"):

            for index, question in enumerate(quiz_questions):

                selected_answer = st.session_state.quiz_answers[index]
                correct_answer = question["answer"]

                st.write(
                    f"**Question {index + 1}:** "
                    f"{question['question']}"
                )

                st.write(f"Your answer: {selected_answer}")
                st.write(f"Correct answer: {correct_answer}")

                if selected_answer == correct_answer:
                    st.success("Correct answer")
                else:
                    st.error("Incorrect answer")

                st.markdown("---")


# ==========================================
# 14. SURVEY ANALYTICS PAGE
# ==========================================

elif page == "Survey Analytics":

    st.title("📊 Community Survey Analytics")

    df = pd.DataFrame(
        st.session_state.survey_data,
        columns=SURVEY_COLUMNS
    )

    if df.empty:

        st.info(
            "No survey responses are available. "
            "Submit a response on the Community Survey page."
        )

    else:

        st.subheader("Key Performance Indicators")

        total_responses = len(df)

        awareness_percent = (
            df["Hemoglobin Awareness"].eq("Yes").mean() * 100
        )

        donation_percent = (
            df["Blood Donation Awareness"].eq("Yes").mean() * 100
        )

        tested_percent = (
            df["Hemoglobin Test Experience"].eq("Yes").mean() * 100
        )

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        col1.metric(
            "Total Survey Responses",
            total_responses
        )

        col2.metric(
            "Hemoglobin Awareness",
            f"{awareness_percent:.1f}%"
        )

        col3.metric(
            "Blood Donation Awareness",
            f"{donation_percent:.1f}%"
        )

        col4.metric(
            "Reported Hemoglobin Testing",
            f"{tested_percent:.1f}%"
        )

        st.markdown("---")

        # Blood group distribution
        st.subheader("1. Blood Group Distribution")

        blood_counts = (
            df["Blood Group"]
            .replace("Unknown", pd.NA)
            .dropna()
            .value_counts()
        )

        if not blood_counts.empty:

            fig, ax = plt.subplots(figsize=(9, 4))

            blood_counts.plot(
                kind="bar",
                ax=ax,
                color="steelblue"
            )

            ax.set_xlabel("Blood Group")
            ax.set_ylabel("Number of Responses")
            ax.set_title("Blood Group Distribution")
            ax.tick_params(axis="x", rotation=0)

            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)

        else:
            st.info("No known blood groups have been recorded.")

        # Hemoglobin awareness
        st.subheader("2. Hemoglobin Awareness")

        hemoglobin_counts = df[
            "Hemoglobin Awareness"
        ].value_counts()

        fig, ax = plt.subplots(figsize=(7, 4))

        hemoglobin_counts.plot(
            kind="bar",
            ax=ax,
            color="seagreen"
        )

        ax.set_xlabel("Awareness")
        ax.set_ylabel("Number of Responses")
        ax.set_title("Hemoglobin Awareness")
        ax.tick_params(axis="x", rotation=0)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

        # Blood donation awareness
        st.subheader("3. Blood Donation Awareness")

        donation_counts = df[
            "Blood Donation Awareness"
        ].value_counts()

        fig, ax = plt.subplots(figsize=(7, 4))

        donation_counts.plot(
            kind="bar",
            ax=ax,
            color="darkorange"
        )

        ax.set_xlabel("Awareness")
        ax.set_ylabel("Number of Responses")
        ax.set_title("Blood Donation Awareness")
        ax.tick_params(axis="x", rotation=0)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

        # Age group distribution
        st.subheader("4. Age Group Distribution")

        age_counts = df["Age Group"].value_counts()

        fig, ax = plt.subplots(figsize=(8, 4))

        age_counts.plot(
            kind="bar",
            ax=ax,
            color="mediumpurple"
        )

        ax.set_xlabel("Age Group")
        ax.set_ylabel("Number of Responses")
        ax.set_title("Survey Participants by Age Group")
        ax.tick_params(axis="x", rotation=0)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

        # Awareness sources
        st.subheader("5. Sources of Awareness")

        source_counts = df[
            "Awareness Source"
        ].value_counts()

        fig, ax = plt.subplots(figsize=(9, 4))

        source_counts.plot(
            kind="bar",
            ax=ax,
            color="teal"
        )

        ax.set_xlabel("Awareness Source")
        ax.set_ylabel("Number of Responses")
        ax.set_title("Where Participants Learn About Blood Health")
        ax.tick_params(axis="x", rotation=25)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

        # Survey records
        st.markdown("---")
        st.subheader("Community Survey Records")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        # Download survey data
        csv_data = df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="📥 Download Survey Data (CSV)",
            data=csv_data,
            file_name="community_blood_awareness.csv",
            mime="text/csv"
        )

        st.caption(
            "Charts show recorded survey responses, not "
            "population-level estimates."
        )


# ==========================================
# 15. FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Blood Group & Hemoglobin Awareness Community Engagement Project"
)

st.caption(
    "Educational use only. This application does not provide "
    "medical diagnosis or replace professional advice."
)