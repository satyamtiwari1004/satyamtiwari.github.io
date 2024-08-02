# 🌟 Satyam Rajesh Tiwari's Portfolio 🌟

Welcome to my personal portfolio! This web application showcases my skills, projects, and professional journey, all built with the power of Python, Django, and AWS.

![Portfolio Screenshot](https://satyam-portfolio-24.s3.ap-south-1.amazonaws.com/img/Portfolio+Snapshot.png)

## 🚀 About Me

Hi, I'm Satyam Rajesh Tiwari! I'm a passionate software developer with a strong background in computer science. My portfolio reflects my journey, projects, and the skills I've honed over the years.

## 🎨 Features

- **Interactive Design:** A clean and modern UI/UX to provide an engaging experience.
- **Project Showcase:** Detailed descriptions and live demos of my projects.
- **Blog:** Insights and articles on tech trends, programming tips, and more.
- **Contact Form:** Get in touch with me directly through the website.

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Deployment:** AWS (EC2, S3, RDS)

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip
- virtualenv
- PostgreSQL

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/satyamtiwari1004/portfolio.git
   cd portfolio
2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  
   
3. **Install the dependencies:**

   ```bash 
   pip install -r requirements.txt

4. **Set up the .env file:**

   Create a .env file in the root directory of the project and add the following variables with your specific details:

   ```bash 
   SECRET_KEY=your_secret_key
   AWS_PRIVATE_KEY=your_aws_private_key
   AWS_SESSION_KEY=your_aws_session_key
   EMAIL_HOST=your_email_host
   EMAIL_PORT=your_email_port
   EMAIL_HOST_USER=your_email_user
   EMAIL_HOST_PASSWORD=your_email_password
   
5. **Apply the migrations:**

   ```bash
   python manage.py migrate

6. **Create a superuser (optional, for accessing the Django admin interface):**

   ```bash
   python manage.py createsuperuser

7. **Run the development server:**

   ```bash
   python manage.py runserver

8. **Access the application:**
Open your web browser and go to http://127.0.0.1:8000/ to view the application.

## Usage

1.	Register an account or log in if you already have one.
2.	Add the URLs of the products you want to track.
3.	Set your desired price thresholds for the products.
4.	Wait for email notifications when the prices drop below your thresholds.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

1.	Fork the repository
2.	Create your feature branch (git checkout -b feature/your-feature)
3.	Commit your changes (git commit -am 'Add some feature')
4.	Push to the branch (git push origin feature/your-feature)
5.	Create a new Pull Request
	
## License   

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the LICENSE file for details.
