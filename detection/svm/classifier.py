import pickle

model = pickle.load(open("detection/svm/classifier.sav", "rb"))
vectorizer = pickle.load(open("detection/svm/vectorizer.sav", "rb"))

def get_poem_type(poem):
    """
    Function to classify input poem as pantun or puisi,
    received text poem as parameter and return poem type
    """
    if len(poem) == 0:
        return False
    vectorized_poem =  vectorizer.transform([poem])
    poem_type = model.predict(vectorized_poem)

    return poem_type[0]
