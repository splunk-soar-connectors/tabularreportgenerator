[comment]: # "Auto-generated SOAR connector documentation"
# Tabular Report Generator

Publisher: Splunk Community  
Connector Version: 1\.0\.1  
Product Vendor: Splunk Community  
Product Name: SOAR  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.2\.0  

This app \(TRG\) provides actions to generate a tabular report that can be sent via email or stored as HTML to vault


Replace this text in the app's **readme.html** to contain more detailed information


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a SOAR asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**image\_list** |  optional  | string | Name of custom list storing images

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[generate report email](#action-generate-report-email) - Generate raw email output containing the report  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'generate report email'
Generate raw email output containing the report

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**report\_json** |  required  | Report specification in JSON format | string |  `trg report json` 
**from** |  required  | Report specification in JSON format | string | 
**to** |  required  | Report specification in JSON format | string | 
**subject** |  required  | Subject of the email to be sent | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.report\_json | string |  `trg report json` 
action\_result\.status | string | 
action\_result\.parameter\.from | string | 
action\_result\.parameter\.to | string | 
action\_result\.parameter\.subject | string | 
action\_result\.message | string | 
action\_result\.data\.0\.rawemail | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 