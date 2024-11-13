import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer

data = pd.read_csv("Heart.csv")

s1 = SimpleImputer(strategy="most_frequent")
data["Ca"] = s1.fit_transform(data[["Ca"]])

x = data.drop(columns=["number", "AHD"])
y = data["AHD"]

categoricalcolumns = ["ChestPain", "Thal"]
numericalcolumns = ["Age", "Sex", "RestBP", "Chol", "Fbs", "RestECG", "MaxHR", "ExAng", "Oldpeak", "Slope", "Ca"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat_encode", OneHotEncoder(), categoricalcolumns),
        ("num_scale", StandardScaler(), numericalcolumns)
    ],
    remainder="passthrough"
)

xtransformed = preprocessor.fit_transform(x)

le = LabelEncoder()
ytransformed = le.fit_transform(y)

accuracies = []

seeds = range(1, 11)
neighbors = range(1, 243)
for seed in seeds:
    xtrain, xtest, ytrain, ytest = train_test_split(xtransformed, ytransformed, test_size=0.2, random_state=seed)
    
    for k in neighbors:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(xtrain, ytrain)
        
        ypred = knn.predict(xtest)
        accuracy = accuracy_score(ytest, ypred)
        
        accuracies.append((seed, k, accuracy))

maxaccuracy = max(accuracies, key=lambda x: x[2])
minaccuracy = min(accuracies, key=lambda x: x[2])

print("\nAll Accuracies:")
for seed, k, accuracy in accuracies:
    print(f"Seed: {seed}, k: {k}, Accuracy: {accuracy:.4f}")

print(f"\nHighest Accuracy: Seed: {maxaccuracy[0]}, k: {maxaccuracy[1]}, Accuracy: {maxaccuracy[2]:.4f}")
print(f"Lowest Accuracy: Seed: {minaccuracy[0]}, k: {minaccuracy[1]}, Accuracy: {minaccuracy[2]:.4f}")

bestseed = [seed for seed, k, accuracy in accuracies if accuracy == maxaccuracy[2]]
worstseed = [seed for seed, k, accuracy in accuracies if accuracy == minaccuracy[2]]

print(f"Highest accuracy is at seed{bestseed}")
print(f"Lowest accuracy is at seed{worstseed}")
