from tools import set_arguments, set_args_from_os_env, set_bool, check_none
from git import Repo, rmtree, Git
import os


def main():
    args = set_arguments()
    args = set_bool(args)
    args = set_args_from_os_env(args)
    
    # delete all from path if dir is not empty
    if args.force == True: rmtree(args.path)
    
    repo = Repo
    if 'https://' in args.repo:
        check_none(args, ['user', 'repo'])
        args.repo = args.repo[args.repo.find('://') + 3:]
        if args.token is not None:
            remote = f"https://{args.user}:{args.token}@{args.repo}"
        elif args.passw is not None:
            remote = f"https://{args.user}:{args.passw}@{args.repo}"
        else:
            print('ОШИБКА: Вы не указали pass или token')

        repo.clone_from(remote, args.path, branch=args.branch)

    elif 'git@' in args.repo:
        # if args.key is None:
        git_ssh_identity_file = args.key or os.path.expanduser(os.getenv('GIT_KEY_PATH')) or os.path.expanduser('~/.ssh/id_rsa')
        # else: git_ssh_identity_file = args.key

        git_ssh_cmd = 'ssh -i %s' % git_ssh_identity_file

        with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
            Repo.clone_from(args.repo, args.path, branch=args.branch)

    else:
        print('ОШИБКА: Путь для клонирования неверен!')
        exit(1)
    # print(args)


    


if __name__ == "__main__":
    main()
