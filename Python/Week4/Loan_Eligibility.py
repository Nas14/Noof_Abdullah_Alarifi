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
