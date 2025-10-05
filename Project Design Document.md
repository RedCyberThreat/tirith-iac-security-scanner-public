
**Project Title:** AWS IaC Security Scanner 

**Team Members:**
+ Mauro 
+ Marco 
+ Matteo
+ Lorenzo 
+ Niccolò 

**Mentor:** Jelena 
**Date:** 5 October 2025

1. **Introduction**

**Problem Statement:** Cloud misconfigurations are a prevasive and significant source of security vulnerabilities, frequently leading to data breaches and compliance issues. Manually identifying these misconfigurations within Infrastructure as Code (IaC) templates, especially in large and complex AWS CloudFormation deployments, is a time-consuming, error-prone and unscalable process. This challenge is compounded by the "shitf-letf" security paradigm, which emphasizes detection issues early in development life-cycle before deployment, reducing the cost and effort of remediation.

**Project Objective:** The project aims to develop a fast, user-friendly, and free, easy to access web-based Minimum Viable Product (MVP) that empowers developers to proactively identify and rectify security misconfigurations in their AWS CloudFormation (JSON) templates before deployment. By providing automated scanning and actionable recommendations, the tool seeks to enhance security posture, enforce best practices, and accelerate secure cloud deployments.

2. **Key Features (MVP)**
+ **Cloud formation Template Upload:** Allows users to upload their CloudFormation JSON templates for scanning 
+ **Automated Security Scanning:** Automatically analyzes the uploaded templates against a predefined set of security rules.
+ **Detection of Misconfigurations:** Identifies common security misconfigurations, as: 
	 - S3 buckets with public access enabled (S3_PUBLIC_ACCESS_BLOCK).
	 -  S3 buckets with server-side encryption (S3_BUCKET_NO_SERVER_SIDE_ENCRYPTION).
	 - IAM policies containing * in the Action field (IAM_POLICY_CONTAINS_ASTERISK_ACTION). 
	 - Security Group ingress rules open to the world on sensitive ports (22, 3389) (SECURITY_GROUP_INGRESS_OPEN_TO_WORLD)
     - RDS DB instances without storage encryption (RDS_INSTANCE_NO_STORAGE_ENCRYPTION) 

+ **Actionable Remediation Recommendations:** Provides clear, concise recommendations on how to fix identified security issues.
+ **Severity Levels:** Assigns a severity (High, Medium, or Low) to each finding. 
+ **User-Friendly Interface:** Presents scan results in an intuitive web interface for easy understanding and navigation 

3. **Low-Level Design:**

![[Low_Level_Design.png]]

The AWS IaC Security Scanner will operate as a web application. The core components will include:
**Frontend (Web Application):** A user interface built with Vite with React and Tailwind CSS that allows users to upload CloudFormation templates. It will display the scan results, including identified misconfigurations, their severity, and recommendations.

**Backend (API & Scanner Engine):** A Python-based backend (using Flask) that handles:
Template Upload & Parsing: Receives the uploaded CloudFormation templates and parses them (JSON), through specific designed functions, into an internal, structured representation.

**Security Rules Engine:** Contains the logic for the predefined security rules. Each rule is designed to identify specific misconfigurations. The logic will be split into two main chunks. One function will be coded by the dev team, while the other will be a more general function that calls the CloudFormation Guard logic.
Quick research, this call will trigger the function developed by the team. This function, by taking the inputted JSON, will analyse the file in search of five pre-defined misconfigurations (the five explained before). Then the function will return a JSON-formatted document containing the misconfigured rules, the threat severity of these misconfigurations, and how the user can fix them.

**Deep research**, this call will trigger a function that implement the CloudFormation Guard logic (that will include a set of best practice rules designed by the team). This function will perform a much deeper scan in the document individuating misconfiguration and threats in the majority of the rules instead that limiting to five. This function also return a JSON file as the Quick research one.

**API Functionality:** When a user sends a quick or deep research request, the API will perform a POST request to pass a JSON-formatted document containing all the needed information (like the type of scan) to the backend logic to start the scan. Then a GET request will be performed. If the scan is still processing, the user will be prompted to wait. If the scan has finished, it will return a JSON-formatted file to the web app that will display the results (threats found, severity, possible suggestions).
The overall workflow will involve the user uploading a template via the web interface. This template is sent to the backend, parsed, analysed by the security rules engine, and the findings are then sent back to the frontend for display to the user.

---

4. **Technologies**

**Programming Languages:**
Python: Primarily for the backend development, including the parsing logic, security rules engine, and API. Python is chosen for its extensive libraries, readability, and suitability for backend processing and security tool development.

**TypeScript:** For frontend development, specifically with React, to create a dynamic and interactive user interface. Strongly typed superset of JS to prevent runtime errors.
Frameworks and Libraries:
React: A JavaScript library for building user interfaces, enabling a responsive and component-based frontend.

**Tailwind CSS:** A utility-first CSS framework for rapidly styling the frontend application.

**Flask:** Python web frameworks for building the backend API. These frameworks are lightweight and efficient for developing RESTful services.

**json_source_map:** Libraries for parsing JSON CloudFormation templates in the backend.

**cnf-lint:** Libraries to request 


**Tools and Services:**
**Jira:** For project management, enabling Scrum methodology, tracking tasks, managing sprints, and organizing the product backlog.

**Git & GitHub:** For version control, collaborative code development, branching, and pull requests to manage code integration. The main repository will be named iac-security-scanner.

**Affinity Designer 2:** For UI/UX design, creating high-fidelity mockups and visual prototypes of the web application.














 








