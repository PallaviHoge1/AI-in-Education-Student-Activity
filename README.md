# Summary of the AI-Enabled School Education System

**Objective:**
The goal of the project is to develop an AI-enabled education system as a proof of concept for Class 1 in a primary school setting. The aim is to enhance educational outcomes using data-driven insights and AI-powered tools.

**Key Features:**

1. **User-Specific Dashboards:**
   - **Teachers:** Dashboards for inputting student performance data, viewing class performance, and accessing customized lesson plans.
   - **Parents:** Read-only dashboards to monitor their child's performance.
   - **Principals and Administrators:** Dashboards to view comprehensive reports on student, teacher, and class performance, and to manage lesson plans.

2. **Educational Framework:**
   - **Hierarchy of Goals:** The system is structured around broad educational goals, curricular goals, competencies, and measurable learning outcomes to ensure a comprehensive approach to student development.
   - **Competencies and Learning Outcomes:** The system focuses on specific competencies and learning outcomes, which are the measurable skills and knowledge that students should demonstrate.

3. **Assessment and Reporting:**
   - **Student Performance Reports:** Generated based on activities that measure specific competencies and learning outcomes.
   - **Teacher Performance Reports:** Analyzed through student outcomes and only accessible to administrators and principals.
   - **Class Performance Reports:** Provide an aggregate view of student performance in a class.

4. **Customized Lesson Plans:**
   - Tailored lesson plans are generated based on the identified learning needs and gaps for each student to address specific educational requirements and improve outcomes.

5. **Activities and Grading:**
   - The system includes a range of activities designed to target specific competencies. These activities are graded on a scale from 1 to 5 to quantify student development in various competencies.

6. **Learning Gaps and Needs:**
   - **Learning Gaps:** Identified as the difference between what a student has learned and what they were expected to learn.
   - **Learning Needs:** Specific requirements for each student to address their learning gaps, which guide the creation of customized lesson plans.

By integrating AI and data-driven methodologies, this project aims to enhance educational quality and provide personalized learning experiences, thereby improving educational outcomes for students.


# How to Setup and use [Developer's Guide]:

Sure! Here’s an updated "How to Use" section that includes instructions for setting up the Python environment, creating a virtual environment, and installing requirements:

### How to Use

### Python Setup

1. **Ensure Python 3.10 is Installed:**
   - Verify that you have Python 3.10 installed on your system. You can check the version by running:

     ```bash
     python3.10 --version
     ```

   - If Python 3.10 is not installed, download and install it from the [official Python website](https://www.python.org/downloads/release/python-3100/).

### Setting Up the Virtual Environment

2. **Create a Virtual Environment:**
   - Navigate to the directory where your project is located.
   - Create a virtual environment named `.venv` by running:

     ```bash
     python3.10 -m venv .venv
     ```

   - This command will create a virtual environment in a directory named `.venv` within your project directory.

3. **Activate the Virtual Environment:**
   - On **Windows**, activate the virtual environment using:

     ```bash
     .venv\Scripts\activate
     ```

   - On **macOS/Linux**, activate it using:

     ```bash
     source .venv/bin/activate
     ```

   - After activation, your terminal prompt should indicate that you are now working within the virtual environment.

### Installing Project Dependencies

4. **Install Required Packages:**
   - Ensure that your virtual environment is activated.
   - Install the necessary packages listed in `requirements.txt` by running:

     ```bash
     pip install -r requirements.txt
     ```

   - This command will install all the dependencies required for your project as specified in the `requirements.txt` file.

### Encrypting Passwords


5. **Encrypt Your Password:**
   - Open your terminal and navigate to the directory containing `encrypt.py`.
   - Run the following command to encrypt your password:

     ```bash
     python encrypt.py
     ```

   - Follow the prompts to enter the password you want to encrypt.
   - The script will generate an encrypted password and save it to the specified file.

6. **Decrypt Your Password:**
   - To decrypt a password, use the same script with the appropriate decryption command. Make sure you provide the correct encryption file and password.
