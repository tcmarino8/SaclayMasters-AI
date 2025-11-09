import sys
import os

def print_ver(name, obj):
    try:
        print(f"{name}: {obj.__version__}")
    except Exception:
        print(f"{name}: (no __version__ attribute)")

print("Python:", sys.version.replace('\n',' '))

# import and print versions
try:
    import cv2
    print_ver('cv2', cv2)
except Exception as e:
    print('cv2 import failed:', e)

try:
    import numpy as np
    print_ver('numpy', np)
except Exception as e:
    print('numpy import failed:', e)

try:
    import matplotlib
    print_ver('matplotlib', matplotlib)
except Exception as e:
    print('matplotlib import failed:', e)

try:
    import skimage
    print_ver('skimage', skimage)
except Exception as e:
    print('skimage import failed:', e)

# Create a small test image using numpy and save with cv2
out_path = 'verify_test_output.png'
try:
    import numpy as np
    import cv2
    img = (np.zeros((100, 200, 3), dtype=np.uint8))
    img[:] = (50, 150, 200)  # BGR color
    cv2.putText(img, 'OK', (50,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)
    cv2.imwrite(out_path, img)
    print(f'Created test image: {os.path.abspath(out_path)}')
except Exception as e:
    print('Failed to create/test image with cv2:', e)

print('Verification finished.')
