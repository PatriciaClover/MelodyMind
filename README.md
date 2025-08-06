# 🎼 MelodyMind
*AI-powered melody generation for musicians and producers.*

> Created by [Patricia Clover (PC)](https://github.com/PatriciaClover) — blending code and creativity.

---

## ✨ What is MelodyMind?
**MelodyMind** is a simple but powerful tool that generates unique melodies based on user input. Just type in a mood, genre, or theme — and let the AI handle the rest.

Built for musicians, producers, and hobbyists who want a spark of inspiration in their workflow. 🎶

---

## 🎹 Features
- 🎯 Prompt-based melody generation (e.g., “uplifting jazz riff” or “moody lo-fi loop”)
- 🧠 Trained RNN model with custom music embeddings
- 💽 Output in `.mid` (MIDI) format for use in any DAW
- 🖤 Minimal interface: no fluff, just music

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/PatriciaClover/MelodyMind.git
cd MelodyMind
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run it

```bash
python run.py --prompt "dreamy ambient intro" --output output.mid
```

---

## 📁 Example

Try generating a melody with:

```bash
python run.py --prompt "nostalgic piano ballad"
```

Check the `examples/` folder for sample input/output.

---

## 🔧 How It Works

MelodyMind uses an RNN trained on a dataset of genre-tagged MIDI clips. Prompts are converted into embeddings, then decoded into sequences of notes, rhythms, and velocities.

Want to train your own model? Check out the `melodymind/model/` directory.

---

## 🧠 Built With

* PyTorch 🎯
* pretty\_midi 🎼
* scikit-learn 🧪

---

## ❤️ Creator

Patricia Clover (PC)
*Musician-turned-coder passionate about AI music generation.*

> *"Where there's music, there's magic; where there's code, there's limitless possibility."*

---

## 📫 Feedback & Collaboration

Have ideas, questions, or want to collaborate?
Feel free to open an issue or reach out via GitHub Discussions.

