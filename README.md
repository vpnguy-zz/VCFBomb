VCFBomb<br />

Usage:<br />
<b>VCFBomb.py </b> <br /> 


Example:<br />
<b>VCFBomb.py</b> - Will launch the simple script asking to select which attack to launch.

<b>Attacks</b><br />
<b>ManyContact</b> - Generates a card with a large number of contacts. Microsoft's "Windows Contacts" creates a window for each contact once a VCF file is opened. Since a single VCF file can contain unlimited contacts this can be exploited to a comical use. The effect is not harmful and easily can be ended by task manager. Can also be used to cause a battery drain on android based systems.<br />
<b>LargeCard</b> - Generates a card with a large name field. By generating a large name field "Windows Contacts" will begin consuming CPU and memory at an alarming rate. On android systems importing the contact file will cause it to not be entered into the phones contact system, in addition attempting to send the contact via bluetooth or gmail application will yield a crash of the file manager application (possible pathway to overflow exploit?)