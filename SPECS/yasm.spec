Name: 		yasm
Version: 	1.3.0
Release: 	1%{?dist}
Summary: 	The Yasm Modular Assembler

License: 	BSD, GPLv2, LGPLv2, Artistic License
URL: 		https://yasm.tortall.net/
Source0: 	http://www.tortall.net/projects/%{name}/releases/yasm-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
Buildarch: x86_64

%description
Yasm is a complete rewrite of the NASM assembler under the “new” BSD License 
(some portions are under other licenses, see COPYING for details). Yasm 
currently supports the x86 and AMD64 instruction sets, accepts NASM and GAS 
assembler syntaxes, outputs binary, ELF32, ELF64, 32 and 64-bit Mach-O, 
RDOFF2, COFF, Win32, and Win64 object formats, and generates source debugging 
information in STABS, DWARF 2, and CodeView 8 formats.

%prep
#%autosetup
%setup -q

%build
%configure
make %{?_smp_mflags}
#%make_build

%install
#rm -rf $RPM_BUILD_ROOT
#$mkdir -p %{buildroot}/%{_bindir}

# Skip make_install to select which files I'm installing
#%make_install

mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man7
install -m 755 yasm %{buildroot}/usr/bin/yasm
install -m 755 vsyasm %{buildroot}/usr/bin/vsyasm
install -m 755 ytasm %{buildroot}/usr/bin/ytasm

# install manual pages
install -m 644 yasm.1 %{buildroot}/%{_mandir}/man1
install -m 644 yasm_arch.7 %{buildroot}/%{_mandir}/man7
install -m 644 yasm_dbgfmts.7 %{buildroot}/%{_mandir}/man7
install -m 644 yasm_objfmts.7 %{buildroot}/%{_mandir}/man7
install -m 644 yasm_parsers.7 %{buildroot}/%{_mandir}/man7


%files
# binaries
%{_bindir}/yasm
%{_bindir}/vsyasm
%{_bindir}/ytasm
# manual pages
%{_mandir}/man1/yasm.1.gz
%{_mandir}/man7/yasm_arch.7.gz
%{_mandir}/man7/yasm_dbgfmts.7.gz
%{_mandir}/man7/yasm_objfmts.7.gz
%{_mandir}/man7/yasm_parsers.7.gz


%changelog

* Sat Dec 7 2019 Orestes Leal Rodriguez <olealrd1981@gmail.com> - for YASM 1.3.0
- rpm build for rhel8.1.x86_64
