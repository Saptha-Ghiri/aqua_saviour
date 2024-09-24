import firebase_admin
from firebase_admin import credentials, storage

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('pass.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'predict-sih.appspot.com','databaseURL': 'https://predict-sih-default-rtdb.firebaseio.com/'}) 

# Reference the bucket
bucket = storage.bucket()

def update_images_with_different_metadata(image_paths, metadata_list):
    for i, image_path in enumerate(image_paths):
        try:
            # Reference the image file
            blob = bucket.blob(image_path)

            # Update the metadata
            blob.metadata = metadata_list[i]  # Assign corresponding metadata
            blob.patch()  # Apply the changes

            print(f'Metadata updated successfully for {image_path}!')
        except Exception as e:
            print(f"Failed to update metadata for {image_path}: {e}")

# List of image paths in Firebase Storage
image_paths = [
    'photos/085782d9-0ce6-4776-a859-aeec91e891e1.jpg',
    'photos/1a1dfc34-3bd5-4a8b-a468-c7c9a8746944.jpg',
    'photos/394813cf-3b66-4cdd-9fd7-37ff2a1e6802.jpg',
    'photos/4b9efe16-3fc2-479a-b1fc-9edba84215a5.jpg',
    'photos/83634ede-5482-4df4-b48c-7c162acf0767.jpg',
    'photos/8c381bac-1e47-40ce-8102-5a69f5739597.jpg',
    'photos/d922ac60-d238-41cc-8954-4667bc204efb.jpg',
    'photos/f94892bc-3890-41a1-8058-fb6948dcfd9b.jpg'
]


# List of metadata for each image
metadata_list = [
    {'contentType': 'image/jpeg', 'latitude': '28.747054', 'longitude': '77.177553'},
    {'contentType': 'image/jpeg', 'latitude': '28.743623', 'longitude': '77.174602'},
    {'contentType': 'image/jpeg', 'latitude': '28.744673', 'longitude': '77.169965'},
    {'contentType': 'image/jpeg', 'latitude': '28.746701', 'longitude': '77.172784'},
    {'contentType': 'image/jpeg', 'latitude': '28.742394', 'longitude': '77.167990'},
    {'contentType': 'image/jpeg', 'latitude': '28.748825', 'longitude': '77.179125'},
    {'contentType': 'image/jpeg', 'latitude': '28.749472', 'longitude': '77.176944'},
    {'contentType': 'image/jpeg', 'latitude': '28.743623', 'longitude': '77.169509'}

]

new_metadata = {
    'contentType': 'image/jpeg',  # Adjust based on image type
    'metadata': {
        'latitude': 'Updated description for the image',
        'longitude': 'Your Name'
    }
}



l = [

[28.744673, 77.169965],
[28.746701, 77.172784],
[28.742394, 77.167990],
[28.743623, 77.169509],

[28.745142, 77.174602],
[28.747054, 77.177553],
[28.748825, 77.179125],
[28.749472, 77.176944]]


update_images_with_different_metadata(image_paths, metadata_list)


