''' You work at a company that receives daily data files
from external partners. These files need to be processed and analyzed,
but first, they need to be transferred to the company's internal network.

The goal of this project is to automate the process of transferring
the files from an external FTP server to the company's internal network.

Here are the steps you can take to automate this process:

    Done - Use the ftplib library to connect to the external FTP server
    and list the files in the directory.

    Done - Use the os library to check for the existence of a local directory
    where the files will be stored.

    Done - Use a for loop to iterate through the files on the FTP server
    and download them to the local directory using the
    ftplib.retrbinary() method.

    Done - Use the shutil library to move the files from the local
    directory to the internal network.

    Done - Use the schedule library to schedule the script
    to run daily at a specific time.

    Done - You can also set up a log file to keep track
    of the files that have been transferred and any errors
    that may have occurred during the transfer process. '''

import datetime
from ftplib import FTP
import os
import shutil
import schedule as sc

def automateFileTransfer():

    # Login to the public FTP server.
    try:
        ftp = FTP('ftp.dlptest.com')
        ftp.login('dlpuser', 'rNrKYTX9g7z3RgJRmxWuGHbeu')
        print('\nLogin successful.')
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + ': Login successful.\n')
    except:
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + ': Login could not be made.\n')

    # Initial listing of the files on the FTP server
    try:
        initialListOfFilesInFtpDirectory = ftp.nlst()
        if len(initialListOfFilesInFtpDirectory) == 0:
            print('\nNo files existed on the FTP server when the initial listing was made.')
            currentDateAndTime = datetime.datetime.now()
            log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + ': No files existed on the FTP server when the initial listing was made.\n')
        else:
            print('\nInitial listing of the files on the FTP server:')
            for filename in initialListOfFilesInFtpDirectory:
                print(filename)
            currentDateAndTime = datetime.datetime.now()
            log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + ': The initial listing of the files on the FTP server has been made.\n')
    except:
        print('\nThe initial listing of the files on the FTP server could not be made.')
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + ': The initial listing of the files on the FTP server could not be made.\n')

    # Files on the server are temporarily kept,
    # so I upload some test files that
    # the script can work with.
    #
    # Preparing upload of test files to the FTP server
    listOfFiles = []
    listOfFilePaths = []
    filesForUploadPath = r'.\DirectoryOfTestFilesForUpload'

    if os.path.exists(filesForUploadPath):
        print(f"\nThe directory for the files that will be uploaded'{filesForUploadPath}' exists.")
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + f": The directory for the files that will be uploaded '{filesForUploadPath}' exists.\n")
    else:
        print(f"\nThe directory for the files that will be uploaded '{filesForUploadPath}' does not exist. \nCreating it now.")
        os.makedirs(filesForUploadPath)
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + f": The directory for the files that will be uploaded '{filesForUploadPath}' did not exist. \nIt has been created.\n")

    try:
        for i in range(1, 6):
            file_name = 'File_' + str(i) + '.txt'
            listOfFiles.append(file_name)
            full_path = os.path.join(filesForUploadPath, file_name)
            listOfFilePaths.append(full_path)
            with open(full_path, 'w') as f:
                f.write('Hello, world! ' + str(i))
        print('The test files have been created.\n')
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + ': The test files have been created.\n')
    except:
        print('Could not create the test files.\n')
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + 'Could not create the test files.\n')

    # for filename in listOfFiles:
    #     print(filename)
    # print()

    # Creating a directory on the FTP server for testing
    ftpDirectoryName = 'testFtpDir'
    if ftpDirectoryName not in ftp.nlst():
        # Create the remote directory
        ftp.mkd(ftpDirectoryName)
        print(f"The directory '{ftpDirectoryName}' has been created on the FTP server.")
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + f": The directory '{ftpDirectoryName}' has been created on the FTP server.\n")
    else:
        print(f"The directory '{ftpDirectoryName}' already exists on the FTP server.")
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + f": The directory '{ftpDirectoryName}' already exists on the FTP server.\n")

    # Change to the created directory
    ftp.cwd(ftpDirectoryName)

    # Get the current directory after changing
    currentFtpServerDirectory = ftp.pwd()
    print(f"Current FTP server directory changed to: {currentFtpServerDirectory}\n")
    # print(ftp.dir())

    for filePath in listOfFilePaths:
        # print(filePath)
        # print(listOfFiles[listOfFilePaths.index(filePath)])
        with open(filePath, 'rb') as f_upload:
            try:
                ftp.storbinary('STOR ' + listOfFiles[listOfFilePaths.index(filePath)], f_upload)
                print(f"Uploaded file '{listOfFiles[listOfFilePaths.index(filePath)]}'.")
                currentDateAndTime = datetime.datetime.now()
                log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + f": Uploaded file '{listOfFiles[listOfFilePaths.index(filePath)]}'.\n")
            except:
                print(f"File '{listOfFiles[listOfFilePaths.index(filePath)]}' could not uploaded.")
                currentDateAndTime = datetime.datetime.now()
                log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + f"File '{listOfFiles[listOfFilePaths.index(filePath)]}' could not uploaded.\n")

    # Accessing the FTP server for download procedure
    pathOfDirectory = './LocalDirectoryForTransferFromServer'

    # Checking if the local directory exists and creating it
    # if it does not exist yet.
    if os.path.exists(pathOfDirectory):
        print(f"\nThe local directory '{pathOfDirectory}' exists.")
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + f": The local directory '{pathOfDirectory}' exists.\n")

    else:
        print(f"\nThe local directory '{pathOfDirectory}' does not exist. Creating it now.")
        os.makedirs(pathOfDirectory)
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + f": The local directory '{pathOfDirectory}' did not exist. It has been created.\n")

    listOfFilesInFtpDirectory = ftp.nlst()

    # Iterating through the files on the FTP server
    # and downloading them to the local directory.
    if listOfFilesInFtpDirectory:
        print("\nFiles exist in the created FTP directory:")
        for filename in listOfFilesInFtpDirectory:
            try:
                with open('./LocalDirectoryForTransferFromServer/'+filename, 'wb') as newFile:
                    ftp.retrbinary('RETR ' + filename, newFile.write)
                    print(f"The file named '{filename}' was downloaded.")
                    currentDateAndTime = datetime.datetime.now()
                    log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + f": The file named '{filename}' was downloaded.\n")
            except:
                print(f"The file named '{filename}' could not be downloaded.")
                currentDateAndTime = datetime.datetime.now()
                log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) +
                          f": The file named '{filename}' could not be downloaded.\n")
    else:
        print("No files exist in the FTP directory.")
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) +
                  ': No files exist in the FTP directory.\n')


    # Moving files from the local directory containing
    # the downloaded files to the directory
    # of the internal network
    sourceLocalDirectory = './LocalDirectoryForTransferFromServer'

    # Getting a list of files in the directory containing
    # the downloaded files.
    listOfDownloadedFiles = []
    for filename in os.listdir(sourceLocalDirectory):
        file_path = os.path.join(sourceLocalDirectory, filename)
        if os.path.isfile(file_path):
            listOfDownloadedFiles.append(filename)

    print('\nList of downloaded files:')
    print(listOfDownloadedFiles)
    # for filename in listOfDownloadedFiles:
    #     print(filename)

    # Moving the downloaded files to the internal network directory.
    destinationDirectoryOfInternalNetwork = r'.\DirectoryOfInternalNetwork'
    if os.path.exists(destinationDirectoryOfInternalNetwork):
        print(f"\nThe directory {destinationDirectoryOfInternalNetwork} on the internal network exists.")
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + f": The directory {destinationDirectoryOfInternalNetwork} on the internal network exists.\n")
    else:
        print('\nThe directory on the internal network does not exist. Creating it now.')
        os.makedirs(destinationDirectoryOfInternalNetwork)
        currentDateAndTime = datetime.datetime.now()
        log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + ': The directory on the internal network did not exist. It has been created.\n')

    for downloadedFile in listOfDownloadedFiles:
        sourcePath = os.path.join(sourceLocalDirectory, downloadedFile)
        destinationPath = os.path.join(destinationDirectoryOfInternalNetwork, downloadedFile)

        try:
            shutil.move(sourcePath, destinationPath)
            print(f"File '{downloadedFile}' has been moved to the directory on the internal network,'{destinationDirectoryOfInternalNetwork}'.")
            currentDateAndTime = datetime.datetime.now()
            log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + f": File '{downloadedFile}' has been moved to the directory \non the internal network,'{destinationDirectoryOfInternalNetwork}'.\n")
        except:
            print(f"Downloaded file '{downloadedFile}' could not be moved.")
            currentDateAndTime = datetime.datetime.now()
            log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + f": Downloaded file '{downloadedFile}' could not be moved.\n")

    ftp.quit()

# Initiating operations log
log = open('Log', 'a')

# automateFileTransfer()

# Scheduling the script to run daily at a specific time.
try:
    scheduledTime = '10:00'
    print('\nThe script has been scheduled to run daily at ' + scheduledTime + '.')
    sc.every().day.at(scheduledTime).do(automateFileTransfer)
    currentDateAndTime = datetime.datetime.now()
    log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + f": The script has been scheduled to run daily at {scheduledTime}.\n")
    while True:
        sc.run_pending()
except:
    print('The execution has stopped.\n')
    currentDateAndTime = datetime.datetime.now()
    log.write(str(currentDateAndTime.strftime("%d-%m-%Y %H:%M:%S")) + ': The execution has stopped.\n')

log.close()
