import os
import io
import cv2
import requests
import numpy as np
from IPython.display import Image, display

base_url = "http://localhost:3000"
endpoint = "/predict"
model = "yolov3-tiny"
model = "yolov3"

full_url = base_url + endpoint + "?model=" + model


def response_from_server(url, image_file, verbose=True):
    """Makes a POST request to the server and returns the response.

    Args:
        url (str): URL that the request is sent to.
        image_file (_io.BufferedReader): File to upload, should be an image.
        verbose (bool): True if the status of the response should be printed. False otherwise.

    Returns:
        requests.models.Response: Response from the server.
    """

    files = {"file": image_file}
    response = requests.post(url, files=files)
    status_code = response.status_code
    if verbose:
        msg = (
            "Everything went well!"
            if status_code == 200
            else "There was an error when handling the request."
        )
        print(msg)
    return response


def display_image_from_response(response):
    """Display image within server's response.
    Args:
        response (requests.models.Response): The response from the server after object detection.
    """
    image_stream = io.BytesIO(response.content)
    image_stream.seek(0)
    print(image_stream.read())
    image_stream.seek(0)
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    filename = "image_with_objects.jpeg"
    cv2.imwrite(f"images_predicted/{filename}", image)
    # display(Image(f"images_predicted/{filename}"))


dir_name = "images_predicted"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

# image_files = ["car2.jpg", "clock3.jpg", "apples.jpg"]

# for image_file in image_files:
#     with open(f"images/{image_file}", "rb") as image_file:
#         prediction = response_from_server(full_url, image_file, verbose=False)

#     display_image_from_response(prediction)

with open("images/minicop.jpeg", "rb") as image_file:
    prediction = response_from_server(full_url, image_file)

display_image_from_response(prediction)
