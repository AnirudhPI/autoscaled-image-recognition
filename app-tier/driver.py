from image_classification import Classifier


if __name__ == "__main__":
    # Create an instance of the Classifier class
    classifier = Classifier()
    
    # Call the get_classification method with a URL
    # url = f"/home/ubuntu/image_proc_folder/test_{i}.JPEG"

    for i in range(5):
        url =  f"/home/ubuntu/image_proc_folder/test_{i}.JPEG"
        classification = classifier.get_classification(url)
        print(f"{url}: {classification}")
