from PIL import Image
import os
import imagehash
import index_display_delete as delete_files

def main():
    def dhash_image(image_path, hash_size=8):
        image = Image.open(image_path)
        resized_image = image.resize(
            (hash_size + 1, hash_size), Image.ANTIALIAS)
        hash_value = imagehash.dhash(resized_image)
        return hash_value

    def find_similar_images(input_directory):
        image_mapping = {}
        similar_images = []

        for root, _, files in os.walk(input_directory):
            for file in files:
                if not (file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")):
                    continue
                file_path = os.path.join(root, file)
                try:
                    image_hash = dhash_image(file_path)
                    if image_hash not in image_mapping:
                        image_mapping[image_hash] = [file_path]
                    else:
                        image_mapping[image_hash].append(file_path)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

        for hash_value, image_paths in image_mapping.items():
            if len(image_paths) > 1:
                similar_images.append(image_paths)

        return similar_images

    input_directory = input(
        "Enter the directory path to check for similar images: ")

    if not os.path.exists(input_directory):
        print("Invalid directory path.")
    else:
        images_found = find_similar_images(input_directory)
        if images_found:
            print("Similar images found:")
            g_files=[]
            for group in images_found:
                print("Group:")
                for image_path in group:
                    s=os.path.getsize(image_path)
                    g_files.append([image_path,s])
                delete_files.main(g_files)
                    
        else:
            print("No similar images found.")
