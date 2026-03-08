---
title: Plant Disease Detection
emoji: 🌿
colorFrom: green
colorTo: green
sdk: gradio
sdk_version: "5.29.0"
app_file: app.py
pinned: false
license: mit
short_description: Plant disease detection with YOLO & multilingual RAG
---

# 🌿 Plant Disease Detection

A production-grade, multilingual plant disease detection and treatment advisory app built for Indian farmers.

---

## 🚀 Features

| Feature | Detail |
|---------|--------|
| **Vision Models** | YOLOv8n & YOLOv12n (fine-tuned on 28-class dataset) |
| **Ensemble Logic** | Confidence-threshold agreement / disagreement routing |
| **Languages** | English · हिन्दी · اردو · తెలుగు |
| **Translation** | IndicTrans2 (`ai4bharat/indictrans2-en-indic-dist-200M`) |
| **Treatment RAG** | Google Gemini 2.0 Flash + ChromaDB vector store |
| **TTS** | `edge-tts` neural voices per language |
| **Fallback** | Symptom-based AI diagnosis when confidence < 50% |

---

## 📁 File Structure

```
plant_disease_app/
├── app.py                  ← Main Gradio application
├── translations.py         ← UI strings + disease taxonomy (all 4 languages)
├── disease_id_mapping.py   ← YOLO class → disease_id mapping
├── treatment_data.py       ← Inline treatment database (all 28 diseases)
├── data_split.yaml         ← Dataset config reference
├── requirements.txt
├── models/
│   ├── finetuned_yolo8n.pt   ← Upload your fine-tuned YOLOv8n weights here
│   └── finetuned_yolo12n.pt  ← Upload your fine-tuned YOLOv12n weights here
└── README.md
```

---

## ⚙️ Setup on Hugging Face Spaces

### Step 1 — Create the Space

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces) → **Create new Space**
2. Set SDK → **Gradio**, Hardware → **CPU (free)** or **T4 GPU** (recommended)
3. Clone the Space repo:
   ```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/plant-disease-detector
   cd plant-disease-detector
   ```

### Step 2 — Upload all project files

Copy all files from this folder into the cloned Space repo:
```bash
cp -r /path/to/plant_disease_app/* .
mkdir -p models
# Copy your trained weights:
cp /path/to/finetuned_yolo8n.pt  models/
cp /path/to/finetuned_yolo12n.pt models/
```

### Step 3 — Install IndicTransToolkit (via packages.txt)

Create a `packages.txt` file in the Space root:
```
git
```

Then add this to a `setup.sh` or as a `pre_install` step. The toolkit is installed automatically via the git dependency in requirements.txt using:
```
# Add this line to requirements.txt:
git+https://github.com/VarunGumma/IndicTransToolkit.git
```

> **Note:** Add the git line directly to requirements.txt — HF Spaces supports `git+https://` installs natively.

### Step 4 — Set Secret Environment Variables

In your Space → **Settings → Repository secrets**, add:

| Secret Name | Value |
|-------------|-------|
| `HF_TOKEN` | Your Hugging Face read token (for IndicTrans2 model download) |
| `GOOGLE_API_KEY` | Your Google AI Studio API key (for Gemini RAG) |
| `YOLO_V8_PATH` | `models/finetuned_yolo8n.pt` (default, change if needed) |
| `YOLO_V12_PATH` | `models/finetuned_yolo12n.pt` |

### Step 5 — Push and deploy

```bash
git add .
git commit -m "Initial deployment"
git push
```

The Space will build automatically. First startup takes ~3–5 minutes (downloading IndicTrans2).

---

## 🔬 Supported Crops & Diseases (28 Classes)

| Crop | Disease Classes |
|------|----------------|
| 🍎 Apple | Black Rot, Cedar Rust, Scab, Healthy |
| 🌽 Corn/Maize | Common Rust, Gray Leaf Spot, Leaf Blight, Northern Leaf Blight, Healthy |
| 🍇 Grape | Black Rot, Esca, Leaf Blight, Healthy |
| 🥔 Potato | Early Blight, Late Blight, Healthy |
| 🍅 Tomato | Bacterial Spot, Bacterial Wilt, Brown Spots, Early Blight, Late Blight, Leaf Mold, Mosaic Virus, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Healthy |

---

## 🏗️ Architecture

```
User uploads image
        │
        ▼
  ┌─────────────────────┐
  │  YOLOv8n  (640×640) │──────┐
  └─────────────────────┘      │
                                ▼
  ┌─────────────────────┐   Ensemble
  │  YOLOv12n (640×640) │──── Logic ──► Confidence ≥ 50%?
  └─────────────────────┘               │              │
                                        YES            NO
                                        │              │
                               ┌────────┘    ┌─────────────────┐
                               │             │  Symptom Fallback│
                               │             │  (Gemini RAG)    │
                               ▼             └─────────────────┘
                    ┌──────────────────┐
                    │  Disease Info    │  ← translations.py
                    │  (28 classes)   │
                    └──────────────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
           Disease Details          Treatment Plan
          (IndicTrans2 TL)         (TREATMENT_DB + RAG)
                    │                     │
                    └──────────┬──────────┘
                               │
                          edge-tts TTS
                         (4 languages)
```

---

## 📝 Licenses & Credits

- **YOLOv8/v12:** Ultralytics AGPL-3.0
- **IndicTrans2:** CC-BY 4.0 (AI4Bharat)
- **Gemini API:** Google Terms of Service
- **Treatment Data:** Compiled from ICAR, TNAU, KVK, UC IPM public resources

---

*Built with ❤️ for Indian agriculture. For crop advisory, always consult your local KVK officer.*