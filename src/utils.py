import pythoncom
import wmi

def set_brightness_windows(brightness):
    pythoncom.CoInitialize()
    wmi_service = wmi.WMI(namespace='wmi')
    monitors = wmi_service.WmiMonitorBrightnessMethods()[0]
    monitors.WmiSetBrightness(brightness, 0)
