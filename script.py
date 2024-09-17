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
        print("Specify the file path of the user list.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    randomized_users = randomize_users(file_path)
    
    for user in randomized_users:
        print(user)
