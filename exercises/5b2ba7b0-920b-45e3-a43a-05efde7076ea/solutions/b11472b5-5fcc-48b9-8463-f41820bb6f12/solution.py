from sklearn.tree import DecisionTreeClassifier
import numpy as np # Training data
X = np.array([ [2.5, -1.2], # temp_anomaly, precip_anomaly [-0.8, 2.3], [0.1, 0.2], [2.8, -1.5], [-0.5, 2.1]
])
y = ['Drought', 'Flood', 'Normal', 'Drought', 'Flood'] # Create and train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y) # New conditions to predict
new_conditions = np.array([ [2.3, -1.1], # Hot and dry [-0.3, 1.8] # Cool and wet
]) # Make predictions
predictions = model.predict(new_conditions) print("Weather Pattern Predictions:")
for i, pred in enumerate(predictions, 1): print(f"Scenario {i}: {pred}")