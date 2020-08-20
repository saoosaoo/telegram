from pydrive.drive import GoogleDrive
from drive_authentication import authenticate
import os

def Upload_file(file_path):
    drive = GoogleDrive(authenticate("my_cred"))
    folder_id = "1l6qp-0L1JDMf8opgoojteQ4DzWZN9Ru_"
    file1 = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folder_id}]})
    file1.SetContentFile(file_path)
    file1.Upload()
    file1.content.close()
    os.unlink(file_path)
    print("업로드 완료!")

if __name__ == "__main__":
    Upload_file("")