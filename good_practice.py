import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load data and split with stratification and a random state
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Create a pipeline with a scaler and a classifier
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier(random_state=42))
])

# Define a parameter grid for GridSearchCV
param_grid = {
    'clf__n_estimators': [50, 100],
    'clf__max_depth': [10, 20],
}

# Find the best model using GridSearchCV (which includes cross-validation)
grid_search = GridSearchCV(pipeline, param_grid, cv=3)
grid_search.fit(X_train, y_train)

# Evaluate the best model with a classification report
print(f"Best parameters: {grid_search.best_params_}")
y_pred = grid_search.predict(X_test)
print(classification_report(y_test, y_pred))