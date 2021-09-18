# deteksi_pantun_puisi

This is a machine learning web based application that can detect type of indonesian poem between *pantun* 
and *puisi* from a text poem. The project was built using django with it's detection feature built with SVM model [poem-type-classification](https://github.com/erwintobing15/poem-type-classification).

## Technologies 
This project is created with:
* Python 3.9.1
* Django 3.2.6
* Anaconda 4.10.3
* Scikit-learn 0.24.2
* Bootstrap 5.1.1

## Setup 
To run this project, install it locally using conda:
```
conda create -n django-env python=3.9.1 anaconda  
conda activate django-env
conda install -c anaconda django 
python manage.py runserver 
```