import os
import kagglehub
from kagglehub import KaggleDatasetAdapter

def download_dataset():

    kaggle_file_path = "twcs/twcs.csv"
    
    local_save_path = os.path.join("src", "data", "twitter_support_data.csv")
    os.makedirs(os.path.dirname(local_save_path), exist_ok=True)

    
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "thoughtvector/customer-support-on-twitter",
        kaggle_file_path,
        pandas_kwargs={"nrows": 50000}
    )


    df.to_csv(local_save_path, index=False, encoding="utf-8")
    print(f"{len(df)} rows saved to {local_save_path}")

    return df

if __name__ == "__main__":
    download_dataset()