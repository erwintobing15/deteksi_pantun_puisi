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
How to run this project and install it locally:
1. Clone the project
```
git clone https://github.com/erwintobing15/deteksi_pantun_puisi.git
cd deteksi_pantun_puisi
```
2. Create virtualenv or you can go ahead to step 3 without creating virtualenv
```
# using conda
conda create -n newenv
conda activate newenv or activate newenv
```
```
# using pip as administrator
pip install virtualenv
virtualenv newenv
newenv\Scripts\activate or source newenv/bin/activate
```
3. Install all dependencies
```
pip install -r requirements.txt
```
4. Run server
```
python manage.py runserver
```
5. Deactivate and delete virtualenv (if you created one)
```
# deactivate virtualenv
conda deactivate or deactivate

# delete virtualenv using conda
conda env remove --name newenv

# there is no command to delete virtualenv using pip, so we need to delete it manually
```
