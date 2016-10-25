import os

def clear_folder(folder):
    print("Clearing '%s' folder ... " %(folder))
    os.system("rm -r -f '%s'" %(folder))
    os.system("mkdir -p '%s'" %(folder))

def get_name(filename):
    return os.path.splitext(os.path.basename(filename))[0]

def convert_to(filename, width, heigth, destination_folder, portrait):

    if not portrait:
        tmp = heigth
        heigth = width
        width = tmp

    destination_file = get_name(filename)
    values = (filename, width, heigth, width, heigth, destination_folder, destination_file)
    command = "convert '%s' -resize %sx%s^ -gravity center  -extent %sx%s %s/%s.jpg" %values

    print("Processing '%s' -> '%s/%s.jpg'" %(filename, destination_folder, destination_file))
    os.system(command)

clear_folder('result/3_5')
clear_folder('result/4')
clear_folder('result/4_7')
clear_folder('result/5_5')
clear_folder('result/ipad')


files = os.listdir('screenshots/')
screenshot_files = ['screenshots/' + f for f in files if f.endswith('.png')]


portrait = True

for s in screenshot_files:
    convert_to(s, 640, 920, 'result/3_5', portrait)
    convert_to(s, 640, 1096, 'result/4', portrait)
    convert_to(s, 750, 1334, 'result/4_7', portrait)
    convert_to(s, 1242, 2208, 'result/5_5', portrait)
    convert_to(s, 1536, 2008, 'result/ipad', portrait)
