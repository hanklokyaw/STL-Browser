# STL Browser App

This Flask application allows users to search for 3D models based on SKU or descriptions and preview them in the browser.


## Features

- Dynamic Search: Search by SKU or description with exact or wildcard matching.
- 3D Model Viewer: View STL files directly in the browser using Three.js.


## Installation

1. Clone the repository:
```bash
git clone https://github.com/hanklokyaw/STL-Browser.git
cd stl-browser
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```


## Additional Information

We extend our gratitude to the THREE team for their invaluable contribution in enabling this application to display STL files directly in the browser. Users interested in exploring more about this technology can visit the THREE.js library for further details.


## Customizing the Application

To customize the application, users can edit the SKU_Description.csv file to modify file names and descriptions associated with the STL files. It is essential to ensure that the updated entries accurately correspond to the correct STL filenames to maintain the application's functionality.
