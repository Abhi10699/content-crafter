import streamlit as st
from api import blip_image_caption, mistral_prompt_request, stable_diffusion_api



# st.title("Content Crafter ✨")


st.markdown("# Content Crafter ✨")
st.write("Unleash your creativity and conquer TikTok with Content Crafter! Craft captivating content effortlessly and stay on top of the latest trends with our powerful idea generator. From trending challenges to viral concepts, Content Crafter provides you with an endless stream of inspiration, ensuring your TikTok videos stand out and make an impact. Discover, create, and share your unique content today, with Content Crafter as your creative companion.")

with st.sidebar:

  # inference api
  st.markdown("# Upload Image")
  uploaded_image = st.file_uploader(label="adsad",type=['png', 'jpg'],label_visibility="collapsed")
  if uploaded_image is not None:
    image_description = blip_image_caption(uploaded_image)
    st.image(uploaded_image, caption=image_description)

  with st.expander("Trending Ideas 💡"):
    st.markdown("**October 14**")
    st.markdown("- Pair an audio with a caption that highlights a risk you’ve recently taken and let the delusion soar.")
    st.markdown("- The perfect opportunity to showcase a killer fit.")
    st.markdown("- Highlight an unexpected moment or a relatable struggle..")

    st.markdown("**October 21**")
    st.markdown("- Pair an audio with a caption that highlights a risk you’ve recently taken and let the delusion soar.")
    st.markdown("- The perfect opportunity to showcase a killer fit.")
    st.markdown("- Highlight an unexpected moment or a relatable struggle..")





main_container = st.empty()
if uploaded_image is not None:
  col1, col2 = st.columns(2)
  with st.spinner("Generating Ideas ✨"):
    tiktok_ideas = mistral_prompt_request(image_description)
    st.markdown(f"\n\n{tiktok_ideas}")

else:
  image = stable_diffusion_api("social mediaidea generator")
  st.image(image, width=500)