
import  os 
from glob import glob
import csv
import urllib.request

BASE_PATH = "flower_image_urls"
OS_BASE_OATH = "FOLDER_PATH_TO_GO_URLS"

def main():
    folders = glob(BASE_PATH, recursive = True)
    print(folders)
    f = []
    count = 0

    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    for (dirpath, dirnames, filenames) in os.walk(BASE_PATH):
        f.extend(filenames)

        break


    flower_name = "none"
    for file in f:
        with open((BASE_PATH+ "/" + file), newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            print(f"reader: {reader}")
            for row in reader:
                flower_name = row['name']
                data = (row['ImageURL'])
      

            
                print(f"Flower Name: {flower_name}")
                path = os.path.join(OS_BASE_OATH, flower_name)
                if(os.path.isdir(path)==False): 
                    os.mkdir(path)
                    print("making directory")
                
            
                print(f"Download this image {data}")
  
                print(f"Path: {path}" )
            
                download_image(data, path + "/", str(count), ".jpg")
                count = count + 1

# end main()

def download_image(url, file_path, file_name, image_exten):
    # set full path to download image
    full_path = file_path + file_name + image_exten
    # download image 
    try:
        urllib.request.urlretrieve(url, full_path.encode('utf-8').strip())
    except Exception:
        pass

# def download_image


if __name__ == "__main__":
    main()