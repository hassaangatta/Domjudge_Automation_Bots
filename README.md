<a name="readme-top"></a>

<!-- PROJECT LOGO -->
# Domjudge Automation Bots

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation and usage">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project consists of the web automation scripts involved in uploading test cases and participant teams' data to Domjudge online coding judge for Procom'23 and ACM Devday'23, held at FAST NUCES Karachi.

### Built With
<!-- <br> -->

* Python 3.x
* Selenium webdriver
* Openpyxl

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Python 3.x
* * For Linux (Debian-based):
  ```sh
     apt install python3
  ```
* * For Windows:<br>
  Download the latest version of <a href="https://www.python.org/downloads/">Python 3</a><br  >
  Also, make sure to check the "Add to PATH" option while installing.

* Selenium webdriver
  ```sh
     pip install selenium
  ```
* Openpyxl
  ```sh
     pip install openpyxl
  ```

### Usage

1. Clone the repo
   ```sh
   git clone https://github.com/hassaangatta/Domjudge_Automation_Bots
   ```
3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. * Configure the server IP and admin password as well as the path to excel spreadsheet in User_Accounts.py file.
   * Configure the server IP, admin password as well as the problem ID and path to testcases directory in Testcases.py file.


5. Run both programs using their respective names.
   ```sh
   python3 User_Accounts.py
   python3 Testcases.py
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Hassaan Gatta - hassaangatta@gmail.com

Linkedin - [Profile](https://www.linkedin.com/in/hassaan-gatta-047865257/)

Project Link: [Domjudge Automation Bots](https://github.com/hassaangatta/Domjudge_Automation_Bots)

<p align="right">(<a href="#readme-top">back to top</a>)</p>