
# Simple Python Development Environment

Welcome to your straightforward, open-source Python development environment\! This guide will walk you through setting up a project using **pure Python**, **VS Code**, and **Git**. This setup is ideal for educational purposes and industrial coding projects, ensuring you're working with standard, widely-used tools.

-----

## 💻 1. Install Required Software

You'll need to install three main tools to get started. All are 100% open-source and free to use.

### Python

The core of our environment. We'll be using a recent version of Python 3.

  * **Download Python**: [https://www.python.org/downloads/](https://www.python.org/downloads/)
  * **Recommendation**: Choose the latest stable release. It's a good idea to check the box that says "Add Python to PATH" during installation.

Once installed, you can verify it by opening **PowerShell** (on Windows) or your terminal (on macOS/Linux) and typing:

```bash
python --version
# or
py --version
```

### Visual Studio Code (VS Code)

This is a powerful and lightweight code editor. It's an industry-standard tool for developers.

  * **Download VS Code**: [https://code.visualstudio.com/](https://code.visualstudio.com/)

After installation, you should install the **Python extension** within VS Code. This extension provides essential features like code completion, linting, and debugging. You can find it by clicking the Extensions icon on the left sidebar and searching for "Python".

### Git

Git is the most popular version control system. It's how you'll track changes to your code and collaborate with others on GitHub.

  * **Download Git**: [https://git-scm.com/downloads](https://git-scm.com/downloads)

After installing Git, you need to configure your identity. This tells Git who is making the changes. In your terminal or PowerShell, run these two commands, replacing the example values with your own.

```bash
git config --global user.name "John Doe"
git config --global user.email "john.doe@example.com"
```

-----

## 🚀 2. Setting Up Your Project

Now that you have the tools, let's create a new project with its own isolated environment.

### Create a Virtual Environment

A virtual environment is a self-contained directory that holds all the packages your project needs. This prevents conflicts between different projects.

1.  Navigate to your project's folder in your terminal.

2.  Run the following command to create a virtual environment named `std_env`:

    ```bash
    python -m venv std_env
    ```

3.  Activate the environment. This must be done every time you start working on your project.

      * **PowerShell**: `./std_env/Scripts/Activate.ps1`
      * **Git Bash/Terminal**: `source std_env/Scripts/activate`

You'll know it's active when you see `(std_env)` at the beginning of your terminal prompt.

### Install Project Packages

It's best practice to use a `requirements.txt` file to manage your project's dependencies. This file lists all the necessary Python packages and their versions.

1.  Create a file named **`requirements.txt`** in your project folder.

2.  Add the packages you need to the file. Here are some common ones for engineering projects:

    ```plaintext
    numpy
    pandas
    matplotlib
    scipy
    pytest
    jupyterlab
    ```

3.  Install all the packages listed in the file with a single command:

    ```bash
    pip install -r requirements.txt
    ```

### Clone a Repository from GitHub

If you're starting a project from a remote repository, you'll use Git to clone it.

```bash
git clone https://github.com/YourUsername/your_project_name.git
```

### SSH Key Setup for GitHub (Optional but Recommended)

For a more secure and streamlined connection to GitHub, you can set up SSH keys. This allows you to push and pull code without repeatedly entering your password.

1.  Generate a new SSH key by running this command in your terminal:

    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```

2.  Follow the prompts. When asked for a passphrase, you can choose to enter one for added security or leave it blank.

3.  Add the key to your GitHub account settings. You can find detailed instructions on the [GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).