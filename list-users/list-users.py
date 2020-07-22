import argparse
from bs4 import BeautifulSoup


def list_users(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        for user in soup.find_all('li', class_='accessListData'):
            user_name = user.find(class_='username').string
            user_role = user.find(class_='performAction').span.string
            print(f'{user_name} ({user_role})')


def handler():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Power BI service url with user list")
    args = parser.parse_args()

    if args.file:
        list_users(args.file)


if __name__ == "__main__":
    handler()
