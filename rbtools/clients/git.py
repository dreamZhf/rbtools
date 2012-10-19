    name = 'Git'

            git_top = execute([self.git, "rev-parse", "--show-toplevel"],
                              ignore_errors=True).rstrip("\n")

            # Top level might not work on old git version se we use git dir
            # to find it.
            if git_top.startswith("fatal:") or not os.path.isdir(git_dir):
                git_top = git_dir

            os.chdir(os.path.abspath(git_top))
                                 'HEAD'], ignore_errors=True).strip()
        if self.head_ref:
            short_head = self._strip_heads_prefix(self.head_ref)
            merge = execute([self.git, 'config', '--get',
                             'branch.%s.merge' % short_head],
                            ignore_errors=True).strip()
            remote = execute([self.git, 'config', '--get',
                              'branch.%s.remote' % short_head],
                             ignore_errors=True).strip()

            merge = self._strip_heads_prefix(merge)
            if remote and remote != '.' and merge:
                self.upstream_branch = '%s/%s' % (remote, merge)
        head_ref = "HEAD"
        if self.head_ref:
            head_ref = self.head_ref
                                   head_ref]).strip()
            diff_lines = self.make_diff(self.merge_base, head_ref)
                            "--no-ext-diff", "--ignore-submodules", rev_range])
        head_ref = "HEAD"
        if self.head_ref:
            head_ref = self.head_ref

                                   head_ref]).strip()