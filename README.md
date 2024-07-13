# Rodeo Registration Management System

A Django-based web application for managing rodeo event registrations. This application uses PostgreSQL for the database, Django Rest Framework for the API, and includes support for environment-specific settings and CORS headers.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Rodeo Registration App is designed to handle registrations for various rodeo events. It includes user management, event registration, and payment processing features. The application is built using Django and provides a RESTful API for frontend integration.

## Features

- User authentication and management
- Event registration
- Payment processing
- CORS support for frontend integration
- Environment-specific configuration

## Technologies Used

- **Backend:** Django, Django Rest Framework
- **Database:** PostgreSQL
- **Environment Management:** django-environ
- **Others:** django-cors-headers

## Installation

To get a local copy up and running, follow these steps:

### Prerequisites

- Python 3.8 or higher
- PostgreSQL
- Virtual environment (venv)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/rodeo-app.git
   cd rodeo-app
