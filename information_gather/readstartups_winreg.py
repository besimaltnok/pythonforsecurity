import _winreg

key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run")
key2 = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\Run")
keys = [key, key2]

startup = []
def liststartup(key):
    try:
        i = 0
        while 1:
            name, path, type = _winreg.EnumValue(key, i)
            startup.append(repr(name))
            print("Name: {:<20} Path : {} ").format(name, path)
            i += 1
    except WindowsError:
        print "*****************"

map(liststartup, keys)
