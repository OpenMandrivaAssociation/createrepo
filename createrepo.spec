%define name	createrepo
%define version 0.9.6
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Creates a common metadata repository
License:	GPLv2+
Group:		System/Configuration/Packaging
Source:		http://linux.duke.edu/projects/metadata/generate/%{name}-%{version}.tar.bz2
Patch0:         ten-changelog-limit.patch
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
%patch0 -p0

%install
rm -rf %{buildroot}
%makeinstall
mkdir -p %buildroot/%py_puresitedir/%name
cp -R %{name}/*py  %buildroot/%py_puresitedir/%name

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc ChangeLog README COPYING
%{_datadir}/%{name}/
%{_bindir}/createrepo
%{_bindir}/modifyrepo
%{_bindir}/mergerepo
%{_mandir}/*/*
%py_puresitedir/%name

