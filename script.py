import random
import sys

def load_users(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        users = [line.strip() for line in f if line.strip()]
    return users

def randomize_users(file_path):
    users = load_users(file_path)
    randomized_users = random.sample(users, len(users))
    return randomized_users

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ユーザーリストのファイルパスを指定してください。")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        randomized_users = randomize_users(file_path)
    except OSError:
        print(f"ファイルを読み込めませんでした: {file_path}")
        sys.exit(1)

    for user in randomized_users:
        print(user)
