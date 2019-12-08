# Unofficial builds (RPM, SRPM) for Red Hat Enterprise Linux 8 (x86_64), and possibly Fedora and CentOS

``NOTES``: The builds stored here comes with no warranty at all, these are personal builds 
           stripped down from most (non-essential) components (like headers, etc.)
           Use at your own risk.

 1. ``YASM v1.3.0`` (https://yasm.tortall.net/) - ``RHEL-8.1-x86_64`` build. ``RPM``, ``SRPM``. I've included just the binaries for it (3) and
    also the man pages (5) for this package to keep it small and simple so anybody can go
    ahead and start coding or just to satisfy a dependency.  I was not able to find the yasm 
    package as a ``RPM``, for that reason I made this build.

    ``File list``: ``yasm vsyasm ytasm yasm.1 yasm_arch.7 yasm_dbgfmts.7 yasm_objfmts.7 yasm_parsers.7``
