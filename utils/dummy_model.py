from sklearn.dummy import DummyClassifier
import joblib

model = DummyClassifier(strategy="most_frequent")
model.fit([[0], [1], [1]], [0, 1, 1])

joblib.dump(model, "models/feedback_model.joblib")

