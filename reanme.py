import os

import inquirer

list_of_paths_names = os.listdir("C:\Work\Projects")
list_of_paths = []
for i in list_of_paths_names:
    path = 'C:\Work\Projects\{}\\build\\app\outputs\\flutter-apk\\app-release.apk'.format(
        i)
    list_of_paths.append(path)
# print(list_of_paths)
paths = [
    inquirer.List(
        'path',
        message="Select Project to rename APK",
        choices=list_of_paths,
    ),
]
selectedPath = inquirer.prompt(paths)['path']
if not os.path.exists(selectedPath):
    print("File Does Not Exist")
else:
    appName = input("Enter App Name: ")
    appVersion = input("Enter AppVersion: ")
    appVersionNumber = input("Enter AppVersionNumber: ")
    buildType = input("Enter Build Type: ")
    list = selectedPath.split('\\')
    appname = list[len(list) - 1].split('.')
    appname[0] = "{}_{}_V{}({})".format(appName, buildType, appVersion,
                                        appVersionNumber)
    newAppName = ".".join(appname)
    list.remove('app-release.apk')
    list.append(newAppName)
    newAppPath = '\\'.join(list)
    os.rename(selectedPath, newAppPath)
