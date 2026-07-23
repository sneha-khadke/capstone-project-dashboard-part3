API-Integrated Interactive Dashboard

Project Overview

This project is an interactive Streamlit dashboard built using Python. It allows users to explore and analyze a dataset through interactive filters, dynamic visualizations, and a live data table. The dashboard also integrates a real-time external REST API using the Python `requests` library to display live weather information.

The dashboard is designed for non-technical users, enabling them to explore the data without writing any code.

---

Features

- Interactive SelectBox
- 3 Dynamic Charts
- Live Data Table
- Weather API Integration

---

Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- Plotly
- Requests

---

Project Structure

```
Part3/
│
├── app.py
├── requirements.txt
├── README.md
└── dataset.csv

```
---

Visualizations

The dashboard contains three interactive visualizations that automatically update based on the selected filter.

1. Bar Chart
Displays comparisons between selected categories.

2. Line Chart
Shows trends and changes across the filtered data.

3. Pie Chart
Displays the percentage distribution of selected categories.

---

Live Data Table

A live Streamlit DataFrame (`st.dataframe`) displays the filtered dataset based on the user's selection.

Users can easily inspect the underlying data used to generate the charts.

---

External REST API Integration

This project integrates a live REST API using Python's `requests` library.


API Used

Endpoint:

https://api.open-meteo.com/v1/forecast?latitude=51.50&longitude=-0.12&current=temperature_2m

HTTP Method:

GET

The dashboard sends a GET request to the Open-Meteo API to retrieve current weather information.


API Response Displayed Field:

temperature_2m

The API returns live weather information.

Weather data by Open-Meteo.com (CC BY 4.0)

These values are extracted from the JSON response returned by the API.

---

Run

streamlit run app.py

Live Dashboard

https://capstone-project-dashboard-part3-enum8x6hyz87bb7wozbzdk.streamlit.app/

---

GitHub Repository

https://github.com/sneha-khadke/capstone-project-dashboard-part3.git

---

Requirements

The project dependencies are listed in requirements.txt.

Typical libraries include:

- streamlit
- pandas
- matplotlib
- plotly
- requests

---

Author

Sneha Khadke

AI/ML Portfolio Project

API Integrated Interactive Dashboard