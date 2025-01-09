STL Browser App

This Flask application allows users to search for 3D models based on SKU or descriptions and preview them in the browser.

Features

Dynamic Search: Search by SKU or description with exact or wildcard matching.

3D Model Viewer: View STL files directly in the browser using Three.js.

Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/stl-browser.git
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


Additional Information

Thanks to the THREE team members who make this app possible to display STL files on the browser. If the user is interested, they could visit the THREE library for more information.



Customizing the Application

Users can modify the file names and descriptions associated with the STL files by editing the SKU_Description.csv file. Ensure that the changes accurately point to the correct STL filenames to maintain functionality.
