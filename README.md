# WasteBot


WasteBot was researched and developed by us during January - November 2019 as a Capstone project at Thapar Institute of Engineering and Technology.

![Robotic Arm](https://github.com/Japkeerat/WasteBot/blob/master/project-photo.jpg)

This prototype uses deep learning, image processing, and some electronics to segregate solid waste into three different categories - Biodegradable, Recyclable, and Non-Recyclable waste.

After going through various failed approaches during our course, we selected to go with transfer learning with VGG-16 as it gave an accuracy of 85.49%. We also observed, more the complex algorithm we chose for transfer learning (For example, ResNet-34, ResNet-50, DenseNet) more bad the model got. So ideal approach looked to use neural network with lesser layers.

Next thing was to handle large computations on Raspberry Pi. As the RAM on Pi is extremely limited (1 GB), idea was to do all the processing on seperate device and only use Pi to control the Robot. This also introduced us to tons of new things to take control of during implementation of Socket Programming. To optimize the time taken to transfer a file and prevent that file to encounter errors during working with OpenCV, we had to choose a non-conventional way of file transfer.

The trained model .hdf5 file can be viewed [here](https://drive.google.com/open?id=1a9mrDxD_9jNlfRWcUz3_OCpI_6kStICh). This file is of 520MB. Using this model, the predictions on the image received are made, and the prediction is sent back to the Raspberry Pi which based on the prediction controls the motors of the robot.

The video explaining the prototype can be viewed [here in this repository](https://github.com/Japkeerat/WasteBot/blob/master/Project%20Explanation%20Video.m4v)

#### Developers
* Harshul Agarwal ([LinkedIn](https://www.linkedin.com/in/harshul-agarwal-1b2313144/))
* Javesh Vasu ([LinkedIn](https://www.linkedin.com/in/javesh-k-5a6a20120/))
* Abhishek Nayyar ([LinkedIn](https://www.linkedin.com/in/abhishek-nayyar-495536145/))
* Japkeerat Singh ([LinkedIn](https://www.linkedin.com/in/japkeeratsingh/))


#### References
* [Classification of Trash for Recyclable Status](https://pdfs.semanticscholar.org/c908/11082924011c73fea6252f42b01af9076f28.pdf?_ga=2.147552948.2039321784.1574850723-1144123513.1574850723) by Gary Thung
