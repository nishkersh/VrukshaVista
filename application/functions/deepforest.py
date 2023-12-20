from deepforest import main
import matplotlib.pyplot as plt
import os

def analyze_url(url):
    current_working_directory = os.getcwd()
    current_working_directory = current_working_directory.replace("\\", "/")
    
    new_url = current_working_directory + url

    print(new_url)

    model = main.deepforest()
    model.use_release()
    
    img = model.predict_image(path=new_url, return_plot=True)
    plt.imshow(img[:,:,::-1])

    boxes = model.predict_image(path=new_url, return_plot=False)
    return len(boxes)