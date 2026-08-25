import streamlit as st
from PIL import Image
from vehicle_detection import detect_vehicles


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Traffic Monitoring System",
    page_icon="🚦",
    layout="wide"
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🚦 Traffic Monitoring System")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Prediction", "Chatbot"]
)


# =========================================================
# HOME PAGE
# =========================================================

if page == "Home":

    st.title("🚦 YOLO-Based Traffic Monitoring System")

    st.write(
        """
        This project uses YOLO object detection to detect and count
        vehicles from uploaded traffic images.

        It also includes a Traffic Rules Chatbot that answers
        basic questions about traffic rules and road safety.
        """
    )

    st.subheader("🚀 Features")

    col1, col2 = st.columns(2)

    with col1:
        st.write("🚗 Car Detection")
        st.write("🏍️ Motorcycle Detection")

    with col2:
        st.write("🚌 Bus Detection")
        st.write("🚚 Truck Detection")

    st.write("🤖 Traffic Rules Chatbot")


# =========================================================
# PREDICTION PAGE
# =========================================================

elif page == "Prediction":

    st.title("🚗 Vehicle Detection")

    st.write(
        "Upload a JPG, JPEG, or PNG traffic image to detect vehicles."
    )

    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file).convert("RGB")

        st.subheader("📷 Uploaded Image")

        st.image(
            image,
            caption="Input Image",
            use_container_width=True
        )

        if st.button("🔍 Detect Vehicles"):

            with st.spinner("Detecting vehicles..."):

                result_image, counts = detect_vehicles(image)

            st.success("Detection completed!")

            st.subheader("🚦 Detected Vehicles")

            st.image(
                result_image,
                caption="YOLO Vehicle Detection",
                use_container_width=True
            )

            st.subheader("📊 Vehicle Count")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("🚗 Cars", counts["Car"])

            with col2:
                st.metric(
                    "🏍️ Motorcycles",
                    counts["Motorcycle"]
                )

            with col3:
                st.metric("🚌 Buses", counts["Bus"])

            with col4:
                st.metric("🚚 Trucks", counts["Truck"])


# =========================================================
# CHATBOT PAGE
# =========================================================

