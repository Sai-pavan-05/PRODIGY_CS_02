import streamlit as st
import numpy as np
from PIL import Image
import io

# ---------------- IMAGE ENCRYPTION LOGIC ----------------
def encrypt_image(img, key):
    arr = np.array(img, dtype=np.uint8)
    np.random.seed(key)  # use key as seed
    key_stream = np.random.randint(0, 256, arr.shape, dtype=np.uint8)
    encrypted_arr = arr ^ key_stream
    return Image.fromarray(encrypted_arr)

def decrypt_image(img, key):
    arr = np.array(img, dtype=np.uint8)
    np.random.seed(key)  # regenerate the same key stream
    key_stream = np.random.randint(0, 256, arr.shape, dtype=np.uint8)
    decrypted_arr = arr ^ key_stream
    return Image.fromarray(decrypted_arr)

# ---------------- AUTO-DETECTION FUNCTION ----------------
def is_encrypted_image(img, threshold=60):
    arr = np.array(img, dtype=np.uint8)
    std = np.std(arr)  # spread of pixel values
    return std > threshold, std

# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="🔐 Image Encryption Tool", page_icon="🖼️", layout="centered")
st.title("🔐 Image Encryption & Decryption Tool")

st.write("Upload an image")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
key = st.slider("Select encryption/decryption key (1-9999)", 1, 9999, 1234)

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")

    # Auto-detect if encrypted
    looks_encrypted, std_val = is_encrypted_image(img)
    suggested_mode = "Decrypt" if looks_encrypted else "Encrypt"

    st.write(f"📊 Pixel StdDev = `{std_val:.2f}` → Suggested Mode: **{suggested_mode}**")
    # Let user override detection
    mode = st.radio("Choose Operation:", ["Encrypt", "Decrypt"], index=0 if suggested_mode=="Encrypt" else 1)

    st.image(img, caption=f"Uploaded Image ({mode} Mode)", use_container_width=True)

    if mode == "Encrypt":
        if st.button("Encrypt"):
            encrypted_img = encrypt_image(img, key)
            st.image(encrypted_img, caption="Encrypted Image", use_container_width=True)

            buf = io.BytesIO()
            encrypted_img.save(buf, format="PNG")
            st.download_button(
                "Download Encrypted Image", 
                data=buf.getvalue(), 
                file_name="encrypted.png", 
                mime="image/png"
            )

    elif mode == "Decrypt":
        if st.button("Decrypt"):
            decrypted_img = decrypt_image(img, key)
            st.image(decrypted_img, caption="Decrypted Image", use_container_width=True)

            buf = io.BytesIO()
            decrypted_img.save(buf, format="PNG")
            st.download_button(
                "Download Decrypted Image", 
                data=buf.getvalue(), 
                file_name="decrypted.png", 
                mime="image/png"
            )

st.caption("💡 Tip: The tool tries to detect if your image looks encrypted. You can always override the suggested mode.")