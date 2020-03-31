# Errors and their solutions

##SMTP_SSL has no attribute 'encode'##
when smtplib not working properly or installation problem due to some reasons

## unused import statement 
when smtplib used first time it was creating a problem so use SMTP from smtplib rather than importing it directly,
or in case try to optimize imports if it works in my case it did'nt work
						 
## unresolved refernce smtp 
becoz smtplib not working or not imported ,if smptlib is making more problem then see from command prompt if it is installed or not ,if not then install it first
                          
## ConnectionRefusedError:[WinError 10061]No connection can be made if target machine refused the error:

either while sending mail internet connection is not proper or using proxy server port 80 is not free
																									  
## smtplib.SMTPResponseException 

## smtplib not imported or installed

## smtplib-SMTPAuthenticationError 
2 step verification i.e. app password  not done for sending email 
##password incorrect 
many times it may show this so its better to add user and password to enviornment variables

## raise SMTPAuthenticationError(code, resp) smtplib.SMTPAuthenticationError: (534, b'5.7.9 Application-specific password required 
2 step verification i.e app password  not done for sending email or turn on less secure app settings by going in security control 
in ur gmail account

## socket.gaierror: [Errno 11001] getaddrinfo failed 
internet connection is not good

## ValueError: I/O operation on closed file 
while reading csv file if file is currently in working 

##`UnicodeDecodeError: 'utf-8' codec can't decode byte 0x98 in position 16: invalid start byte` 
it may include a charcter in csv file which is not decoded by utf8 try `utf16` , `cp437`,`cp1252` encodings or if u have to only read the file then use 'r' or 'rb'

ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.= error while installing sendEmail
UnicodeDecodeError: 'charmap' codec cant decode bye X in position Y  = same as utf8 error
_csv.error : line contains NULL = remove it by using replacing NULL character by space one option is this in csv file content
