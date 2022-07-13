This code will create/update smax change request.

-1 Before an apply create a CR related to change <- input from PR / Branch etc
-2 Update CR with fields specific to the change (initial CR does not have all the fields until created)
  1 User
  2 Team
  3 etc
-3 cache or write to key/value store the CR ID
-4 apply
-5 update and close CR
