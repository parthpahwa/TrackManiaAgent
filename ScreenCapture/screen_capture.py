import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api

def screen_capture(region=(0,40, 800, 600)):

    desktop_handle = win32gui.GetDesktopWindow()

    if region:
            left,top,x2,y2 = region
            width = x2 - left + 1
            height = y2 - top + 1
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    device_context = win32gui.GetWindowDC(desktop_handle)
    py_device_context = win32ui.CreateDCFromHandle(device_context)
    memory_device_context = py_device_context.CreateCompatibleDC()

    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(py_device_context, width, height)
    
    memory_device_context.SelectObject(bmp)
    memory_device_context.BitBlt((0, 0), (width, height), py_device_context, (left, top), win32con.SRCCOPY)
    
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)

    py_device_context.DeleteDC()
    memory_device_context.DeleteDC()
    
    win32gui.ReleaseDC(desktop_handle, device_context)
    win32gui.DeleteObject(bmp.GetHandle())
    
    return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
