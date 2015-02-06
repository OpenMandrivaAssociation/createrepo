Name:		createrepo
Version:	0.9.9
Release:	4
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


%changelog
* Tue Aug 28 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9.9-3
+ Revision: 815945
- Add python-deltarpm to requires.

* Sat May 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9.9-2
+ Revision: 799587
- rebuild

* Sat Mar 26 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.9.9-1
+ Revision: 648565
- new version 0.9.9
- clean top of spec
- requires yum >= 3.2.23
- fix p0
- update file list

* Wed Feb 23 2011 Bruno Cornec <bcornec@mandriva.org> 0.9.8-6
+ Revision: 639415
- creatrepo needs yum to work

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.9.8-5mdv2011.0
+ Revision: 592384
- rebuild for python 2.7

* Wed May 05 2010 Michael Scherer <misc@mandriva.org> 0.9.8-4mdv2010.1
+ Revision: 542709
- fix wrong file list, signaled by xrg on irc, due to missing BuildRequires
- remove old Requires

* Tue Mar 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.9.8-3mdv2010.1
+ Revision: 517172
-  use /%%{py_puresitedir}/%%{name}/* in file list to fix rebuild
- fix rebuilt
- fix source, url
- update to 0.9.8

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.9.6-3mdv2010.0
+ Revision: 437152
- rebuild

* Wed Feb 18 2009 Michael Scherer <misc@mandriva.org> 0.9.6-2mdv2009.1
+ Revision: 342524
- fix usage, missing modules
- fix license

* Thu Jan 15 2009 Jérôme Soyer <saispo@mandriva.org> 0.9.6-1mdv2009.1
+ Revision: 329837
- New upstream release

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.4.8-3mdv2009.0
+ Revision: 243726
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.4.8-1mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

