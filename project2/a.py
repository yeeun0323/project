#PLEASE WRITE THE GITHUB URL BELOW!
#

import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
#import sklearn.model_selection as ms
#from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

def load_dataset(dataset_path):
	csv = pd.read_csv(dataset_path)
	frame = pd.DataFrame(csv)
	return frame

def dataset_stat(dataset_df):	
	return len(dataset_df.columns)-1, len(dataset_df.loc[dataset_df['target'] == 0]), len(dataset_df.loc[dataset_df['target'] == 1])

def split_dataset(dataset_df, testset_size):
	return train_test_split(dataset_df.target == 0, dataset_df.target == 1, test_size=testset_size)

def decision_tree_train_test(x_train, x_test, y_train, y_test):
    dt_cls = tree.DecisionTreeClassifier()
    dt_cls.fit(x_train, y_train)
    acc = accuracy_score(y_test, dt_cls.predict(x_test))
    prec = precision_score(y_test, dt_cls.predict(x_test))
    recall = recall_score(y_test, dt_cls.predict(x_test))
    return acc, prec, recall

def random_forest_train_test(x_train, x_test, y_train, y_test):
    rf_cls = RandomForestClassifier()
    rf_cls.fit(x_train,y_train)
    acc = accuracy_score(rf_cls.predict(x_test),y_test)
    prec = precision_score(rf_cls.predict(x_test),y_test)
    recall = recall_score(rf_cls.predict(x_test),y_test)
    return acc, prec, recall

def svm_train_test(x_train, x_test, y_train, y_test):
    pipe = make_pipeline(StandardScaler())
    pipe.fit(x_train,y_train)
    acc = accuracy_score(pipe.predict(x_test),y_test)
    prec = precision_score(pipe.predict(x_test),y_test)
    recall = recall_score(pipe.predict(x_test),y_test)
    return acc, prec, recall

def print_performances(acc, prec, recall):
	#Do not modify this function!
	print ("Accuracy: ", acc)
	print ("Precision: ", prec)
	print ("Recall: ", recall)

if __name__ == '__main__':
	#Do not modify the main script!
	data_path = sys.argv[1]
	data_df = load_dataset(data_path)

	n_feats, n_class0, n_class1 = dataset_stat(data_df)
	print ("Number of features: ", n_feats)
	print ("Number of class 0 data entries: ", n_class0)
	print ("Number of class 1 data entries: ", n_class1)

	print ("\nSplitting the dataset with the test size of ", float(sys.argv[2]))
	x_train, x_test, y_train, y_test = split_dataset(data_df, float(sys.argv[2]))

	acc, prec, recall = decision_tree_train_test(x_train, x_test, y_train, y_test)
	print ("\nDecision Tree Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = random_forest_train_test(x_train, x_test, y_train, y_test)
	print ("\nRandom Forest Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = svm_train_test(x_train, x_test, y_train, y_test)
	print ("\nSVM Performances")
	print_performances(acc, prec, recall)