This repo has been created with the intention of automate change requests:

This code will create/update smax change request.

Download Fields.xlsx and find the actual field name in question. 

-1 Before an apply create a CR related to change <- input from PR / Branch etc
-2 Update CR with fields specific to the change (initial CR does not have all the fields until created)
  1 User
  2 Team
  3 etc
-3 cache or write to key/value store the CR ID
-4 apply
-5 update and close CR

API at:
https://docs.microfocus.com/doc/SMAX/2022.05/BulkUpdate

Get any IDs needed from test tenant:
https://us2-smax.saas.microfocus.com/saw/ess?TENANTID=107894932

by clicking the icon next to the field in question:
 

Then do a search if needed,
 
Do a get to find out the subcategories having the main actual name.