elif page == "Chatbot":

    st.title("🤖 Traffic Rules Chatbot")

    st.write(
        "Ask questions about traffic rules, traffic lights, "
        "road signs, helmets, seat belts and more."
    )

    question = st.text_input(
        "Ask your question:"
    )

    if question:

        q = question.lower().strip()


        # -------------------------------------------------
        # STOP SIGN
        # -------------------------------------------------

        if (
            "stop sign" in q
            or "what is stop sign" in q
            or "what does stop sign mean" in q
        ):

            answer = (
                "A STOP sign means you must come to a complete stop "
                "before proceeding. Check for pedestrians and other "
                "vehicles, then continue only when it is safe."
            )


        # -------------------------------------------------
        # RED LIGHT
        # -------------------------------------------------

        elif (
            "red light" in q
            or "red signal" in q
            or (
                "red" in q
                and "traffic" in q
            )
        ):

            answer = (
                "A red traffic light means STOP. You should stop "
                "before the stop line or pedestrian crossing and "
                "wait until the signal changes."
            )


        # -------------------------------------------------
        # YELLOW LIGHT
        # -------------------------------------------------

        elif (
            "yellow light" in q
            or "yellow signal" in q
            or (
                "yellow" in q
                and "traffic" in q
            )
        ):

            answer = (
                "A yellow traffic light warns that the signal may "
                "soon turn red. Slow down and stop if it is safe "
                "to do so."
            )


        # -------------------------------------------------
        # GREEN LIGHT
        # -------------------------------------------------

        elif (
            "green light" in q
            or "green signal" in q
            or (
                "green" in q
                and "traffic" in q
            )
        ):

            answer = (
                "A green traffic light generally means you may "
                "proceed, but only when the road is clear and "
                "it is safe to move."
            )


        # -------------------------------------------------
        # SPEED LIMIT
        # -------------------------------------------------

        elif (
            "speed limit" in q
            or "how fast" in q
            or "speed" in q
        ):

            answer = (
                "Speed limits depend on the type of road, vehicle "
                "and local traffic regulations. Always follow the "
                "speed limit shown on road signs."
            )


        # -------------------------------------------------
        # HELMET
        # -------------------------------------------------

        elif (
            "helmet" in q
            or "wear helmet" in q
        ):

            answer = (
                "Two-wheeler riders should wear a properly fastened "
                "protective helmet for safety and to comply with "
                "applicable traffic laws."
            )


        # -------------------------------------------------
        # SEAT BELT
        # -------------------------------------------------

        elif (
            "seat belt" in q
            or "seatbelt" in q
        ):

            answer = (
                "Drivers and passengers should wear seat belts. "
                "Seat belts help reduce the risk of serious injury "
                "during accidents."
            )


        # -------------------------------------------------
        # DRIVING LICENCE
        # -------------------------------------------------

        elif (
            "driving licence" in q
            or "driving license" in q
            or "licence" in q
            or "license" in q
        ):

            answer = (
                "A driver must have a valid driving licence or "
                "license appropriate for the type of vehicle "
                "they are driving."
            )


        # -------------------------------------------------
        # OVERTAKING
        # -------------------------------------------------

        elif (
            "overtake" in q
            or "overtaking" in q
            or "pass another vehicle" in q
        ):

            answer = (
                "Overtake only when it is legal and safe. Check "
                "your mirrors and blind spots, signal properly, "
                "and make sure the road ahead is clear."
            )


        # -------------------------------------------------
        # PARKING
        # -------------------------------------------------

        elif (
            "parking" in q
            or "where can i park" in q
            or "park vehicle" in q
        ):

            answer = (
                "Park only in permitted areas. Do not block traffic, "
                "pedestrian crossings, entrances, or emergency access."
            )


        # -------------------------------------------------
        # ROAD SIGNS
        # -------------------------------------------------

        elif (
            "road sign" in q
            or "road signs" in q
            or "traffic sign" in q
            or "sign meaning" in q
        ):

            answer = (
                "Road signs provide warnings, instructions, and "
                "important information to road users. Always follow "
                "the instructions shown on traffic signs."
            )


        # -------------------------------------------------
        # TRAFFIC RULES
        # -------------------------------------------------

        elif (
            "traffic rule" in q
            or "traffic rules" in q
            or "driving rules" in q
        ):

            answer = (
                "Basic traffic rules include obeying traffic signals "
                "and road signs, following speed limits, wearing "
                "required safety equipment, and driving carefully."
            )


        # -------------------------------------------------
        # ACCIDENT
        # -------------------------------------------------

        elif (
            "accident" in q
            or "crash" in q
        ):

            answer = (
                "After an accident, stop safely, check for injuries, "
                "contact emergency services if necessary, and follow "
                "the required legal and insurance procedures."
            )


        # -------------------------------------------------
        # PEDESTRIAN CROSSING
        # -------------------------------------------------

        elif (
            "pedestrian" in q
            or "zebra crossing" in q
            or "crosswalk" in q
        ):

            answer = (
                "Drivers should slow down and watch carefully for "
                "pedestrians. Give pedestrians priority where required "
                "and follow the traffic signals at crossings."
            )


        # -------------------------------------------------
        # GENERAL ROAD SAFETY
        # -------------------------------------------------

        elif (
            "road safety" in q
            or "drive safely" in q
            or "safe driving" in q
        ):

            answer = (
                "Safe driving includes following traffic rules, "
                "maintaining a safe speed and distance, avoiding "
                "distractions, and paying attention to other road users."
            )


        # -------------------------------------------------
        # UNKNOWN QUESTION
        # -------------------------------------------------

        else:

            answer = (
                "Sorry, I currently answer questions about STOP signs, "
                "traffic lights, speed limits, helmets, seat belts, "
                "driving licences, overtaking, parking, road signs, "
                "accidents, pedestrians and general traffic rules."
            )


        st.subheader("🤖 Answer")

        st.info(answer)