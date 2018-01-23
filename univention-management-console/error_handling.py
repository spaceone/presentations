def error_handling(self, etype, exc, etraceback):
    message = _('''There is currently not enough free memory.
    Please try again later.''')
    if isinstance(exc, IOError) and exc.errno == errno.ENOMEM:
        raise UMC_Error(message)
