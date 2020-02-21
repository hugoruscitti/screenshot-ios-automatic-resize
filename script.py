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

clear_folder('result/iphone/3_5')
clear_folder('result/iphone/4')
clear_folder('result/iphone/4_7')
clear_folder('result/iphone/5_5')
clear_folder('result/iphone/5_8')
clear_folder('result/iphone/6_5')
clear_folder('result/ipad/12_9')
clear_folder('result/ipad/10_5')
clear_folder('result/ipad/9_7')
clear_folder('result/ipad/7_9')
clear_folder('result/ipad/7_9')
clear_folder('result/ipad/12_9')
clear_folder('result/watch/42')
clear_folder('result/watch/38')


files = os.listdir('screenshots/')
screenshot_files = ['screenshots/' + f for f in files if f.endswith('.png')]


portrait = False

for s in screenshot_files:
    convert_to(s, 640, 920, 'result/iphone/3_5', portrait)
    convert_to(s, 640, 1096, 'result/iphone/4', portrait)
    convert_to(s, 750, 1334, 'result/iphone/4_7', portrait)
    convert_to(s, 1242, 2208, 'result/iphone/5_5', portrait)
    convert_to(s, 1125, 2436, 'result/iphone/5_8', portrait)
    convert_to(s, 1242, 2688, 'result/iphone/6_5', portrait)
    convert_to(s, 2048, 2732, 'result/ipad/12_9', portrait)
    convert_to(s, 1668, 2224, 'result/ipad/10_5', portrait)
    convert_to(s, 1536, 2048, 'result/ipad/9_7', portrait)
    convert_to(s, 2048, 2732, 'result/ipad/12_9', portrait) 
    convert_to(s, 1536, 2048, 'result/ipad/7_9', portrait)
    convert_to(s, 312, 390, 'result/watch/42', portrait)
    convert_to(s, 272, 340, 'result/watch/38', portrait)
