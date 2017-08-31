%global srcname regex

Name:           python-%{srcname}
Version:        2017.04.05
Release:        1%{?dist}
Summary:        Alternative regular expression module, to replace re
# see also https://code.google.com/p/mrab-regex-hg/issues/detail?id=124
License:        Python and CNRI
URL:            https://bitbucket.org/mrabarnett/mrab-regex
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  /usr/bin/rst2html


%description
This new regex implementation is intended eventually to replace
Python's current re module implementation.

For testing and comparison with the current 're' module the new
implementation is in the form of a module called 'regex'.


%package -n python2-%{srcname}
Summary:        Alternative regular expression module, to replace re
Group:          Development/Languages
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
This new regex implementation is intended eventually to replace
Python's current re module implementation.

For testing and comparison with the current 're' module the new
implementation is in the form of a module called 'regex'.


%package -n python3-%{srcname}
Summary:        Alternative regular expression module, to replace re
Group:          Development/Languages
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This new regex implementation is intended eventually to replace
Python's current re module implementation.

For testing and comparison with the current 're' module the new
implementation is in the form of a module called 'regex'.


%prep
%setup -qc -n %{srcname}-%{version}

pushd %{srcname}-%{version}
# will be rebuilt
rm docs/Features.html
popd

mv %{srcname}-%{version} python2
cp -a python2 python3


%build
pushd python2
%py2_build
# rebuild the HTML doc
rst2html docs/Features.rst > docs/Features.html
popd

pushd python3
%py3_build
# rebuild the HTML doc
rst2html docs/Features.rst > docs/Features.html
popd


%install
pushd python2
%py2_install
popd

pushd python3
%py3_install
popd


%files -n python2-%{srcname}
%doc python2/README
%doc python2/docs/Features.html
%doc python2/docs/UnicodeProperties.txt
%{python2_sitearch}/*


%files -n python3-%{srcname}
%doc python3/README
%doc python3/docs/Features.html
%doc python3/docs/UnicodeProperties.txt
%{python3_sitearch}/*


%changelog
* Fri Jun 30 2017 David Goerger - 2017.04.05
- update to latest

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.09.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2016.09.22-2
- Rebuild for Python 3.6

* Sat Sep 24 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.09.22-1
- Update to 2016.09.22.

* Sun Aug  7 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.07.21-1
- Update to 2016.07.21.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2016.06.24-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul  4 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.06.24-1
- Update to 2016.06.24.

* Mon Jun 13 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.06.05-1
- Update to 2016.06.05.

* Fri Jun  3 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.06.02-1
- Update to 2016.06.02.
- Update upstream URL.

* Mon May 30 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.05.23-1
- Update to 2016.05.23.

* Fri Apr 29 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.04.25-1
- Update to 2016.04.25.

* Sat Apr  9 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.04.08-1
- Update to 2016.04.08.
- Update upstream URL.

* Tue Apr  5 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.04.02-1
- Update to 2016.04.02.

* Mon Mar  7 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.03.02-2
- Update to 2016.03.02.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2016.01.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2016.01.10-1
- Update to 2016.01.10.

* Sun Dec 20 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.11.22-1
- Update to 2015.11.22.
- Follow updated Python packaging guidelines.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.07.19-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul 27 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.07.19-1
- Update to 2015.07.19.

* Thu Jun 25 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.06.24-1
- Update to 2015.06.24.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.05.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.05.28-1
- Update to 2015.05.28.

* Sat May 23 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.05.10-1
- Update to 2015.05.10.

* Sat Mar 21 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2015.03.18-1
- Update to 2015.03.18.
- Apply updated Python packaging guidelines.

* Thu Jan  8 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2014.12.24-1
- Update to 2014.12.24.

* Sun Dec 21 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2014.12.15-1
- Update to 2014.12.15.

* Sat Dec 13 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2014.11.14-1
- Update to 2014.11.14.
- Rebuild the HTML docs.
- Update License tag.
- Update upstream URL.

* Wed Oct 22 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2014.10.09-1
- Initial version.
