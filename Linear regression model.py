import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Step 1: Load the data
# Make sure to adjust the file path as necessary
data = pd.read_csv('House Price India.csv')

# Step 2: Explore the data
print(data.head())
print(data.info())

# Step 3: Preprocess the data
# Select relevant features
features = ['LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'TotalBsmtSF', 
            'GarageCars', 'GarageArea', 'FullBath', 'BedroomAbvGr', 'Neighborhood']
target = 'SalePrice'

# Handle missing values for the selected features
data = data[features + [target]].dropna()

# Split the data into features and target
X = data[features]
y = data[target]

# Step 4: Encoding categorical features
# Use OneHotEncoder for categorical features
categorical_features = ['Neighborhood']
numeric_features = list(set(features) - set(categorical_features))

# Create a ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='mean'), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Step 5: Create a pipeline with preprocessing and model training
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

# Step 6: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Train the model
pipeline.fit(X_train, y_train)

# Step 8: Make predictions and evaluate the model
y_pred = pipeline.predict(X_test)

# Calculate RMSE and R²
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f'Root Mean Squared Error: {rmse}')
print(f'R² Score: {r2}')