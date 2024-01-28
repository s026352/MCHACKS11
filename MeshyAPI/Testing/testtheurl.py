import requests
import os

def download_file(url, destination_folder, file_name):
    # Make a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Construct the full path for the destination file
        destination_path = os.path.join(destination_folder, file_name)

        # Save the content to the destination file
        with open(destination_path, 'wb') as file:
            file.write(response.content)

        print(f"File downloaded successfully to: {destination_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

# Example usage
fbx_url = "https://assets.meshy.ai/email%7C65b47a6f69034588d49e31ee/tasks/018d492e-21f8-7046-ae40-3b148e52a58d/output/model.fbx?Expires=1706589061&Signature=q7awNMfi9IF7Oz-zR26AqLPu42k2c793tofBuRKqcWnFzQQMERddEfLcoMCUGu8dkWLQJXA2Kx9e~s9wt9lE-RWmPsDvsp2z9qp8lVyj7cqqkiuEiMd~Y2bUwqaIu67OZRhtFA9vW7h-4ADHKx5bYx3XzUvpC7eMBrOHRqEzzGH9DLyiyog-1plDKtVLwY7XHMz7edaFY7xy8mmjebpU60KkU50Ug-YI1B2dsHqSOsaCLEr5HTkvIjOJtC9hiKEB1OJDXnTHW81LVHqojbYnWZFIV4J8QBF1aO2YHt9DwGhKsMOcZCJ9QpzgfUbywwv9E87LMES1AFZx0--p8XE8vQ__&Key-Pair-Id=KL5I0C8H7HX83"
url = fbx_url
destination_folder = os.path.join(os.path.dirname(__file__), "3D hand\Assets\Prof")
file_name = "NewModel.fbx"

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Call the function to download the file
download_file(url, destination_folder, file_name)
