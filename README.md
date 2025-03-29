# Buckshot Assistent
# 🎲 Probability Simulator

## 📌 Overview
This project is a probability simulator designed to demonstrate conditional probability calculations in a visual and interactive way. The core feature of this program is the **percentage bar**, which updates dynamically based on calculated probabilities.

## 🛠️ Features
- 🎯 **Interactive probability calculation**
- 📊 **Dynamic percentage bar** representation
- 📡 **Uses an external probability library** for accuracy
- 🖥️ **Graphical representation** for better visualization

## 📷 Screenshots
_(Insert images here)_

## 🔬 Understanding the Probability Behind the Percentage Bar
The percentage bar is calculated based on **conditional probability**. Given an event **A** and a condition **B**, the probability of **A** happening given **B** has already occurred is given by:

\[
P(A | B) = \frac{P(A \cap B)}{P(B)}
\]

Where:
- \( P(A | B) \) is the probability of event A occurring given that B has already occurred.
- \( P(A \cap B) \) is the probability of both A and B happening.
- \( P(B) \) is the probability of event B occurring.

This conditional probability is used to update the percentage bar dynamically, providing a real-time estimation based on new inputs.

## 📚 About Tkinter
Tkinter is the standard GUI (Graphical User Interface) library for Python. It provides a simple yet powerful way to create desktop applications with graphical elements like buttons, labels, sliders, and progress bars. Tkinter is built on top of the Tk GUI toolkit and comes pre-installed with Python, making it a convenient choice for creating user interfaces.

Key Features of Tkinter:
Lightweight & Easy to Use: Tkinter provides a straightforward API for creating GUI applications without requiring additional dependencies.

- Cross-Platform Compatibility: Since Tkinter is part of Python’s standard library, it works on Windows, macOS, and Linux.

- Widget-Based System: Includes various built-in widgets like Label, Button, Entry, Canvas, Frame, and Progressbar to build rich interfaces.

- Customizability: Widgets support styling and event handling, allowing for dynamic and interactive applications.

Tkinter in This Project
In this project, Tkinter is used to create the percentage bar, which visually represents a probability calculation. The progress bar dynamically updates based on conditional probability calculations, giving users an intuitive way to interpret the results.

The library ensures accuracy and optimizes computational performance, making the simulator highly reliable.

## 🚀 Installation & Usage
### 🔧 Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/Mapnbp/Buckshot-Assistent.git
   ```
2. Navigate to the project directory:
   ```sh
   cd probability-simulator
   ```
3. Install dependencies (doesnt heve yet):
   ```sh
   pip install -r requirements.txt
   ```

### ▶️ Usage
Run the script:
```sh
python simulator.py
```
Adjust parameters as needed and observe the probability changes in the percentage bar.

## 🤝 Contributing
Feel free to fork this repository and submit pull requests! Any improvements or suggestions are welcome.

## 📜 License
This project is licensed under the MIT License.

---

📧 **Contact:** If you have any questions, feel free to reach out!

##🚀 Future Improvements
Add the option to set initial quantities of balls.

Implement animations for the removal process.

Export data to CSV/Excel.

Additionally, data will be collected and an inference will be made using the R programming language to verify if the probabilistic model corresponds to the real functioning of the game.

