from pathlib import Path
import streamlit as st # pip install streamlit
from PIL import Image #pip install pillow

#---Path settings---
This_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
Assets_DIR = This_DIR / "assets"
Styles_DIR = This_DIR / "styles"
CSS_File = Styles_DIR / "main.css"

#--General settings---
Stripe_checkout= "https://buy.stripe.com/test_fZu00k9Jj2F3g1me2n9fW00"
Contact_email = "DrivAIjl@gmail.com"
Product_Name =  "Little Planner"
Product_Tagline = "Let us do one small thing first and let momentum do the rest"
Product_Description = """ Feeling Overwhelmed? This simple planner can help with day to day tasks you wont find anywhere else:

- Write down your top 3 priorities for the day so you stay focused.
- Block out time for each task so you know when to work on what.
- Check off completed items to track progress and stay motivated.
- Review your planner each morning and evening to stay organized.
- Keep it simple—dont overload your day with too many tasks.

**Let simplicity become your new superpower**
"""

#--- Page Configuration ---

st.set_page_config(
    page_title=Product_Name,
    page_icon=":star:",
    layout="centered",
    initial_sidebar_state="collapsed"
)

#---Main page---
st.header(Product_Name)
st.subheader(Product_Tagline)
left_col, right_col = st.columns ((2,1))
with left_col:
    st.text("")
    st.write(Product_Description)
    st.markdown(
        f'<a href={Stripe_checkout} class= "button"> 🗓️ Get Little Planner</a>',
            unsafe_allow_html=True
                    )

with right_col:
    product_image = Image.open(Assets_DIR / "Screenshot 2025-11-30 135310.png")
    st.image(product_image, width=450 )
