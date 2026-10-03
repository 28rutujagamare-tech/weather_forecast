# 🌦️ Django Weather Forecast

A simple **Weather Forecast web application built with Django and Python** that allows users to search for a city and view its current weather information using the **OpenWeather API**.

## 📌 Project Overview

This project demonstrates how to build a Django application that communicates with an external REST API.

Users can enter a city name, and the application fetches the latest weather information from the OpenWeather API and displays it on a weather details page.

## ✨ Features

* 🔍 Search weather by city name
* 🌡️ Display current temperature
* ☁️ Display weather conditions
* 💧 Display humidity
* 🌍 Fetch real-time weather data using OpenWeather API
* ⚠️ Display an error message for invalid city names
* 🖥️ Simple and user-friendly interface

## 🛠️ Technologies Used

* **Python**
* **Django**
* **HTML**
* **CSS**
* **REST API**
* **OpenWeather API**
* **Requests Library**

## 📂 Project Structure

```text
weather_project/
│
├── weather/
│   ├── migrations/
│   ├── templates/
│   │   └── weather/
│   │       ├── form.html
│   │       └── weather_data.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── weather_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```

> The exact folder structure may vary depending on the project setup.

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project directory

```bash
cd django-weather-forecast
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, you can install the required packages using:

```bash
pip install django requests
```

### 6. Add your OpenWeather API Key

Get an API key from OpenWeather and add it to your Django view.

For example:

```python
api_key = "YOUR_API_KEY"
```

⚠️ **Do not upload your actual API key to GitHub.**

For a public repository, it is better to store the API key in an environment variable.

### 7. Run migrations

```bash
python manage.py migrate
```

### 8. Start the Django development server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 🔄 How It Works

The application follows this basic flow:

```text
User enters city
        ↓
Django receives the request
        ↓
Weather API request is sent
        ↓
OpenWeather API returns weather data
        ↓
Django processes the response
        ↓
Weather details are displayed
```

## 📡 API Used

This project uses the **OpenWeather Current Weather API** to retrieve weather information based on the city entered by the user.

The API response provides information such as:

* City name
* Temperature
* Weather description
* Humidity
* Weather conditions

## 🎯 Learning Objectives

Through this project, I practiced:

* Creating a Django project and application
* Handling GET and POST requests
* Working with Django templates
* Using Django messages
* Sending requests to an external REST API
* Processing JSON API responses
* Displaying dynamic data in HTML
* Handling API errors and invalid input

## 🔮 Future Improvements

Some improvements that can be added in the future:

* 📅 5-day weather forecast
* 🌡️ Celsius/Fahrenheit conversion
* 📍 Weather based on current location
* 🌅 Sunrise and sunset information
* 📱 Responsive UI
* 🌤️ Weather icons
* 🔐 Secure API key management using environment variables

## 👩‍💻 Author

**Rutuja Gamare**

Aspiring Python Developer | Django | REST APIs

---

⭐ If you found this project useful, feel free to explore the repository.
