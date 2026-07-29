import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(
    page_title="Mango Disease Prediction",
    page_icon="🥭",
    layout="wide"
)

def set_bg():
    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(
            rgba(245,255,245,0.92),
            rgba(230,255,230,0.92)
        );
    }

    .main-title {
        text-align:center;
        color:#1B5E20;
        font-size:42px;
        font-weight:bold;
    }

    .sub-title {
        text-align:center;
        color:#2E7D32;
        font-size:20px;
    }

    .card {
        background:white;
        padding:20px;
        border-radius:15px;
        box-shadow:0px 4px 10px rgba(0,0,0,0.15);
        margin-bottom:15px;
    }

    </style>
    """, unsafe_allow_html=True)

set_bg()

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "🏠 Home",
        "🦠 Disease Description",
        "📊 Disease Prediction",
        "👨‍💻 About Us"
    ]
)

if menu == "🏠 Home":

    # ==============================
    # HOME PAGE
    # ==============================

    st.markdown(
        """
        <h1 style='text-align:center;color:#1B5E20;'>
        🥭 Mango Disease Prediction
        </h1>

        <h4 style='text-align:center;color:#555555;'>
        AI-powered prediction of major mango diseases using weather,
        historical disease severity and machine learning models.
        </h4>

        <hr style="border:1px solid #D8EFD3;">
        """,
        unsafe_allow_html=True
    )
    st.image("home.jpg", use_container_width=True)
    # ==============================
    # INFORMATION CARDS
    # ==============================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.success("### 📅 Forecast\n\n**1 Week Ahead**")

    with col2:
        st.info("### 🌦 Weather\n\nRF • RD • RH • Temperature")

    with col3:
        st.warning("### 🦠 Diseases\n\n5 Major Diseases")


    st.write("")
    st.write("")

    # ==============================
    # OBJECTIVES & DISEASES
    # ==============================

    left, right = st.columns([1.3,1])

    with left:

        st.subheader("🎯 Objectives")

        st.markdown("""
        ✅ Early disease warning

        ✅ Weather-based disease prediction

        ✅ Disease risk assessment

        ✅ Decision support for farmers

        ✅ One-week-ahead prediction
        """)

    with right:

        st.subheader("🦠 Diseases Covered")

        st.markdown("""
        🟢 Leaf Anthracnose

        ⚫ Black Banded

        🔴 Red Rust

        🟤 Die Back

        ⚪ Sooty Mould
        """)

    st.divider()

    # ==============================
    # HOW IT WORKS
    # ==============================

    st.subheader("⚙️ How It Works")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.info("🌦\n\nWeather Data")

    with c2:
        st.info("📈\n\nHistorical Disease")

    with c3:
        st.info("🤖\n\nMachine Learning")

    with c4:
        st.success("📊\n\nDisease Prediction")

    st.divider()

    # ==============================
    # ABOUT
    # ==============================

    st.subheader("📖 About the System")

    st.write(
        """
