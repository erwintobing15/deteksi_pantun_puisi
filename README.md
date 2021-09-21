# deteksi_pantun_puisi

![Screenshoot Web](../assets/demo.PNG?raw=true)

This is a machine learning web based application that can detect type of indonesian poem between *pantun*
and *puisi* from a text poem. This project was built using django and trained SVM machine learning model [poem-type-classification](https://github.com/erwintobing15/poem-type-classification).

## Demo
Check out live demo [here](http://deteksipantunpuisi.pythonanywhere.com/).

## Technologies
This project is created with:
* Python 3.9.1
* Django 3.2.7
* Scikit-learn 0.24.2
* Bootstrap 5.1.1

## Setup
To run this project, open cmd/terminal on project directory and install it locally using conda:
```
conda create -n myenv python==3.9.1 django==3.2.7 scikit-learn==0.24.2
conda activate myenv or activate myenv
python manage.py runserver

conda deactivate
```
or install it using pip as administrator:
```
pip install virtualenv
virtualenv myenv
myenv\Scripts\activate or source myenv/bin/activate

pip install django==3.2.7
pip install scikit-learn==0.24.2
python manage.py runserver

deactivate
```
