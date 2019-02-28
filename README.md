# College Admission Predictor and Smart List Generator (CAPSLG)


[![Python Version](https://img.shields.io/pypi/pyversions/Django.svg?style=for-the-badge)](https://www.python.org/downloads/)
[![Issues](https://img.shields.io/github/issues/raoniz/CAPSLG.svg?style=for-the-badge)](https://github.com/raoniz/CAPSLG/issues)
![Language Count](https://img.shields.io/github/languages/count/raoniz/CAPSLG.svg?style=for-the-badge&color=orange)
[![Requirements](https://img.shields.io/requires/github/raoniz/CAPSLG.svg?style=for-the-badge)](https://github.com/raoniz/CAPSLG/blob/master/requirements.txt)
![Top Language](https://img.shields.io/github/languages/top/raoniz/CAPSLG.svg?style=for-the-badge&color=red&label=html%20used)
[![License: GPL-2.0](https://img.shields.io/badge/License-GPL--3.0-success.svg?style=for-the-badge)](https://opensource.org/licenses/GPL-3.0)
![Size](https://img.shields.io/github/repo-size/raoniz/CAPSLG.svg?style=for-the-badge&color=yellow)



A Django based web-project to compute probability of a student to secure admission in an Engineering college within the Mumbai region.

----

## Pre-requisites

* Python 3.6+ (If not available, kindly download from [here](https://www.python.org/downloads/))
* Python Virtual Environment (optional), install virtual environment using:

  ```console
  pip install virtualenv
  ```

**Note**: *Virtual Environment isolates your project from other installed python packages thus, preventing package version dependencies.*

## Configuration

0. Start python virtual enviroment. (optional)
    1. Create environment.

      ```console
      virtualenv [environment_name]
      ```

    2. Activate environment.
  
      ```console
      cd [environment_name]      
      \Scripts\activate
      ```
1. Create a folder named *mysite* in the [*environment_name*] folder.
2. Clone or download the repository inside the *mysite* folder.

      ```console
      cd mysite
      git clone https://github.com/raoniz/CAPSLG.git
      ```
       
3. Install all the required python packages.

      ```console
      pip install -r requirements.txt
      ```
      
4. Run the server.
      ```console
      python manage.py runserver
      ```

5. Visit the local server at `http://localhost:8000/index/`
