import pandas as pd

def load_dataset(file_path):
    """Load dataset from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

if __name__ == "__main__":
    dataset_path = "datasets/distance_data.csv"  # Modify as needed
    data = load_dataset(dataset_path)
    if data is not None:
        print(data.head())