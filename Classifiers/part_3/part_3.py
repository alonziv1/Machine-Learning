import pandas as pd
import numpy as np
import verify_gradients
import functions as f

#Creating moon dataset
X_moons, y_moons = f.make_moons1(plot = True)
verify_gradients.compare_gradients(X_moons, y_moons, deltas=np.logspace(-9, -1, 12))
f.train_svm(X_moons, y_moons)

#create relevant dataframe for the svm_clf
train_data= pd.read_csv("train_ds.csv")
test_data= pd.read_csv("test_ds.csv")
f.plot_data(data = train_data , x_label = 'PCR_05',y_label = 'sugar_levels', hue = 'spread', title = "Marginal and joint distribution of PCR_05 and sugar_levels according to 'spread' label")
X_train, y_train, X_test, y_test = f.split(train_data, test_data)
X_train = X_train.to_numpy()
y_train = y_train.to_numpy()

#train and tuning hyperparameter
f.pre_tuning_svm_clf(X_train, y_train)
optimal_C = f.tuning_C_hyperparameter(X_train, y_train, start = -1 , end= 2)
f.train_and_test_tuned_C_svm_clf(X_train, y_train, X_test, y_test, optimal_C =2 )