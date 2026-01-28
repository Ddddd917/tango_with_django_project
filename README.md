

# Rango: A Tango with Django 2 Project

> "Rango says... hello world!" 
> 
> 

This repository contains the **Rango** web application, developed as part of the **Web Application Development 2 (WAD2)** course at the **University of Glasgow**. The project is a hands-on implementation based on the book *Tango with Django 2: A beginner's guide to web development* by Leif Azzopardi and David Maxwell.

---

## 🚀 Project Overview

Rango is a directory-based web application that allows users to browse through user-defined categories to access various web pages. The application follows a 3-tier system architecture consisting of a Client (Web Browser), Middleware (Django), and a Database (SQLite).

### Core Features

* **Category Management**: View, create, and browse categories.


* **Page Links**: Access external links associated with specific categories.


* **User Engagement**: Track page views and "likes" for categories.


* **Authentication**: User registration and login functionality (to be implemented in later chapters).



---

## 🛠 Tech Stack

The development environment is strictly configured to match the course assessment criteria:

* **Language**: Python 3.11 


* **Framework**: Django 2.2.28 (LTS) 


* **Database**: SQLite3 


* **Libraries**: Pillow (for image handling) 


* **Environment Management**: Anaconda/Conda 



---

## 💻 Local Setup Instructions

To get this project running on your local machine, follow these steps:

1. **Clone the Repository**
```bash
git clone https://github.com/<your-username>/tango_with_django_project.git
cd tango_with_django_project

```


2. **Activate the Environment**
Ensure you have the `rango` conda environment active:


```bash
conda activate rango

```


3. **Verify Dependencies**
Ensure Django 2.2.28 and Pillow are installed:


```bash
pip install django==2.2.28 pillow

```


4. **Run the Development Server**
```bash
python manage.py runserver

```


Access the site at `http://127.0.0.1:8000/`.



---

## 📁 Project Structure

This project follows the directory structure required for automated testing:

```text
tango_with_django_project/       <-- Git Repository Root
[cite_start]├── manage.py                     <-- Django management script [cite: 147, 302]
[cite_start]├── db.sqlite3                    <-- Local database (ignored by Git) [cite: 143, 144]
[cite_start]├── .gitignore                    <-- Git exclusion rules [cite: 108, 144]
├── README.md                     <-- Project documentation
[cite_start]└── tango_with_django_project/    <-- Project configuration folder [cite: 147]
    [cite_start]├── settings.py               <-- Project settings [cite: 148]
    [cite_start]├── urls.py                   <-- URL declarations [cite: 148, 303]
    [cite_start]└── wsgi.py                   <-- WSGI config [cite: 148]

```

---



## 🤝 Credits



* **Course**: Web Application Development 2 (WAD2), University of Glasgow.


