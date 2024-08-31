from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


svm_model = SVC(kernel='linear') 
svm_model.fit(x_train, y_train)
svm_pred = svm_model.predict(x_test)

svm_accuracy = accuracy_score(y_test, svm_pred)
print("SVM Accuracy:", svm_accuracy)
