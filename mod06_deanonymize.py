import pandas as pd

def load_data(anon_path, aux_path):
    """Load the anonymized and auxiliary datasets."""
    anon = pd.read_csv(anon_path)
    aux = pd.read_csv(aux_path)
    return anon, aux

def link_records(anon, aux):
    
    
    if 'zip3' not in anon.columns:
        anon = anon.copy()
        anon['zip3'] = anon['zip'].astype(str).str[:3]
    if 'zip3' not in aux.columns:
        aux = aux.copy()
        aux['zip3'] = aux['zip'].astype(str).str[:3]

    
    matches = pd.merge(anon, aux, on=['age', 'gender', 'zip3'], how='inner')

    
    matches = matches.drop_duplicates(subset=['age', 'gender', 'zip3'])

    return matches

def deanonymization_rate(matches, anon):
    
    rate = len(matches) / len(anon)
    return rate