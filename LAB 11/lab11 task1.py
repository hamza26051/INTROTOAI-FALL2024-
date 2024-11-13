import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,StandardScaler
from sklearn.impute import SimpleImputer

data = pd.read_csv("Heart.csv")

s1 = SimpleImputer(strategy="most_frequent")

data["Ca"] = s1.fit_transform(data[["Ca"]])

print(data.info())


x=data.drop(columns=["number", "AHD"])
y=data["AHD"]

categoricalcolumns=["ChestPain","Thal"]
numericalcolumns=["Age","Sex","RestBP", "Chol", "Fbs", "RestECG", "MaxHR", "ExAng", "Oldpeak", "Slope", "Ca"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat_encode", OneHotEncoder(), categoricalcolumns),
        ("num_scale", StandardScaler(), numericalcolumns)
    ],
    remainder="passthrough"
)

xtransformed = preprocessor.fit_transform(x)
le=LabelEncoder()
ytransformed=le.fit_transform(y)
xtrain,xtest,ytrain,ytest=train_test_split(xtransformed,ytransformed, test_size=0.2, random_state=42)

accuracies=[]
neighbors=range(1,243)

for k in neighbors:
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(xtrain,ytrain)
    ypred=knn.predict(xtest)
    accuracy=accuracy_score(ytest,ypred)
    accuracies.append(accuracy)

maxaccuracy=max(accuracies)
minaccuracy=min(accuracies)

print(maxaccuracy)
print(minaccuracy)

best_k = [neighbors[i] for i, acc in enumerate(accuracies) if acc == maxaccuracy]
worst_k = [neighbors[i] for i, acc in enumerate(accuracies) if acc == minaccuracy]

print(f"highest accuracy is at k{best_k}")

print(f"lowest accuracy is at k{worst_k}")



