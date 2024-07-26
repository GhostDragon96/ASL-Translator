import os
import argparse

# Create a new ArgumentParser object
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('PATH', help='Path to jetson-infrence. ')

# Parse the arguments
args = parser.parse_args()

path = str(args.PATH)

os.system(f"cd {path}/python/training/classification/")

os.system('git clone --recursive https://github.com/GhostDragon96/ASL-Translator')

os.system('mkdir /data/ASL/')

os.system('mv ASL-Translator/data /data/ASL')

os.system('mkdir /models/ASL/')

os.system('mv ASL-Translator/resnet18.onnx models/ASL/')

os.system('rm ASL-Translator --recursive')