# **🛡️ Tirith: AWS IaC Security Scanner**

An open-source, user-centric security scanning platform for **AWS CloudFormation (CFN)** templates. Tirith transforms complex CLI-based security audits into a seamless, visual, drag-and-drop web experience, making IaC security accessible to every developer.

### **Project Goals & Philosophy**

The Tirith project was created to address the friction in modern Infrastructure as Code (IaC) workflows. While command-line tools like CFN-LINT and cfn-nag are powerful, they often slow down the initial development and audit phases.

**Our Core Value:** To prioritize the human user. Tirith provides:

* **Zero-Friction Auditing:** No installation required; simply drag and drop your CFN template.  
* **Visual Remediation:** Clear, color-coded results with line-number specific guidance on how to fix misconfigurations.  
* **Dual-Layer Scanning:** Quick Scan for critical, high-severity risks, and Deep Search for comprehensive compliance.

## **💻 Technical Stack**

Tirith is built on a modular, scalable architecture with a clear separation of concerns:

| Component | Technologies | Purpose |
| :---- | :---- | :---- |
| **Frontend (UI)** | React (with Vite), TypeScript, Tailwind CSS | Provides a dynamic, responsive, and intuitive user interface. |
| **Backend API** | Python (Flask) | Handles routing, manages file uploads, and orchestrates the scanning process. |
| **Core Logic** | CFN-LINT (Integrated via Custom API) | The core engine for security policy enforcement and misconfiguration detection. |

### **🚀 Running Instructions**

Here are the steps for anyone who clones this repository to get the **Tirith** scanner running on their local machine.

1. **Prerequisites:** Ensure you have **Git** and **pnpm** installed on your system.  
   * *Note: This project uses **pnpm**, not npm or yarn. Using a different package manager may cause issues.*  
2. **Clone the Repository:** Open your terminal and run the following command, replacing \<repository-url\> with your Git URL.  
   git clone \<repository-url\>

3. **Navigate to Project Directory:**  
   cd \<project-name\>

4. **Install Dependencies:** Run the **pnpm** install command. This reads the pnpm-lock.yaml file to install the exact versions of all project dependencies and creates the node\_modules folder.  
   pnpm install

5. **Build the Frontend:**  
   pnpm build

6. **Run the Development Server:** Start the Flask development server to view the application in your browser.  
   python3 main.py

   Your terminal will output the local URL where the application is running (usually http://localhost:8080).

## **🤝 Contribution**

Tirith is an open-source project. We welcome contributions, bug reports, and suggestions for future features such as Terraform support or custom policy creation\!
