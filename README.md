## Overview

### Barbados 1763 Voyage Coordinate Map

This Django-based app visualizes the journey of Nevil Maskelyne during the 1763 voyage to Barbados, where he tested John Harrison's marine timekeeper (H4). The app plots latitude and longitude coordinates from the journey on an interactive map using Leaflet.js. 

#### Key Features:
- **Interactive Map**: Displays Maskelyne's travel route and positions with markers. 
- **Linked Data**: Each marker includes links to relevant sections of the logbook, allowing users to explore the source material.
- **Coordinate Viewer**: A side panel lists all coordinates and allows navigation by clicking individual entries.
- **CSV Data**: Coordinates and metadata are dynamically loaded from a CSV file.

## Project Structure 
The project utilizes a single app structure to handle all functionality:

```
JOURNEYMAP/
├── journey/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── mapapp/
│   ├── migrations/
│   │   └── __init__.py
│   ├── static/
│   │   └── mapapp/
│   │       └── coordinates.csv
│   ├── templates/
│   │   └── journey_map.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── .gitignore
├── README.md
├── db.sqlite3
├── manage.py
├── venv/
```

## Installation

1. Clone the repository:
   ```
   git clone git@github.com:Bluee21/BARBADOS_1763_VOYAGE_MAP.git
   ```
2. Navigate to the project directory:
   ```
   cd BARBADOS_1763_VOYAGE_MAP/journey 
   ```
3. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the required packages:
   ```
   pip3 install --upgrade -r requirements.txt
   ```   
5. Run the development server:
   ```
   python3 manage.py runserver
   ```

## Usage 

How to Interact

- **Click on a Location**: Clicking a location in the side panel will zoom the map to that point and open a popup with additional details.
- **View Coordinates**: Each location has a link to view the exact latitude, longitude, or both in a new tab.
- **Route Path**: The locations are sorted by the nearest neighbor algorithm and connected with a polyline on the map. You can see the path between coordinates with arrows along the route.