This application predicts the severity of major mango diseases one week in advance
using weather parameters, historical disease severity, and machine learning models.
The system supports early disease warning and timely disease management decisions
for sustainable mango production.
        """
    )

    st.divider()

    st.caption(
        "Developed by **Mr. K. Kathirvel M.** | "
        "M.Sc. in Agricultural Statistics | "
        "Tamil Nadu Agricultural University"
    )

elif menu == "🦠 Disease Description":

    st.title("🦠 Mango Disease Description")

    disease_info = st.selectbox(
        "Select Disease",
        [
            "Leaf Anthracnose",
            "Black Banded",
            "Red Rust",
            "Die Back",
            "Sooty Mould"
        ],
        key="disease_description"
    )

    if disease_info == "Leaf Anthracnose":
       
        st.markdown("""
        ### Leaf Anthracnose - Colletotrichum gloeosporioides

        **Pathogen:** 
        - Mycelium: Hyaline, septate. Acervull (Asexual fruiting body) produced on twigs only have setae.
        - Conidiophores: Hyaline, short and aseptate.
        - Conidia: Hyaline, single celled, cylindrical shaped with two oil granules.


        **Symptoms:**
        - Observed on leaves, tender shoots, panicles and fruits.
        - Leaves show black spots with grey centre. Affected portion, fall off and exhibit ragged appearance. Severely diseased leaves fall off leaving the barren twigs.
        - Twigs show dark brown lesions, which will enlarge and results in die - back/twig blight.
        - Flowers show necrosis, withering and shedding (blossom blight / panicle anthracnose). Colour of the blighted flowers become brown to black.
        """)

    elif disease_info == "Black Banded":

        st.markdown("""
        ### Black Banded - Rhinocladium corticolum

        **Symptoms:**
        - Black banded disease is characterized by the development of black, velvety or felt-like fungal growth on the midribs of leaves, bark of twigs, branches, and trunks. 
        - The fungal growth gradually enlarges and forms distinct black bands that may encircle twigs, branches, and larger limbs.
        - The disease commonly develops on colonies of scale insects, which provide a favourable substrate for fungal growth.
        - Although the fungus does not directly kill branches or twigs, it produces a conspicuous black-banded appearance that reduces the aesthetic quality of the tree and can interfere                  with normal growth when severe.
        - The characteristic black bands on affected plant parts are the key diagnostic symptom, giving the disease its name "Black Banded Disease."
        """)

    elif disease_info == "Red Rust":

        st.markdown("""
        ### Red Rust - Cephaleuros virescens

        **Pathogen:** 
        - Upper surface of the spots comprise of the sporangiophores and sterile hairs.
        - Sterile hairs: Orange and pointed.
        - Sporangia: Thick, orange and 2 types. Sessile sporangia develop directly on the thallus.
        - Pedicellate sporangia (3-6) borne on swollen vesicle present at the tip of rigid and septate sporangiophore.


        **Symptoms:**
        - Circular slightly raised red rusty velvety spots on the leaves and young twigs.
        - Later spots become cream to white velvet texture.
        - Reduction in photosynthetic activity and defoliation lowers the vitality of the host plant.
        """)

    elif disease_info == "Die Back":

        st.markdown("""
        ### Die Back - Lasioditlobla theobromae

        **Pathogen:**        
        - Lasioditlobla theobromae produces pycnidia as its asexual fruiting body.
        - Pycnidiospores: Hyaline, bl called with longitudinal striations in Lasiodiplodia. But Diplodia produces hyaline, thin aseptate
        - Pycnidiospores and olive brown, thick, bi-celled pycnidiospores with 4-6 longitudinal striations.


        **Symptoms:**
        - Affects twigs, branches, panicles, and fruits.
        - Bark darkens from the tip of young twigs and spreads to leaves.
        - Leaves turn brown, curl upward, and eventually fall, giving a scorched appearance.
        - Twigs and branches gradually dry from the tip downward (die-back).
        """)

    elif disease_info == "Sooty Mould":
      
        st.markdown("""
        ### Sooty Mould - Capnodium mangiferae

        **Pathogen:** 
        - Fungus produces 5 types of conidia such Torula, Trichothecium,  Coniothecium, Brachysporium,nAscospores from Pseudothecia
     
    
        **Symptoms:**
        - Black, superficial sooty fungal growth develops on leaves, stems, flowers, and fruits.
        - Reduces the photosynthetic efficiency of the plant.
        - Infection during flowering leads to poor fruit set.
        - Diseased fruits have poor market quality and reduced economic value.
        - The fungus grows on the sugary honeydew secretions produced by mango hoppers, scale insects, coccids, and mealybugs.
        - Disease incidence is more severe in old, dense orchards with low light intensity.
        - Trees located in the center of orchards are generally more affected than those on the eastern side.	      
        """)

elif menu == "📊 Disease Prediction":

    st.title("📊 Disease Prediction")

    disease = st.selectbox(
        "Select Disease",
        [
            "Leaf Anthracnose",
            "Black Banded",
            "Red Rust",
            "Die Back",
            "Sooty Mould"
        ],
        key="disease_prediction"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Weather Parameters")

        rf = st.number_input(
            "Rainfall (RF) mm",
            min_value=0.0,
            value=25.0
        )

        rd = st.number_input(
            "Rainy Days (RD)",
            min_value=0,
            value=2
        )

        rh = st.number_input(
            "Humidity (RH) %",
            min_value=0.0,
            max_value=100.0,
            value=80.0
        )

        tmax = st.number_input(
            "Maximum Temperature (°C)",
            value=34.0
        )

        tmin = st.number_input(
            "Minimum Temperature (°C)",
            value=25.0
        )

    with col2:
        st.subheader("Field Parameters")

        current_disease = st.number_input(
            "Current Disease Severity (%)",
            min_value=0.0,
            max_value=100.0,
            value=15.0
        )

        week = st.number_input(
            "Week Number (1-52)",
            min_value=1,
            max_value=52,
            value=24
        )

    model_files = {
        "Leaf Anthracnose": "LEAF ANTHRACNOSE_farmer_forecast.pkl",
        "Black Banded": "BLACK_BANDED_farmer_forecast.pkl",
        "Red Rust": "RED RUST_farmer_forecast.pkl",
        "Die Back": "DIE BACK_farmer_forecast.pkl",
        "Sooty Mould": "SOOTY MOULD_farmer_forecast.pkl"
    }

    if st.button("Predict Disease Risk", key="forecast_button"):

        try:

            T_avg = (tmax + tmin) / 2
            T_Range = tmax - tmin

            week_sin = np.sin(2 * np.pi * week / 52)
            week_cos = np.cos(2 * np.pi * week / 52)

            input_data = pd.DataFrame([[
                rf,
                rd,
                rh,
                tmax,
                tmin,
                T_avg,
                T_Range,
                current_disease,
                week_sin,
                week_cos
            ]], columns=[
                "RF",
                "RD",
                "RH",
                "T_MAX",
                "T_MIN",
                "T_avg",
                "T_Range",
                "DISEASE",
                "week_sin",
                "week_cos"
            ])

            model_file = model_files[disease]

            if not os.path.exists(model_file):
                st.error(f"Model file not found: {model_file}")
                st.stop()

            model = joblib.load(model_file)

            forecast = float(model.predict(input_data)[0])

            if forecast < 20:
                risk = "🟢 Low"
                advice = "Routine monitoring is sufficient."

            elif forecast < 40:
                risk = "🟡 Moderate"
                advice = "Inspect orchard regularly."

            elif forecast < 60:
                risk = "🟠 High"
                advice = "Start disease management measures."

            else:
                risk = "🔴 Epidemic"
                advice = "Immediate control measures required."

            st.success("Forecast Completed")

            st.metric(
                "Predicted Disease Severity (%)",
                f"{forecast:.2f}"
            )

            st.subheader("Risk Assessment")
            st.write(f"**Risk Level:** {risk}")
            st.write(f"**Recommendation:** {advice}")

        except Exception as e:
            st.error(str(e))

elif menu == "👨‍💻 About Us":

    st.title("👨‍💻 About Us")

    st.markdown("""
    ## 🥭 Mango Disease Prediction

    This web application was developed to predict major mango diseases
    using weather parameters and machine learning techniques. The system
    provides an early warning to support timely disease management and
    improve decision-making in mango cultivation.

    ### 👨‍🎓 Developer

    **Mr. Kathirvel M.**

    PG Student, Agricultural Statistics

    Department of Physical Sciences and Information Technology

    Agricultural Engineering College and Research Institute

    Tamil Nadu Agricultural University (TNAU)

    Coimbatore – 641003, Tamil Nadu, India

    ---

    ### 👨‍🔬 Scientific Guidance

    **Dr. S. Muthuramalingam**

    Associate Professor (Horticulture)

    Department of Fruit Science

    Horticultural College and Research Institute

    Tamil Nadu Agricultural University (TNAU)

    Periyakulam – 625604, Tamil Nadu, India

    <br>

    **Dr. A. Vijayasamundeeswari**

    Associate Professor (Plant Pathology)

    Department of Fruit Science

    Horticultural College and Research Institute

    Tamil Nadu Agricultural University (TNAU)

    Periyakulam – 625604, Tamil Nadu, India

    📧 vijayasamundeeswari.a@tnau.ac.in

    ---

    ### 📍 Study Area

    Theni District, Tamil Nadu, India

    ---

    ### 🙏 Acknowledgement

    The developer gratefully acknowledges the **ICAR – All India Coordinated Research Project (AICRP) on Fruits**,
    Department of Fruit Science, Horticultural College and Research Institute,
    Tamil Nadu Agricultural University, Periyakulam, for providing the
    long-term research data used in developing and validating this
    Mango Disease Prediction.

    ---


    ### 🎯 Purpose

    To provide an early warning system for major mango disease outbreaks
    by integrating weather parameters and machine learning models, thereby
    supporting farmers, researchers, and extension personnel in making
    timely disease management decisions.
    """)