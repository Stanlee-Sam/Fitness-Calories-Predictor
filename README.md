# Fitness Calories Predictor

A Streamlit web application that predicts the number of calories burned during physical activities based on user input. Built using Python and Pandas.

## Features

* Upload or select physical activity data.
* Predict calories burned based on activity metrics.
* Interactive, user-friendly interface.
* Works directly in the browser using Streamlit.

## Demo

You can run the app locally or deploy it to [Streamlit Cloud](https://streamlit.io/).

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/fitness-calories-predictor.git
cd fitness-calories-predictor
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

## Dataset

The app uses a cleaned dataset stored in Google Drive. The CSV is loaded directly from a shared link. No local file setup is needed for deployment.

## Dependencies

* Python 3.10+
* Streamlit
* Pandas
* Scikit-learn (if any ML model is used)

## Usage

1. Enter your activity details in the sidebar or input fields.
2. Click **Predict** to see the estimated calories burned.
3. Explore the dataset and predictions in the main interface.

## License

This project is open-source and free to use under the MIT License.


