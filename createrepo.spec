%define name	createrepo
%define version 0.4.8
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Creates a common metadata repository
License:	GPL
Group:		System/Configuration/Packaging
Source:		http://linux.duke.edu/projects/metadata/generate/%{name}-%{version}.tar.bz2
URL:		http://linux.duke.edu/metadata/
Requires:	python >= 2.1
Requires:	python-rpm
Requires:	python-libxml2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This utility will generate a common metadata repository from a directory of
rpm packages

%prep
%setup -q

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{_datadir}/%{name}
%doc ChangeLog README
%{_datadir}/%{name}/*
%{_bindir}/%{name}
%{_bindir}/modifyrepo
%{_mandir}/man8/createrepo.8*


