from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
import joblib
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
from sklearn.preprocessing import MinMaxScaler

def generate_features(row):
    values = np.array(row['values'])
    date = np.array(row['dates'])
    id = np.array(row['id'])
    return {
        'mean': np.mean(values),
        'std': np.std(values),
        'min': np.min(values),
        'max': np.max(values),
        'median': np.median(values),
        'skew' : skew(values),
        'kurtosis' : kurtosis(values),
        'date' : date,
        'id' : id
    }


test = pd.read_parquet('test.parquet', engine='pyarrow')
pre_features = test.apply(generate_features, axis=1, result_type='expand')
pre_features_without_date = pre_features.drop(['date'], axis=1)
for col in pre_features_without_date.columns:
    pre_features_without_date.fillna(pre_features_without_date[col].mean(), inplace=True)
id = pre_features_without_date['id']
scaler = MinMaxScaler()
scaled_pre_features_without_date_array = scaler.fit_transform(pre_features_without_date)
scaled_pre_features_without_date_data = pd.DataFrame(data = scaled_pre_features_without_date_array, columns=pre_features_without_date.columns)
X = scaled_pre_features_without_date_data.drop(['id'], axis=1)
X['id']  = id
X.set_index('id', inplace=True)
model = joblib.load('random_forest_model.pkl')
y_pred_proba = model.predict_proba(X)
submission = pd.DataFrame({'id': id, 'pred' : y_pred_proba[:, 1]})
submission.to_csv('submission.csv', index=False)