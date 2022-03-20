## Build the model
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
### Create the estimator

estimator = XGBClassifier(objective =
                          'binary:logistic',
                          nththread = 6,
                          seed = 45,
                         silent = True)

parameters = {
    'max_depth': range(9, 11, 1),
    'n_estimators': range(1000, 1200, 50),
    'learning_rate': [0.01, 0.005]
}

grid_search = GridSearchCV(
    estimator=estimator,
    param_grid=parameters,
    scoring = 'roc_auc',
    n_jobs = 1,
    cv = 3,
    verbose=True
)

print("Estimator: ",estimator,'\n \n Parameters: ', parameters, '\n \n Grid search parameters: ', grid_search)

## Fit the model to the train Data 
%timeit grid_search.fit(X_train_SMOTE, y_train_SMOTE)
