This study is a case study requested by a company I applied to, which asks me to classify shipping images according to postal companies. For data privacy reasons, no photos or labels have been added.

First, I researched how to label the given images. After trying several different methods, I decided 
that the labelme application was the one I needed. Thanks to its user-friendly interface and ease of use, I was able to label the data easily with this application. The application stored the necessary classes for labels and their locations in a JSON file. 
    
During this process, I examined how much data I labeled for each class with label_inspect.ipynb. I updated the initial class names I used with the code I wrote here. 
    
With the code put_text_temp.ipynb, I learned how to place text on an image in the way I wanted, which would be useful at the end of the project. 

I started developing the model, but I encountered dimension issues because I drew the boundaries of the labels with different number of corners while labeling the data. I identified and changed labels that had a different number of corners than 4 with point_inspect.ipynb. Then I returned to improving the model. 

First, for the sake of giving an idea, I used a simple two-layer CNN structure, but this was not sufficient. I tried several CNN architectures that I knew from before. I used architectures similar to Alex-Net, Efficientnet, and ResNet, but they did not give very good results. Finally, I decided on the Le-Net 5 architecture, which has a very high accuracy rate compared to the others. 

During this process, I wrote a code that copies images to avoid copying the original images every time I wrote text on the labels in the images. This code can be found in the replace_img_w_org.ipynb notebook. 

I wrote a program with main.py that takes an image path as input. After running this program, if the user provides the path of their image as input to the program, the program will place the predicted class in the location it predicted on the image as text. 

IMPORTANT NOTE: The program does not create a new image. It writes on top of the existing image. Therefore, it is essential to back up your image.