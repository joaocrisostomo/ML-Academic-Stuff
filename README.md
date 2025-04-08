# GitHub SSH Configuration for Personal and Professional Accounts

This guide helps you configure separate SSH keys for your **personal** and **professional** GitHub accounts on the same machine.

---

## 🚀 Step-by-Step Instructions

### 1. Generate a New SSH Key for Your Personal Account

```bash
ssh-keygen -t rsa -b 4096 -C "jdiogo.rcosta@gmail.com"
```

🔐 **Important:** When prompted for a file to save the key, **don’t overwrite your existing key**
(usually `~/.ssh/id_rsa`).
Instead, use a custom name: bash CopyEdit”

Enter file in which to save the key:
```bash
~/.ssh/id_rsa_personal
```
You can enter a passphrase (recommended) or leave it empty.

### 2. Add Your SSH Key to the SSH Agent Start the SSH agent in the background:
```bash
eval "$(ssh-agent -s)"
```

### 3. Add Your Public Key to GitHub
Display the new public key:
```bash
cat ~/.ssh/id_rsa_personal.pub
```
Copy the output and add it to your GitHub SSH keys settings for your personal account

###4. Create an SSH Config File
Edit or create the SSH config file:
```bash
nano ~/.ssh/config
```

```bash
# Personal GitHub
Host github-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa_personal

# Work GitHub (default)
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa
```

### 5. Clone Repositories Using the Correct Host
Use the github-personal alias for personal repositories:
```bash
git clone git@github-personal:your-username/your-repo.git
Ex: git clone git@github-personal:Real-World-ML/real-time-ml-system-cohort-4.git
```
