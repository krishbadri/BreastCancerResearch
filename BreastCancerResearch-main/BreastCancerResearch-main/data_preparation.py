from sklearn.model_selection import train_test_split

label_mapping = {'benign': 0, 'malignant': 1, 'normal': 2}
y_val = []
for label in y:
    y_val.append(label_mapping[label])

x_train, x_test, y_train, y_test = train_test_split(
    x.reshape(len(x), -1),  
    y_val,
    test_size=0.25,
    random_state=42
)
