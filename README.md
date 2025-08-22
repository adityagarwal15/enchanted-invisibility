# 🪄 Enchanted Invisibility Cloak

A fun **real-time invisibility cloak effect** built with **OpenCV, Mediapipe, and TensorFlow Lite**.  
Inspired by Harry Potter's cloak of invisibility ✨

---

## 🚀 Features
- Real-time webcam-based background subtraction
- Press `b` to capture background
- Step into the frame → your body disappears!
- Simple controls (`q` to quit)
- Lightweight: uses TensorFlow Lite with XNNPACK delegate for CPU

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **OpenCV** – Image processing & webcam capture
- **Mediapipe** – Segmentation model
- **TensorFlow Lite** – Lightweight inference
- **Numpy** – Array processing

---

## 📂 Project Structure
```
enchanted-invisibility/
│
├── main.py               # Entry point – run this file
├── requirements.txt      # Dependencies
├── README.md             # Documentation
├── .gitignore            # Ignored files/folders
│
├── models/               # (Optional) ML models
│   └── body_segmentation.tflite
│
├── output/               # Saved outputs (if any)
│
└── venv310/              # Local virtual environment (ignored)
```

---

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/enchanted-invisibility.git
   cd enchanted-invisibility
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv310
   source venv310/bin/activate      # macOS/Linux
   venv310\Scripts\activate         # Windows (PowerShell)
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the program**
   ```bash
   python main.py
   ```

---

## 🎮 Usage

- Run `main.py`
- Stand **away from camera**
- Press **`b`** → Captures background (without you)
- Step into frame → **Invisibility effect activated 🪄**
- Press **`q`** → Quit

---

## 📸 Demo

(Add a GIF or screenshot here once you test it!)

---

## ⚠️ Notes

- Works best with **stable lighting & plain backgrounds**
- If background capture fails, press **`b`** again
- Warnings like `Feedback manager requires a model...` are **safe to ignore**

---

## 🧑‍💻 Author

**Aditya Agarwal**  
Third-year Computer Science & Engineering Student, MIT Manipal

---

## 📜 License

MIT License – Free to use and modify
