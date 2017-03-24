git filter-branch -f --commit-filter '
                GIT_COMMITTER_NAME="Erika Azabache";
                GIT_AUTHOR_NAME="Erika Azabache";
                GIT_COMMITTER_EMAIL="erika@doravel.me";
                GIT_AUTHOR_EMAIL="erika@doravel.me";
                git commit-tree "$@";
        ' HEAD
