# CRPS-FocusUs
### Cardio Risk Prediction System (CRPS) is a web-based Machine Learning Project with a user-friendly interface that is built with Django. It predicts whether the patient has heart disease or not using Machine Learning (ML) Algorithm Logistic Regression. 

#### In CRPS data is extracted from the patient which includes different 13 parameters like blood pressure, age, sex, etc. This data is then fed to the trained model which provides the outcome in the form of probability ranging value 0-1.

####  In CRPS data is extracted from the patient which includes different 13 parameters like blood pressure, age, sex, etc. This data is then fed to the trained model which provides the outcome in the form of probability ranging value 0-1.

#### 13 different attributes are :
![Attributes](https://focusustech.com/media/tinymce/13-attributes-of-hdps.jpg)

### How to run the project :
#### Install python and its libraries NumPy, Pandas and Sklearn along with Django. 
```
pip install django sklearn
```
#### Run following commands
```
python manage.py collectstatic
python manage.py makemigrations 
python manage.py migrate
python manage.py createsuperuser
```
#### To run the server type the following command
    python manage.py runserver
