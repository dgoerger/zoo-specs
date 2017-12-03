Name:           newsboat
Version:        2.10.1
Release:        1%{?dist}
Summary:        Configurable text-based feed reader

Group:          Applications/Internet
License:        MIT
URL:            https://newsboat.org/
Source0:        https://newsboat.org/releases/%{version}/%{name}-%{version}.tar.xz
# docs aren't build by default, see https://github.com/newsboat/newsboat/issues/66
Patch0:         newsboat-builddocs.patch

BuildRequires:  asciidoc
BuildRequires:  gettext
BuildRequires:  json-c-devel
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  stfl-devel
Requires:       stfl
Requires:       libxml2

%description
Newsboat is a feed reader for text terminals. Newsboat's great
configurability and vast number of features make it a perfect choice for people
that need a slick and fast feed reader that can be completely controlled via
keyboard.


%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{optflags}"
./config.sh
make %{?_smp_mflags} prefix=%{_prefix}


%install
%make_install prefix=%{_prefix}
# %%doc will be used in %%files to pull in the documentation
rm -rf %{buildroot}/%{_datadir}/doc/%{name}
# remove executable permissions on man pages
find %{buildroot}/%{_mandir} -type f -exec chmod -x '{}' ';'
# remove exectuable permissions on contrib/ scripts
find contrib/ -type f -exec chmod -x '{}' ';'
%find_lang %{name}


%files -f %{name}.lang
%doc doc
%license LICENSE
%{_mandir}/man1/*
%{_bindir}/*


%changelog
* Sun Dec 03 2017 David Goerger - 2.10.1-1
- repackage as Newsboat
- update to 2.10.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 23 2015 Ben Boeckel <mathstuf@gmail.com> - 2.9-1
- update to 2.9
- use %%license macro
- backup patched files
- use ncurses6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.8-7
- Rebuilt for GCC 5 C++11 ABI change

* Fri Dec 05 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.8-6
- add solarized-light colorscheme

* Thu Dec 04 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.8-5
- remove executable permissions from contrib/ scripts
- improve solarized dark colorscheme

* Thu Dec 04 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.8-4
- include contrib/ folder

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.8-1
- update to upstream release 2.8
- remove redundant patch (merged upstream)

* Tue Sep 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.7-1
- update to upstream release 2.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 19 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.6-1
- update to upstream release 2.6
- remove redundant patch

* Fri Feb 22 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.5-5
- apply newsbeuter-2.5-json-boolean-include.patch

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Ben Boeckel <mathstuf@gmail.com> - 2.5-1
- Update to 2.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 10 2011 Ben Boeckel <mathstuf@gmail.com> - 2.4-1
- Update to 2.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 05 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.3-3
- rebuild for new libxml2

* Wed Sep 29 2010 jkeating - 2.3-2
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.3-1
- newsbeuter 2.3

* Tue May 18 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.2-1
- bugfix release
- added google reader support

* Mon Jan 25 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.1-1
- New upstream source 2.1

* Wed Nov 11 2009 Thomas Janssen <thomasj@fedoraproject.org> 2.0-8
- Added BR ncurses-devel

* Fri Oct 02 2009 Thomas Janssen <thomasj@fedoraproject.org> 2.0-7
- Minor spec changes

* Sun Jun 28 2009 Byron Clark <byron@theclarkfamily.name> 2.0-6
- Correct changelog version numbers
- Generate config.mk
- Removed executable bits on manpages

* Wed Jun 10 2009 Byron Clark <byron@theclarkfamily.name> 2.0-5
- Better summary

* Sat Jun 6 2009 Byron Clark <byron@theclarkfamily.name> 2.0-4
- Use find_lang macro for translations
- Remove explicit library requires
- Use _prefix macro instead of an explicit prefix
- Install documentation with doc

* Sun May 31 2009 Byron Clark <byron@theclarkfamily.name> 2.0-3
- Add a description

* Thu May 21 2009 Byron Clark <byron@theclarkfamily.name> 2.0-2
- Fix libxml2 dependency

* Thu May 21 2009 Byron Clark <byron@theclarkfamily.name> 2.0-1
- Initial release
