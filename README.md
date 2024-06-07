# Car Sales Advertisements

## Description
This project is a tool to simulate random events and visualize various aspects of car sales advertisements. It uses Streamlit for the interactive web interface, along with several data visualization libraries to create informative charts and plots.

## Live Demo
You can access the live version of the app [here](https://car-ads-byzt.onrender.com).

## Features
- Visualize the distribution of vehicle prices, odometer readings, and days listed for sale.
- Understand the distribution of different vehicle conditions.
- Explore relationships between vehicle price and odometer reading, as well as price and cylinder count.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `pandas`: For data manipulation and analysis
  - `streamlit`: For creating the interactive web application
  - `streamlit_option_menu`: For creating a customizable menu in the Streamlit app
  - `altair`: For declarative statistical visualization
  - `plotly.express` and `plotly.graph_objects`: For creating interactive plots and charts
  - `scipy`: For scientific computing

## Installation

### Prerequisites
- Python 3.x
- `pip` package manager

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/haladesigns/car-ads.git
    ```
2. Navigate to the project directory:
    ```bash
    cd your-repo-name
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the project:
    ```bash
    streamlit run app.py
    ```

## Usage
1. Open the terminal and navigate to the project directory.
2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
3. The app will open in your default web browser. You can interact with the visualizations and explore the data on car sales advertisements.

## Known Issues

### Menu Navigation
Currently, the menu navigation is not functional. While the menu items for "Plots," "Correlations," and "Contact" are displayed, selecting them does not trigger the intended actions or navigation. This is a feature that will be implemented in the near future. In the meantime, users can still interact with the visualizations and other functionalities directly through the main interface.


## Contributing
If you would like to contribute to this project, please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please contact datasleuthlabs@gmail.com