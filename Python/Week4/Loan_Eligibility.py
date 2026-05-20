# Problem 7: Loan Eligibility
# ---------------------------
# A bank decides on a loan based on three factors:
#   - Age must be between 21 and 65 (inclusive).
#   - The applicant must have a job (answer "yes" or "no").
#   - Monthly income (in SAR) determines the result:
#        income >= 5000          -> "Approved"
#        income between 3000 and 4999 -> "Approved with conditions"
#        income below 3000       -> "Rejected: low income"

# If age is outside 21–65            -> "Rejected: age not eligible"
# If applicant has no job             -> "Rejected: no job"

# Ask the user for age, income, and job status, then print the
# result.

# Use logical operators for the age range, and nested if statements
# for the job check and income tiers.


age = int(input("Enter Your Age: "))
income = int(input("Enter Your Income: "))
job_status = input("Do You Have a Job (yes/no)? ")
if 21 <= age <= 65:
    if job_status == "yes":
        if income >= 5000:
            print ("Approved")
        elif 3000 <= income < 5000:
            print ("Approved with conditions")
        else:
             print ("Rejected: low income")
    else:
        print ("Rejected: no job")         
else:
    print ("Rejected: age not eligible")