import streamlit as st

st.set_page_config(page_title="Home Instead Onboarding Assistant", layout="centered")

st.title("🏡 Home Instead Onboarding Assistant")
st.markdown("Welcome to the guided onboarding experience. Select a module below to begin:")

modules = {
  "Welcome": {
    "text": "Welcome to Home Instead! We're thrilled to have you join our mission of enhancing the lives of aging adults and their families.",
    "video": "IMG_3116.MOV"
},
    "Company Overview": {
        "text": "Home Instead is a leading provider of in-home care for seniors. We emphasize dignity, respect, and quality. You’ll be part of a team that values connection, consistency, and compassionate care.",
        "video": "24FCB3426_FY24_HI_HOME_CONSIDERATION_META_1x1_06.mp4"
    },
    "Caregiver Role": {
        "text": "As a Care Professional, you'll assist clients with daily activities such as meal prep, light housekeeping, companionship, and personal care. Each client is unique, and your role is to support them in living comfortably and safely at home.",
	"video": "https://youtu.be/le6i1Fgnhuc?si=2qhVc3C4iXVOfeFK"
    },
    "Policies": {
        "text": "Policies include mandatory reporting, confidentiality, professional conduct, and attendance expectations. Please refer to your employee handbook for full details. Always reach out with questions — we’re here to support you."
    },
    "Training Requirements": {
        "text": "All Care Pros must complete the Home Instead Training Program within the first 30 days. This includes modules on dementia care, safety, communication, and emergency procedures.",
        "video": "https://www.youtube.com/watch?v=Awf45u6zrP0"
    },
    "First Week Checklist": {
        "text": "\n".join([
            "✔ Complete your orientation paperwork",
            "✔ Watch the welcome video",
            "✔ Attend shadow shift with experienced Care Pro",
            "✔ Review the Client Care Plan guide",
            "✔ Confirm your training schedule"
        ])
    }
}

selected = st.selectbox("Select a module:", list(modules.keys()))

if selected:
    st.subheader(f"📘 {selected}")
    st.write(modules[selected]["text"])

    if "video" in modules[selected]:
        st.video(modules[selected]["video"])