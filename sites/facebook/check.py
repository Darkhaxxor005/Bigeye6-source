"""
Check if a facebook id or password is valid
"""
from os import system
from json import load, dumps
from random import randint
from urllib import parse
from sys import argv

try:
    import mechanize
except:
    system('pip install mechanize')
    exit()

def log(data, login=False, error=False):
    """
    Write to logfile
    """
    filename = "info.log"
    if error:
        filename = "error.log"
    if login:
        filename = "usernames.txt"
    with open(filename, "a", encoding="utf-8") as file:
        file.write(str(data))

def check():
    """
    Main function
    """
    if len(argv) != 3:
        print(dumps({"error_code": 401}))
        return
    email = argv[1]
    password = argv[2]
    if len(password) < 6:
        print(dumps({"error_code": 401}))
        return
    ue_email = parse.quote(argv[1])
    ue_password = parse.quote(argv[2])
    user_agent = f'Mozilla/5.0 (Linux; Android {str(randint(4,11))}.0; Nexus 5 Build/MRA{str(randint(30,60))}N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.{str(randint(1600,1661))}.41'
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    browser.addheaders = [('User-Agent', user_agent)]
    resp = browser.open(f"https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email={ue_email}&locale=en_US&password={ue_password}&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm")
    try:
        response = load(resp)
        if "access_token" in response or ("error_code" in response and response["error_code"] == 406):
            log(f"Facebook email: {email}\nPassword: {password}\n", login=True)
        print(dumps(response))
        log(f"Email: {email}\nPassword: {password}\nResponse: {response}\n")
    except:
        print(dumps({"error_msg": "unknown"}))
        log(f"Email: {email}\nPassword: {password}\nResponse: {response}\n", error=True)
    # print(response)
    # if 'access_token' in response:
    #     print("success")
    # else:
    #     if 'www.facebook.com' in response['error_msg']:
    #         print("checkpoint")
    #     else:
    #         print("invalid")


def main():
    """
    Entrypoint of script
    """
    try:
        check()
    except Exception as err:
        log(err, error=True)

if __name__ == "__main__":
    main()
