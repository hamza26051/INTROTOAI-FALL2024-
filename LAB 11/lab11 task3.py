import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import confusion_matrix

names = [
    "erythema", "scaling", "definite-borders", "itching", "koebner phenomenon", "polygonal papules", "follicular papules", 
    "oral-mucosal involvement", "knee elbow involvement", "scalp involvement", "family history", "melanin incontinence", 
    "eosinophils in the infiltrate", "pnl infiltrate", "fibrosis of the papillary dermis", "exocytosis", "acanthosis", "hyperkeratosis", 
    "parakeratosis", "clubbing of the rete ridges", "elongation of the rete ridges", "thinning of the suprapapillary epidermis", 
    "spongiform pustule", "munro microabcess", "focal hypergranulosis", "disappearance of the granular layer", 
    "vacuolisation and damage of the basal layer", "spongiosis", "saw-tooth appearance of retes", "follicular horn plug", 
    "perifollicular parakeratosis", "inflammatory monoluclear infiltrate", "band-like infiltrate", "age", "class"
]

data = pd.read_csv("dermatology.data", names=names)
data.replace('?', pd.NA, inplace=True)
data = data.apply(pd.to_numeric, errors='ignore')
x = data.drop(columns=["class"])
y = data["class"]
imputer = SimpleImputer(strategy='most_frequent')
ximputed = imputer.fit_transform(x)
kn = KNeighborsClassifier(n_neighbors=5)
cv_score = cross_val_score(kn, ximputed, y, cv=10)
print(f"Cross-validation mean score: {cv_score.mean()}")
xtrain, xtest, ytrain, ytest = train_test_split(ximputed, y, test_size=0.3, random_state=42)
kn.fit(xtrain, ytrain)
ypred = kn.predict(xtest)
cm = confusion_matrix(ytest, ypred)
print("Confusion Matrix:\n", cm)
