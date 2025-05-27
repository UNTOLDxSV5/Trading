from collections import defaultdict
from pathlib import Path

def inspect_clusters(df, log_filename="cluster_inspection.txt"):
    log_dir = Path(r"C:\Users\srini\OneDrive\Desktop\comment-classifier-project\src\logs")
    log_dir.mkdir(parents=True, exist_ok=True)  # create folder if needed
    
    log_path = log_dir / log_filename
    
    cluster_examples = defaultdict(set)  # unique comments per cluster
    
    with open(log_path, 'w', encoding='utf-8') as f:
        for _, row in df.iterrows():
            cluster_examples[row['cluster']].add(row['cleaned_comment'])
        
        for cluster in sorted(cluster_examples.keys()):
            f.write(f"\nCluster {cluster}:\n")
            for comment in sorted(cluster_examples[cluster]):
                f.write(comment + '\n')
    
    print(f"Clusters saved to {log_path}")
