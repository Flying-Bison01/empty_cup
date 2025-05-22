🧱 EmptyCup Assignment – Interior Designers Listing
This project is a full stack web application for listing interior designers. It supports features like viewing designer details, shortlisting designers, hiding listings, and more. This is built for the EmptyCup assignment as a mobile-first web application.

🌐 Live Demo
Frontend: [Link to deployed frontend]

Backend: [Link to deployed backend API]


📦 Backend Setup (Flask)
# 1. Navigate to the backend folder
cd backend

# 2. Install dependencies
pip install flask flask-cors

# 3. Run the Flask server
python app.py


📦 Frontend Setup
# 1. Navigate to the frontend folder
cd frontend

# 2. Run the on the live server
Just click on live-server.



🛠️ API Endpoints
Method	Endpoint	Description
GET	/designers	Get all visible designers
GET	/designers/<id>	Get a specific designer
POST	/designers/<id>/shortlist	Toggle shortlist status
POST	/designers/<id>/hide	Hide the designer from listings



✨ Tech Stack
Frontend: HTML, Tailwind CSS, Vanilla JS

Backend: Flask (Python)

Deployment: Netlify / Render 


👨‍💻 Author
Adnan Saifi


📃 License
This project is licensed for assignment/demo use only.