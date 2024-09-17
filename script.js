const fs = require("fs");

const loadUsers = (filePath) => {
  return fs
    .readFileSync(filePath, "utf-8")
    .split("\n")
    .map((user) => user.trim())
    .filter((user) => user !== "");
}

const shuffleUsers = (users) => {
  for (let i = users.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [users[i], users[j]] = [users[j], users[i]];
  }
  return users;
}

const randomizeUsers = (filePath) => {
  const users = loadUsers(filePath);
  return shuffleUsers(users);
}

const filePath = process.argv[2];

if (!filePath) {
  console.log("ユーザーリストのファイルパスを指定してください。");
  process.exit(1);
}

const randomizedUsers = randomizeUsers(filePath);

randomizedUsers.forEach((user) => {
  console.log(user);
});
