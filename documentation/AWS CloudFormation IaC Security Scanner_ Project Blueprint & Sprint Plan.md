# **AWS CloudFormation IaC Security Scanner: Project Blueprint & Sprint Plan**

## **Project Vision & Core Strategy**

* **Project Vision**: To create a fast, user-friendly web application that empowers developers to proactively find and fix security misconfigurations in their **AWS CloudFormation** templates before deployment.  
* **IaC Type**: The project specializes in **AWS CloudFormation** templates (YAML/JSON format).  
* **Target Audience**: The primary audience includes **Individual Developers**, **Students & Educators**, and **Small Teams/Startups** who need a quick, free, web-based tool for initial security checks.  
* **Tech Stack**:  
  * **Frontend**: **React** & **Tailwind CSS**.  
  * **Backend**: **Python** (Flask/FastAPI).  
  * **Libraries**: PyYAML for parsing.  
* **Core Tooling**:  
  * **Project Management**: **Jira**.  
  * **Version Control**: **Git & GitHub** (using `main`, `develop`, and feature branches).  
  * **Design**: **Figma**.

## **Team Roles & Responsibilities**

* **Mauro**: Project Manager & Frontend Support.  
* **Marco**: Lead Frontend Developer.  
* **Niccolò**: UI/UX Design & Backend Developer (Analyzer & API Logic). Owner for Figma prototype.  
* **Lorenzo**: Backend Developer (Parsing & Data Structures).  
* **Matteo**: Backend Developer (Security Rules Engine).  
* **Scrum Roles**: A **Product Owner (PO)** and a **Scrum Master (SM)** will be assigned from the team members.

---

## **Program Timeline: 11-Week Scrum Sprint Plan**

### **Phase 1: Foundation & Design (Weeks 1-3)**

* **Week 1 – Sprint 0: Onboarding & Foundation Setup**  
  * **Goals**: Initial setup, team alignment, and foundational discussions.  
  * **Deliverables**: Create **Jira** project and set up **GitHub repo**. Define project scope and  
     **5 security rules**.  
  * **Jira**: **EPIC-1: Project Foundation & Initial Setup**.  
* **Week 2 – Sprint 1: Finalize Design Document**  
  * **Goals**: Submit final project idea & design document.  
  * **Deliverables**: Final Design Document, including competitor analysis (Checkov, cfn-lint, KICS) and unique value proposition.  
  * **Jira**: **EPIC-1 continued**.  
* **Week 3 – Sprint 2: UX/UI Design \+ Planning**  
  * **Goals**: Submit full design doc with prototype. UI mockups in Figma.  
  * **Deliverables**: **Figma prototype finalized** (Owner: Niccolò). Submit low-level system design and architecture.  
  * **Jira**: Add Jira **EPIC for UI/UX**.

### **Phase 2: Implementation (Weeks 4-7)**

* **Week 4 – Sprint 3: Start Implementation**  
  * **Goals**: Start coding backend modules and frontend scaffolding.  
  * **Deliverables**: Start development of **Backend Scanner Engine** (Parsing, Rule Engine, Analyzer). Set up  
     **React \+ Tailwind** and File Upload Component.  
  * **Jira**: Begin **EPIC-2: Backend Scanner Engine Development** and **EPIC-3: Web UI**.  
* **Week 5 – Sprint 4: Continue Implementation \+ Market Insights**  
  * **Goals**: Functional backend and dynamic UI. Start user testing.  
  * **Deliverables**: MVP Backend Functional. UI wired to mock backend to display results. Conduct basic  
     **user testing** (min. 3 users).  
  * **Jira**: Continue **EPIC-2** and **EPIC-3**.  
* **Week 6 – Sprint 5: Midpoint Integration and Refinement**  
  * **Goals**: Connect frontend to real API. Resolve bugs.  
  * **Deliverables**: **Connect live Flask API** (remove mock data). Backend fully functional. Create bug tickets in Jira.  
  * **Jira**: Focus on completing core features within **EPIC-2** and **EPIC-3**.  
* **Week 7 – Sprint 6: Continue Full Stack Development**  
  * **Goals**: Final rule implementation. Unit testing.  
  * **Deliverables**: Finalize **all 5 security rules** and API error handling. Implement  
     **unit tests for each rule**. UI polish.  
  * **Jira**: Continue working on active sprints.

### **Phase 3: Integration & Submission (Weeks 8-11)**

* **Week 8 – Sprint 7: Integration & Testing**  
  * **Goals**: Integrate components into final MVP. Complete test cases.  
  * **Deliverables**: Complete rule coverage tests. Code merged into `develop`. Internal testing.  
  * **Jira**: Shift focus to integration tasks.  
     **EPIC-4: Enhancements, Testing & Documentation**.  
* **Week 9 – Sprint 8: Finalization**  
  * **Goals**: Polish application. Mentor review and final team QA.  
  * **Deliverables**: Address **mentor feedback**. QA using Jira bug backlog.  
     **PR from `develop` → `main`**.  
  * **Jira**: Begin **EPIC-4 continued**.  
* **Week 10 – Sprint 9: Submissions**  
  * **Goals**: Submit final version of code, design document, and demo video.  
  * **Deliverables**: Record demo walkthrough. Submit final code and design document.  
  * **Jira**: **GitHub tag: `v1.0.0`**.  
* **Week 11 – Sprint 10: Final Presentation Prep**  
  * **Goals**: Create pitch deck and practice pitch.  
  * **Deliverables**: Final PPT submission. Rehearsals and dry run with mentors.

