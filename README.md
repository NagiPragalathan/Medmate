# Medmate

Medmate is an innovative health management platform designed to facilitate virtual consultations by integrating IoT devices. The platform collects vital health data from clients, such as temperature, heartbeat, glucose levels, and more, to provide comprehensive and real-time monitoring and diagnostics.

## Features

- **Virtual Consultations**: Enable real-time consultations between patients and healthcare providers.
- **IoT Integration**: Collect and monitor health data including temperature, heartbeat, glucose levels, etc., using IoT devices.
- **Health Data Dashboard**: View and analyze patient data through an intuitive dashboard.
- **Secure Communication**: Ensure secure and private communication between patients and healthcare providers.
- **Appointment Scheduling**: Schedule and manage appointments seamlessly.
- **Notifications and Alerts**: Receive notifications and alerts for critical health events and upcoming appointments.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite3
- **IoT Integration**: Various IoT devices for health monitoring
- **Real-time Communication**: WebSockets for real-time data transmission

## Installation and Setup

### Prerequisites

- Python 3.x
- pip (Python Package Installer)
- IoT devices (temperature sensors, heart rate monitors, glucose meters, etc.)

### Steps

1. **Clone the Repository**
    
    bash
    
    Copy code
    
    `git clone https://github.com/NagiPragalathan/Medmate.git
    cd Medmate` 
    
2. **Install Dependencies**
    
    bash
    
    Copy code
    
    `pip install -r requirements.txt` 
    
3. **Configure IoT Devices**
    
    Ensure that your IoT devices are properly configured and connected to the system. Follow the device-specific instructions to set up the data transmission to the Medmate platform.
    
4. **Run Migrations**
    
    bash
    
    Copy code
    
    `python manage.py migrate` 
    
5. **Start the Development Server**
    
    bash
    
    Copy code
    
    `python manage.py runserver` 
    
6. **Open the Platform**
    
    Open your browser and navigate to `http://localhost:8000` to access Medmate.
    

## Project Structure

arduino

Copy code

`Medmate/
├── assets/
│   ├── images/
│   └── sounds/
├── css/
│   └── style.css
├── js/
│   └── main.js
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── consult.html
│   └── health_data.html
├── medmate/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── requirements.txt
└── README.md` 

## Usage

- **Dashboard**: View a summary of health data and upcoming appointments.
- **Virtual Consultation**: Start a virtual consultation session and view real-time health data.
- **Health Data**: Access detailed views of collected health data including temperature, heartbeat, and glucose levels.
- **Appointment Management**: Schedule, view, and manage appointments.

## IoT Integration

Medmate integrates with various IoT devices to collect real-time health data. The data is securely transmitted and displayed on the platform, allowing healthcare providers to monitor patient health continuously.

### Supported IoT Devices

- Temperature Sensors
- Heart Rate Monitors
- Glucose Meters
- Other compatible health monitoring devices

## Contribution

Contributions to the Medmate project are welcome! If you would like to contribute, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://chatgpt.com/c/LICENSE) file for details.
