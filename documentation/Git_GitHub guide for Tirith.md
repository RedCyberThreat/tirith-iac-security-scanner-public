## **Step 1: Clone the Repository to Your Local Machines**

Each team member needs to get a copy of the repository on their local development machine.

1. **Go to the Repository Page:** On GitHub, go to your **tirith-iac-security-scanner** repository's main page.  
2. **Click "Code":** Look for the green "Code" button.  
3. **Copy HTTPS URL:** In the dropdown, make sure "HTTPS" is selected, and then click the copy icon next to the URL.  
   * *Example URL:* `https://github.com/YourGitHubUsername/tirith-iac-security-scanner.git`  
4. **Open Terminal/Git Bash:** On your local machine, open your preferred terminal or Git Bash (for Windows).  
5. **Navigate to Desired Directory:** Use `cd` to go to the directory where you want to store your project (e.g., `cd Documents/Projects`).

**Clone the Repository:** Run the `git clone` command followed by the copied URL:  
Bash  
git clone https://github.com/YourGitHubUsername/tirith-iac-security-scanner.git

6.   
7. **Enter Credentials:** You'll be prompted for your GitHub username and **Personal Access Token (PAT)**. Using a PAT is more secure than your password for command-line Git operations. If you don't have one, you'll need to create it in your GitHub settings (Settings \> Developer settings \> Personal access tokens).

Each team member should perform this step.

## **Step 2: Set Up the `develop` Branch**

Your

**main** branch will always hold the stable, deployable code. All active development will happen on the

**develop** branch.

**Navigate to the Repository Directory:** In your terminal, `cd` into the newly cloned `iac-security-scanner` directory.  
Bash  
cd tirith-iac-security-scanner

1. 

**Create the `develop` Branch:** Create a new branch named `develop` from `main`.  
Bash  
git checkout \-b develop

2. This command creates the  
    `develop` branch and switches you to it.

**Push `develop` to GitHub:** Push this new branch to your remote GitHub repository.  
Bash  
git push \-u origin develop

3. The  
    `-u origin develop` sets the **upstream branch**, so future `git push` and `git pull` commands on `develop` will automatically refer to `origin/develop`.  
4. **Set `develop` as Default (Optional but Recommended):** You can set `develop` as the default branch in GitHub's settings for better visibility of active development.  
   * Go to your repository on GitHub.  
   * Click "Settings".  
   * In the left sidebar, click "Branches".  
   * Under "Default branch," click the dropdown next to  
      `main` and select `develop`. Click "Update".  
     This will make  
      `develop` the default view when someone visits your repo, reflecting your active development.

## **Step 3: Implement the Feature Branch Workflow**

Now, ensure all team members understand and follow this workflow for their daily development:

**Pull Latest `develop`:** Before starting any new task (user story or subtask), always pull the latest changes from `develop` to your local machine.  
Bash  
git checkout develop  
git pull origin develop

1. 

**Create a New Feature Branch:** Create a new branch for your specific task. Use a clear naming convention, typically  
 `feature/<jira-ticket-id>-<short-description>` or `fix/<jira-ticket-id>-<short-description>`.  
Bash  
git checkout \-b feature/AISS-123-template-parser

2. *(Replace AISS-123 with your actual Jira issue key.)*

**Develop and Commit:** Work on your task, make changes, and commit them regularly to your feature branch.  
Bash  
git add .  
git commit \-m "AISS-123: Implemented basic YAML template parser"

3. 

**Push Feature Branch:** Push your feature branch to GitHub.  
Bash  
git push origin feature/AISS-123-template-parser

4.   
5. **Open a Pull Request (PR):**  
   * Once your feature is complete and tested locally, go to your repository on GitHub.  
   * GitHub will usually prompt you to "Compare & pull request" when it detects a new branch pushed.  
   * Crucially, set the  
      **base branch** to `develop` (not `main`). Your PR should be from  
      `feature/your-branch` into `develop`.  
   * Add a clear title and description, referencing your Jira ticket.  
   * Request a code review from at least one other team member (e.g., Niccolò, as designated code reviewer).  
6. **Code Review and Merge:**  
   * Reviewers will check the code, provide feedback, and request changes if necessary.  
   * Once approved, the feature branch can be merged into  
      `develop`.  
   * It's good practice to use "  
     **Squash and merge**" or "**Rebase and merge**" to keep the `develop` history clean, especially for smaller features.  
7. **Delete Feature Branch:** After merging, delete the feature branch from GitHub (and optionally locally with `git branch -d feature/your-branch`).

This setup ensures a structured, collaborative, and clean development process for our AWS IaC Security Scanner.

**(Figure 1 Example of local repository \- Image showing `git clone` and `cd` commands)**

Bash  
$ git clone https://github.com/RedCyberThreat/tirith-iac-security-scanner.git  
Cloning into 'tirith-iac-security-scanner' ...  
remote: Enumerating objects: 4, done.  
remote: Counting objects: 100% (4/4), done.  
remote: Compressing objects: 100% (4/4), done.  
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0\)  
Receiving objects: 100% (4/4), done.  
$ cd tirith-iac-security-scanner/  
