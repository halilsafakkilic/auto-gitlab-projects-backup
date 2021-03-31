import os
from config import private_token, repoUrlType
from functions import write_log, load_projects

write_log('Operation starting...')
write_log('*' * 30, False)

write_log('Getting the project list you can access from GitLab.')
projects = load_projects(private_token)
write_log('Your projects fetched.')

write_log('*' * 30, False)

for project in projects:
    if repoUrlType == 'ssh':
        projectUri = project['ssh_url_to_repo']
    else:
        projectUri = project['http_url_to_repo']

    write_log(projectUri + ' cloning...')

    targetDirectory = 'repositories/' + project['path'] + '.git'

    if os.path.exists(targetDirectory):
        write_log(targetDirectory + ' deleting...')
        os.system('rm -rf ' + targetDirectory)

    os.system('git clone --mirror --progress ' + projectUri + ' ' + targetDirectory)

    write_log(targetDirectory + ' clone completed!')
    write_log('*' * 30, False)

write_log('*' * 30, False)
write_log('Operation completed.')
