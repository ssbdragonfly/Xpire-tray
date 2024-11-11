# Xpire Tray

A smart food management system that helps track food expiration dates and provides nutritional assessments using image recognition.

### Project Overview

Xpire Tray is an app built with CustomTkinter that helps users manage their food inventory and track expiration dates across different storage locations (pantry, fridge, freezer). It includes features for both manual entry and image-based food recognition, along with nutritional analysis capabilities.

### Key Features

1. **Food Storage Management**
   - Track food items across multiple storage locations
   - Automated expiration date monitoring
   - Desktop notifications for items nearing expiration
   - Support for different storage conditions (pantry, fridge, freezer)

2. **Smart Food Recognition**
   - Image-based food identification using LogMeal API
   - Automatic nutritional information extraction
   - Support for multiple image formats (PNG, JPEG, SVG, JFIF)

3. **Nutritional Assessment**
   - Comprehensive nutrition analysis
   - Health index calculation
   - Recommendations for dietary adjustments
   - Tracking of key nutrients (carbs, sugar, sodium, protein, fat)

### Technologies Used

- **Frontend**: CustomTkinter
- **Image Processing**: LogMeal API
- **Notification System**: Plyer
- **Data Storage**: Pickle-based (local)
- **More Libraries**: Requests, CTkMessagebox

### Installation

1. Clone the repository
`git clone https://github.com/ssbdragonfly/Xpire-tray`
`cd Xpire-tray`
2. Install dependencies:
`bash`
`pip install r-requirements.txt`

### Usage

1. Start the application:
`bash`
`python main.py`

2. Add food items either by:
   - Entering comma-separated names in the text field
   - Using the "Choose file" button to upload food images
   - Using the "Nutrition Assessment" button for detailed analysis

3. Follow the prompts to specify storage locations and view expiration notifications

### Data Structure

The application uses a CSV database (`foods.csv`) containing detailed information about:
- Storage durations for different conditions
- Expiration timelines
- Storage recommendations
- Food categories and keywords

### Future Development

1. **Database Expansion**
   - Add more food items and categories
   - Include additional storage conditions
   - Expand nutritional information

2. **User Interface Improvements**
   - Visual representation of food storage locations
   - Interactive expiration timeline
   - Customizable notification settings

3. **Feature Additions**
   - Recipe recommendations based on expiring items
   - Shopping list generation
   - Meal planning integration
