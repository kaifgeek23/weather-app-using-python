
🌤️ Weather App (Tkinter + OpenWeather API)

A simple and user-friendly Weather Application built using Python (Tkinter GUI) that fetches real-time weather data using the OpenWeather API.

📌 Features
🌍 Select city/state from dropdown
🌡️ Displays temperature (in °C)
☁️ Shows weather condition (e.g., Clouds, Rain)
📝 Detailed weather description
📊 Atmospheric pressure info
🎨 Clean and minimal GUI using Tkinter
🛠️ Tech Stack
Python
Tkinter (GUI)
Requests (API calls)
OpenWeather API
📷 UI Preview

(You can add a screenshot here later if you want)

🚀 How It Works
User selects a city/state from dropdown.
Clicks on "Show Details" button.
App sends request to OpenWeather API.
Weather data is fetched and displayed on screen.
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/weather-app.git
cd weather-app
2. Install dependencies
pip install requests
3. Run the application
python app.py
🔑 API Key Setup

This project uses OpenWeather API.

Replace the API key in the code:

appid=YOUR_API_KEY

Get your free API key from:
👉 https://openweathermap.org/api

⚠️ Note
Temperature is converted from Kelvin → Celsius
Some state names may not return accurate results (API works best with city names)
📌 Improvements You Can Add
🌐 Add search bar for custom city input
📍 Auto-detect location
🎨 Improve UI with themes
📅 Add 5-day weather forecast
🌡️ Add humidity & wind speed
🤝 Contributing

Feel free to fork this repo and improve it. Pull requests are welcome!

📄 License

This project is open-source and free to use.
