# Cloud CI Lab Project
## Project Overview

This project demonstrates the implementation of a simple Continuous Integration (CI) pipeline using GitHub Actions and Python. The pipeline automatically validates code changes whenever updates are pushed to the repository.

The project simulates a real cloud engineering workflow where application code is automatically tested before deployment.


## Technologies Used

* Python
* Git
* GitHub
* GitHub Actions
* YAML
* VS Code


## Project Structure

cloud-ci-lab-project/
│
├── app.py
├── test_app.py
├── README.md
│
└── .github/
    └── workflows/
        └── ci.yml

## Application

### app.py
The application prints:
print("Cloud CI Pipeline Running")


## Test Script
### test_app.py
The test validates that the application runs successfully without errors.


## GitHub Actions Workflow
The CI pipeline performs the following tasks automatically:

1. Checks out repository code
2. Sets up Python runtime
3. Prints Python version
4. Runs the application
5. Executes tests
6. Displays build completion message


## Workflow Trigger
The workflow is triggered automatically on every push to the repository.


on:
  push:

## Pipeline Screenshots

### Successful Pipeline Run

![Successful Run](screenshots/successful-run.png)

### Failed Pipeline Run

![Failed Run](screenshots/failed-run.png)

### Fixed Pipeline Run

![Fixed Run](screenshots/fixed-run.png)


## Issues Encountered and Resolutions

### 1. YAML Indentation Errors
Issue:
The GitHub Actions workflow failed due to incorrect YAML indentation.

Resolution:
The indentation structure was corrected to properly nest jobs, steps, and workflow configurations.


### 2. Python Not Installed Locally
Issue:
The local machine could not recognize the `python` command.

Resolution:
Python was installed and added to the system PATH environment variable.


### 3. Workflow Syntax Errors
Issue:
Extra formatting text and incorrect spacing caused workflow validation failures.

Resolution:
The workflow file was cleaned and rewritten using proper YAML formatting.


## Learning Outcomes

Through this project, I learned how to:

* Create and manage GitHub repositories
* Build a simple CI pipeline using GitHub Actions
* Configure workflow automation using YAML
* Run automated application tests
* Interpret pipeline logs and debug failures
* Apply basic GitOps principles
* Use version control effectively in cloud engineering workflows

## Conclusion

This project provided practical experience in implementing Continuous Integration workflows using GitHub Actions. It demonstrated how automation can improve software reliability by validating code changes before deployment.
