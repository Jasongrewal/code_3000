# packages
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# set seed
seed = 314

def train_model(X, y, seed=seed):
    """
    Build a GBM on given data
    """
    model = GradientBoostingClassifier(
    loss="log_loss",
    learning_rate=0.02,
    n_estimators=1500,
    max_depth=3,
    max_leaf_nodes=18,
    subsample=0.8,
    min_samples_leaf=10,
    min_samples_split=15,
    max_features="log2",
    validation_fraction=0.20,
    n_iter_no_change=30,
    tol=1e-5,
    random_state=seed
)
    model.fit(X, y)
    return model