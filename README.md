🔐 Image Encryption Tool

A simple yet powerful **Image Encryption & Decryption app** built with **Python + Streamlit**.  
This project lets you **securely scramble your images** using a **random key-stream XOR technique**, making them look like random noise, and then recover them back with the same key. 🖼️✨

---

📖 Project Overview

The **Image Encryption Tool** provides an interactive way to **encrypt and decrypt images** with just a few clicks.

* Built with **Streamlit** for a smooth and user-friendly UI.  
* Uses **random key-stream XOR** for stronger scrambling compared to simple shift ciphers.  
* Includes **auto-detection** to suggest whether an uploaded image looks encrypted.  
* Preserves image quality during encryption and decryption.  
* Supports **file downloads** for both encrypted and decrypted images.  

---

✨ Features

✅ Encrypt images with a customizable key (1–9999).  
✅ Decrypt instantly with the same key.  
✅ Auto-detects if an image looks like encrypted noise.  
✅ Interactive **slider-based control** for key selection.  
✅ Real-time results in a clean UI.  
✅ Beginner-friendly & lightweight to run locally.  

---

🖥️ How It Works

1. Upload an image (JPG, JPEG, PNG).  
2. Select a **key** (1–9999).  
3. Click **Encrypt** to scramble the image into noise.  
4. Upload the encrypted image + same key, and click **Decrypt** to restore the original.  

The XOR-based encryption works by combining pixel values with a pseudo-random key stream:  

```

Pixel Value ⊕ Random Key Stream = Encrypted Pixel

````

Using the same key again regenerates the same key stream, reversing the process.

---

🚀 Getting Started

1. Clone the repo

```bash
git clone https://github.com/Sai-pavan-05/image-encryption-tool.git
cd image-encryption-tool
````

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
streamlit run ImgEnc.py
```

4. Open in browser

Visit 👉 `http://localhost:8501`

---

📂 Code Structure

```
image_encryption_tool/
│── app.py              # Main Streamlit app
│── requirements.txt    # Dependencies
│── README.md           # Documentation
```

Key functions in `ImgEnc.py`:

* `encrypt_image(img, key)` → Encrypts image using random key-stream XOR.
* `decrypt_image(img, key)` → Decrypts image using the same key-stream.
* `is_encrypted_image(img)` → Auto-detection logic (checks pixel randomness).

---

🎯 Use Cases

🔹 Learning basic image cryptography concepts.
🔹 Demonstrating how XOR-based encryption works.
🔹 Lightweight educational project for students.
🔹 Fun tool for experimenting with image scrambling.

---

📸 Demo Screenshot (Optional)

![image alt]()

---

📜 License

This project is open-source under the **MIT License**.
