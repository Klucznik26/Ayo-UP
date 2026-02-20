AyoUP 1.2 – Intelligent Image Upscaler 🚀🖼️







AyoUP is a fast and lightweight desktop image upscaler powered by the waifu2x-ncnn-vulkan engine.
Built for creators who need high-quality upscaling with a clean interface and efficient workflow.

Part of the Ayo Ecosystem.

📸 Program Preview
Dark Theme	Light Theme	Relax Theme	Batch Mode	Settings

	
	
	
	
🆕 What’s New in 1.2

🎨 New Creative Theme added to the theme system

🌍 Expanded multilingual support (12 languages)

🧠 Internal Qt translation layer – fully translated file dialogs without system .qm dependency

✨ Smooth discard animation (rotate -90° + fade transition)

⚙️ Code cleanup and performance improvements

🧹 Removed artificial delays and debug prints

🗂️ Refactored file handling using pathlib

🚀 Key Features
🖼️ High-Quality Image Upscaling

Upscale images using the powerful waifu2x-ncnn-vulkan engine.

Perfect for:

AI-generated images

illustrations & digital art

wallpapers

photography

batch workflows

📂 Advanced Batch Processing

Process multiple files effortlessly:

Select multiple images

Load entire folders

Recursive subfolder scanning

Drag & Drop support:

single files

multiple files

directories

⚡ Modern UX & Smart Interface
🎴 Fan Preview System

Displays a dynamic fan of thumbnails when multiple files are queued.

▶️ Smart Run Button

The Run button transforms into a live progress indicator during processing.

🧠 Intelligent UI Behavior

File counter appears only when needed

UI clears automatically after completion

Controls are locked during processing to prevent conflicts

🎞️ Discard Animation (New in 1.2)

After processing, images smoothly rotate (-90°) and fade out, revealing the next item in queue.

🎨 Themes

AyoUP supports a consistent visual identity:

Dark Theme (default)

Light Theme

Relax Theme

Creative Theme (new in 1.2)

All dialogs use non-native Qt rendering for full theme consistency and localization control.

🌍 Supported Languages

Fully translated interface including Qt file dialogs.

🇵🇱 Polish

🇺🇸 English

🇪🇸 Spanish

🇷🇴 Romanian

🇵🇹 Portuguese

🇺🇦 Ukrainian

🇨🇿 Czech

🇸🇮 Slovenian

🇱🇻 Latvian

🇱🇹 Lithuanian

🇪🇪 Estonian

🇬🇪 Georgian

The application uses an internal Qt translation layer to ensure consistent localization across all systems.

🏗️ Architecture Highlights

Modular GUI structure

ThemeManager-based styling system

InternalQtTranslator (no external .qm dependency)

Fully non-native Qt dialogs for styling and localization control

Modern file handling via pathlib

Clean event loop (no blocking delays)

🛠️ Technology

Developed using a modern Python + Qt stack:

Language: Python 3.10+

GUI: PySide6 (Qt for Python)

Engine: waifu2x-ncnn-vulkan

Development Environment: Linux (Fedora / openSUSE)

🌌 Ayo Ecosystem

AyoARCH – ZIP image viewer

AyoCONVERT – high-quality file conversion

AyoSORT – intelligent image categorization

More projects:
👉 https://klucznik26.github.io/AyoWWW/

📥 Installation
1️⃣ Clone repository
git clone https://github.com/Klucznik26/Ayo-UP.git
cd Ayo-UP
2️⃣ Install dependencies
pip install PySide6
3️⃣ Download waifu2x engine

Download waifu2x-ncnn-vulkan from:
https://github.com/nihui/waifu2x-ncnn-vulkan

Place the executable in the project directory or configure its path in settings.

4️⃣ Run application
python main.py

Teraz wystarczy:

git add README.md
git commit -m "Fix README screenshots paths"
git push
