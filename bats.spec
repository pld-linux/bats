Summary:	Bash Automated Testing System
Name:		bats
Version:	0.4.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://github.com/sstephenson/bats/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	aeeddc0b36b8321930bf96fce6ec41ee
Patch0:		install.patch
URL:		https://github.com/sstephenson/bats
BuildRequires:	bash
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_prefix}/lib

%description
Bats is a TAP-compliant testing framework for Bash. It provides a
simple way to verify that the UNIX programs you write behave as
expected.

Bats is most useful when testing software written in Bash, but you can
use it to test any UNIX program.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '1 s,#!.*bash,#!/bin/bash,' libexec/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_libexecdir},%{_mandir}}
./install.sh $RPM_BUILD_ROOT%{_prefix}
ln -sf ../lib/bats $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/bats
%attr(755,root,root) %{_libexecdir}/bats
%attr(755,root,root) %{_libexecdir}/bats-exec-suite
%attr(755,root,root) %{_libexecdir}/bats-exec-test
%attr(755,root,root) %{_libexecdir}/bats-format-tap-stream
%attr(755,root,root) %{_libexecdir}/bats-preprocess
%{_mandir}/man1/bats.1*
%{_mandir}/man7/bats.7*
