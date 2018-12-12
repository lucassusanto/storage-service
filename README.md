# storage-service

SaaS file storage API implementation using Python and Flask. Cloud Computing Class Final Project.

## Features

1. Authentication
2. Create file
3. Delete file
4. Open file content
5. List of files
6. Make directory
7. Delete directory
8. List of directories
9. Move file location
10. Move directory

## Requirements

1. Tested in Python 3.7.0
2. Python packages:
"""
pip install bcrypt pyjwt flask flask_restful gevent pickledb uuid
"""

## Run Server

python main.py

## Files

1. AuthController.py: Authentication and registration controller
2. AuthRoutes.py: Contains Login and Register API
3. FileController.py: File operations controller
4. FileRoutes.py: Contains file operations API
5. main.py: Main execution file
6. UsersModel.py: Model interacting with 'users.db' file
7. requirements.txt: List of required python packages

## Sample Commands (APIs)

- Register
curl http://localhost:5000/register -X POST -d "{\"username\": \"admin\", \"password\": \"123456\"}"

- Login
curl http://localhost:5000/login -X POST -d "{\"username\": \"admin\", \"password\": \"123456\"}"

- Create file
curl http://localhost:5000/create -X POST -H "Authorization:<token>" -d "{\"file_path\": \"test1.txt\", \"file_content\": \"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"}"

- Open file
curl http://localhost:5000/open -X POST -H "Authorization:<token>" -d "{\"file_path\": \"coba.txt\"}"

- Delete file
curl http://localhost:5000/delete -X POST -H "Authorization:<token>" -d "{\"file_path\": \"test1.txt\"}"

- List files
curl http://localhost:5000/lsfile -X POST -H "Authorization:<token>" -d "{\"folder_path\": \"\"}"

- Create directory
curl http://localhost:5000/mkdir -X POST -H "Authorization:<token>" -d "{\"folder_path\": \"new_folder_1\"}"

- Delete directory
curl http://localhost:5000/rmdir -X POST -H "Authorization:<token>" -d "{\"folder_path\": \"new_folder_1\"}"

- List directories
curl http://localhost:5000/lsdir -X POST -H "Authorization:<token>" -d "{\"folder_path\": \"\"}"

- Move files
curl http://localhost:5000/mvfile -X POST -H "Authorization:<token>" -d "{\"src\": \"test1.txt\", \"des\": \"new_folder_1\"}"

- Move dirs
curl http://localhost:5000/mvdir -X POST -H "Authorization:<token>" -d "{\"src\": \"new_folder_2\", \"des\": \"new_folder_1\"}"
