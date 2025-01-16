press_release = """

ACE IT Support, a nationwide leader in IT services, is growing its footprint in the IT industry with the opening of an office in Orlando, Florida. ACE currently supports IT in over 57 territories across 23 states and has been named the number-one IT support franchise in the United States by Entrepreneur Magazine's annual Franchise 500 list.

"""

# Remove the leading and trailing whitespace (new lines) from press_release

press_release = press_release.strip()

# Replace the phrase "IT" with "Information Technology" in the press release.  Our research shows "Informatics" tests better than "IT"

press_release = press_release.replace("IT","Informatics")

# We changed our company name! replace the phrase "ACE" with "ICE" 

press_release = press_release.replace("ACE","ICE")

# Our research shows that it's best to shout our press releases. Make the entire press release uppercased!

press_release = press_release.upper()

# Print out the updated press release with all of the above changes:


print(press_release)

#ICE INFORMATICS SUPPORT, A NATIONWIDE LEADER IN INFORMATICS SERVICES, IS GROWING ITS FOOTPRINT IN THE INFORMATICS INDUSTRY WITH THE OPENING OF AN OFFICE IN ORLANDO, FLORIDA. ICE CURRENTLY SUPPORTS INFORMATICS IN OVER 57 TERRITORIES ACROSS 23 STATES AND HAS BEEN NAMED THE NUMBER-ONE INFORMATICS SUPPORT FRANCHISE IN THE UNITED STATES BY ENTREPRENEUR MAGAZINE'S ANNUAL FRANCHISE 500 LIST.
