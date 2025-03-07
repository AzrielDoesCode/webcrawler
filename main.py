import requests
import time
from plyer import notification
from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem, Icon

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to create a simple weather icon for the system tray
def create_image(width, height):
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.ellipse((0, 0, width, height), fill=(0, 128, 255))  # Example icon
    return image

# Function to send weather notifications
def notify_weather(city):
    api_key = 'bd5e378503939ddaee76f12ad7a97608'  # Replace with your actual API key
    weather_data = get_weather(city, api_key)
    
    if weather_data:
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        notification.notify(
            title="Weather Update",
            message=f"{city}: {temp}°C, {description}",
            timeout=10
        )

# Function to handle quitting the application
def on_quit(icon, item):
    icon.stop()

# Main function to run the application in the system tray
def run(icon):
    while True:
        notify_weather("YourCity")  # Replace with desired city name
        time.sleep(7200)  # Wait for 2 hours before next update

# Create and configure the system tray icon
icon = Icon("Weather App")
icon.icon = create_image(64, 64)
icon.menu = pystray.Menu(MenuItem('Quit', on_quit))

# Start the icon and run the app
icon.run(run)