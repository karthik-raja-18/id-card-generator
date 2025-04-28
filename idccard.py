import random
import datetime
import qrcode

def generate_id_card(company, college_logo_path, student_name, department, student_image_path, blood_group, dob, phone_number, address):
    # Generate a unique ID number
    idno = random.randint(10000000, 90000000)

    # Generate QR code data
    qr_data = f'Name: {student_name}\nDepartment: {department}\nID: {idno}'

    # Save the QR code image
    qr_code_path = f'{idno}.png'
    qr_code = qrcode.make(qr_data)
    qr_code.save(qr_code_path)

    # Create HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ID CARD GENERATOR</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f0f0f0;
            }}
            .container {{
                width: 500px;
                margin: 50px auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                margin-bottom: 20px;
            }}
            .logo {{
                max-width: 100%;
                max-height: 100%;
            }}
            .student-img {{
                width: 200px;  /* Set the fixed width */
                height: 200px; /* Set the fixed height */
                margin: 0 auto; /* Center the image */
                overflow: hidden; /* Hide overflow */
                border-radius: 50%; /* Make it round */
            }}
            .student-img img {{
                max-width: 100%; /* Make the image responsive */
                display: block; /* Remove any default inline styles */
                margin: 0 auto; /* Center the image */
            }}
            .qr-code {{
                max-width: 200px;
                max-height: 200px;
                display: block;
                margin: 0 auto;
            }}
            .info {{
                margin-top: 20px;
            }}
            .info p {{
                margin: 10px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>{company}</h2>
                <img src="{college_logo_path}" alt="College Logo" class="logo">
            </div>
            <div class="info">
                <p><strong>Name:</strong> {student_name}</p>
                <p><strong>Department:</strong> {department}</p>
                <div class="student-img">
                    <img src="{student_image_path}" alt="Student Image">
                </div>
                <p><strong>Blood Group:</strong> {blood_group}</p>
                <p><strong>Date of Birth:</strong> {dob}</p>
                <p><strong>Phone Number:</strong> {phone_number}</p>
                <p><strong>Address:</strong> {address}</p>
                <img src="{qr_code_path}" alt="QR Code" class="qr-code">
            </div>
        </div>
    </body>
    </html>
    """

    # Save HTML content to a file
    html_file_path = f'{student_name}_ID.html'
    with open(html_file_path, 'w') as file:
        file.write(html_content)

    print(f'ID Card HTML generated: {html_file_path}')

# Input details
company = input('Enter Your College Name: ')
college_logo_path = input('Enter the path to your college logo: ')
student_name = input("Enter Student's Full Name: ")
department = input("Enter Student's Department: ")
student_image_path = input('Enter the path to your student image: ')
blood_group = input("Enter Student's Blood Group: ")
dob = input("Enter Student's Date Of Birth: ")
phone_number = input("Enter Student's Phone Number: ")
address = input("Enter Student's Address: ")

# Generate ID card HTML
generate_id_card(company, college_logo_path, student_name, department, student_image_path, blood_group, dob, phone_number, address)