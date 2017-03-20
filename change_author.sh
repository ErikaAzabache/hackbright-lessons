git filter-branch -f --commit-filter '
                GIT_COMMITTER_NAME="Erika Azabache";
                GIT_AUTHOR_NAME="Erika Azabache";
                GIT_COMMITTER_EMAIL="me@erikaazabache.com";
                GIT_AUTHOR_EMAIL="me@erikaazabache.com";
                git commit-tree "$@";
        ' HEAD
