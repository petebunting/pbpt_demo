# This comment can be used to generate a set of template scripts
# the path to the database connection file should be specified
# and the output path for the template scripts which are to be 
# generated.

# In this case, the output directory will be the current directory (i.e., '.')
# The database connection file is within the home folder.

pbpt_gen_template.py -o . -d /home/pete/.pbpt_db_conn.txt


# NOTE, the database connection file should have the format:
# postgresql://<db_user>:<db_pass>@127.0.0.1:5432/<db_name>
# <db_user> - is the username for the database
# <db_pass> - is the password for the database
# <db_name> - is the name of the database
# 127.0.0.1:5432 - is the IP address and port for the database. This is the default for a local database using the default port number.

# If you are configuring a database to use with pb_process_tools 
# I would recommend that you increase the default concurrent connections
# to more than you would expect (i.e., double the number of concurrent 
# tasks you expect to use as it takes a while for the DB to release
# a connection so you need to configure the database to have more than 
# you would think to avoid errors. 



