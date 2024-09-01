<div align="center">
     <h1 align="center">Bill Master</h1>
     <img src="https://github.com/user-attachments/assets/ad0eb4e7-7103-415d-96b9-2b1052edd6f5" height=90px width=90px/>
     <br/>
     <br/>
     <img alt="Static Badge" src="https://img.shields.io/badge/Python-red?style=for-the-badge&logo=python&logoColor=white">
     <img alt="Static Badge" src="https://img.shields.io/badge/Tkinter-darkblue?style=for-the-badge">
     <img alt="Static Badge" src="https://img.shields.io/badge/GUI%20Application-darkgreen?style=for-the-badge">
     <br/>
     <br/>
     <!-- Open Source -->
     <img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103">
     <br/>
     <!-- Contributions -->
     <img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=#013220">
     <!-- Built By -->
     <img src="https://img.shields.io/badge/Built%20by-Abhinav%20Kumar-0059b3">
     <!-- Maintained -->
     <img src="https://img.shields.io/static/v1.svg?label=Maintained&message=Yes&color=red">
     <br/>
     <!-- --------------------------------------------- -->
     <br/>
     <!-- License -->
     <img alt="GitHub License" src="https://img.shields.io/github/license/abhinavkumar2369/Bill-Master">
     <br/>
     <!-- Commit Count -->
     <img alt="GitHub commit activity (branch)" src="https://img.shields.io/github/commit-activity/t/abhinavkumar2369/Bill-Master/main">
     <!-- Repo Size -->
     <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/abhinavkumar2369/Bill-Master?style=flat&color=orange">
     <!-- Repo Code -->
     <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/abhinavkumar2369/Bill-Master">
     <br/>
     <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/abhinavkumar2369/Bill-Master?style=flat&color=orange">
     <!-- Language Count -->
     <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/abhinavkumar2369/Bill-Master">
     <!-- Watchers -->
     <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/abhinavkumar2369/Bill-Master?style=flat">
     <!-- Forks -->
     <img alt="GitHub forks" src="https://img.shields.io/github/forks/abhinavkumar2369/Bill-Master?style=flat&color=orange">
     <br/>
     <img alt="GitHub Release" src="https://img.shields.io/github/v/release/abhinavkumar2369/Bill-Master">
</div>

<!------------------------------------------------->

## Overview 💫
- Bill Master is a comprehensive billing application designed to streamline the billing process.
- It features a user-friendly login interface and various functionalities to manage billing efficiently.

<!------------------------------------------------->

## Features 🌟
- User authentication (login/register)
- Home screen dashboard
- Bill creation and management
- PDF bill generation for printouts
- MongoDB integration for data storage

<!------------------------------------------------->

## Prerequisites 📋
Before you begin, ensure you have met the following requirements:
- Python 3.7+
- pip (Python package manager)
- MongoDB (local installation or Atlas account)

<!------------------------------------------------->

## Installation 🛠️

1. Clone the repository:
   
     ```sh
     git clone https://github.com/abhinavkumar2369/Bill-Master.git
     cd Bill-Master
     ```

2. Install the required dependencies:
   ```sh
   pip install pymongo pillow bcrypt
   ```

<!------------------------------------------------->


## MongoDB Setup 🍃

### Option 1: Local MongoDB Installation
- Download and install MongoDB Community Edition from the official website.
- Start the MongoDB service.
- Update the connection string in the application to use mongodb://localhost:27017.

### Option 2: MongoDB Atlas (Cloud)
- Create a free account on MongoDB Atlas.
- Set up a new cluster and obtain the connection string.
- Replace the placeholder connection string in the application with your Atlas connection string.


<!------------------------------------------------->


## Configuration ⚙️

- Update the connection string in main.py

  ```py
  mongo_uri = "mongodb+srv://<username>:<password>@<cluster-address>/<dbname>?<options>"
  ```
  
- If using MongoDB Atlas, make sure to whitelist your IP address in the Atlas dashboard.


<!------------------------------------------------->


### Running the Application 🚀
- Run the main application file:
     ```python
     python main.py
     ```

<!------------------------------------------------->


## Screenshot 🖼️

### ➡️ Login
![Login](https://github.com/user-attachments/assets/83e6974c-c20c-4f19-9e8f-504dae4843d5)

### ➡️ Register
![Register](https://github.com/user-attachments/assets/92961f06-2891-498e-9aed-3d9bb882b31d)

### ➡️ HomeScreen
![HomeScreen](https://github.com/user-attachments/assets/07d70219-c92c-496d-b4ec-e02666d374c7)

### ➡️ ViewBills
![View Bills](https://github.com/user-attachments/assets/a7f9f55c-2335-4568-aa85-a1332d7c6a00)

### ➡️ Bill PDF (For PrintOut)
![image](https://github.com/user-attachments/assets/b1a5f695-1106-4293-bd07-3253e8518e56)

### ➡️ MongoDb Integration
![Mongo Db ](https://github.com/user-attachments/assets/47cdf9c8-43ae-43da-b7c6-0432a019474f)

<br/>

## Demonstration Video 📽️
[![Watch the video](https://github.com/user-attachments/assets/aad55736-ef21-48d8-8640-522cae3c43ac)](https://github.com/user-attachments/assets/07201489-ef59-47a2-bbd5-42a5d9a895f9)



<!------------------------------------------------->



## Contributions 🧑‍🤝‍🧑
- We welcome contributions from the community!.



<!------------------------------------------------->



## License 🪪
- This project is licensed under the MIT License.
- See the [LICENSE](LICENSE) file for more details.
