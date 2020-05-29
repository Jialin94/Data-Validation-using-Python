# Data-Validation-using-Python
validate csv file

Validation Rules

student: 9 digits. acceptable formats: 000000000, 000 000 000  
password: a-z, A-Z, 0-9, ascii printable special characters, minimum 12 characters 
username: a-z, A-Z, 0-9, minimum 3 characters, maximum 20 characters  
email: username@domain.TLD, username, domain and TLD will conform to the rules above for a “username” field. 
There will only be one TLD (i.e. no multiples like domain.co.uk) 
previous: Confirm that this data field is identical to the previous line’s data field (excluding whitespace) 
phone: A North American phone number. Possible formats: 1234567890, 123.456.7890, 123-456-7890, (123) 456-7890  
postal: A Canadian postal code. Possible formats: A0A0A0, A0A 0A0  
address: A string field containing a-z, A-Z, 0-9, periods and dashes. 
binary: A single binary string, must contain only 1s and 0s with no breaks between digits 
bio: A generic string field. Report “no” only if the field contains any html tags.

Sample Input File  
student,999999999 
password,abcd1234  
username,user123  
email,testuser@testdomain.com  
previous,testuse@testdomain.com  
phone,123-456-7890  
postal,M86 72Z  
address,123 street blvd. 
binary,11110000  
bio,    hello world  
student,9999 9999  
student,      111111111  
password,123456abcdef!!  
username,stevedave  
previous,stevedave  
phone,((416-111-1234  
postal,H1R3T7  
bio,Hello<script>World</script> 

Sample Output  
yes  
no  
yes  
yes  
no  
yes  
no  
yes  
yes  
yes  
no  
yes  
yes  
yes  
yes  
no  
yes  
no 
