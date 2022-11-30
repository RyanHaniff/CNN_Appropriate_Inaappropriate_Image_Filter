from PIL import Image
import os


class RemoveCorruptImages:

    def __init__(self, data_directory):
        self.data_dir = data_directory
        self.image_path = ""

    def verify_image(self):
        img = Image
        try:
            img = Image.open(self.image_path)
            img.verify()
            img.close()
            # cv2.imread(image_path)
            return True
        except (IOError, OSError, Image.DecompressionBombError, PermissionError):
            print('Issue with image {}'.format(self.image_path))
            img.close()
            return False
        finally:
            img.close()

    def remove_images(self):
        corrupt_images = []
        count = 0
        for image_class in os.listdir(self.data_dir):
            for image in os.listdir(os.path.join(self.data_dir, image_class)):
                self.image_path = os.path.join(self.data_dir, image_class, image)
                # print(image_path)
                # print(count)
                if not self.verify_image():
                    print("removing image {}".format(self.image_path))
                    os.remove(self.image_path)
                    corrupt_images.append(self.image_path)
                count += 1
        print(corrupt_images)


def main():
    data_dir = 'data/train'
    image_exts = ['jpeg', 'jpg', 'bmp', 'png']


if __name__ == '__main__':
    main()
