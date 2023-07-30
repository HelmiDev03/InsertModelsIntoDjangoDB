# Insert Models Into Django DataBase
During my end-of-year internship at a tech company, I undertook the task of creating a user-friendly dashboard for both clients and employees. To make the platform efficient and scalable,  I needed to devise a mechanism for seamlessly inserting new users into the company's database, enabling them to access the dashboard and utilize its features effectively.

To achieve this and before  diving more deeply into the dashboard features, I developed a Python script that accepts user data in a structured text file. The script supports different models, including Clients, Employees, Stagiaires, DevLogiciels, ,ResponsableRH and GestionnaireServiceClient, each with specific formats for data entry.

By following the predefined format, HR personnel can effortlessly add new users to the system. For instance, for new employees, they only need to provide essential information such as username, password, full name, address, email, role, and employment status. Similarly, interns can be inserted into the database with details like their username, password, name, address, email, specialization, faculty, and the username of their assigned Encadrant.

The script ensures that the data conforms to the required formats and that necessary fields are not left empty. If any errors occur, the script handles them gracefully, providing helpful error messages to guide the HR personnel in correcting the data.

This efficient solution not only simplifies the process of onboarding new users but also ensures that the company's database remains organized and up-to-date. With the dashboard now successfully integrated into the company's workflow, employees and clients can conveniently log in and access the platform's features, making their experience smooth and rewarding. 



## Text File Format

The text file must adhere to the following formats for each model:

1. **Client**:
   ```
   Client,username,password,nom,prenom,adresse,email,"","","",""
   ```

2. **Stagiaire**:
   ```
   Employe,username,password,nom,prenom,adresse,email,Stagiaire,specialite,faculte,encadrant_username
   ```
3. **Encadrant**:
   ```
    Employe,username,password,nom,prenom,adresse,email,Encadrant,"","",""
   ```  

4. **DevLogiciel**:
   ```
   Employe,username,password,nom,prenom,adresse,email,Devlogiciel, technologies_utilisees,"",""
   ```
   Make sure `technologies_utilisees` is in the format `x|y|z|t`, where `x`, `y`, `z`, and `t` are chosen from the set of valid technologies (SpringBoot, Django, NodeJS, Flask).

5. **ResponsableRH**:
   ```
   Employe,username,password,nom,prenom,adresse,email,ResponsableRH,"","",""
   ```
6. **GestionnaireServiceClient**:
   ```
   Employe,username,password,nom,prenom,adresse,email,GestionnaireServiceClient,"","",""
   ```

## Usage

1. Ensure you have a Django project set up and the necessary models (Client, Employe, Stagiaire, DevLogiciel, ResponsableRH) defined in your Django application.

2. Create a text file with data entries following the formats mentioned above.

3. Run the Python script and provide the text file as an argument.

   ```
   python add_objects.py Your_FileName.txt
   make sure you update the line  path = f'C:\\Users\\helmi\\OneDrive\\Desktop\\pfa2023\\myenv\\myproject\\{input}.txt' with the path of you own textfile
   ```

4. The script will process the text file and insert the models into the Django database.
5.  Text File must follow the format provided in the exemple_of_text file provided like this

6. If any errors occur during the insertion process (e.g., incorrect format or missing data), the script will print informative error messages and handle them gracefully


  
 # Security Importance
 
In addition to providing a streamlined process for HR personnel to insert new users into the database, I also implemented a user-friendly signup mechanism that empowers employees and clients to create their accounts independently. This feature encourages a self-service approach and reduces administrative overhead.

When an employee or client accesses the platform for the first time, they can easily navigate to the signup page and enter their relevant details, such as username, password, name, address, and email. Upon submission, the system automatically creates a new account in a pending state, awaiting approval from the website administrator.

To maintain security and control over user access, an administrator must review and verify the information provided by each applicant. Once authenticated, the administrator can approve or reject the user's request for account activation. This approval process ensures that only authorized individuals gain access to the platform, safeguarding sensitive information and resources within the tech company.

By offering both HR-assisted user insertion and a self-signup option, the dashboard caters to various scenarios and allows for a more inclusive user experience. The combination of HR-facilitated registration and administrator approval adds an extra layer of security and ensures the website's integrity. This inclusive approach fosters collaboration between different stakeholders and enhances the overall efficiency and user satisfaction of the platform.

Feel free to modify and extend the project to suit your specific needs. Happy coding!
