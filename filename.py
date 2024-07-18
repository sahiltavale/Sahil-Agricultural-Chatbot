import streamlit as st
import numpy as np
import pickle
from streamlit_lottie import st_lottie
import requests
#------------------------------------------------------

with st.sidebar:
    st.title('''       😎 KP APP 🤖        ''')
    st.markdown("------------------")
    option = "About"
    st.markdown(f"<h3 style='text-align: center;'>{option}</h3>",unsafe_allow_html=True)
    st.markdown('''
     Kundeshwar V. Pundalik believes that KP APP has the potential to revolutionize various industries, such as customer service, education, and entertainment.
    💡 Note: No API key required!
    ''')
    st.write('Made with ❤️ by Kundeshwar Pundalik 😍')




#-------------------------------------------------------

# Load the trained model
with open('dtr (1).pkl', 'rb') as file:
    dtr = pickle.load(file)
def lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
# Define the encoders
Area_Encoder = {
    'Albania': 0, 'Algeria': 1, 'Angola': 2, 'Argentina': 3, 'Armenia': 4, 'Australia': 5, 'Austria': 6, 'Azerbaijan': 7,
    'Bahamas': 8, 'Bahrain': 9, 'Bangladesh': 10, 'Belarus': 11, 'Belgium': 12, 'Botswana': 13, 'Brazil': 14, 'Bulgaria': 15,
    'Burkina Faso': 16, 'Burundi': 17, 'Cameroon': 18, 'Canada': 19, 'Central African Republic': 20, 'Chile': 21, 'Colombia': 22,
    'Croatia': 23, 'Denmark': 24, 'Dominican Republic': 25, 'Ecuador': 26, 'Egypt': 27, 'El Salvador': 28, 'Eritrea': 29,
    'Estonia': 30, 'Finland': 31, 'France': 32, 'Germany': 33, 'Ghana': 34, 'Greece': 35, 'Guatemala': 36, 'Guinea': 37,
    'Guyana': 38, 'Haiti': 39, 'Honduras': 40, 'Hungary': 41, 'India': 42, 'Indonesia': 43, 'Iraq': 44, 'Ireland': 45, 'Italy': 46,
    'Jamaica': 47, 'Japan': 48, 'Kazakhstan': 49, 'Kenya': 50, 'Latvia': 51, 'Lebanon': 52, 'Lesotho': 53, 'Libya': 54,
    'Lithuania': 55, 'Madagascar': 56, 'Malawi': 57, 'Malaysia': 58, 'Mali': 59, 'Mauritania': 60, 'Mauritius': 61, 'Mexico': 62,
    'Mex': 63
}
loettir_2 = lottie("https://assets10.lottiefiles.com/packages/lf20_7fCbvNSmFD.json")
Item_Encoder = {
    'Maize': 0, 'Potatoes': 1, 'Rice, paddy': 2, 'Sorghum': 3, 'Soybeans': 4, 'Wheat': 5, 'Cassava': 6, 'Sweet potatoes': 7,
    'Plantains and others': 8, 'Yams': 9
}

def prediction(Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item):
    # Encode the categorical features
    encoded_area = Area_Encoder[Area]
    encoded_item = Item_Encoder[Item]

    # Create an array of the input features
    features = np.array([[average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, encoded_area, encoded_item]], dtype=object)

    # Make the prediction
    predicted_yield = dtr.predict(features)

    return predicted_yield[0]

# Streamlit app
st.title("Crop Yield Prediction")

st.write("""
## Input the following features to predict the crop yield:
""")
st_lottie(loettir_2)
Year = st.number_input("Year", min_value=1900, max_value=2100, value=2020)
average_rain_fall_mm_per_year = st.number_input("Average Rainfall (mm per year)", min_value=0.0, value=1000.0)
pesticides_tonnes = st.number_input("Pesticides (tonnes)", min_value=0.0, value=100.0)
avg_temp = st.number_input("Average Temperature (°C)", min_value=-50.0, max_value=50.0, value=20.0)
Area = st.selectbox("Area", list(Area_Encoder.keys()))
Item = st.selectbox("Item", list(Item_Encoder.keys()))

if st.button("Predict"):
    result = prediction(Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item)
    st.write(f"Predicted Yield: {result:.2f} hg/ha")

