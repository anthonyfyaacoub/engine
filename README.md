# Steam Recommendation Engine

This repository contains the code for a Steam game recommendation engine. It uses data from the Steam platform, processes it, and provides personalized game recommendations based on user preferences.

# Features

API for data extraction: Retrieves Steam data, such as user play history and game details.
Data preparation: Cleans and organizes the data for further processing.
Data preprocessing: Transforms the data into a suitable format for training the recommendation model.
Data modeling: Trains a recommendation model using the LightFM library with BPR Loss, WARP Loss, and SVD.
Frontend: A user-friendly interface to input a user ID and view recommended games.
Backend: Handles model deployment and serves game recommendations.
# Prerequisites

To run this project locally, you will need:

Python 3.7 or higher
A Steam API key (obtainable from Steam's API page)
# Installation

Clone the repository:
bash
Copy code
git clone https://github.com/JPB22/steam-recommendation-engine.git
Change directory to the project folder:
bash
Copy code
cd steam-recommendation-engine
Create a virtual environment:
Copy code
python -m venv venv
Activate the virtual environment:
On Windows:
Copy code
venv\Scripts\activate
On Linux/macOS:
bash
Copy code
source venv/bin/activate
Install the required packages:
Copy code
pip install -r requirements.txt
Create a .env file in the root directory of the project and add your Steam API key:
makefile
Copy code
STEAM_API_KEY=your_api_key_here
3 Usage

### Start the backend server:
bash
Copy code
python backend/app.py
### In a new terminal window, start the frontend:
bash
Copy code
cd frontend
npm install
npm start
Open your browser and navigate to http://localhost:3000.
Enter a Steam user ID and click "Get Recommendations" to see the recommended games.


# Important Links 

APIs:

Steamspy api -> [https://partner.steamgames.com/doc/webapi](https://steamspy.com/api.php)

Project:

Project Template -> https://github.com/miguelgfierro/project_template


# Sources:

· https://github.com/nadinezab/video-game-recs
