

Function get-pwdset($user)
{	
	$defaultPassword = "Abc1234!"
	
	$userfound=net user | findstr /i $user
	if ($userfound -match $user)
		{
			 write-host "$user already exists"
			 
			$output = net user $user $defaultPassword
			write-host $output
			
			If( $output -match  "successfully")
			{
				$Password_Last_set_time=net user $user | find /I "Password last set"
				write-host $user $Password_Last_set_time
				
			}
			else
			{
				write-host "Net command failed while setting password for " $user 
			}
		}
	else
		{
		  write-host "$user User dosent exists"
		}
	
}


get-pwdset "tst10"