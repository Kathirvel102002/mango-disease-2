import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(
    page_title="Mango Disease Forecast System",
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

    # =========================
    # HERO BANNER
    # =========================

    st.markdown("""
    <style>

    .hero{
        position:relative;
        height:430px;
        border-radius:20px;
        overflow:hidden;
        margin-bottom:35px;
        background-image:
        linear-gradient(rgba(0,0,0,.45),rgba(0,0,0,.45)),
        url("https://github.com/Kathirvel102002/mango-disease-2/blob/main/home.jpg");
        background-size:cover;
        background-position:center;
    }

    .hero-text{
        position:absolute;
        left:50%;
        top:50%;
        transform:translate(-50%,-50%);
        text-align:center;
        color:white;
        width:85%;
    }

    .hero-title{
        font-size:52px;
        font-weight:700;
        margin-bottom:15px;
    }

    .hero-sub{
        font-size:22px;
        line-height:1.6;
    }

    .section-title{
        font-size:32px;
        font-weight:bold;
        color:#1B5E20;
        margin-top:20px;
        margin-bottom:15px;
    }

    .feature-card{
        background:white;
        border-radius:18px;
        padding:25px;
        text-align:center;
        box-shadow:0 5px 18px rgba(0,0,0,.12);
        border-top:5px solid #2E7D32;
        transition:0.3s;
        height:170px;
    }

    .feature-card:hover{
        transform:translateY(-6px);
    }

    .feature-icon{
        font-size:42px;
    }

    .feature-title{
        font-size:20px;
        font-weight:bold;
        margin-top:10px;
        color:#1B5E20;
    }

    .feature-text{
        color:#555;
        font-size:16px;
    }

    .box{
        background:white;
        border-radius:18px;
        padding:25px;
        box-shadow:0 5px 18px rgba(0,0,0,.10);
    }

    .disease{
        display:inline-block;
        padding:10px 18px;
        margin:8px;
        border-radius:25px;
        background:#E8F5E9;
        color:#1B5E20;
        font-weight:bold;
        font-size:17px;
    }

    .footer{
        text-align:center;
        color:#666;
        margin-top:40px;
        padding-top:20px;
        border-top:1px solid #DDD;
        font-size:16px;
    }

    </style>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="hero">

        <div class="hero-text">

            <div class="hero-title">
            🥭 Mango Disease Forecast System
            </div>

            <div class="hero-sub">
            AI-powered prediction of major mango diseases using weather,
            historical disease severity and machine learning techniques.
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


    # =========================
    # INFORMATION CARDS
    # =========================

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="feature-card">
        <div class="feature-icon">📅</div>
        <div class="feature-title">Forecast Horizon</div>
        <div class="feature-text">
        One Week Ahead
        </div>
        </div>
        """,unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
        <div class="feature-icon">🌦</div>
        <div class="feature-title">Weather Inputs</div>
        <div class="feature-text">
        RF • RD • RH • Temperature
        </div>
        </div>
        """,unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
        <div class="feature-icon">🦠</div>
        <div class="feature-title">Diseases Covered</div>
        <div class="feature-text">
        Five Major Mango Diseases
        </div>
        </div>
        """,unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">Machine Learning</div>
        <div class="feature-text">
        Random Forest Prediction
        </div>
        </div>
        """,unsafe_allow_html=True)



    st.markdown("<br>",unsafe_allow_html=True)



    left,right = st.columns([1.2,1])

    with left:

        st.markdown('<div class="box">',unsafe_allow_html=True)

        st.markdown('<div class="section-title">🎯 Objectives</div>',
                    unsafe_allow_html=True)

        st.markdown("""

✅ Early disease warning

✅ Weather-based disease prediction

✅ Disease risk assessment

✅ Decision support for farmers

✅ Improve timely disease management

        """)

        st.markdown("</div>",unsafe_allow_html=True)

    with right:

        st.markdown('<div class="box">',unsafe_allow_html=True)

        st.markdown('<div class="section-title">🦠 Diseases Covered</div>',
                    unsafe_allow_html=True)

        st.markdown("""

<span class="disease">Leaf Anthracnose</span>

<span class="disease">Black Banded</span>

<span class="disease">Red Rust</span>

<span class="disease">Die Back</span>

<span class="disease">Sooty Mould</span>

        """,unsafe_allow_html=True)

        st.markdown("</div>",unsafe_allow_html=True)



    st.markdown("<br>",unsafe_allow_html=True)



    st.markdown('<div class="section-title">⚙️ How It Works</div>',
                unsafe_allow_html=True)

    c1,c2,c3,c4,c5 = st.columns(5)

    with c1:
        st.info("🌦\n\nWeather Data")

    with c2:
        st.info("📈\n\nHistorical Disease")

    with c3:
        st.info("🧮\n\nFeature Engineering")

    with c4:
        st.info("🤖\n\nRandom Forest Model")

    with c5:
        st.success("📊\n\nDisease Risk Prediction")



    st.markdown("""
    <div class="footer">

    <b>Mango Disease Forecast System</b><br>

    Developed by <b>Mr. Kathirvel M.</b><br>

    Department of Agricultural Statistics<br>

    Tamil Nadu Agricultural University

    </div>
    """,unsafe_allow_html=True)

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

        **Symptoms**
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


        **Symptoms**
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
     
    
        **Symptoms**
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

    if st.button("Forecast Disease Risk", key="forecast_button"):

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
    ## Mango Disease Forecast System

    This application was developed for forecasting major mango diseases
    using weather data and machine learning.

    ### Developer

    **Mr. Kathirvel M.**

    PG Student of Agricultural Statistics

    Department of Physical Sciences and Information Technology

    Agricultural Engineering College and Research Institute

    Tamil Nadu Agricultural University,Coimbatore, Tamil Nadu 641003, India

    ### Study Area

    Theni District, Tamil Nadu, India

    ### Technologies Used

    - Python
    - Streamlit
    - Machine Learning
    - XGBoost
    - Pandas
    - NumPy

    ### Purpose

    To provide an early warning system for mango disease outbreaks and
    support timely disease management decisions.
    """)