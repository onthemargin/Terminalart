# Terminal Art 🎨

An interactive ASCII art gallery featuring cute animals and creatures. Available in both Python terminal (using Textual) and HTML web versions.

**Author:** On The Margin

## 🖼️ Gallery Overview

Terminal Art is an interactive gallery that displays hand-crafted ASCII art of various animals. Browse through the collection using an elegant menu interface and enjoy colorful ASCII representations of your favorite creatures.

### Featured Art

- **🐕 Dog** - A friendly yellow dog
- **🐱 Cat** - A cute cat with paws
- **🐦 Bird** - A flying bird
- **🐟 Fish** - A swimming fish
- **🦋 Butterfly** - A colorful butterfly
- **🐰 Rabbit** - A cute rabbit with ears
- **🐍 Snake** - A slithering snake
- **🐸 Frog** - A jumping frog
- **🦉 Owl** - A wise owl

## 🚀 How to Use

### Python Terminal Version
1. Install requirements: `pip install -r requirements.txt`
2. Run the application: `python app.py`
3. Navigate through the menu using arrow keys or click on items
4. Press 'q' or 'Escape' to quit

### HTML Web Version
1. Open `index.html` in your web browser
2. Click on any animal in the left menu
3. View the ASCII art displayed in the center
4. Enjoy the colorful representations!

## 📋 Requirements

### Python Terminal Version
- Python 3.8+
- textual >= 0.47.0
- rich >= 13.0.0
- Terminal with Unicode and ANSI color support

### HTML Web Version
- Modern web browser with JavaScript support
- No additional dependencies required

## 🎯 Features

### Python Terminal Version
- Built with Textual framework for rich terminal UI
- Interactive menu with keyboard and mouse support
- Live preview as you navigate
- Colorful ASCII art with proper markup
- Responsive terminal interface
- Header and footer with status information

### HTML Web Version
- Clean, modern web interface
- Responsive design for mobile and desktop
- Gradient background with blended ASCII art
- Color-coded animals matching terminal version
- Click-based navigation
- Smooth transitions and hover effects

## 🛠️ Project Structure

```
terminalart/
├── app.py                 # Main Textual application
├── generators/
│   ├── base.py           # Base generator class
│   ├── registry.py       # Generator registry
│   ├── dog.py            # Dog ASCII art
│   ├── cat.py            # Cat ASCII art
│   ├── bird.py           # Bird ASCII art
│   ├── fish.py           # Fish ASCII art
│   ├── butterfly.py      # Butterfly ASCII art
│   ├── rabbit.py         # Rabbit ASCII art
│   ├── snake.py          # Snake ASCII art
│   ├── frog.py           # Frog ASCII art
│   └── owl.py            # Owl ASCII art
├── index.html            # Web version
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🎨 Adding New Art

To add your own ASCII art:

1. Create a new generator file in `generators/` directory
2. Extend the `AsciiGenerator` base class
3. Implement the required properties and `generate()` method
4. The registry will automatically discover your new generator

Example:
```python
from generators.base import AsciiGenerator

class MyArtGenerator(AsciiGenerator):
    @property
    def name(self) -> str:
        return "My Art"

    @property
    def description(self) -> str:
        return "Description of my art"

    def generate(self) -> str:
        return """[color]ASCII art here[/color]"""
```

---

## 📄 License

MIT License

Copyright (c) 2025 On The Margin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## ⚠️ Educational Disclaimer

**This project is created for educational purposes only.** It is intended to demonstrate:
- Python programming with Textual framework
- Object-oriented design patterns
- Terminal-based user interfaces
- Dynamic content generation
- Web development with vanilla JavaScript

This software is provided as-is for learning and educational use. Please use responsibly.

**Development Note:** This project was created with the assistance of [Claude Code](https://claude.ai/code), Anthropic's interactive CLI tool for software development.
