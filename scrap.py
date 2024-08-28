import pandas as pd
import pickle
# Load the model and label encoder from the pickle file
with open('./models/mic_classification_best.pkl', 'rb') as file:
    model_and_encoder = pickle.load(file)

model = model_and_encoder['model']
label_encoder = model_and_encoder['label_encoder']

# Load the test set
test_set = pd.read_csv('./test_sets/MIC_test_set.csv')

# Ensure categorical columns are properly formatted
categorical_columns = test_set.select_dtypes(include=['object']).columns

# Convert the categorical columns to 'category' dtype
for col in categorical_columns:
    test_set[col] = test_set[col].astype('category')

# Separate the features and target for the entire test set
X_test = test_set.drop(columns=['MIC'])
y_test = test_set['MIC']

# Select the first test example
test_example_x = X_test.iloc[[0]]  # Ensure it's a DataFrame
test_example_y = y_test.iloc[0]

# Predict the test example
y_pred = model.predict(test_example_x)

# Decode the predicted label
y_pred_decoded = label_encoder.inverse_transform(y_pred)
# Decode the actual label
test_example_y_decoded = label_encoder.inverse_transform([test_example_y])[0]

print(f"Predicted: {y_pred_decoded[0]}, Actual: {test_example_y_decoded}")