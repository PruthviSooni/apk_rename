import os

import inquirer
from yaml import YAMLError, safe_load

# Getting CWD
dir = os.getcwd()

# List For Storing SDK Path
pathList = []

# Getting Flutter SDK Path
sdkPath = "C:\\FlutterSDK"

# Adding Path to [pathList]
for i in os.scandir(sdkPath):
    pathList.append(i.name)

# Prompt Selection for flutter version
choiceList = [inquirer.List(
    "path", message="Select Flutter version", choices=pathList), ]
action = inquirer.prompt(choiceList)
selectedVersion = action['path']


# Flutter Build apk command
result = os.system('"{} build apk --release"'.format(selectedVersion))

# Appending CWD with release apk path
apkPath = '{}\\build\\app\outputs\\flutter-apk\\app-release.apk'.format(dir)

# Check for [result] if it 0 then success
if result == 0:
    currentAppName = ""
    currentAppVersion = ""
    if not os.path.exists(apkPath):
        print("File Does Not Exist")
    else:
        # Getting App Name and App Version pubspec.yaml file from the current PWD path
        yamlDir = "{}\\pubspec.yaml".format(dir)
        with open(yamlDir, "r") as stream:
            try:
                data = safe_load(stream)
                currentAppName = str(data['name']).upper()
                currentAppVersion = str(data['version']).split("+")[0]
                print("APP NAME: "+currentAppName)
                print("APP VERSION: " + currentAppVersion)
            except YAMLError as exc:
                print(exc)
        print("""
------------------------------------------------------------------------------
Format your flutter apk name from app-release.apk to {}_BUILT_TYPE_V{}(1).apk
 - Built Type -> TEST eg..
 - App Build Number -> (1)
------------------------------------------------------------------------------
        """.format(currentAppName, currentAppVersion))
        buildType = input("Enter Build Type: ")
        buildNumber = input("Enter Build Number: ")
        list = apkPath.split('\\')
        #
        # Split app-release.apk --> ['app-release','apk']
        appName = list[len(list) - 1].split('.')
        #
        # Appending new name
        appName[0] = "{}_{}_V{}({})".format(currentAppName, buildType.upper(), currentAppVersion,
                                            buildNumber)
        newAppName = ".".join(appName)
        list.remove('app-release.apk')
        list.append(newAppName)
        newAppPath = '\\'.join(list)
        os.rename(apkPath, newAppPath)
else:
    print("Could Not Find Flutter Project")
