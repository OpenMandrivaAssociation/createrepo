Name:		createrepo
Version:	0.9.9
Release:	3
Summary:	Creates a common metadata repository
License:	GPLv2+
Group:		System/Configuration/Packaging
Source0:	http://createrepo.baseurl.org/download/%{name}-%{version}.tar.gz
Patch0:         createrepo-0.9.9-ten-changelog-limit.patch
URL:		http://createrepo.baseurl.org/
Requires:	python-rpm
Requires:	yum >= 3.2.23
Requires:	python-deltarpm
Requires:	python-libxml2
BuildRequires:	python-devel
BuildArch:	noarch

%description
This utility will generate a common metadata repository from a directory of
rpm packages

%prep
%setup -q
%patch0 -p0

%install
%makeinstall
mkdir -p %buildroot/%py_puresitedir/%name
cp -R %{name}/*py  %buildroot/%py_puresitedir/%name

%files
%doc ChangeLog README COPYING
%{_datadir}/%{name}/
%{_bindir}/createrepo
%{_bindir}/modifyrepo
%{_bindir}/mergerepo
%{_mandir}/*/*
/%{py_puresitedir}/%{name}/*
%{_sysconfdir}/bash_completion.d/createrepo.bash
