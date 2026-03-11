import pandas as pd

def load_data(anon_path, aux_path):
    anon = pd.read_csv(anon_path)
    aux = pd.read_csv(aux_path)
    return anon, aux

def link_records(anon, aux):
    anon = anon.copy()
    aux = aux.copy()

    if 'zip3' not in anon.columns:
        anon['zip3'] = anon['zip'].astype(str).str[:3]
    if 'zip3' not in aux.columns:
        aux['zip3'] = aux['zip'].astype(str).str[:3]

    # Rename name column in aux so it shows up as matched_name
    aux = aux.rename(columns={'name': 'matched_name'})

    matches = pd.merge(anon, aux, on=['age', 'gender', 'zip3'], how='inner')

    # Only keep truly unique matches (exactly one aux record per anon record)
    match_counts = matches.groupby(['age', 'gender', 'zip3']).size().reset_index(name='count')
    unique_groups = match_counts[match_counts['count'] == 1][['age', 'gender', 'zip3']]
    matches = pd.merge(matches, unique_groups, on=['age', 'gender', 'zip3'], how='inner')

    return matches

def deanonymization_rate(matches, anon):
    if len(anon) == 0:
        return 0.0
    return len(matches) / len(anon)