import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

clf = MLPClassifier(random_state=1, max_iter=50, verbose=True, activation='logistic')
clf.fit(x_train, y_train)
pred = clf.predict(x_test)

accuracy = accuracy_score(y_test, pred)
print(f"MLP Classifier Accuracy: {accuracy}")

plt.plot(clf.loss_curve_)
plt.title('Loss Curve')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.show()
