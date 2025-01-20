# Car Sales Advertisements

## Table of Contents
1. [Project Overview](#Project-Overview)
2. [Live Demo](#live-demo)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Installation](#installation)
   1. [Prerequisites](#prerequisites)
   2. [Steps](#steps)
6. [Usage](#usage)
7. [Known Issues](#known-issues)
   1. [Menu Navigation](#menu-navigation)
   2. [Minimizing & Expanding the Expanders](#minimizing--expanding-the-expanders)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact](#contact)

## Project Overview
This project is a tool to simulate random events and visualize various aspects of car sales advertisements. It uses Streamlit for the interactive web interface, along with several data visualization libraries to create informative charts and plots.

## Live Demo
You can access the live version of the app [here](https://car-ads-byzt.onrender.com).
![Main](https://github.com/user-attachments/assets/a96d474b-0817-4546-8373-a2c1e64e8e45)


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
  - `plotly.express` and `plotly.graph_objects`: For creating interactive plots and charts

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

### Minimizing & Expanding the Expanders
At the moment, there is a bug affecting the minimization and expansion of all expanders. For the minimize function to work, all expanders must first have beeen expanded. Likewise, If all expanders are manually minimized, the 'Expand All' button will not work as expected. This issue is being addressed and will be resolved in a future release.

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
For any questions or feedback, please contact hala.francis@gmail.com
