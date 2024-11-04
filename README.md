# iCropMap

Welcome to iCropMap! This project provides an interactive map to visualize crop data across different states and counties in the USA.

## Features

- Interactive map displaying crop data by state and county
- Choropleth layers to visualize crop data intensity
- Custom popups with detailed information
- Scoreboard displaying crop data statistics

## Prerequisites

- Python 3.x
- Virtual environment (venv)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Seth-Keenan/iCropMap
    cd iCropMap
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    ```

3. **Activate the virtual environment:**

    - On macOS and Linux:

        ```sh
        source venv/bin/activate
        ```

    - On Windows:

        ```sh
        .\venv\Scripts\activate
        ```

4. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **API Key:**

    Retrieve an API key from the USDA Crop Statistic API, and create a config.py file and input "API_KEY=[your api key here]"

2. **Start the FastAPI server:**

    ```bash
    fastapi run
    ```

3. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:8000
    ```

## Endpoints

- **Home Page:**

    ```
    GET /
    ```

    Displays the main page with the interactive map.

- **Map Page:**

    ```
    GET /map?crop=<crop>&year=<year>
    ```

    Displays the map with crop data for the specified crop and year.

- **County Map Page:**

    ```
    GET /county_map
    ```

    Displays the county-level map.

- **Contact Page:**

    ```
    GET /contact
    ```

    Displays the contact page.

## Project Structure

- **main.py:** FastAPI application setup and endpoints.
- **map.py:** Map generation and data processing.
- **data.py:** Data fetching and processing.
- **static/**: Static files (CSS, JS, images).
- **templates/**: HTML templates.

## Acknowledgements

- [Folium](https://python-visualization.github.io/folium/) for interactive maps
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework

## Contact

For any questions or inquiries, please contact [sethkeenan6@gmail.com](mailto:sethkeenan6@gmail.com).