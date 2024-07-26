# ASL Translator

This code aims to translate American Sign Language (ASL) letters to text on your computer. 

![97% E](E-out.jpg?raw=true "97% E")

## The Algorithm

For my project I decided to train AI on understanding letters in ASL. I re-trained the ResNet-18 model on 750 images per letter, including delete, space, and none. This will allow the user to either upload a photo or a image stream (from a camera or video scource) and output it to a file, a Real-Time Streaming Protocol (RTSP), or WebRTC. 

## Running this project

First, connect to your Jetson and download the `Create Project.py` file to your Jetson. Then, install the repository by running the `python3 Create Project.py [PATH TO YOUR JETSON INFERENCE FOLDER]` ([Jetson-Inference Github](https://github.com/dusty-nv/jetson-inference)). After that, using the `mv` command, move the `resnet18.onnx` file to a new folder in models called ASL. Also move the data folder to data and name it ASL. Next, change directories to your classification folder using `cd jetson-inference/python/training/classification/`. Then, run the **ASL Translator** using this command: `imagenet.py --model=model/ASL/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=data/ASL/labels.txt [PATH TO TEST FILE] [PATH TO OUTPUT FOR TEST FILE]`, being sure to include your paths. If you would like to do live video, replace your test file path with `/dev/video0`. The only issue with this is you won't be able to see the live feed. To fix this, we can output the feed to either a WebRTC or a RTSP. To do this you replace the output path with with `rtsp://@:1234/out` (RTSP) or `webrtc://@:1234` (WebRTC). Then to watch RTSP, open a network stream capable apllication such as VLC Media Player and type `rtsp://[YOUR JETSON'S IP ADRESS]:1234/out`. To watch WebRTC, go to your internet browser and type `[YOUR JETSON'S IP ADRESS]:1234`. 

[View a video explanation here](video link)

### Possible Improvments

It is possible that the original AI (ResNet18) is not good at detecting hand signals. To remedy this, you can retrain another model on this data and see if it works. To learn how to do that, go to [Jetson Inference](https://github.com/dusty-nv/jetson-inference/tree/master) and look at the retraining explanations. 
