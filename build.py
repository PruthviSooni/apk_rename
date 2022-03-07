import os

# Getting CWD
dir = os.getcwd()

# Flutter Build apk command
result = os.system('"flutter build apk --release"')

# Appending CWD with release apk path
dir = '{}\\build\\app\outputs\\flutter-apk\\app-release.apk'.format(dir)
print(dir)

# Check for [result] if it 0 then success
if result == 0:
    if not os.path.exists(dir):
        print("File Does Not Exist")
    else:
        print("""
------------------------------------------------------------------------------
Format your flutter apk name from apk-release.apk to TEST_BUILT_TYPE_V1(1).apk
 TEST_BUILT_TYPE_V1(1).apk
 - Built Type -> TEST eg..
 - Appversion -> V1
 - App Version Code -> (1)
------------------------------------------------------------------------------
        """)
        appName = input("Enter App Name: ")
        appVersion = input("Enter AppVersion: ")
        appVersionNumber = input("Enter AppVersionNumber: ")
        buildType = input("Enter Build Type: ")
        list = dir.split('\\')
        appname = list[len(list) - 1].split('.')
        appname[0] = "{}_{}_V{}({})".format(appName, buildType, appVersion,
                                            appVersionNumber)
        newAppName = ".".join(appname)
        list.remove('app-release.apk')
        list.append(newAppName)
        newAppPath = '\\'.join(list)
        os.rename(dir, newAppPath)
else:
    print("Somthing went wrong")
