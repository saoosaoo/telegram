from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate(cred_path):
    gauth = GoogleAuth()
    # 인증 파일 불러오는 코드
    gauth.LoadCredentialsFile(f"{cred_path}.txt")
    if gauth.credentials is None:
        # 또는 local webserver 대신 commandline이나 url을 활용할 수도 있습니다(위의 내용 참고)
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()

    # Save the current credentials to a file
    gauth.SaveCredentialsFile(f"{cred_path}.txt")
    return gauth

if __name__ == "__main__":
    authenticate("my_cred")