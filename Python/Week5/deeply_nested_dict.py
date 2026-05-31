
# Problem 4 (H.W): Company Structure (deeply nested)
# --------------------------------------------
# You have a company dict with departments. Each department has
# a manager, team size, and a list of projects:

#     company = {
#         "ceo": "Ahmed",
#         "departments": {
#             "engineering": {
#                 "manager": "Sara",
#                 "team_size": 12,
#                 "projects": ["Backend API", "Mobile App"],
#             },
#             "design": {
#                 "manager": "Omar",
#                 "team_size": 5,
#                 "projects": ["Website Redesign"],
#             },
#         },
#     }

# Do the following:
#   1. Print the CEO's name.
#   2. Print the engineering manager's name.
#   3. Print the design team's size.
#   4. Print the FIRST engineering project.
#   5. Print the TOTAL team size (engineering + design).
#   6. Update the design team's size to 6.
#   7. Add a new department "marketing" with manager "Lina",
#      team_size 3, and an empty project list.
#   8. Print the marketing department after adding it.

# Expected output:
#     CEO: Ahmed
#     Engineering manager: Sara
#     Design team size: 5
#     First engineering project: Backend API
#     Total team size: 17
#     Marketing: {'manager': 'Lina', 'team_size': 3, 'projects': []}

# Solution:

company = {
        "ceo": "Ahmed",
        "departments": {
            "engineering": {
                "manager": "Sara",
                "team_size": 12,
                "projects": ["Backend API", "Mobile App"],
            },
            "design": {
                "manager": "Omar",
                "team_size": 5,
                "projects": ["Website Redesign"],
            },
        },
    }

print (f"CEO: {(company["ceo"])}")
print (F"Engineering manager: {(company["departments"]["engineering"]["manager"])}")
print (f"Design team size: {(company['departments']['design']['team_size'])}")
print (f"First engineering project: {(company['departments']['engineering']['projects'][0])}")
print (f"Total team size: {(company['departments']['engineering']['team_size'])+(company['departments']['design']['team_size'])}")
company['departments']['design'].update ({"team_size": 6})
# print (f"Updated_Design_Team_Size {(company['departments']['design']['team_size'])}")
company['departments'].update ({'marketing':{'manager': 'Lina', 'team_size': 3, 'projects': []}})
print (f"Marketing: {(company['departments']['marketing'])}")