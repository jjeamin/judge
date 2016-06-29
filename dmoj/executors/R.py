from dmoj.cptbox.handlers import ACCESS_DENIED
from dmoj.judgeenv import env
from .base_executor import ScriptExecutor


class Executor(ScriptExecutor):
    ext = '.R'
    name = 'R'
    nproc = -1  # needs a bunch
    command = env['runtime'].get('Rscript')
    test_program = 'writeLines(readLines(file("stdin")))'
    syscalls = ['mkdir', 'setup', 'fork', 'waitpid', 'getpgrp', 'dup2', 'nanosleep',
                'sched_getaffinity', 'execve',
                ('socket', ACCESS_DENIED),
                ('socketcall', ACCESS_DENIED)]

    fs = ['stdin', '.*\.(?:so|rdb|rdx|rds|R)', '/lib/', '/etc/ld\.so\.(?:cache|preload|nohwcap)$', '/proc/stat$',
          '/usr/lib/', '/usr/local/lib/', '/etc/passwd$', '/proc/meminfo$', '/sys/devices/system/cpu/online$',
          '/etc/nsswitch.conf$', '/etc/group$', '/dev/(?:null|urandom|random|tty|stdin|stdout|stderr)$']

    def get_cmdline(self):
        return [self.get_command(), '--vanilla', self._code]


initialize = Executor.initialize
