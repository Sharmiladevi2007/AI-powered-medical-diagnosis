from sklearn.linear_model import logisticregression
from sklearn.metrics import accuracy_score , confusion_matrix,classification_report

model= logisticregression()

model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,_pred)
print(f"accuracy: {accuacy * 100:.2f}%")

print("Confusion matrix:")
print(confusion_matrix(y_test,y_pred))
print("Classififcation report:")
print(classification report(y_test,y_pred))

