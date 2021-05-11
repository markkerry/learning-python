# Key/Value pair
# All keys have to be unique

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Jun"])
print(monthConversions.get("Jul"))

# Can set a default value if key not available
print(monthConversions.get("fdfds", "Not a valid key"))