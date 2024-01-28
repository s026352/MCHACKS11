import requests
import os
from config import API_KEY, IMGUR_CLIENT_ID

# Function to upload image to Imgur and get the image URL
def upload_image_to_imgur(image_path, client_id):
    imgur_api_url = "https://api.imgur.com/3/upload"
    headers = {"Authorization": f"Client-ID {client_id}"}

    with open(image_path, "rb") as image_file:
        files = {"image": (os.path.basename(image_path), image_file)}
        response = requests.post(imgur_api_url, headers=headers, files=files)

    response_data = response.json()
    image_url = response_data.get("data", {}).get("link")
    return image_url

# Specify the path to the locally stored image file
image_file_path = "heycode\\boris-vaisband_220x220.jpg"

# Specify your Imgur client ID (replace with your actual client ID)
imgur_client_id = IMGUR_CLIENT_ID

# Upload the image to Imgur and get the image URL
theurl = upload_image_to_imgur(image_file_path, imgur_client_id)

payload = {
    "image_url": theurl,
    "enable_pbr": True,
}
headers = {
    "Authorization": API_KEY
}

response = requests.post(
    "https://api.meshy.ai/v1/image-to-3d",
    headers=headers,
    json=payload,
)
response.raise_for_status()
print(response.json())

# Parse the JSON response
response_data = response.json()

# Access the 'result' key and store it in a variable
result_variable = response_data.get('result')

first = True
status = "no"
fbx_url = ""
while (first or status!="SUCCEEDED"):
    first = False
    task_id = result_variable
    headers = {
        "Authorization": API_KEY
    }

    response = requests.get(
        f"https://api.meshy.ai/v1/image-to-3d/{task_id}",
        headers=headers,
    )
    response.raise_for_status()
    response_back = response.json()
    fbx_url = response_back.get('model_urls', {}).get('fbx')
    status = response_back.get('status')

print(fbx_url)


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
url = fbx_url
destination_folder = os.path.join(os.path.dirname(__file__), "3D hand\Assets\Prof")
file_name = "BorisModel.fbx"

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Call the function to download the file
download_file(url, destination_folder, file_name)
