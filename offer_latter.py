from datetime import date

def generate_offer_letter(name, age, title, reporting_name, salary):
    position = title  # Assuming position and title are the same
    today_date = date.today().strftime("%B %d, %Y")
    
    letter = f"""To,
{name}

Dear {name},

We are pleased to offer you the position of {position} at Catalyst Programmers. Based on your skills and our discussions, we are confident in your potential to be a valuable asset to our team.

Position Details:
    Job Title: {title}
    Location: Jaipur
    Start Date: {today_date}
    Reporting To: Mr. {reporting_name}
    Work Hours: Full-time | Monday to Friday, 10:00 AM to 7:00 PM (Remote)

Compensation and Benefits:
    Monthly Salary: ₹{salary}

This offer is contingent upon the successful completion of any necessary background checks and the submission of required documents. On your first day, please bring valid identification and any documents requested by HR.

Please confirm your acceptance of this offer by replying to this letter or signing below and returning a scanned copy by email to catalystprogrammers@gmail.com.
"""

    return letter

# Input from user
if __name__ == "__main__":
    name = input("Enter candidate's name: ")
    age = input("Enter candidate's age: ")  # Not used in template, but collected
    title = input("Enter job title: ")
    reporting_name = input("Enter reporting manager's name: ")
    salary = input("Enter monthly salary: ")

    offer_letter = generate_offer_letter(name, age, title, reporting_name, salary)
    print("\nGenerated Offer Letter:\n")
    print(offer_letter)

