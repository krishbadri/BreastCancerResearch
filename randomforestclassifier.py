from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix

rf_model = RandomForestClassifier(
    n_estimators=150,
    random_state=42,
    verbose=True
)

kfold = KFold(n_splits=5, shuffle=True, random_state=42)
cv_results = cross_val_score(rf_model, x_train, y_train, cv=kfold, scoring='accuracy')

print("Cross-Validation Scores:", cv_results)
print("Mean Accuracy:", cv_results.mean())
