
import os
import json
import sys

from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential

site_name = sys.argv[1]
username = sys.argv[2]
psword = sys.argv[3]
folder_name = sys.argv[4]
path = sys.argv[5] # filename 
print(" ")
print("site_name  : " + site_name)
print("username   : " + username)
print("password   : " + psword)
print("folder_name: " + folder_name)
print("path       : " + path)

site_url="https://slsoffice.sharepoint.com/sites/"+ site_name

ctx = ClientContext(site_url).with_credentials(UserCredential(username, psword))

with open(path, 'rb') as content_file:
    file_content = content_file.read()

list_title = "Documents"
target_folder = ctx.web.lists.get_by_title(list_title).root_folder.folders.get_by_url(folder_name) # give name of the folder here which you wish to upload a file 
# target_folder = ctx.web.lists.get_by_title(list_title).root_folder # this one will upload file on root folder directly
name = os.path.basename(path)
target_file = target_folder.upload_file(name, file_content).execute_query()
print(" ")
print("File has been uploaded to url: {0}".format(target_file.serverRelativeUrl))
